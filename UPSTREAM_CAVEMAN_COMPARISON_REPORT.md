# ecoMode vs Upstream Baseline Report

Date: 2026-07-05  
ecoMode path: `D:\project skill\ecomode`  
Upstream repo: `https://github.com/JuliusBrussee/caveman`  
Upstream ref tested: `origin/main`  
Upstream SHA: `0d95a81d35a9f2d123a5e9430d1cfc43d55f1bb0`  
Tokenizer: `tiktoken:gpt-4o-mini`

## Truth First

ecoMode performs better than the tested upstream compression baseline on this local benchmark
suite.

This does **not** prove ecoMode is better than every skill on the internet. It
proves ecoMode beats the tested upstream baseline across the current
16-case suite.

## Result

```text
benchmark_pass: yes
eco_case_wins: 16/16
exact_pass: 16/16
```

| Metric | Baseline | ecoMode | Winner |
|--------|---------|---------|--------|
| Output tokens | 513 | 252 | ecoMode |
| Savings vs normal | 29.9% | 65.6% | ecoMode |
| Case wins | - | 16/16 | ecoMode |
| Exact preservation | - | 16/16 | ecoMode |
| Token advantage | - | 261 fewer than baseline | ecoMode |
| Skill instruction tokens | 1245 | 1049 | ecoMode |

## Benchmark Command

From `D:\project skill\ecomode`:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

Output:

```text
method: tiktoken:gpt-4o-mini
react-rerender: normal=39 baseline=22 ecomode=14 eco_delta=+8 saved=64.1% exact=True win=True
db-pooling: normal=31 baseline=16 ecomode=11 eco_delta=+5 saved=64.5% exact=True win=True
auth-expiry: normal=45 baseline=25 ecomode=12 eco_delta=+13 saved=73.3% exact=True win=True
deploy-order: normal=40 baseline=21 ecomode=18 eco_delta=+3 saved=55.0% exact=True win=True
review-double-charge: normal=43 baseline=22 ecomode=18 eco_delta=+4 saved=58.1% exact=True win=True
destructive-sql: normal=28 baseline=21 ecomode=16 eco_delta=+5 saved=42.9% exact=True win=True
tcp-udp: normal=59 baseline=64 ecomode=15 eco_delta=+49 saved=74.6% exact=True win=True
node-memory-leak: normal=70 baseline=45 ecomode=22 eco_delta=+23 saved=68.6% exact=True win=True
sql-explain: normal=54 baseline=40 ecomode=24 eco_delta=+16 saved=55.6% exact=True win=True
hash-collisions: normal=46 baseline=39 ecomode=14 eco_delta=+25 saved=69.6% exact=True win=True
cors-error: normal=53 baseline=40 ecomode=17 eco_delta=+23 saved=67.9% exact=True win=True
debounce-search: normal=50 baseline=41 ecomode=16 eco_delta=+25 saved=68.0% exact=True win=True
git-rebase-merge: normal=47 baseline=38 ecomode=15 eco_delta=+23 saved=68.1% exact=True win=True
queue-topic: normal=50 baseline=32 ecomode=16 eco_delta=+16 saved=68.0% exact=True win=True
sql-injection-review: normal=37 baseline=24 ecomode=13 eco_delta=+11 saved=64.9% exact=True win=True
spanish-pooling: normal=40 baseline=23 ecomode=11 eco_delta=+12 saved=72.5% exact=True win=True

total_normal: 732
total_baseline: 513 (29.9% saved)
total_ecomode: 252 (65.6% saved)
eco_token_advantage: 261
eco_case_wins: 16/16
exact_pass: 16/16
benchmark_pass: yes
```

## Skill Instruction Overhead

Command:

```bash
python scripts/estimate_savings.py --before "D:/project skill/caveman/skills/caveman/SKILL.md" --after "D:/project skill/ecomode/SKILL.md"
```

Output:

```text
before_tokens: 1245
after_tokens: 1049
saved_tokens: 196
savings_percent: 15.7%
```

Interpretation: ecoMode's loaded core skill instruction is smaller than
the upstream baseline's loaded core skill instruction. Extra ecoMode references are
progressively loaded only when needed.

## Why ecoMode Performs Better Here

The upstream baseline mainly compresses grammar and tone. ecoMode removes whole unnecessary
ideas first, then compresses wording.

ecoMode advantages in this suite:

- delta-first answers
- no roleplay/tone overhead
- shorter next-action phrasing
- exact-text preservation checks
- lower core instruction overhead
- honest 90% target language
- benchmark and lint scripts included

## 90% Claim Check

Command:

```bash
python scripts/estimate_savings.py --before tests/sample_before.txt --after tests/sample_after.txt
```

Output:

```text
before_tokens: 65
after_tokens: 12
saved_tokens: 53
savings_percent: 81.5%
target_90_met: no
```

Interpretation: ecoMode reached extreme compression on the sample but did not
hit 90%. The skill correctly says "up to 90%" or "target 90%" unless measured.

## Limits

This benchmark is stronger than before, but still limited.

Current coverage:

- React debugging
- DB pooling
- auth boundary bug
- deploy order
- code review
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
- Spanish response

Still missing:

- 100+ randomized tasks
- real model-generated A/B runs
- human clarity ratings
- long code-generation tasks
- full PR review threads
- multilingual set beyond one Spanish case
- cost accounting across whole sessions

## Verdict

ecoMode is performing better than the tested upstream baseline on the current
expanded local benchmark.

Best honest claim:

> ecoMode beats the upstream baseline on this 16-case local benchmark with 16/16 wins,
> 65.6% output savings vs 29.9%, and 15.7% lower core skill instruction overhead.

Do not claim:

> ecoMode is proven best of all skills everywhere.

That requires broader independent benchmarking.
