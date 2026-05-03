---
id: skill.compositional.cleanup
kind: skill
scope: compositional
category: workflow
domain: cleanup
summary: Remove dead code, stale configuration, and unused generated artifacts safely.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.build
  - rule.atomic.source-code
optional_tools: []
---

# Cleanup

Use project discovery to understand ownership, entry points, generated files,
configuration references, tests, and package metadata before deleting or
simplifying anything.

Prefer small cleanup changes with clear evidence that the removed code,
configuration, dependency, or artifact is unused.

Do not mix broad refactors with cleanup unless the task explicitly asks for it.
Avoid changing public behavior, compatibility, generated-output conventions, or
security posture as a side effect.

Verify with commands that cover the removed surface. Report what was removed,
why it was safe to remove, validation performed, and any remaining references or
uncertainty.
