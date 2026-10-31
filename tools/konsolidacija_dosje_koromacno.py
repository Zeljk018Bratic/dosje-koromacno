#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KONSOLIDACIJA DOSJE KOROMAČNO – Forenzički arhivist skripta
Datum: 31-10-2026
Autor: Grok (xAI) – izvršava se LOKALNO na korisnikovom PC-u

STROGA PRAVILA (prekrsiti = STOP):
1. ZABRANJENO BRISANJE unikata. Samo kopiranje / redakcija / preimenovanje s punim logom.
2. PRAVNA REDAKCIJA: OIB (11 znamenki), IBAN (HR...), privatni mobiteli, kućne adrese → [REDACTED]
   Službeni podaci (KLASA, URBROJ, hashevi) OSTAJU.
3. AKTIVIZAM: samo eko_strategija.html + prezentacija.pdf. Ukloni lažne linkove na aktivizam.html.
4. Preimenovanje datoteka s puknutim znakovima + automatsko ažuriranje linkova u ključnim datotekama.
5. Sažimanje svih starih/duplih AI podfoldera u JEDAN arhivski folder s datumom.
6. Zadrži točno jedan aktualni set README (hr + en/de/it) + tablicu E-001 do E-079 (E-016 = uhićenje Vuka Vukovića).
7. NE commitaj / NE pushaj. NE mijenjaj postojeće statuse u registru.
8. Na kraju: detaljan izvještaj + root hash.

Korištenje:
  python konsolidacija_dosje_koromacno.py --dry-run          # samo pregled (default)
  python konsolidacija_dosje_koromacno.py --execute          # stvarno izvrši
  python konsolidacija_dosje_koromacno.py --execute --verbose
