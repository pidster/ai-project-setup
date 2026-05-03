---
id: skill.compositional.release
kind: skill
scope: compositional
category: workflow
domain: release
summary: Prepare changelog, versioning, tags, artifacts, and release notes.
depends_on:
  - skill.atomic.git
  - skill.atomic.project-discovery
  - skill.compositional.build
  - skill.compositional.test
  - skill.compositional.sync-generated
  - rule.atomic.git-safety
optional_tools: []
---

# Release

Use project discovery to identify release process documentation, version files,
changelog conventions, package artifacts, tags, signing, publishing steps, and
CI release checks.

Inspect the commit range and generated artifacts that belong to the release.
Separate user-facing changes, internal maintenance, security fixes, breaking
changes, and migration notes.

Update version metadata, changelog entries, release notes, generated artifacts,
and package manifests through the repository's intended workflow.

Run release validation before tagging or publishing when available. Report the
release version, commit range, artifacts, validation performed, publishing
status, and any manual follow-up.
