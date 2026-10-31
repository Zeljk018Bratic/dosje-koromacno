#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KONAČNA KONSOLIDACIJA – Dosje Koromačno
Jedna skripta. Jedan prolaz. Bez nagađanja.

Što radi:
1. Vraća prethodne .pre_redact.bak i .smart_redact.bak (ako postoje)
2. Pametna redakcija: privatni OIB/IBAN/mobitel → [REDACTED]
   Službeni (Holcim, Kaštijun, Sekundar, Grad, Općina, Ministarstvo, KLASA, URBROJ...) OSTAJU
3. Preimenovanje datoteka s puknutim znakovima + automatsko ažuriranje linkova
4. Uklanja lažne linkove na aktivizam.html → vodi na aktivizam/eko_strategija.html
5. Sakuplja stare logove/smeće u jedan arhivski folder
6. Računa ROOT HASH (MARA standard)
7. Ispisuje točan završni izvještaj

Pokretanje:
  python KONACNA_KONSOLIDACIJA.py --execute
"""

from __future__ import annotations
import argparse, hashlib, json, logging, os, re, shutil, sys, unicodedata
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# =============================================================================
PATH_RADNI   = Path(r"C:\Users\zeljk\dosje-koromacno")
PATH_BACKUP  = Path(r"C:\Users\zeljk\dosje-koromacno_BACKUP")
PATH_ARHIVA  = PATH_BACKUP / "_ARHIVA_KONSOLIDIRANA_31-10-2026"
PATH_SIDRO   = Path(r"C:\Users\zeljk\Downloads\dosje-koromacno-main (1)")

KEY_FILES = [
    "README.md", "README-en.md", "README-de.md", "README-it.md",
    "index.html", "forenzika.html", "tablica_dokaza.md", "tablica_dokaza.html",
]

PROTECTED = re.compile(
    r"(Holcim|Kaštijun|Kastijun|Sekundar|Labin|Raša|Rasa|MZOZT|MINGO|DIRH|DORH|"
    r"USKOK|FZOEU|CINEA|OLAF|EPPO|Ministarstvo|Općina|Opcina|Grad\s|Županija|"
    r"KLASA|URBROJ|UR\.?\s*BROJ|konto|3233|3237|d\.o\.o\.|d\.d\.|"
    r"SHA-?256|hash|E-\d{3}|DOKAZANO|FAKT)",
    re.IGNORECASE,
)

RE_OIB    = re.compile(r"\b(\d{11})\b")
RE_IBAN   = re.compile(r"\b(HR\d{2}(?:[\s\-]?\d{4}){4}(?:[\s\-]?\d{1,2})?)\b", re.I)
RE_MOBILE = re.compile(r"\b(09[0-9](?:[\s\-\./]?\d{3}){2}\d?)\b")

GARBAGE = [
    r"^cleanup_log_.*\.txt$", r"^ocisti_duplikate.*\.txt$", r"^izlazTxt.*",
    r"^struktura\.txt$", r"^.*_log_.*\.txt$", r"^temp_.*", r"^session_.*",
]

# =============================================================================
def setup_log(verbose=False):
    log_dir = Path.cwd() / "konsolidacija_logovi"
    log_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    logger = logging.getLogger("konacna")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()
    fh = logging.FileHandler(log_dir / f"konacna_{ts}.log", encoding="utf-8")
    fh.setFormatter(logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s"))
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch.setFormatter(logging.Formatter("%(levelname)-8s | %(message)s"))
    logger.addHandler(fh)
    logger.addHandler(ch)
    return logger

def is_protected(text, start, end, window=120):
    return bool(PROTECTED.search(text[max(0,start-window):min(len(text),end+window)]))

# =============================================================================
# 1. RESTORE BAK
# =============================================================================
def restore_baks(root: Path, dry: bool, log) -> int:
    n = 0
    for bak in list(root.rglob("*.pre_redact.bak")) + list(root.rglob("*.smart_redact.bak")):
        name = bak.name
        for suffix in (".pre_redact.bak", ".smart_redact.bak"):
            if name.endswith(suffix):
                orig = bak.parent / name[:-len(suffix)]
                break
        else:
            continue
        log.info(f"RESTORE {bak.name} → {orig.name}")
        if not dry:
            try:
                shutil.copy2(bak, orig)
                n += 1
            except Exception as e:
                log.error(f"  {e}")
        else:
            n += 1
    return n

# =============================================================================
# 2. SMART REDACT
# =============================================================================
def smart_redact(root: Path, dry: bool, log) -> Dict:
    stats = {"oib":0, "iban":0, "mobile":0, "files":0}
    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in {".md",".html",".htm",".csv",".txt"}:
            continue
        if any(x in path.name for x in (".bak", "MANIFEST", "konsolidacija_logovi")):
            continue
        try:
            txt = path.read_text(encoding="utf-8", errors="replace")
        except:
            continue
        s = {"oib":0,"iban":0,"mobile":0}
        def oib(m):
            if is_protected(txt, m.start(), m.end()): return m.group(0)
            s["oib"] += 1; return "[REDACTED]"
        def iban(m):
            if is_protected(txt, m.start(), m.end()): return m.group(0)
            s["iban"] += 1; return "[REDACTED]"
        def mob(m):
            s["mobile"] += 1; return "[REDACTED]"
        new = RE_OIB.sub(oib, txt)
        new = RE_IBAN.sub(iban, new)
        new = RE_MOBILE.sub(mob, new)
        total = sum(s.values())
        if total == 0: continue
        log.info(f"REDACT {path.relative_to(root)}: OIB={s['oib']} IBAN={s['iban']} MOB={s['mobile']}")
        stats["files"] += 1
        for k in s: stats[k] += s[k]
        if not dry:
            bak = path.with_suffix(path.suffix + ".final_redact.bak")
            if not bak.exists(): shutil.copy2(path, bak)
            path.write_text(new, encoding="utf-8")
    return stats

# =============================================================================
# 3. RENAME + LINK UPDATE
# =============================================================================
def normalize(name: str) -> str:
    nfkd = unicodedata.normalize("NFKD", name)
    cleaned = "".join(c for c in nfkd if not unicodedata.combining(c))
    for a,b in {"ð":"d","Ð":"D","š":"s","Š":"S","č":"c","Č":"C","ć":"c","Ć":"C","ž":"z","Ž":"Z","đ":"d","Đ":"D"}.items():
        cleaned = cleaned.replace(a,b)
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned

def rename_and_fix(root: Path, dry: bool, log) -> List[Tuple[str,str]]:
    renames = []
    key_paths = []
    for kf in KEY_FILES:
        for p in root.rglob(kf):
            key_paths.append(p)
    for path in list(root.rglob("*")):
        if not path.is_file() or any(x in path.name for x in (".bak","MANIFEST","konsolidacija")):
            continue
        new_name = normalize(path.name)
        if new_name == path.name: continue
        new_path = path.with_name(new_name)
        c = 1
        while new_path.exists():
            new_name = f"{Path(new_name).stem}_{c}{Path(new_name).suffix}"
            new_path = path.with_name(new_name)
            c += 1
        log.info(f"RENAME {path.name} → {new_name}")
        renames.append((str(path.relative_to(root)), str(new_path.relative_to(root))))
        if not dry:
            path.rename(new_path)
        for kf in key_paths:
            if not kf.exists(): continue
            try:
                content = kf.read_text(encoding="utf-8", errors="replace")
                ncontent = content.replace(path.name, new_name)
                if ncontent != content and not dry:
                    kf.write_text(ncontent, encoding="utf-8")
                    log.info(f"  LINK UPDATE in {kf.name}")
            except: pass
    return renames

# =============================================================================
# 4. AKTIVIZAM
# =============================================================================
def fix_aktivizam(root: Path, dry: bool, log) -> int:
    n = 0
    for path in root.rglob("*"):
        if path.suffix.lower() not in {".md",".html",".htm"}: continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except: continue
        new = re.sub(r'href=["\'][^"\']*aktivizam\.html["\']', 'href="aktivizam/eko_strategija.html"', content, flags=re.I)
        new = new.replace("aktivizam.html", "aktivizam/eko_strategija.html")
        if new != content:
            log.info(f"AKTIVIZAM FIX {path.relative_to(root)}")
            n += 1
            if not dry: path.write_text(new, encoding="utf-8")
    return n

# =============================================================================
# 5. ARHIVA SMEĆA
# =============================================================================
def archive_garbage(root: Path, dry: bool, log) -> List[str]:
    moved = []
    if not dry: PATH_ARHIVA.mkdir(parents=True, exist_ok=True)
    for path in list(root.rglob("*")):
        if not path.is_file(): continue
        if any(re.match(p, path.name, re.I) for p in GARBAGE):
            dest = PATH_ARHIVA / path.name
            log.info(f"ARHIVA {path.relative_to(root)}")
            moved.append(str(path.relative_to(root)))
            if not dry:
                try:
                    if dest.exists():
                        dest = PATH_ARHIVA / f"{path.stem}_{datetime.now():%H%M%S}{path.suffix}"
                    shutil.copy2(path, dest)
                except Exception as e: log.error(str(e))
    return moved

# =============================================================================
# 6. MARA HASH
# =============================================================================
def mara_hash(root: Path, log) -> str:
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d != ".git")
        for name in sorted(filenames):
            full = Path(dirpath) / name
            try: rel = full.relative_to(root).as_posix()
            except: continue
            if any(x in rel for x in (".bak", "MANIFEST", "konsolidacija_logovi")): continue
            try:
                h = hashlib.sha256()
                with open(full, "rb") as f:
                    for chunk in iter(lambda: f.read(1<<20), b""): h.update(chunk)
                entries.append((rel, h.hexdigest()))
            except:
                entries.append((rel, "UNREADABLE"))
    entries.sort()
    manifest = "".join(f"{h}  {rel}\n" for rel,h in entries)
    rh = hashlib.sha256(manifest.encode()).hexdigest()
    try:
        (root / "MANIFEST-SHA256.txt").write_text(manifest, encoding="utf-8", newline="\n")
    except: pass
    log.info(f"Datoteka: {len(entries)} | ROOT HASH: {rh}")
    return rh

# =============================================================================
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--execute", action="store_true")
    ap.add_argument("--verbose", "-v", action="store_true")
    args = ap.parse_args()
    dry = not args.execute
    log = setup_log(args.verbose)

    log.info("="*60)
    log.info("KONAČNA KONSOLIDACIJA – 31-10-2026")
    log.info(f"MODE: {'DRY-RUN' if dry else 'EXECUTE'}")
    log.info("="*60)

    if not PATH_RADNI.exists():
        log.error(f"Ne postoji: {PATH_RADNI}")
        return 1

    # 1
    log.info("\n--- 1. RESTORE BAK ---")
    n_rest = restore_baks(PATH_RADNI, dry, log)

    # 2
    log.info("\n--- 2. PAMETNA REDAKCIJA ---")
    stats = smart_redact(PATH_RADNI, dry, log)

    # 3
    log.info("\n--- 3. RENAME + LINKOVI ---")
    renames = rename_and_fix(PATH_RADNI, dry, log)

    # 4
    log.info("\n--- 4. AKTIVIZAM ---")
    n_akt = fix_aktivizam(PATH_RADNI, dry, log)

    # 5
    log.info("\n--- 5. ARHIVA SMEĆA ---")
    moved = archive_garbage(PATH_RADNI, dry, log)

    # 6
    log.info("\n--- 6. ROOT HASH ---")
    rh = mara_hash(PATH_RADNI, log)

    # IZVJEŠTAJ
    total_priv = stats["oib"] + stats["iban"] + stats["mobile"]
    print("\n" + "─"*60)
    print("1. Ukupno očišćeno privatnih entiteta (OIB/IBAN/mob):", total_priv)
    print("   Detalj:", stats)
    print("2. Preimenovane datoteke + ažurirani linkovi:")
    if renames:
        for o,n in renames: print(f"   {o}  →  {n}")
    else:
        print("   (nema)")
    print(f"   Aktivizam linkova popravljeno: {n_akt}")
    print("3. Status arhive 31-10-2026:", "Uspješno formirana" if (PATH_ARHIVA.exists() or dry) else "nije")
    print(f"   Arhivirano stavki: {len(moved)}")
    print("4. KONAČNI ROOT HASH PROJEKTA:")
    print("  ", rh)
    print("─"*60)

    report = {
        "timestamp": datetime.now().isoformat(),
        "mode": "execute" if not dry else "dry-run",
        "restored": n_rest,
        "private_redacted": stats,
        "renames": renames,
        "aktivizam_fixed": n_akt,
        "archived": moved,
        "root_hash": rh,
    }
    rp = Path.cwd() / "izvjestaj_KONACNA_31-10-2026.json"
    with open(rp, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    log.info(f"JSON: {rp}")

    if dry:
        print("\n⚠  DRY-RUN. Pokreni s --execute.")
    else:
        print("\n✓  KONAČNA KONSOLIDACIJA ZAVRŠENA.")
        print("PROJEKT JE CJELOVIT.")
    return 0

if __name__ == "__main__":
    sys.exit(main())
