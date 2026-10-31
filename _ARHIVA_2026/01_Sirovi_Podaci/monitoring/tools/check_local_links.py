#!/usr/bin/env python3
"""Check local Markdown links without making network requests."""

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit


LINK = re.compile(r"!?\[[^\]]*\]\((?:<([^>]+)>|([^\s)]+))[^)]*\)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("directory", type=Path, nargs="?", default=Path("."))
    args = parser.parse_args()
    root = args.directory.resolve()
    if not root.is_dir():
        parser.error(f"not a directory: {root}")

    broken: list[tuple[Path, str]] = []
    checked = 0
    for source in sorted(root.rglob("*.md")):
        if ".git" in source.relative_to(root).parts:
            continue
        text = source.read_text(encoding="utf-8")
        for match in LINK.finditer(text):
            target = match.group(1) or match.group(2) or ""
            parsed = urlsplit(target)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            local = (source.parent / unquote(parsed.path)).resolve()
            if root not in local.parents and local != root:
                broken.append((source, target))
            elif not local.exists():
                broken.append((source, target))
            checked += 1

    if broken:
        for source, target in broken:
            print(f"BROKEN {source.relative_to(root).as_posix()}: {target}")
        print(f"Checked {checked} local links; broken: {len(broken)}")
        return 1

    print(f"Checked {checked} local links; broken: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
