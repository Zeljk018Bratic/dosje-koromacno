#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
KONSOLIDACIJA RECOVERY + PAMETNA REDAKCIJA – Dosje Koromačno
Datum: 31-10-2026

CILJ:
1. Vratiti sve iz .pre_redact.bak (poništi prethodnu preagresivnu redakciju)
2. Primijeniti PAMETNI kontekstualni filtar:
   - Privatne osobe → [REDACTED]
   - Pravne osobe / institucije (Holcim, Kaštijun, Sekundar, Grad Labin, Općina Raša,
     MZOZT, DIRH, DORH, USKOK, FZOEU, KLASA, URBROJ...) → OSTAJU NETAKNUTI
3. Sakupiti stare logove u _ARHIVA_KONSOLIDIRANA_31-10-2026
4. Popraviti aktivizam linkove
5. Izračunati ROOT HASH (MARA standard)

Korištenje:
  python konsolidacija_recovery_smart.py --execute --verbose
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
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Tuple

# =============================================================================
# PUTANJE
# =============================================================================

PATH_RADNI = Path(r"C:\Users\zeljk\dosje-koromacno")
PATH_BACKUP = Path(r"C:\Users\zeljk\dosje-koromacno_BACKUP")
PATH_ARHIVA = PATH_BACKUP / "_ARHIVA_KONSOLIDIRANA_31-10-2026"
PATH_SIDRO = Path(r"C:\Users\zeljk\Downloads\dosje-koromacno-main (1)")

# Riječi koje označavaju SLUŽBENI / JAVNI kontekst → ne redigirati
PROTECTED_KEYWORDS = re.compile(
    r"(Holcim|Kaštijun|Kastijun|Sekundar|Labin|Raša|Rasa|"
    r"MZOZT|MINGO|DIRH|DORH|USKOK|FZOEU|CINEA|OLAF|EPPO|"
    r"Ministarstvo|Općina|Opcina|Grad\s|Županija|Zupanija|"
    r"KLASA|URBROJ|UR\.?\s*BROJ|konto|3233|3237|"
    r"d\.o\.o\.|d\.d\.|j\.d\.o\.o\.|"
    r"SHA-?256|hash|E-\d{3}|DOKAZANO|FAKT)",
    re.IGNORECASE,
)

# Privatni kontekst (jača šansa da je privatni podatak)
PRIVATE_HINTS = re.compile(
    r"(mobitel|telefon|adresa|stanuje|ulica|kuća|kuca|"
    r"osobni|privatni|građanin|gradanin|prosvjednik|"
    r"@gmail\.|@proton\.|@outlook\.|@yahoo\.)",
    re.IGNORECASE,
)

RE_OIB = re.compile(r"\b(\d{11})\b")
RE_IBAN = re.compile(
    r"\b(HR\d{2}(?:[\s\-]?\d{4}){4}(?:[\s\-]?\d{1,2})?)\b",
    re.IGNORECASE,
)
RE_MOBILE = re.compile(r"\b(09[0-9](?:[\s\-\./]?\d{3}){2}\d?)\b")

# Stari logovi / privremene datoteke za arhivu
LOG_PATTERNS = [
    r"^cleanup_log_.*\.txt$",
    r"^ocisti_duplikate.*\.txt$",
    r"^izlazTxt.*",
    r"^struktura\.txt$",
    r"^.*_log_.*\.txt$",
    r"^temp_.*",
    r"^session_.*",
    r"^ai_.*",
    r"^chatgpt_.*",
    r"^claude_.*",
    r"^grok_.*",
]


# =============================================================================
# LOGGING
# =============================================================================

def setup_logging(verbose: bool = False) -> logging.Logger:
    log_dir = Path.cwd() / "konsolidacija_logovi"
    log_dir.mkdir(exist_ok=True)
    ts = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file = log_dir / f"recovery_smart_{ts}.log"

    logger = logging.getLogger("recovery_smart")
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
    logger.info(f"Log: {log_file}")
    return logger


# =============================================================================
# 1. RESTAURACIJA IZ .pre_redact.bak
# =============================================================================

def restore_from_bak(root: Path, dry_run: bool, logger: logging.Logger) -> int:
    """Vrati originalne datoteke iz .pre_redact.bak"""
    restored = 0
    for bak in root.rglob("*.pre_redact.bak"):
        # original = bez .pre_redact.bak
        original = bak.with_suffix("").with_suffix(bak.suffix.replace(".pre_redact.bak", ""))
        # Bolje: Path("file.md.pre_redact.bak") → "file.md"
        name = bak.name
        if name.endswith(".pre_redact.bak"):
            orig_name = name[: -len(".pre_redact.bak")]
            original = bak.parent / orig_name
        else:
            continue

        logger.info(f"RESTORE: {bak.name} → {original.name}")
        if not dry_run:
            try:
                shutil.copy2(bak, original)
                restored += 1
            except Exception as e:
                logger.error(f"  Greška restore {bak}: {e}")
        else:
            restored += 1
    return restored


