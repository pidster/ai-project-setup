---
id: skill.compositional.onboard-repo
kind: skill
scope: compositional
category: workflow
domain: onboard-repo
summary: Inspect a repository and generate initial AI-tool guidance.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.policy-check
  - skill.compositional.docs-update
  - rule.atomic.source-code
optional_tools: []
---

# Onboard Repo

Use project discovery to identify repository purpose, instruction files,
language ecosystems, package managers, tests, builds, services, CI, generated
files, security posture, and existing workflow documentation.

Preserve existing project guidance. Do not replace established instructions with
generic assumptions, and do not introduce vendor-specific policy as the source of
truth.

Generate initial AI-tool guidance from observed repository evidence: canonical
rules, reusable skills, vendor capability data, adapter notes, and generated
outputs where the project architecture supports them.

Run policy checks and available validation before delivery. Report evidence
used, guidance created or updated, validation performed, assumptions, and open
questions for maintainers.
