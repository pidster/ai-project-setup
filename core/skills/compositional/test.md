---
id: skill.compositional.test
kind: skill
scope: compositional
category: workflow
domain: test
summary: Select and run repository-appropriate tests for a change.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Test

Use project discovery to identify test commands, test configuration, changed
files, and affected packages or workspaces.

Prefer repository-defined test scripts and CI-equivalent commands over generic
test invocations.

Run the narrowest meaningful test first when the affected surface is clear.
Broaden to package, workspace, integration, or full-suite tests when the change
touches shared behavior, public contracts, generated artifacts, build setup, or
security-sensitive code.

Stop on failures. Preserve the exact failing command, summarize the failing
surface, and report the next useful isolation step.
