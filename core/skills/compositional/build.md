---
id: skill.compositional.build
kind: skill
scope: compositional
category: workflow
domain: build
summary: Run repository-appropriate build or package checks.
depends_on:
  - skill.atomic.project-discovery
  - skill.atomic.language-toolchain
  - rule.atomic.source-code
optional_tools: []
---

# Build

Use project discovery to identify build scripts, package commands, generated
artifact requirements, and CI build steps.

Prefer existing repository build commands over direct compiler, bundler, or
packager invocations when both are available.

Scope the build to the affected package or workspace when the repository
structure supports it. Broaden to the full build when shared configuration,
public artifacts, dependency metadata, or cross-package contracts are affected.

Stop on failures. Preserve the exact failing command, identify whether the
failure is compile-time, packaging, generation, dependency, or configuration
related, and report the next useful diagnostic step.
