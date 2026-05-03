---
id: skill.compositional.pr-create
kind: skill
scope: compositional
category: workflow
domain: pr-create
summary: Prepare a pull request with summary, validation, and risk notes.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.review
  - skill.compositional.pre-commit
  - rule.atomic.git-safety
optional_tools: []
---

# PR Create

Inspect branch state, worktree status, staged changes, commit history, changed
files, and relevant project guidance before preparing a pull request.

Ensure the branch contains only intentional commits for the requested work. Do
not include unrelated local changes or generated churn that is not tied to the
change.

Run relevant validation or record why validation was unavailable. Review the diff
for design-impacting changes, generated output, security risk, and missing tests.

Write a pull request summary that covers user-visible behavior or content
changes, validation performed, risk, and follow-up work. Keep implementation
detail proportional to the review burden.
