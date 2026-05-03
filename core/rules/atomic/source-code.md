---
id: rule.atomic.source-code
kind: rule
scope: atomic
category: policy
domain: source-code
summary: General source-code invariants that apply across programming languages.
depends_on: []
---

# Source Code

Preserve the existing project style and public behavior unless the task explicitly
requires a change.

Prefer small, cohesive changes. Avoid broad rewrites, unused abstractions, and
speculative generalization.

Do not weaken validation, authorization, error handling, typing, or tests just to
make a change easier.

Keep generated code distinct from hand-authored code and update generated files
through the intended generator where one exists.
