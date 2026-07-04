# ecoMode Evaluation

Use this to judge whether ecoMode output is better than an upstream compact-output baseline.

## Scorecard

Rate 0-2 each:

- Solves request
- Preserves facts
- Clear next action
- No needless prose
- No harmful omission
- Exact strings preserved
- Natural professional tone

Pass: 12/14 or higher.

## Savings Bands

- 0-30%: weak compression
- 31-60%: useful compression
- 61-80%: strong compression
- 81-90%: extreme compression
- 90%+: only realistic for verbose source or delta-only answers

## Failures

Fail output if it:

- claims measured 90% without measurement
- hides safety risk
- changes command/code/error text
- asks unnecessary questions
- restates user prompt
- uses roleplay voice
- drops reason user needs to trust answer

## Comparison To Baseline

ecoMode should win by:

- natural language, no roleplay
- delta-only answers
- mode-specific output contracts
- honest measurement
- clarity gates
- exact-text protection

The baseline may be shorter sentence-by-sentence, but ecoMode should be shorter for
whole-answer cost by omitting irrelevant content.

## Benchmark Command

Run:

```bash
python scripts/benchmark_compare.py --cases tests/benchmark_cases.json
```

Pass target:

- ecoMode wins every case or reports intentional safety tradeoff
- exact preservation 100%
- no filler lint issues
- average token saving vs normal is stronger than baseline
