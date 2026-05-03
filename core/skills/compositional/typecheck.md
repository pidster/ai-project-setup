---
id: skill.compositional.typecheck
kind: skill
scope: compositional
category: workflow
domain: typecheck
summary: Run static type checks and interpret failures.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Typecheck

Use project discovery to identify typecheck commands, compiler checks, typed
workspaces, generated type artifacts, and CI-equivalent validation.

Prefer repository-defined typecheck or compiler-check commands over generic tool
invocations.

Scope type checks to affected packages when supported. Broaden when shared types,
public contracts, generated clients, dependency metadata, or cross-package
interfaces are affected.

Do not weaken type strictness, suppress errors, or cast away uncertainty just to
make the check pass. Fix the underlying contract or report the unresolved type
risk.
