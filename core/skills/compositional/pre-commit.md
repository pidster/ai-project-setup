---
id: skill.compositional.pre-commit
kind: skill
scope: compositional
category: workflow
domain: pre-commit
summary: Run repository-appropriate checks before committing.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
optional_tools: []
---

# Pre-Commit

Use project discovery to identify affected ecosystems and available validation
commands.

Prefer existing repository scripts and CI-equivalent commands over invented
commands.

Run the narrowest meaningful checks first, then broaden if the change touches
shared behavior, public contracts, generated artifacts, or security-sensitive
code.

Stop on failures, preserve the exact failing command, and report the next useful
debugging step.
