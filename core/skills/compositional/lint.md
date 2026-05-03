---
id: skill.compositional.lint
kind: skill
scope: compositional
category: workflow
domain: lint
summary: Run repository linters and interpret failures.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Lint

Use project discovery to identify linters, formatter overlap, configuration
files, affected packages, CI lint commands, and repository-defined scripts.

Prefer repository-defined lint commands over generic tool invocations.

Scope linting to the affected package or workspace when supported. Broaden when
shared configuration, generated artifacts, public contracts, or cross-package
code are affected.

Treat lint failures as signals about correctness, consistency, or maintainability
within the project style. Do not silence rules or weaken configuration without
explicit rationale.
