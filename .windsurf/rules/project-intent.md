---
trigger: always_on
description: Project architecture and policy boundaries for ai-project-setup
---

# Project Intent

Follow `AGENTS.md` as the primary repository instruction source.

This repository is a vendor-neutral content compiler for AI-tool rules, skills,
and instructions. Canonical policy belongs in core content. Vendor-specific files
adapt that content to each tool's mechanics and must not become separate policy
sources.

Keep language guidance generic by default. Add language-specific extensions only
where the language or ecosystem materially differs.

Raise conflicts between user instructions, `AGENTS.md`, design documents, and
vendor-specific mechanics instead of silently resolving them.
