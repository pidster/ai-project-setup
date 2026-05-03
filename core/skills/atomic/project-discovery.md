---
id: skill.atomic.project-discovery
kind: skill
scope: atomic
category: domain
domain: project-discovery
summary: Discover repository structure, ecosystems, commands, and local guidance.
depends_on: []
commands:
  - git
---

# Project Discovery

Inspect repository guidance before making assumptions.

Look for instruction files, manifests, lockfiles, package metadata, build files,
test configuration, CI configuration, and existing scripts.

Prefer repository-defined commands over generic commands when both exist.

Record uncertain findings as assumptions instead of converting them into policy.
