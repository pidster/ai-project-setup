---
id: skill.compositional.coverage
kind: skill
scope: compositional
category: workflow
domain: coverage
summary: Measure coverage and identify meaningful validation gaps.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - rule.atomic.source-code
optional_tools: []
---

# Coverage

Use project discovery to identify existing coverage commands, reports, CI
thresholds, and affected packages or workspaces.

Prefer repository-defined coverage commands over generic tool invocations.

Measure coverage only where it can inform risk. Focus on meaningful gaps in
changed behavior, public contracts, edge cases, error paths, and
security-sensitive logic. Avoid adding shallow tests only to improve aggregate
percentages.

Report the command used, relevant coverage signal, uncovered risk, and the
smallest useful test or validation follow-up.