# =============================================================================
# 2. PAMETNA REDAKCIJA
# =============================================================================

def is_protected_context(text: str, start: int, end: int, window: int = 120) -> bool:
    left = max(0, start - window)
    right = min(len(text), end + window)
    snippet = text[left:right]
    return bool(PROTECTED_KEYWORDS.search(snippet))


def is_likely_private(text: str, start: int, end: int, window: int = 80) -> bool:
    left = max(0, start - window)
    right = min(len(text), end + window)
    snippet = text[left:right]
    return bool(PRIVATE_HINTS.search(snippet))


def smart_redact_text(content: str, stats: Dict[str, int]) -> str:
    def _oib(m: re.Match) -> str:
        if is_protected_context(content, m.start(), m.end()):
            return m.group(0)  # službeni – ostavi
        # Ako nema zaštite, redigiraj (konzervativno za privatne)
        stats["oib"] += 1
        return "[REDACTED]"

    def _iban(m: re.Match) -> str:
        if is_protected_context(content, m.start(), m.end()):
            return m.group(0)
        stats["iban"] += 1
        return "[REDACTED]"

    def _mobile(m: re.Match) -> str:
        # Mobiteli su gotovo uvijek privatni
        stats["mobile"] += 1
        return "[REDACTED]"

    content = RE_OIB.sub(_oib, content)
    content = RE_IBAN.sub(_iban, content)
    content = RE_MOBILE.sub(_mobile, content)
    return content


def smart_redact_all(root: Path, dry_run: bool, logger: logging.Logger) -> Dict[str, int]:
    totals = {"oib": 0, "iban": 0, "mobile": 0, "files": 0}
    extensions = {".md", ".html", ".htm", ".csv", ".txt"}

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in extensions:
            continue
        if ".pre_redact.bak" in path.name or "konsolidacija_logovi" in str(path):
            continue
        if "MANIFEST-SHA256" in path.name:
            continue

        try:
            original = path.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            logger.warning(f"Ne mogu pročitati {path}: {e}")
            continue

        stats = {"oib": 0, "iban": 0, "mobile": 0}
        new_content = smart_redact_text(original, stats)
        total = sum(stats.values())
        if total == 0:
            continue

        logger.info(f"SMART REDACT {path.relative_to(root)}: "
                    f"OIB={stats['oib']} IBAN={stats['iban']} MOB={stats['mobile']}")
        totals["files"] += 1
        for k in ("oib", "iban", "mobile"):
            totals[k] += stats[k]

        if not dry_run:
            # Novi backup prije pisanja
            bak = path.with_suffix(path.suffix + ".smart_redact.bak")
            if not bak.exists():
                shutil.copy2(path, bak)
            path.write_text(new_content, encoding="utf-8")

    return totals


# =============================================================================
# 3. ARHIVA STARIH LOGOVA
# =============================================================================

def collect_old_logs(root: Path, dry_run: bool, logger: logging.Logger) -> List[str]:
    moved = []
    if not dry_run:
        PATH_ARHIVA.mkdir(parents=True, exist_ok=True)

    for path in list(root.rglob("*")):
        if not path.is_file():
            continue
        name = path.name
        if any(re.match(pat, name, re.IGNORECASE) for pat in LOG_PATTERNS):
            dest = PATH_ARHIVA / name
            logger.info(f"ARHIVA LOG: {path.relative_to(root)} → {dest}")
            moved.append(str(path.relative_to(root)))
            if not dry_run:
                try:
                    if dest.exists():
                        ts = datetime.now().strftime("%H%M%S")
                        dest = PATH_ARHIVA / f"{path.stem}_{ts}{path.suffix}"
                    shutil.copy2(path, dest)  # kopiraj, ne briši
                except Exception as e:
                    logger.error(f"  Greška: {e}")
    return moved


# =============================================================================
# 4. AKTIVIZAM LINKOVI
# =============================================================================

def fix_aktivizam_links(root: Path, dry_run: bool, logger: logging.Logger) -> List[str]:
    actions = []
    for path in root.rglob("*"):
        if path.suffix.lower() not in {".md", ".html", ".htm"}:
            continue
        try:
            content = path.read_text(encoding="utf-8", errors="replace")
        except Exception:
            continue

        original = content
        # Ukloni lažne linkove na aktivizam.html
        content = re.sub(
            r'href=["\'][^"\']*aktivizam\.html["\']',
            'href="aktivizam/eko_strategija.html"',
            content,
            flags=re.IGNORECASE,
        )
        content = content.replace("aktivizam.html", "aktivizam/eko_strategija.html")

        if content != original:
            actions.append(str(path.relative_to(root)))
            logger.info(f"FIX AKTIVIZAM LINK: {path.relative_to(root)}")
            if not dry_run:
                path.write_text(content, encoding="utf-8")
    return actions


