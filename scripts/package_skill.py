#!/usr/bin/env python3
"""Create an ecoMode skill zip for upload-based skill systems."""

from __future__ import annotations

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


EXCLUDE_DIRS = {".git", "__pycache__", ".pytest_cache", ".mypy_cache"}
EXCLUDE_SUFFIXES = {".pyc", ".zip"}


def should_include(path: Path) -> bool:
    if any(part in EXCLUDE_DIRS for part in path.parts):
        return False
    if path.suffix in EXCLUDE_SUFFIXES:
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", default="ecomode-skill.zip")
    parser.add_argument("--root", default=".")
    args = parser.parse_args()

    root = Path(args.root).resolve()
    out = Path(args.out).resolve()

    with ZipFile(out, "w", ZIP_DEFLATED) as zf:
        for path in root.rglob("*"):
            if not path.is_file() or not should_include(path.relative_to(root)):
                continue
            zf.write(path, path.relative_to(root).as_posix())

    print(f"created: {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
