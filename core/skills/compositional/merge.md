---
id: skill.compositional.merge
kind: skill
scope: compositional
category: workflow
domain: merge
summary: Update a branch, resolve conflicts, validate, and prepare a safe merge.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.pre-commit
  - skill.compositional.test
  - rule.atomic.git-safety
optional_tools: []
---

# Merge

Inspect branch state, remote state, worktree status, changed files, and project
guidance before merging or updating a branch.

Do not discard local or user changes to simplify a merge. Preserve intentional
changes from both sides and inspect conflicts in their surrounding context.

Resolve conflicts by maintaining behavior, public contracts, generated-output
conventions, and security posture. Regenerate derived files through the intended
generator when conflicts affect generated output.

Validate the merged result with checks appropriate to the conflict surface.
Report the merge source, conflicts resolved, validation performed, and any
remaining risk.
