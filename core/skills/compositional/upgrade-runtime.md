---
id: skill.compositional.upgrade-runtime
kind: skill
scope: compositional
category: workflow
domain: upgrade-runtime
summary: Upgrade language, runtime, or framework versions with compatibility checks.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.update-dependencies
  - skill.compositional.test
  - skill.compositional.build
  - rule.atomic.source-code
optional_tools: []
---

# Upgrade Runtime

Use project discovery to identify runtime declarations, version managers,
framework metadata, lockfiles, CI matrices, container images, deployment
configuration, and compatibility constraints.

Inspect release notes, migration guides, deprecations, breaking changes, and
ecosystem support windows before applying the upgrade.

Keep the upgrade scoped to the requested runtime, language, or framework unless
the migration explicitly requires dependency or configuration updates.

Update generated files, lockfiles, CI configuration, and docs through intended
workflows. Verify with builds, tests, type checks, or end-to-end checks
appropriate to the runtime surface. Report compatibility impact and remaining
migration work.
