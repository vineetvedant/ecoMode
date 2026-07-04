# ecoMode

Ultra-compact communication skill for Codex. ecoMode is built to save output
tokens while keeping answers understandable, professional, and technically exact.

It is inspired by the same problem space as an existing upstream compression
skill, but uses a different strategy:

- upstream baseline compresses sentence style
- ecoMode removes unnecessary meaning first, then compresses wording

That makes ecoMode shorter on the included benchmark while avoiding roleplay
voice.

## Results

Tested against upstream baseline main:

```text
upstream SHA: 0d95a81d35a9f2d123a5e9430d1cfc43d55f1bb0
benchmark cases: 16
ecoMode wins: 16/16
exact preservation: 16/16
baseline tokens: 513
ecoMode tokens: 252
ecoMode advantage: 261 fewer tokens
baseline savings vs normal: 29.9%
ecoMode savings vs normal: 65.6%
benchmark_pass: yes
```

Core skill instruction overhead:

```text
baseline SKILL.md: 1245 tokens
ecoMode SKILL.md: 1049 tokens
ecoMode saves 196 instruction tokens
```

Full report:

- [Upstream baseline comparison](UPSTREAM_CAVEMAN_COMPARISON_REPORT.md)
- [Benchmark report](BENCHMARK_REPORT.md)

## Honest Claim

ecoMode beats the upstream baseline on the included 16-case local benchmark.

It is not proven to be the best compression skill in the world. That would need
a larger independent benchmark across many real tasks, models, languages, and
whole-session cost traces.

The 90% goal is treated honestly:

- `up to 90%` when task allows
- `target 90%` when optimizing
- measured only when benchmark output proves it

## Why ecoMode Works

Most terse modes save tokens by dropping grammar:

```text
Pool reuse open DB connections. No new connection per request.
```

ecoMode saves more by deleting unnecessary ideas:

```text
Pool reuses DB connections; skips per-request handshake.
```

Core rules:

- answer with the smallest useful shape
- prefer delta-only output
- preserve exact code, commands, paths, URLs, errors, APIs, and config keys
- expand only when compression would cause risk or confusion
- avoid roleplay voice
- benchmark claims instead of guessing

## Modes

| Mode | Use |
|------|-----|
| `eco` | Default compact answer |
| `eco max` | Maximum safe compression |
| `eco explain` | Short teaching answer with cause and mental model |
| `eco code` | Code or commands first, minimal prose |
| `eco review` | One-line actionable review findings |

Example prompt:

```text
Use ecoMode. Explain database connection pooling.
```

Maximum compression:

```text
Use ecoMode max. Explain why my React component re-renders.
```

## Install For Codex

Copy this folder into your Codex skills directory:

```powershell
Copy-Item -Path . -Destination "$env:USERPROFILE\.codex\skills\ecomode" -Recurse -Force
```

Restart Codex, then invoke:

```text
[$ecomode](C:\Users\YOUR_NAME\.codex\skills\ecomode\SKILL.md) explain git rebase vs merge
```

Or use natural language:

```text
Use ecoMode. Save tokens. Review this diff.
```

## Repository Layout

```text
ecomode/
├── SKILL.md
├── README.md
├── BENCHMARK_REPORT.md
├── UPSTREAM_CAVEMAN_COMPARISON_REPORT.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── comparison-report.md
│   ├── evaluation.md
│   ├── examples.md
│   └── playbook.md
├── scripts/
│   ├── benchmark_compare.py
│   ├── eco_lint.py
│   └── estimate_savings.py
└── tests/
    ├── benchmark_cases.json
    ├── eco_outputs.txt
    ├── sample_after.txt
    └── sample_before.txt
```

## Benchmark

Run:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

Expected:

```text
benchmark_pass: yes
```

Measure any before/after pair:

```bash
python scripts/estimate_savings.py --before before.txt --after after.txt
```

Lint an ecoMode output:

```bash
python scripts/eco_lint.py --file output.txt
```

## Design Philosophy

ecoMode optimizes for total useful answer cost, not just sentence style.

Compression order:

1. remove repeated context
2. remove unnecessary ideas
3. preserve exact technical strings
4. choose a compact output shape
5. add clarity only where omission would cause wrong action

## Safety

ecoMode expands when short output would be risky:

- destructive commands
- security findings
- legal, medical, or financial topics
- ordered migrations or deploys
- user confusion
- exact reproduction steps

Short is good. Wrong is expensive.

## License

MIT. See [LICENSE](LICENSE).
