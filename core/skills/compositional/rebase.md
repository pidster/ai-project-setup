---
id: skill.compositional.rebase
kind: skill
scope: compositional
category: workflow
domain: rebase
summary: Rebase a branch with conflict handling and post-rebase validation.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.pre-commit
  - skill.compositional.test
  - rule.atomic.git-safety
optional_tools: []
---

# Rebase

Inspect branch state, upstream target, commit range, worktree status, and project
guidance before rebasing.

Do not rewrite public or shared history unless the workflow and user request
allow it. Preserve user changes and avoid destructive cleanup during conflict
resolution.

Resolve conflicts commit by commit when needed, preserving the intent of both the
rebased work and upstream changes. Regenerate derived files through the intended
generator when generated output is affected.

Validate the rebased result with checks appropriate to the changed and conflicted
surface. Report the upstream target, conflict handling, validation performed,
and any remaining risk.
