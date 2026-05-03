---
id: skill.compositional.migrate
kind: skill
scope: compositional
category: workflow
domain: migrate
summary: Run a structured codebase migration with checkpoints and validation.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.build
  - skill.compositional.review
  - rule.atomic.source-code
optional_tools: []
---

# Migrate

Use project discovery to identify the migration scope, affected packages,
public contracts, generated artifacts, tests, tooling, and compatibility
constraints.

Break large migrations into checkpoints that can be reviewed and validated.
Avoid mixing unrelated cleanup, formatting churn, or behavior changes into the
migration unless explicitly required.

Apply established project patterns and migration tools before inventing new
abstractions. Preserve public behavior unless the migration intentionally changes
it and the compatibility impact is documented.

Validate incrementally and at the final scope. Report migration strategy,
checkpoints completed, validation performed, behavior changes, and remaining
follow-up work.
