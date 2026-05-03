---
id: skill.atomic.language-toolchain
kind: skill
scope: atomic
category: domain
domain: language-toolchain
summary: Select language and package tooling from repository evidence.
depends_on:
  - skill.atomic.project-discovery
commands: []
---

# Language Toolchain

Select tooling from repository evidence such as manifests, lockfiles, scripts,
tool configuration, CI configuration, and user instructions.

Do not assume a project uses a tool because the repository contains one matching
file. Prefer the narrowest command that validates the files being changed.

When multiple ecosystems are present, scope commands to the affected workspace or
package where possible.
