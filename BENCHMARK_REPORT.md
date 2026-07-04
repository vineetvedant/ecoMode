# ecoMode Benchmark Report

Date: 2026-07-05  
Project: `D:\project skill\ecomode`  
Baseline: `D:\project skill\caveman\skills\caveman\SKILL.md`  
Tokenizer: `tiktoken:gpt-4o-mini`

## Summary

ecoMode beats caveman on the current local benchmark suite.

| Metric | Caveman | ecoMode |
|--------|---------|---------|
| Total tokens | 127 | 89 |
| Savings vs normal | 43.8% | 60.6% |
| Case wins | - | 6/6 |
| Exact preservation | - | 6/6 |
| Token advantage | - | 38 fewer than caveman |

Result: `benchmark_pass: yes`

## Method

Command:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

The benchmark compares three outputs for each case:

- `normal`: verbose baseline answer
- `caveman`: caveman-style compressed answer
- `ecomode`: ecoMode compressed answer

Each case checks:

- token count
- ecoMode token advantage over caveman
- required term preservation
- per-case win/loss

## Case Results

| Case | Normal | Caveman | ecoMode | ecoMode Advantage | Saved vs Normal | Exact | Win |
|------|--------|---------|---------|-------------------|-----------------|-------|-----|
| react-rerender | 39 | 22 | 14 | 8 | 64.1% | yes | yes |
| db-pooling | 31 | 16 | 11 | 5 | 64.5% | yes | yes |
| auth-expiry | 45 | 25 | 12 | 13 | 73.3% | yes | yes |
| deploy-order | 40 | 21 | 18 | 3 | 55.0% | yes | yes |
| review-double-charge | 43 | 22 | 18 | 4 | 58.1% | yes | yes |
| destructive-sql | 28 | 21 | 16 | 5 | 42.9% | yes | yes |

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

Caveman compresses sentence style. ecoMode removes unnecessary ideas first.

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