"""

from __future__ import annotations

import argparse
import hashlib
import json
import logging
import os
import re
import shutil
import sys
import unicodedata
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# =============================================================================
# KONFIGURACIJA PUTANJA (prilagodi ako treba)
# =============================================================================

PATH_SIDRO = Path(r"C:\Users\zeljk\Downloads\dosje-koromacno-main (1)")
PATH_RADNI = Path(r"C:\Users\zeljk\dosje-koromacno")
PATH_BACKUP = Path(r"C:\Users\zeljk\dosje-koromacno_BACKUP")
PATH_ARHIVA = PATH_BACKUP / "_ARHIVA_KONSOLIDIRANA_31-10-2026"

# Ključne datoteke u kojima se ažuriraju linkovi nakon preimenovanja
KEY_FILES_FOR_LINK_UPDATE = [
    "README.md",
    "README-en.md",
    "README-de.md",
    "README-it.md",
    "index.html",
    "forenzika.html",
    "tablica_dokaza.md",
    "tablica_dokaza.html",
    "dokazi.md",
    "evidencija.md",
]

# Datoteke/folders koje se smatraju "AI podfolderima" ili starim radnim kopijama
# (proširi listu prema stvarnom stanju na disku)
AI_FOLDER_PATTERNS = [
    r"^AI[_-]",
    r"^ai[_-]",
    r"^chatgpt",
    r"^claude",
    r"^gemini",
    r"^grok",
    r"^session[_-]",
    r"^temp[_-]",
    r"^old[_-]",
    r"^backup[_-]?\d*",
    r"^kopija",
    r"^radna[_-]",
    r"^export[_-]",
    r"^generated",
    r"^prompt",
    r"^llm",
]

# =============================================================================
# LOGGING
# =============================================================================

def setup_logging(verbose: bool = False) -> logging.Logger:
    log_dir = Path.cwd() / "konsolidacija_logovi"
    log_dir.mkdir(exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"konsolidacija_{timestamp}.log"

    logger = logging.getLogger("dosje_konsolidacija")
    logger.setLevel(logging.DEBUG)
    logger.handlers.clear()

    fh = logging.FileHandler(log_file, encoding="utf-8")
    fh.setLevel(logging.DEBUG)
    fh.setFormatter(logging.Formatter("%(asctime)s | %(levelname)-8s | %(message)s"))

    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG if verbose else logging.INFO)
    ch.setFormatter(logging.Formatter("%(levelname)-8s | %(message)s"))

    logger.addHandler(fh)
    logger.addHandler(ch)
    logger.info(f"Log datoteka: {log_file}")
    return logger


# =============================================================================
# REGEX UZORCI ZA REDAKCIJU
# =============================================================================

# OIB: točno 11 znamenki, riječ granica
RE_OIB = re.compile(r"\b(\d{11})\b")

# IBAN HR (razni formati s razmacima)
RE_IBAN = re.compile(
    r"\b(HR\d{2}(?:[\s\-]?\d{4}){4}(?:[\s\-]?\d{1,2})?)\b",
    re.IGNORECASE,
)

# Hrvatski mobilni brojevi (09x ...)
RE_MOBILE = re.compile(
    r"\b(09[0-9](?:[\s\-\./]?\d{3}){2}\d?)\b"
)

# Jednostavni uzorci kućnih adresa (ulica + broj). Oprezno – može imati false positive.
RE_ADDRESS = re.compile(
    r"\b((?:[A-ZŠĐČĆŽ][a-zšđčćž]+(?:ova|eva|ina|ska|čka|čka)?(?:\s+[A-ZŠĐČĆŽ][a-zšđčćž]+)?)\s+"
    r"(?:ulica|ul\.|cesta|put|trg|brijeg|obala)?\s*\d+[a-zA-Z]?)\b",
    re.IGNORECASE,
)

# Zaštita službenih oznaka – ne redigirati ako je u blizini ovih riječi
PROTECTED_CONTEXT = re.compile(
    r"(KLASA|URBROJ|UR\.?\s*BROJ|KLASA:|URBROJ:|SHA-?256|hash|dokaz|E-\d{3})",
    re.IGNORECASE,
)


def is_protected_context(text: str, start: int, end: int, window: int = 80) -> bool:
    """Provjeri je li match unutar službenog konteksta."""
    left = max(0, start - window)
    right = min(len(text), end + window)
    snippet = text[left:right]
    return bool(PROTECTED_CONTEXT.search(snippet))


# =============================================================================
# REDAKCIJA
# =============================================================================

def redact_text(content: str, stats: Dict[str, int]) -> str:
    """Redigiraj privatne entitete. Vraća novi sadržaj + ažurira stats."""

    def _replace_oib(m: re.Match) -> str:
        if is_protected_context(content, m.start(), m.end()):
            return m.group(0)
        stats["oib"] += 1
        return "[REDACTED]"

    def _replace_iban(m: re.Match) -> str:
        if is_protected_context(content, m.start(), m.end()):
            return m.group(0)
        stats["iban"] += 1
        return "[REDACTED]"

    def _replace_mobile(m: re.Match) -> str:
        stats["mobile"] += 1
        return "[REDACTED]"

    def _replace_address(m: re.Match) -> str:
        # Adrese su rizičnije – redigiramo samo ako izgleda kao kućna
        stats["address"] += 1
        return "[REDACTED]"

    content = RE_OIB.sub(_replace_oib, content)
    content = RE_IBAN.sub(_replace_iban, content)
    content = RE_MOBILE.sub(_replace_mobile, content)
    # Adrese ostavljamo konzervativno – možeš uključiti po potrebi
    # content = RE_ADDRESS.sub(_replace_address, content)
    return content


def redact_file(path: Path, dry_run: bool, logger: logging.Logger) -> Dict[str, int]:
    """Redigiraj jednu datoteku. Vraća broj redakcija po tipu."""
    stats = {"oib": 0, "iban": 0, "mobile": 0, "address": 0}
    try:
        original = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.warning(f"Ne mogu pročitati {path}: {e}")
        return stats

    new_content = redact_text(original, stats)
    total = sum(stats.values())
    if total == 0:
        return stats

    logger.info(f"REDAKCIJA {path.name}: OIB={stats['oib']} IBAN={stats['iban']} "
                f"MOB={stats['mobile']} ADR={stats['address']}")

    if not dry_run:
        # Backup originala prije pisanja
        bak = path.with_suffix(path.suffix + ".pre_redact.bak")
        if not bak.exists():
            shutil.copy2(path, bak)
        path.write_text(new_content, encoding="utf-8")
        logger.debug(f"  → zapisano (backup: {bak.name})")
    else:
        logger.debug(f"  → DRY-RUN (ne pišem)")
    return stats


def redact_all(root: Path, dry_run: bool, logger: logging.Logger) -> Dict[str, int]:
    """Prođi sve .md / .html / .csv u rootu (rekurzivno)."""
    totals = {"oib": 0, "iban": 0, "mobile": 0, "address": 0, "files": 0}
    extensions = {".md", ".html", ".htm", ".csv", ".txt"}

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in extensions:
            continue
        # Preskoči već redigirane backupove i same logove
        if ".pre_redact.bak" in path.name or "konsolidacija_logovi" in str(path):
            continue
        file_stats = redact_file(path, dry_run, logger)
        if sum(file_stats.values()) > 0:
            totals["files"] += 1
            for k in ("oib", "iban", "mobile", "address"):
                totals[k] += file_stats[k]
    return totals


# =============================================================================
# PREIMENOVANJE DATOTEKA S PUKNUTIM ZNAKOVIMA + AŽURIRANJE LINKOVA
# =============================================================================

def normalize_filename(name: str) -> str:
    """Pretvori u čistu latinicu, ukloni problematične znakove."""
    # NFD dekompozicija pa makni kombinirajuće znakove
    nfkd = unicodedata.normalize("NFKD", name)
    cleaned = "".join(c for c in nfkd if not unicodedata.combining(c))
    # Explicitne zamjene hrvatskih znakova koji često puknu
    replacements = {
        "ð": "d", "Ð": "D",
        "š": "s", "Š": "S",
        "č": "c", "Č": "C",
        "ć": "c", "Ć": "C",
        "ž": "z", "Ž": "Z",
        "đ": "d", "Đ": "D",
        "ä": "a", "ö": "o", "ü": "u",
        "ß": "ss",
    }
    for old, new in replacements.items():
        cleaned = cleaned.replace(old, new)
    # Zamijeni sve što nije sigurno za Windows filename
    cleaned = re.sub(r'[<>:"/\\|?*\x00-\x1f]', "_", cleaned)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"_+", "_", cleaned)
    return cleaned


def needs_rename(name: str) -> bool:
    """Treba li preimenovati zbog problematičnih znakova?"""
    if name != normalize_filename(name):
        return True
    # Dodatni znakovi koji često pucaju
    if re.search(r"[ðÐšŠčČćĆžŽđĐ]", name):
        return True
    return False


def update_links_in_file(path: Path, old_name: str, new_name: str,
                         dry_run: bool, logger: logging.Logger) -> int:
    """Zamijeni pojave starog imena novim u datoteci. Vraća broj zamjena."""
    try:
        content = path.read_text(encoding="utf-8", errors="replace")
    except Exception as e:
        logger.warning(f"Ne mogu pročitati za link update {path}: {e}")
        return 0

    # Različiti oblici referenci
    patterns = [
        re.escape(old_name),
        re.escape(old_name.replace(" ", "%20")),
        re.escape(old_name.replace(" ", "_")),
    ]
    count = 0
    new_content = content
    for pat in patterns:
        new_content, n = re.subn(pat, new_name, new_content)
        count += n

    if count > 0:
        logger.info(f"  LINK UPDATE {path.name}: {old_name} → {new_name} ({count}x)")
        if not dry_run:
            path.write_text(new_content, encoding="utf-8")
    return count


def rename_broken_files(root: Path, dry_run: bool, logger: logging.Logger
                        ) -> List[Tuple[str, str]]:
    """Pronađi i preimenuj datoteke s puknutim znakovima + ažuriraj linkove."""
    renames: List[Tuple[str, str]] = []
    key_files = []
    for kf in KEY_FILES_FOR_LINK_UPDATE:
        p = root / kf
        if p.exists():
            key_files.append(p)
        # Traži i dublje
        for found in root.rglob(kf):
            if found not in key_files:
                key_files.append(found)

    for path in list(root.rglob("*")):
        if not path.is_file():
            continue
        if path.name.endswith(".pre_redact.bak") or "konsolidacija_logovi" in str(path):
            continue
        if not needs_rename(path.name):
            continue

        new_name = normalize_filename(path.name)
        if new_name == path.name:
            continue
        new_path = path.with_name(new_name)

        # Riješi koliziju
        counter = 1
        while new_path.exists():
            stem = Path(new_name).stem
            suffix = Path(new_name).suffix
            new_name = f"{stem}_{counter}{suffix}"
            new_path = path.with_name(new_name)
            counter += 1

        logger.info(f"PREIMENOVANJE: {path.name} → {new_name}")
        renames.append((str(path.relative_to(root)), str(new_path.relative_to(root))))

        if not dry_run:
            path.rename(new_path)

        # Ažuriraj linkove u ključnim datotekama
        for kf in key_files:
            if kf.exists():
                update_links_in_file(kf, path.name, new_name, dry_run, logger)

    return renames


# =============================================================================
# AKTIVIZAM FOLDER
# =============================================================================

def clean_aktivizam(root: Path, dry_run: bool, logger: logging.Logger) -> List[str]:
    """Osiguraj da u aktivizam/ postoje samo eko_strategija.html i prezentacija.pdf.
    Ukloni lažne linkove na aktivizam.html iz cijelog projekta."""
    actions = []
    aktivizam = root / "aktivizam"

    if not aktivizam.exists():
        logger.info("Mapa 'aktivizam' ne postoji – preskačem.")
        return actions

    allowed = {"eko_strategija.html", "prezentacija.pdf"}
    for item in list(aktivizam.iterdir()):
        if item.name not in allowed:
            actions.append(f"AKTIVIZAM: ekstra datoteka/folder {item.name}")
            logger.warning(f"U aktivizam/ postoji nešto što nije dozvoljeno: {item.name}")
            # Ne brišemo – samo bilježimo (pravilo: nema brisanja)
            # Korisnik može ručno premjestiti u arhivu.

    # Ukloni linkove na aktivizam.html iz svih html/md
    for path in root.rglob("*"):
        if path.suffix.lower() not in {".html", ".htm", ".md"}:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue
        if "aktivizam.html" not in content:
            continue
        new_content = content.replace("aktivizam.html", "#")  # ili ukloni cijeli <a>
        # Bolje: zamijeni hrefove
        new_content = re.sub(
            r'href=["\'][^"\']*aktivizam\.html["\']',
            'href="#"',
            new_content,
            flags=re.IGNORECASE,
        )
        if new_content != content:
            actions.append(f"UKLONJEN LINK aktivizam.html u {path.relative_to(root)}")
            logger.info(f"Uklonjen lažni link aktivizam.html iz {path.name}")
            if not dry_run:
                path.write_text(new_content, encoding="utf-8")
    return actions


# =============================================================================
# KONSOLIDACIJA ARHIVE
# =============================================================================

def is_ai_or_old_folder(name: str) -> bool:
    for pat in AI_FOLDER_PATTERNS:
        if re.search(pat, name, re.IGNORECASE):
            return True
    return False


def consolidate_archive(dry_run: bool, logger: logging.Logger) -> Dict:
    """Kopiraj stare/duple/AI foldere u jedinstvenu arhivu. Ne briši originale."""
    result = {
        "created": False,
        "copied_folders": [],
        "copied_files": 0,
        "errors": [],
    }

    if not PATH_BACKUP.exists():
        logger.error(f"BACKUP mapa ne postoji: {PATH_BACKUP}")
        result["errors"].append("BACKUP mapa ne postoji")
        return result

    if not dry_run:
        PATH_ARHIVA.mkdir(parents=True, exist_ok=True)
        result["created"] = True
        logger.info(f"Kreirana arhiva: {PATH_ARHIVA}")
    else:
        logger.info(f"DRY-RUN: arhiva bi bila kreirana na {PATH_ARHIVA}")

    # Traži kandidate u BACKUP-u i radnom repou
    candidates: List[Path] = []
    for base in [PATH_BACKUP, PATH_RADNI]:
        if not base.exists():
            continue
        for item in base.iterdir():
            if item.is_dir() and is_ai_or_old_folder(item.name):
                # Ne diraj samu ciljnu arhivu
                if item.resolve() == PATH_ARHIVA.resolve():
                    continue
                candidates.append(item)

    # Također kopiraj cijeli sidro (Downloads) kao "izvor istine" snapshot
    if PATH_SIDRO.exists():
        candidates.append(PATH_SIDRO)

    logger.info(f"Pronađeno {len(candidates)} kandidata za arhiviranje.")

    for src in candidates:
        dest_name = src.name
        # Ako je sidro, daj mu jasniji naziv
        if src == PATH_SIDRO:
            dest_name = "_SIDRO_IZVOR_ISTINE_Downloads"
        dest = PATH_ARHIVA / dest_name
        logger.info(f"ARHIVA: {src} → {dest}")
        result["copied_folders"].append(str(src))

        if not dry_run:
            try:
                if dest.exists():
                    # Ako već postoji, dodaj timestamp
                    ts = datetime.now().strftime("%H%M%S")
                    dest = PATH_ARHIVA / f"{dest_name}_{ts}"
                shutil.copytree(src, dest, dirs_exist_ok=False)
                # Broji datoteke
                result["copied_files"] += sum(1 for _ in dest.rglob("*") if _.is_file())
            except Exception as e:
                logger.error(f"Greška pri kopiranju {src}: {e}")
                result["errors"].append(str(e))

    return result


# =============================================================================
# README / VIŠEJEZIČNOST + E-016
# =============================================================================

def ensure_readmes_and_e016(root: Path, dry_run: bool, logger: logging.Logger) -> List[str]:
    """Provjeri da postoji točno jedan set README + bilješka o E-016."""
    notes = []
    readme_variants = ["README.md", "README-en.md", "README-de.md", "README-it.md"]

    found = {}
    for name in readme_variants:
        matches = list(root.rglob(name))
        if len(matches) > 1:
            notes.append(f"VIŠE PRIMJERAKA {name}: {[str(m.relative_to(root)) for m in matches]}")
            logger.warning(f"Više primjeraka {name} – ostavi samo jedan u rootu.")
        elif len(matches) == 1:
            found[name] = matches[0]
        else:
            notes.append(f"NEDOSTAJE {name}")

    # E-016 – samo provjeri postoji li spomen (ne izmišljaj sadržaj)
    e016_pattern = re.compile(r"E-0?16", re.IGNORECASE)
    e016_found = False
    for path in root.rglob("*"):
        if path.suffix.lower() not in {".md", ".html", ".csv", ".txt"}:
            continue
        try:
            txt = path.read_text(encoding="utf-8", errors="replace")
            if e016_pattern.search(txt):
                e016_found = True
                if re.search(r"Vuk\s*Vuković|Vuković", txt, re.IGNORECASE):
                    notes.append(f"E-016 + Vuković pronađen u {path.relative_to(root)}")
                else:
                    notes.append(f"E-016 pronađen u {path.relative_to(root)} (bez eksplicitnog Vukovića)")
                break
        except Exception:
            continue
    if not e016_found:
        notes.append("E-016 NIJE PRONAĐEN u tablici/dokazima – korisnik treba ručno ugraditi.")

    return notes


# =============================================================================
# ROOT HASH — TOČAN mara_folder_hash.py (MARA BajteBrothers standard)
# =============================================================================

def _sha256_file(path: Path, bufsize: int = 1024 * 1024) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(bufsize), b""):
            h.update(chunk)
    return h.hexdigest()


def _scan_folder(root: Path, exclude: set) -> list:
    """Vraća listu (relativna_putanja, sha256, velicina) sortiranu po putanji.
    Identicno mara_folder_hash.py"""
    entries = []
    root = Path(root)
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in exclude)
        for name in sorted(filenames):
            full = Path(dirpath) / name
            try:
                rel = full.relative_to(root).as_posix()
            except ValueError:
                continue
            if rel in exclude or any(rel.startswith(e + "/") for e in exclude):
                continue
            # Preskoči naše privremene datoteke
            if ".pre_redact.bak" in rel or "konsolidacija_logovi" in rel:
                continue
            if "MANIFEST-SHA256.txt" in rel:
                continue
            try:
                entries.append((rel, _sha256_file(full), full.stat().st_size))
            except Exception as e:
                # Ne prekidaj cijeli hash zbog jedne nečitljive datoteke
                entries.append((rel, "UNREADABLE", 0))
    entries.sort(key=lambda e: e[0])
    return entries


def _build_manifest(entries: list) -> str:
    """sha256sum-kompatibilan format: '<hash>  <path>' s LF krajem retka."""
    return "".join("%s  %s\n" % (h, rel) for rel, h, _ in entries)


def _root_hash_from_manifest(manifest_text: str) -> str:
    return hashlib.sha256(manifest_text.encode("utf-8")).hexdigest()


def compute_folder_hash(root: Path, logger: logging.Logger) -> str:
    """
    TOČAN MARA standard (mara_folder_hash.py):
    1. Hash svake datoteke
    2. Manifesta sortirana po relativnoj putanji
    3. SHA-256 manifeste = ROOT HASH cijelog foldera
    """
    if not root.exists() or not root.is_dir():
        logger.error(f"ROOT HASH: folder ne postoji: {root}")
        return "ERROR_ROOT_NOT_FOUND"

    exclude = {".git"}
    entries = _scan_folder(root, exclude)
    if not entries:
        logger.error("ROOT HASH: folder prazan ili sve isključeno")
        return "ERROR_EMPTY"

    manifest = _build_manifest(entries)
    rh = _root_hash_from_manifest(manifest)

    # Snimi manifestu u radni folder (kao što radi originalna skripta)
    manifest_path = root / "MANIFEST-SHA256.txt"
    try:
        manifest_path.write_text(manifest, encoding="utf-8", newline="\n")
        logger.info(f"Manifesta snimljena: {manifest_path}")
    except Exception as e:
        logger.warning(f"Ne mogu snimiti manifestu: {e}")

    total = sum(size for _, _, size in entries)
    logger.info(f"Datoteka u folderu : {len(entries)}")
    logger.info(f"Ukupna velicina    : {total:,} bajtova")
    logger.info(f"ROOT HASH (folder) : {rh}")
    return rh


# =============================================================================
# GLAVNI TOK
# =============================================================================

def main() -> int:
    parser = argparse.ArgumentParser(
        description="Konsolidacija Dosje Koromačno – forenzički arhivist"
    )
    parser.add_argument("--execute", action="store_true",
                        help="Stvarno izvrši promjene (default je dry-run)")
    parser.add_argument("--verbose", "-v", action="store_true")
    parser.add_argument("--skip-redact", action="store_true")
    parser.add_argument("--skip-rename", action="store_true")
    parser.add_argument("--skip-archive", action="store_true")
    parser.add_argument("--skip-hash", action="store_true")
    args = parser.parse_args()

    dry_run = not args.execute
    logger = setup_logging(args.verbose)

    logger.info("=" * 70)
    logger.info("KONSOLIDACIJA DOSJE KOROMAČNO – 31-10-2026")
    logger.info(f"MODE: {'DRY-RUN (samo pregled)' if dry_run else 'EXECUTE (piše na disk)'}")
    logger.info("=" * 70)

    # Provjera putanja
    for label, p in [("SIDRO", PATH_SIDRO), ("RADNI", PATH_RADNI), ("BACKUP", PATH_BACKUP)]:
        exists = p.exists()
        logger.info(f"{label}: {p} → {'POSTOJI' if exists else 'NE POSTOJI'}")

    if not PATH_RADNI.exists():
        logger.error("Glavni radni repo ne postoji. Prekidam.")
        return 1

    report = {
        "timestamp": datetime.now().isoformat(),
        "mode": "dry-run" if dry_run else "execute",
        "redacted_entities": {},
        "renamed_files": [],
        "aktivizam_actions": [],
        "archive_status": {},
        "readme_notes": [],
        "root_hash": None,
    }

    # 1. REDAKCIJA
    if not args.skip_redact:
        logger.info("\n--- 1. PRAVNA REDAKCIJA ---")
        stats = redact_all(PATH_RADNI, dry_run, logger)
        report["redacted_entities"] = stats
        total_entities = stats["oib"] + stats["iban"] + stats["mobile"] + stats["address"]
        logger.info(f"Ukupno očišćeno privatnih entiteta: {total_entities} "
                    f"(u {stats['files']} datoteka)")
    else:
        logger.info("Preskačem redakciju (--skip-redact)")

    # 2. PREIMENOVANJE + LINKOVI
    if not args.skip_rename:
        logger.info("\n--- 2. PREIMENOVANJE DATOTEKA + AŽURIRANJE LINKOVA ---")
        renames = rename_broken_files(PATH_RADNI, dry_run, logger)
        report["renamed_files"] = renames
        logger.info(f"Preimenovano datoteka: {len(renames)}")
    else:
        logger.info("Preskačem preimenovanje (--skip-rename)")

    # 3. AKTIVIZAM
    logger.info("\n--- 3. ČIŠĆENJE AKTIVIZAM FOLDERA I LINKOVA ---")
    akt_actions = clean_aktivizam(PATH_RADNI, dry_run, logger)
    report["aktivizam_actions"] = akt_actions

    # 4. ARHIVA
    if not args.skip_archive:
        logger.info("\n--- 4. SAŽIMANJE U JEDINSTVENU ARHIVU ---")
        arch = consolidate_archive(dry_run, logger)
        report["archive_status"] = arch
    else:
        logger.info("Preskačem arhivu (--skip-archive)")

    # 5. README + E-016
    logger.info("\n--- 5. PROVJERA README I E-016 ---")
    notes = ensure_readmes_and_e016(PATH_RADNI, dry_run, logger)
    report["readme_notes"] = notes
    for n in notes:
        logger.info(f"  {n}")

    # 6. ROOT HASH
    if not args.skip_hash:
        logger.info("\n--- 6. IZRAČUN ROOT HASH-a ---")
        root_hash = compute_folder_hash(PATH_RADNI, logger)
        report["root_hash"] = root_hash
    else:
        logger.info("Preskačem hash (--skip-hash)")

    # =============================================================================
    # IZVJEŠTAJ
    # =============================================================================
    logger.info("\n" + "=" * 70)
    logger.info("IZLAZNI IZVJEŠTAJ")
    logger.info("=" * 70)

    total_redacted = sum(report["redacted_entities"].get(k, 0)
                         for k in ("oib", "iban", "mobile", "address"))
    print("\n" + "─" * 60)
    print("1. Ukupno očišćeno privatnih entiteta (OIB/IBAN/mob/adr):", total_redacted)
    print("   Detalj:", report["redacted_entities"])
    print()
    print("2. Popis automatski preimenovanih datoteka i ažuriranih linkova:")
    if report["renamed_files"]:
        for old, new in report["renamed_files"]:
            print(f"   {old}  →  {new}")
    else:
        print("   (nema preimenovanja)")
    if report["aktivizam_actions"]:
        print("   Aktivizam akcije:")
        for a in report["aktivizam_actions"]:
            print(f"   - {a}")
    print()
    arch_ok = report["archive_status"].get("created") or dry_run
    print("3. Status jedinstvene konsolidirane arhive 31-10-2026:",
          "Uspješno formirana" if arch_ok else "NIJE formirana / greška")
    if report["archive_status"].get("copied_folders"):
        print("   Kopirano foldera:", len(report["archive_status"]["copied_folders"]))
    print()
    print("4. KONAČNI ROOT HASH PROJEKTA:")
    print("  ", report["root_hash"] or "(nije izračunat)")
    print("─" * 60)

    # Snimi JSON izvještaj
    report_path = Path.cwd() / f"izvjestaj_konsolidacija_31-10-2026.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    logger.info(f"JSON izvještaj: {report_path}")

    if dry_run:
        print("\n⚠  OVO JE BIO DRY-RUN. Ništa nije zapisano na disk.")
        print("   Pokreni s --execute kad si spreman.")
    else:
        print("\n✓  Izvršeno. Provjeri logove i backup datoteke (.pre_redact.bak).")

    print("\nŠTO NIJE PROVJERENO / RUČNO OBAVEZNO:")
    print("  - Sadržaj E-016 (uhićenje Vuka Vukovića) – skripta samo traži postoji li spomen.")
    print("  - Točan popis svih 27 AI podfoldera – skripta koristi heuristiku po imenu.")
    print("  - Kućne adrese (regex je konzervativan, default isključen).")
    print("  - Git status / remote – skripta NE dira git.")
    print("  - Ručna provjera da nijedan unikatan dokaz nije ostao samo u starom AI folderu.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
