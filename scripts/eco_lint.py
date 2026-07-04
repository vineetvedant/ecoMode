#!/usr/bin/env python3
"""Lint ecoMode output for filler, unsafe claims, and compression risks."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


FILLER = [
    "sure",
    "of course",
    "happy to",
    "i think",
    "maybe",
    "perhaps",
    "it might be worth",
    "you may want to consider",
    "as an ai",
    "in summary",
]

INVENTED_ABBREVIATIONS = [
    "cfg",
    "impl",
    "req",
    "res",
    "fn",
]

UNMEASURED_90 = re.compile(r"\b(?:save[sd]?|saving[s]?)\s+(?:exactly\s+)?90%|\b90%\s+(?:guarantee|guaranteed)\b", re.I)


def read_input(path: str | None, text: str | None) -> str:
    if text is not None:
        return text
    if path:
        return Path(path).read_text(encoding="utf-8")
    raise SystemExit("Provide --file or --text.")


def line_number(text: str, index: int) -> int:
    return text.count("\n", 0, index) + 1


def find_terms(text: str, terms: list[str]) -> list[str]:
    lower = text.lower()
    hits = []
    for term in terms:
        pos = lower.find(term)
        if pos >= 0:
            hits.append(f"L{line_number(text, pos)}: avoid filler `{term}`")
    return hits


def find_abbrev(text: str) -> list[str]:
    hits = []
    for abbr in INVENTED_ABBREVIATIONS:
        for match in re.finditer(rf"(?<![`/\w.-]){re.escape(abbr)}(?![`/\w.-])", text, re.I):
            hits.append(f"L{line_number(text, match.start())}: avoid unclear abbreviation `{match.group(0)}`")
    return hits


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--file")
    parser.add_argument("--text")
    parser.add_argument("--allow-measured-90", action="store_true")
    parser.add_argument("--max-lines", type=int, default=12, help="0 disables line-count check")
    args = parser.parse_args()

    text = read_input(args.file, args.text)
    issues = []
    issues.extend(find_terms(text, FILLER))
    issues.extend(find_abbrev(text))

    if not args.allow_measured_90:
        match = UNMEASURED_90.search(text)
        if match:
            issues.append(f"L{line_number(text, match.start())}: avoid guaranteed 90% claim without measurement")

    if args.max_lines and len(text.splitlines()) > args.max_lines:
        issues.append(f"output over {args.max_lines} lines; check whether ecoMode should be tighter")

    if issues:
        print("eco_lint: fail")
        for issue in issues:
            print(f"- {issue}")
        return 1

    print("eco_lint: pass")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
