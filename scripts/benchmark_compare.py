#!/usr/bin/env python3
"""Compare ecoMode fixtures against caveman fixtures."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


def rough_tokens(text: str) -> int:
    return len(re.findall(r"\w+|[^\w\s]", text, flags=re.UNICODE))


def count_tokens(text: str, model: str) -> tuple[int, str]:
    try:
        import tiktoken  # type: ignore

        enc = tiktoken.encoding_for_model(model)
        return len(enc.encode(text)), f"tiktoken:{model}"
    except Exception:
        return rough_tokens(text), "rough"


def includes_all(text: str, terms: list[str]) -> bool:
    haystack = text.lower()
    return all(term.lower() in haystack for term in terms)


def pct_saved(before: int, after: int) -> float:
    return ((before - after) / before * 100.0) if before else 0.0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", required=True)
    parser.add_argument("--model", default="gpt-4o-mini")
    args = parser.parse_args()

    cases = json.loads(Path(args.cases).read_text(encoding="utf-8"))
    totals = {
        "normal": 0,
        "caveman": 0,
        "ecomode": 0,
        "eco_wins": 0,
        "exact_pass": 0,
    }
    method = "rough"
    rows = []

    for case in cases:
        normal, method = count_tokens(case["normal"], args.model)
        caveman, _ = count_tokens(case["caveman"], args.model)
        ecomode, _ = count_tokens(case["ecomode"], args.model)
        exact = includes_all(case["ecomode"], case.get("must_include", []))
        eco_wins = ecomode <= caveman and exact

        totals["normal"] += normal
        totals["caveman"] += caveman
        totals["ecomode"] += ecomode
        totals["eco_wins"] += int(eco_wins)
        totals["exact_pass"] += int(exact)

        rows.append(
            {
                "id": case["id"],
                "normal": normal,
                "caveman": caveman,
                "ecomode": ecomode,
                "eco_vs_caveman": caveman - ecomode,
                "eco_saved_vs_normal": pct_saved(normal, ecomode),
                "exact": exact,
                "win": eco_wins,
            }
        )

    print(f"method: {method}")
    for row in rows:
        print(
            "{id}: normal={normal} caveman={caveman} ecomode={ecomode} "
            "eco_delta={eco_vs_caveman:+d} saved={eco_saved_vs_normal:.1f}% "
            "exact={exact} win={win}".format(**row)
        )

    caveman_saved = pct_saved(totals["normal"], totals["caveman"])
    ecomode_saved = pct_saved(totals["normal"], totals["ecomode"])
    print("")
    print(f"total_normal: {totals['normal']}")
    print(f"total_caveman: {totals['caveman']} ({caveman_saved:.1f}% saved)")
    print(f"total_ecomode: {totals['ecomode']} ({ecomode_saved:.1f}% saved)")
    print(f"eco_token_advantage: {totals['caveman'] - totals['ecomode']}")
    print(f"eco_case_wins: {totals['eco_wins']}/{len(cases)}")
    print(f"exact_pass: {totals['exact_pass']}/{len(cases)}")

    ok = (
        totals["eco_wins"] == len(cases)
        and totals["exact_pass"] == len(cases)
        and totals["ecomode"] < totals["caveman"]
    )
    print(f"benchmark_pass: {'yes' if ok else 'no'}")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
