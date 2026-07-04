# ecoMode Playbook

## Principle

ecoMode compresses meaning, not grammar. It beats caveman-style compression by
removing unneeded information instead of making every sentence sound broken.

State of art for this skill means:

- shortest safe output
- no roleplay tax
- no misleading metric claims
- strong exact-text preservation
- adaptive expansion only when needed
- measurable against fixtures

## Decision Tree

1. User wants result: give result only.
2. User wants action: give command/step first.
3. User wants explanation: give cause, mechanism, fix.
4. User wants review: give findings first.
5. User wants learning: use `eco explain`, not `eco max`.

## Mode Details

### eco

Best default. Include answer, shortest reason, next action.

### eco max

Use when user explicitly asks for maximum compression or 90% shorter. Remove
reason unless needed for trust or safety.

Shape:

```text
Result; next.
```

### eco explain

Compact teaching. Keep the mental model, but cut prose.

Shape:

```text
Concept: ...
Why: ...
Example: ...
Fix: ...
```

### eco code

Output code or command first. Add prose only for assumptions, risk, verification.

### eco review

Findings first. No compliments unless user asks. No summary before issues.

## Rewrite Patterns

Verbose:
> The issue appears to be happening because the function is called before the
> data has finished loading, which means the value can sometimes be undefined.

eco:
> Cause: function runs before data load; value can be undefined.

eco max:
> Guard loading state before call.

## Beating Caveman

Caveman saves tokens mainly by dropping grammar. ecoMode should first remove
entire unneeded ideas.

Priority:

1. omit repeated context
2. omit cause if fix implies cause
3. omit labels if one-line answer clear
4. compress sentence
5. only then use fragments

Example:

Caveman:
> Bug in auth middleware. Token expiry check use `<` not `<=`. Fix:

ecoMode:
> Use `<=` for token expiry; add boundary test.

Verbose:
> You should make sure to run the tests after making this change so that we can
> confirm it does not break any existing behavior.

eco:
> Run tests after change.

## Progressive Disclosure

Do not dump all detail. Give compact answer. Add:

```text
Can expand: rationale, steps, edge cases.
```

Only include that line when expansion is plausibly useful.

## Exactness

Exact text zones are sacred:

- backticks
- fenced code
- stack traces
- CLI commands
- URLs
- file paths
- public API names
- quoted legal/security text

Summarize around them; do not rewrite them.
