---
id: skill.compositional.scaffold-feature
kind: skill
scope: compositional
category: workflow
domain: scaffold-feature
summary: Create a new feature following existing project structure and patterns.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - skill.compositional.test
  - skill.compositional.docs-update
  - rule.atomic.source-code
optional_tools: []
---

# Scaffold Feature

Use project discovery to identify existing feature layout, naming conventions,
entry points, tests, docs, generated files, configuration, and ownership
boundaries.

Follow established project patterns before introducing new abstractions,
directories, dependencies, or framework conventions.

Create the smallest useful feature skeleton that supports the requested
workflow: source files, tests, configuration, docs, generated artifacts, and
integration points where appropriate.

Verify the scaffold with targeted tests, builds, type checks, or generated-output
freshness checks. Report files created, patterns followed, validation performed,
and intentional gaps left for later implementation.
