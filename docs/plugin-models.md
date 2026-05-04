# Plugin Models

Last reviewed: 2026-05-04

This document defines how the project classifies vendor plugin and extension
models. It does not replace per-vendor capability data.

Use `vendors/<vendor>/plugin-model.yaml` for structured source-backed facts.
Use `docs/vendors/*.md` for product-specific human notes.

## Categories

`package_manifest`: the product has a first-class installable plugin package
with a manifest and optional bundled components.

`module_plugin`: the product loads executable plugin modules or package
dependencies, but does not use a dedicated plugin manifest package model.

`direct_config_only`: the product exposes project, user, system, or enterprise
configuration surfaces, but no verified repo-native plugin package model.

`none_verified`: no verified plugin or direct extension model has been recorded.

## Design Guidance

Keep plugin package metadata separate from direct project configuration.

Direct project configuration belongs in the normal adapter surfaces for a
product. Plugin package configuration belongs in plugin manifests, plugin-local
component files, or marketplace catalog files where the product supports them.

Do not infer plugin packaging from the existence of skills, hooks, MCP, commands,
or agents. A product can support those capabilities directly without supporting
an installable plugin package.

## Vendor Data

- [Claude Code](../vendors/claude/plugin-model.yaml)
- [Codex](../vendors/codex/plugin-model.yaml)
- [GitHub Copilot](../vendors/copilot/plugin-model.yaml)
- [Cursor](../vendors/cursor/plugin-model.yaml)
- [Devin](../vendors/devin/plugin-model.yaml)
- [OpenCode](../vendors/opencode/plugin-model.yaml)
- [Windsurf](../vendors/windsurf/plugin-model.yaml)
