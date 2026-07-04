#!/usr/bin/env python3
"""Estimate token savings between normal and ecoMode text."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def rough_tokens(text: str) -> int:
    # Conservative fallback: words + punctuation clusters + code-ish symbols.
    return len(re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE))


def count_tokens(text: str, model: str) -> tuple[int, str]:
    try:
        import tiktoken  # type: ignore

        encoding = tiktoken.encoding_for_model(model)
        return len(encoding.encode(text)), f"tiktoken:{model}"
    except Exception:
        return rough_tokens(text), "rough"


def read_text(path: str | None, inline: str | None) -> str:
    if inline is not None:
        return inline
    if path is None:
        raise SystemExit("Provide --before/--after file or --before-text/--after-text.")
    return Path(path).read_text(encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--before")
    parser.add_argument("--after")
    parser.add_argument("--before-text")
    parser.add_argument("--after-text")
    parser.add_argument("--model", default="gpt-4o-mini")
    args = parser.parse_args()

    before = read_text(args.before, args.before_text)
    after = read_text(args.after, args.after_text)

    before_tokens, method = count_tokens(before, args.model)
    after_tokens, _ = count_tokens(after, args.model)
    saved = before_tokens - after_tokens
    pct = (saved / before_tokens * 100) if before_tokens else 0.0

    print(f"method: {method}")
    print(f"before_tokens: {before_tokens}")
    print(f"after_tokens: {after_tokens}")
    print(f"saved_tokens: {saved}")
    print(f"savings_percent: {pct:.1f}%")
    print(f"target_90_met: {'yes' if pct >= 90 else 'no'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
