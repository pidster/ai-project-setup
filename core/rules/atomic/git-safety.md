---
id: rule.atomic.git-safety
kind: rule
scope: atomic
category: policy
domain: git
summary: Git safety invariants for AI-assisted repository work.
depends_on: []
---

# Git Safety

Do not stage unrelated changes.

Do not discard or rewrite user changes unless the user explicitly requests it.

Before committing, inspect the diff and understand the scope being recorded.

Report dirty worktree state when it affects the requested task.
