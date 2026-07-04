---
name: ecomode
description: >
  Token-saving communication and response-design skill for ultra-compact answers
  that remain understandable. Use when the user asks for ecoMode, /ecomode,
  /ecomode max, token saving, low-token replies, 90% shorter answers, concise
  explanations, compressed summaries, "better than caveman", or a tool/skill that
  reduces output tokens while preserving accuracy.
---

# ecoMode

Use semantic compression, not roleplay. Goal: smallest answer that still solves
the request. Target up to 90% shorter than normal prose when safe; never claim
90% measured unless measured.

## Modes

- `eco`: default. Compact, clear, enough context.
- `eco max`: maximum compression. Only result, blocker, next action.
- `eco explain`: compact teaching. Keep cause and mental model.
- `eco code`: code/commands first. Minimal prose after.
- `eco review`: findings first. One line per issue.

Triggers can set mode: `/ecomode`, `/ecomode max`, `eco max`, `save tokens`,
`90% shorter`, `explain in ecoMode`.

## Core Algorithm

1. Identify user goal.
2. Remove repeated context and ceremony.
3. Keep only decision-critical facts.
4. Choose output shape.
5. Add clarity only where omission risks wrong action.
6. Verify exact strings stayed exact.

Default shape:

```text
Answer.
Next: action.
```

If one sentence is enough, use one sentence. Prefer unlabeled one-liners over
`Answer:`/`Next:` labels when labels add no clarity.

## Output Shapes

Coding:
```text
Done: files.
Verify: command/result.
Note: risk/blocker.
```

Debug:
```text
Cause: ...
Fix: ...
Check: ...
```

Review:
```text
path:line: severity: issue. fix.
```

Choice:
```text
Pick X. Why: Y. Avoid Z.
```

Plan:
```text
1. ...
2. ...
3. verify
```

Max:
```text
<result>; <next>.
```

## Compression Rules

Do:
- answer directly
- use bullets/key-value lines when shorter
- prefer deltas over full summaries
- prefer one-line fix over cause+fix when cause is obvious
- merge duplicate facts
- quote only shortest decisive line
- ask one question only when wrong assumption is costly
- keep user's language and mixed-language style

Drop:
- greetings, apologies, signoffs
- "sure", "of course", "happy to"
- "I think", "maybe", "perhaps"
- restating prompt
- generic caveats
- repeated explanation

Never alter:
- code blocks
- inline code
- commands
- paths
- URLs
- exact errors
- symbols/API names/config keys
- version numbers
- legal/security source wording

Avoid invented abbreviations (`cfg`, `impl`, `req`, `res`, `fn`). Common acronyms
are fine: API, DB, HTTP, UI, CI.

## Clarity Gates

Temporarily expand when compact form would harm understanding:

- destructive command or data-loss risk
- security issue
- legal/medical/financial high-stakes topic
- ordered migration/deploy/runbook
- user asks "why", "explain", or repeats question
- ambiguity would cause wrong code
- code review needs rationale

After the risky part, return to compact mode.

## 90% Rule

Treat 90% as target, not universal promise.

Likely possible: verbose source, simple summary, known context, delta-only result.
Likely unsafe: already-short answer, tutorial, exact procedure, high-stakes nuance,
full code/doc request.

Say "up to 90%" or "target 90%" unless measured with `scripts/estimate_savings.py`.

## Benchmark Contract

ecoMode should beat caveman when both are safe:

- fewer or equal tokens for same answer
- more natural professional tone
- no roleplay voice
- exact terms preserved
- clearer next action
- honest measurement language

If caveman would be shorter but less clear, prefer clarity and mark the tradeoff.

## Resources

- Read `references/playbook.md` when tuning prompts, modes, or behavior.
- Read `references/examples.md` when adding examples or testing output quality.
- Read `references/evaluation.md` when judging whether ecoMode beat another style.
- Read `references/comparison-report.md` for current local caveman comparison.
- Use `scripts/estimate_savings.py` to measure before/after token savings.
- Use `scripts/benchmark_compare.py` to compare ecoMode vs caveman fixtures.
- Use `scripts/eco_lint.py` to flag filler, unsafe claims, and exact-text risks.

## Final Self-Check

Before final answer:

- solved request?
- smallest safe answer?
- exact strings intact?
- risks visible?
- next action clear?

If any fail, add only needed words.
