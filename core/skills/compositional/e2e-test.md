---
id: skill.compositional.e2e-test
kind: skill
scope: compositional
category: workflow
domain: e2e-test
summary: Run browser or end-to-end validation against realistic workflows.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.service-start
  - skill.compositional.test
  - rule.atomic.source-code
optional_tools: []
---

# E2E Test

Use project discovery to identify end-to-end test frameworks, service startup
requirements, fixtures, seeded data, browser dependencies, and CI-equivalent
commands.

Prefer repository-defined end-to-end commands and documented service setup over
generic tool invocations.

Run focused scenarios that cover the changed user workflow or integration
surface. Broaden when routing, authentication, persistence, public contracts, or
shared UI behavior are affected.

Preserve failing artifacts, logs, screenshots, traces, or videos when available.
Report the command used, service state, scenario coverage, failures, and any
environment limitation.
