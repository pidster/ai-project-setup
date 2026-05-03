---
id: skill.atomic.git
kind: skill
scope: atomic
category: domain
domain: git
summary: Use Git safely and intentionally during AI-assisted changes.
depends_on:
  - rule.atomic.git-safety
commands:
  - git
---

# Git

Use Git to inspect state, understand changed files, and prepare intentional
commits.

Check worktree status before staging or committing.

Stage only files that belong to the requested change.

When reporting work, distinguish committed changes, uncommitted changes, and
untracked files.
