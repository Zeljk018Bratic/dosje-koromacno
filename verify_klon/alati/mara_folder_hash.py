#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
mara_folder_hash.py — SHA-256 otisak CIJELOG foldera (MARA BajteBrothers standard)

Zasto ovo postoji:
  SHA-256 radi nad bajtovima jedne datoteke. "Hash foldera" kao primitiv NE
  postoji — zato se radi MANIFESTA: hash svake datoteke (sortirano po relativnoj
  putanji), a zatim SHA-256 te manifeste = JEDAN "korijenski" otisak cijelog
  foldera (Merkle-root princip, isti kao što git radi s tree objektima).

Upotreba:
  python3 mara_folder_hash.py <folder>                      # generiraj manifestu + root hash
  python3 mara_folder_hash.py <folder> --out MANIFEST.txt   # drugo ime izlazne datoteke
  python3 mara_folder_hash.py <folder> --verify MANIFEST.txt# provjeri folder protiv ranije manifeste
  python3 mara_folder_hash.py <folder> --exclude .git audio # preskoči navedene podfoldere

Izlaz:
  - MANIFEST-SHA256.txt  (format kompatibilan sa `sha256sum -c`)
  - ROOT HASH na stdoutu (jedan redak — to je otisak cijelog foldera)

Provjera kod primatelja (Linux/macOS):
  sha256sum -c MANIFEST-SHA256.txt        # svaka datoteka pojedinačno
  sha256sum MANIFEST-SHA256.txt           # mora dati isti ROOT HASH

OpenTimestamps:
  Umjesto 136 datoteka, na a.opentimestamps.org uploadaš SAMO manifestu
  (ili samo root hash) — jedan timestamp dokazuje stanje cijelog foldera.
"""
import argparse
import hashlib
import os
import sys

DEFAULT_EXCLUDE = {".git"}


def sha256_file(path, bufsize=1024 * 1024):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(bufsize), b""):
            h.update(chunk)
    return h.hexdigest()


def scan(root, exclude):
    """Vraca listu (relativna_putanja, sha256, velicina) sortiranu po putanji."""
    entries = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = sorted(d for d in dirnames if d not in exclude)
        for name in sorted(filenames):
            full = os.path.join(dirpath, name)
            rel = os.path.relpath(full, root).replace(os.sep, "/")
            if rel in exclude or any(rel.startswith(e + "/") for e in exclude):
                continue
            entries.append((rel, sha256_file(full), os.path.getsize(full)))
    entries.sort(key=lambda e: e[0])
    return entries


def build_manifest(entries):
    """sha256sum-kompatibilan format: '<hash>  <path>' s LF krajem retka."""
    return "".join("%s  %s\n" % (h, rel) for rel, h, _ in entries)


def root_hash(manifest_text):
    return hashlib.sha256(manifest_text.encode("utf-8")).hexdigest()


def cmd_hash(root, out, exclude):
    if not os.path.isdir(root):
        sys.exit("Greska: '%s' nije folder." % root)
    entries = scan(root, exclude)
    if not entries:
        sys.exit("Greska: folder je prazan (ili je sve iskljuceno).")
    manifest = build_manifest(entries)
    with open(out, "w", encoding="utf-8", newline="\n") as f:
        f.write(manifest)
    rh = root_hash(manifest)
    total = sum(size for _, _, size in entries)
    print("Datoteka u folderu : %d" % len(entries))
    print("Ukupna velicina    : %s bajtova" % format(total, ","))
    print("Manifesta          : %s" % os.path.abspath(out))
    print("ROOT HASH (folder) : %s" % rh)
    return rh


def cmd_verify(root, manifest_path, exclude):
    if not os.path.isfile(manifest_path):
        sys.exit("Greska: manifesta '%s' ne postoji." % manifest_path)
    with open(manifest_path, "r", encoding="utf-8") as f:
        old_text = f.read()
    old = {}
    for line in old_text.splitlines():
        if not line.strip():
            continue
        parts = line.split("  ", 1)
        if len(parts) == 2:
            old[parts[1]] = parts[0]
    entries = scan(root, exclude)
    new = {rel: h for rel, h, _ in entries}

    added = sorted(set(new) - set(old))
    removed = sorted(set(old) - set(new))
    changed = sorted(p for p in set(old) & set(new) if old[p] != new[p])

    ok = not (added or removed or changed)
    print("=== PROVJERA: %s ===" % manifest_path)
    for p in changed:
        print("  PROMIJENJENO : %s" % p)
    for p in added:
        print("  DODANO       : %s" % p)
    for p in removed:
        print("  OBRISANO     : %s" % p)
    if ok:
        print("  Sve datoteke identicne manifesti.")
    old_root = root_hash(old_text)
    new_root = root_hash(build_manifest(entries))
    print("Stari ROOT HASH : %s" % old_root)
    print("Novi  ROOT HASH : %s" % new_root)
    print("REZULTAT        : %s" % ("MATCH — folder nije mijenjan" if ok and old_root == new_root else "MISMATCH — vidi razlike gore"))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser(description="SHA-256 otisak cijelog foldera (manifesta + root hash).")
    ap.add_argument("folder", help="folder koji se hashira")
    ap.add_argument("--out", default=None, help="izlazna manifesta (default: MANIFEST-SHA256.txt u folderu)")
    ap.add_argument("--exclude", nargs="*", default=None, help="folderi/datoteke koje se preskacu (default: .git)")
    ap.add_argument("--verify", default=None, metavar="MANIFEST", help="provjeri folder protiv postojece manifeste")
    args = ap.parse_args()

    exclude = set(args.exclude) if args.exclude is not None else set(DEFAULT_EXCLUDE)
    if args.verify:
        sys.exit(cmd_verify(args.folder, args.verify, exclude))
    out = args.out or os.path.join(args.folder, "MANIFEST-SHA256.txt")
    cmd_hash(args.folder, out, exclude)


if __name__ == "__main__":
    main()
