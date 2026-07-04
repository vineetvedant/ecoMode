# ecoMode Benchmark Report

Date: 2026-07-05  
Project: `D:\project skill\ecomode`  
Baseline: `D:\project skill\caveman\skills\caveman\SKILL.md`  
Tokenizer: `tiktoken:gpt-4o-mini`

## Summary

ecoMode beats the upstream baseline on the current local benchmark suite.

| Metric | Baseline | ecoMode |
|--------|---------|---------|
| Total tokens | 513 | 252 |
| Savings vs normal | 29.9% | 65.6% |
| Case wins | - | 16/16 |
| Exact preservation | - | 16/16 |
| Token advantage | - | 261 fewer than baseline |

Result: `benchmark_pass: yes`

## Method

Command:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

The benchmark compares three outputs for each case:

- `normal`: verbose baseline answer
- `caveman`: upstream baseline compressed answer
- `ecomode`: ecoMode compressed answer

Each case checks:

- token count
- ecoMode token advantage over baseline
- required term preservation
- per-case win/loss

## Case Results

| Case | Normal | Baseline | ecoMode | ecoMode Advantage | Saved vs Normal | Exact | Win |
|------|--------|---------|---------|-------------------|-----------------|-------|-----|
| react-rerender | 39 | 22 | 14 | 8 | 64.1% | yes | yes |
| db-pooling | 31 | 16 | 11 | 5 | 64.5% | yes | yes |
| auth-expiry | 45 | 25 | 12 | 13 | 73.3% | yes | yes |
| deploy-order | 40 | 21 | 18 | 3 | 55.0% | yes | yes |
| review-double-charge | 43 | 22 | 18 | 4 | 58.1% | yes | yes |
| destructive-sql | 28 | 21 | 16 | 5 | 42.9% | yes | yes |
| tcp-udp | 59 | 64 | 15 | 49 | 74.6% | yes | yes |
| node-memory-leak | 70 | 45 | 22 | 23 | 68.6% | yes | yes |
| sql-explain | 54 | 40 | 24 | 16 | 55.6% | yes | yes |
| hash-collisions | 46 | 39 | 14 | 25 | 69.6% | yes | yes |
| cors-error | 53 | 40 | 17 | 23 | 67.9% | yes | yes |
| debounce-search | 50 | 41 | 16 | 25 | 68.0% | yes | yes |
| git-rebase-merge | 47 | 38 | 15 | 23 | 68.1% | yes | yes |
| queue-topic | 50 | 32 | 16 | 16 | 68.0% | yes | yes |
| sql-injection-review | 37 | 24 | 13 | 11 | 64.9% | yes | yes |
| spanish-pooling | 40 | 23 | 11 | 12 | 72.5% | yes | yes |

## Sample 90% Target Check

Command:

```bash
python scripts/estimate_savings.py --before tests/sample_before.txt --after tests/sample_after.txt
```

Result:

| Metric | Value |
|--------|-------|
| Before tokens | 65 |
| After tokens | 12 |
| Saved tokens | 53 |
| Savings | 81.5% |
| 90% target met | no |

Interpretation: ecoMode reaches extreme compression on this sample, but not 90%.
The skill correctly treats 90% as an "up to / target" claim unless measured.

## Why ecoMode Wins

The upstream baseline compresses sentence style. ecoMode removes unnecessary ideas first.

ecoMode advantages:

- semantic compression before grammar compression
- no roleplay voice
- shorter whole-answer output
- explicit exact-text preservation
- clearer action-focused outputs
- honest benchmark language

## Limits

This is a local benchmark suite, not a universal claim.

Current suite size: 16 cases. It covers:

- React explanation
- DB explanation
- auth boundary bug
- deploy ordering
- code review finding
- destructive SQL warning
- TCP vs UDP
- Node memory leak
- SQL EXPLAIN
- hash collisions
- CORS
- debounce
- git rebase vs merge
- queue vs topic
- SQL injection review
- Spanish DB pooling

Before claiming broad superiority, add more cases:

- long tutorials
- multilingual prompts
- code generation finals
- legal/security warnings
- command outputs
- PR reviews
- user confusion/clarification

## Reproduce

From `D:\project skill\ecomode`:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
python scripts/estimate_savings.py --before tests/sample_before.txt --after tests/sample_after.txt
python scripts/eco_lint.py --file tests/eco_outputs.txt --max-lines 10
```

Expected:

```text
benchmark_pass: yes
target_90_met: no
eco_lint: pass
```