# =============================================================================
# 5. ROOT HASH (MARA)
# =============================================================================

def _sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def compute_mara_hash(root: Path, logger: logging.Logger) -> str:
    exclude = {".git"}
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in exclude)
        for name in sorted(filenames):
            full = Path(dirpath) / name
            try:
                rel = full.relative_to(root).as_posix()
            except ValueError:
                continue
            if any(x in rel for x in (".pre_redact.bak", ".smart_redact.bak",
                                      "konsolidacija_logovi", "MANIFEST-SHA256")):
                continue
            try:
                entries.append((rel, _sha256_file(full), full.stat().st_size))
            except Exception:
                entries.append((rel, "UNREADABLE", 0))
    entries.sort(key=lambda e: e[0])
    manifest = "".join(f"{h}  {rel}\n" for rel, h, _ in entries)
    rh = hashlib.sha256(manifest.encode("utf-8")).hexdigest()

    try:
        (root / "MANIFEST-SHA256.txt").write_text(manifest, encoding="utf-8", newline="\n")
    except Exception as e:
        logger.warning(f"Ne mogu snimiti manifestu: {e}")

    logger.info(f"Datoteka: {len(entries)} | ROOT HASH: {rh}")
    return rh


# =============================================================================
# MAIN
# =============================================================================

def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    parser.add_argument("--verbose", "-v", action="store_true")
    args = parser.parse_args()
    dry_run = not args.execute

    logger = setup_logging(args.verbose)
    logger.info("=" * 70)
    logger.info("RECOVERY + PAMETNA REDAKCIJA – 31-10-2026")
    logger.info(f"MODE: {'DRY-RUN' if dry_run else 'EXECUTE'}")
    logger.info("=" * 70)

    if not PATH_RADNI.exists():
        logger.error(f"Radni repo ne postoji: {PATH_RADNI}")
        return 1

    # 1. RESTORE
    logger.info("\n--- 1. RESTAURACIJA IZ .pre_redact.bak ---")
    n_restored = restore_from_bak(PATH_RADNI, dry_run, logger)
    logger.info(f"Vraćeno datoteka: {n_restored}")

    # 2. SMART REDACT
    logger.info("\n--- 2. PAMETNA REDAKCIJA (samo privatno) ---")
    stats = smart_redact_all(PATH_RADNI, dry_run, logger)
    total_private = stats["oib"] + stats["iban"] + stats["mobile"]
    logger.info(f"Redigirano privatnih entiteta: {total_private}")

    # 3. ARHIVA LOGOVA
    logger.info("\n--- 3. SAŽIMANJE STARIH LOGOVA ---")
    moved = collect_old_logs(PATH_RADNI, dry_run, logger)
    logger.info(f"Arhivirano logova: {len(moved)}")

    # 4. AKTIVIZAM
    logger.info("\n--- 4. FIX AKTIVIZAM LINKOVA ---")
    akt = fix_aktivizam_links(PATH_RADNI, dry_run, logger)

    # 5. HASH
    logger.info("\n--- 5. ROOT HASH (MARA) ---")
    root_hash = compute_mara_hash(PATH_RADNI, logger)

    # IZVJEŠTAJ
    print("\n" + "─" * 60)
    print("1. Vraćeno iz .pre_redact.bak:", n_restored)
    print("2. Redigirano PRIVATNIH entiteta (OIB/IBAN/mob):", total_private)
    print("   Detalj:", stats)
    print("3. Arhivirano starih logova:", len(moved))
    if moved:
        for m in moved[:15]:
            print(f"   - {m}")
        if len(moved) > 15:
            print(f"   ... i još {len(moved)-15}")
    print("4. Aktivizam linkovi popravljeni:", len(akt))
    print("5. KONAČNI ROOT HASH:")
    print("  ", root_hash)
    print("─" * 60)

    report = {
        "timestamp": datetime.now().isoformat(),
        "mode": "dry-run" if dry_run else "execute",
        "restored_from_bak": n_restored,
        "private_redacted": stats,
        "archived_logs": moved,
        "aktivizam_fixed": akt,
        "root_hash": root_hash,
    }
    report_path = Path.cwd() / "izvjestaj_recovery_smart_31-10-2026.json"
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=2)
    logger.info(f"JSON: {report_path}")

    if dry_run:
        print("\n⚠  DRY-RUN. Pokreni s --execute za stvarne izmjene.")
    else:
        print("\n✓  Recovery + pametna redakcija izvršena.")

    return 0


if __name__ == "__main__":
    sys.exit(main())
