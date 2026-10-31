#!/usr/bin/env python3
"""Create a deterministic SHA-256 manifest for files in a directory."""

import argparse
import hashlib
from pathlib import Path


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for chunk in iter(lambda: source.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def manifest_entries(root: Path, excluded: Path | None = None) -> list[tuple[str, str]]:
    files = (
        path
        for path in root.rglob("*")
        if path.is_file()
        and path.resolve() != excluded
        and ".git" not in path.relative_to(root).parts
    )
    entries = [(path.relative_to(root).as_posix(), sha256(path)) for path in files]
    return sorted(entries, key=lambda entry: entry[0])


def manifest_text(entries: list[tuple[str, str]]) -> str:
    return "".join(f"{digest}  {path}\n" for path, digest in entries)


def verify(root: Path, manifest: Path) -> int:
    if not manifest.is_file():
        raise ValueError(f"manifest not found: {manifest}")

    old: dict[str, str] = {}
    for line_number, line in enumerate(
        manifest.read_text(encoding="utf-8").splitlines(), start=1
    ):
        digest, separator, path = line.partition("  ")
        if not separator or len(digest) != 64 or not path or path in old:
            raise ValueError(f"invalid manifest entry at line {line_number}")
        old[path] = digest

    new = dict(manifest_entries(root, manifest.resolve()))
    added = sorted(new.keys() - old.keys())
    removed = sorted(old.keys() - new.keys())
    changed = sorted(path for path in old.keys() & new.keys() if old[path] != new[path])
    print(
        f"Files: {len(new)}; added: {len(added)}; "
        f"removed: {len(removed)}; changed: {len(changed)}"
    )
    if added or removed or changed:
        return 1

    print(f"SHA-256: {sha256(manifest)}")
    print("Result: MATCH")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--output",
        type=Path,
        help="manifest path (default: MANIFEST_SHA256.txt in the directory)",
    )
    mode.add_argument("--verify", type=Path, help="verify against an existing manifest")
    args = parser.parse_args()

    root = args.directory.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    if args.verify:
        try:
            return verify(root, args.verify.resolve())
        except ValueError as error:
            parser.error(str(error))

    output = (args.output or root / "MANIFEST_SHA256.txt").resolve()
    entries = manifest_entries(root, output)
    if not entries:
        parser.error(f"no files found in: {root}")

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(manifest_text(entries), encoding="utf-8", newline="\n")
    print(f"Files: {len(entries)}")
    print(f"Manifest: {output}")
    print(f"SHA-256: {sha256(output)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
