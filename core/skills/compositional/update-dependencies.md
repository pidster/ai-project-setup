---
id: skill.compositional.update-dependencies
kind: skill
scope: compositional
category: workflow
domain: update-dependencies
summary: Update dependency sets safely and verify affected behavior.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.build
  - rule.atomic.security
  - rule.atomic.source-code
optional_tools: []
---

# Update Dependencies

Use project discovery to identify package managers, manifests, lockfiles,
workspaces, dependency groups, changelog sources, and existing update commands.

Keep updates scoped to the requested dependency, ecosystem, or risk unless the
task explicitly asks for a broad refresh.

Inspect meaningful release notes, migration notes, security advisories, and
breaking-change signals before accepting major or behavior-sensitive updates.

Update generated lockfiles or dependency metadata through the intended package
manager. Do not hand-edit generated dependency output unless the ecosystem
explicitly requires it.

Verify with the narrowest meaningful tests or builds, then broaden when shared
runtime behavior, public contracts, security-sensitive code, or generated
artifacts are affected.
