# Documentation Index

This directory separates quick lookup from detailed vendor research.

## Quick Lookup

Use this table first when deciding which adapter surface to target. Product
details, sources, caveats, and adapter notes live in the linked vendor pages.

| Product | Rich Fit | Instructions / Rules | Skills | Workflows / Commands | Agents | Hooks / Runtime Controls | MCP / Plugins | Details |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Claude Code | Full | `CLAUDE.md`, `.claude/rules/*` | `.claude/skills/*` | `.claude/commands/*` | `.claude/agents/*` | `.claude/settings.json` hooks; plugin `hooks/hooks.json`; permissions | MCP, plugins | [Claude Code](vendors/claude-code.md) |
| Codex | Full, different command/rule shape | `AGENTS.md`, `AGENTS.override.md`, nested instructions, fallback filenames; `.codex/rules/*` for execution policy | `.agents/skills/*` | built-in slash commands, skill invocation; no verified custom command prompt files | `.codex/agents/*.toml` | `.codex/config.toml`, hooks, approvals, sandbox | MCP, plugins, connector apps | [Codex](vendors/codex.md) |
| Cursor | Partial, plugin model provisional | `.cursor/rules/*.mdc`, `AGENTS.md` / `CLAUDE.md` in CLI; plugin rules announced | Plugin skills announced; package schema pending | `.cursor/commands/*`, manual rules | Plugin subagents announced; schema pending | Plugin hooks announced; schema pending | MCP, Marketplace plugins | [Cursor](vendors/cursor.md) |
| Devin for Terminal | Full, different rule shape | `AGENTS.md`, `AGENT.md`, `CLAUDE.md`, nested/imported rules; no `.devin/rules/*` | `.devin/skills/*`, `.agents/skills/*` | skills invoked as `/skill-name` | `.devin/agents/*`, `.agents/agents/*` | `.devin/hooks.v1.json`, `.devin/config.json` | MCP via `.devin/config.json` | [Devin](vendors/devin.md) |
| Devin product | Partial | `AGENTS.md`, external repo setup | `.agents/skills/*`, also scans `.github/skills/*`, `.claude/skills/*` | External repo setup / skills | No verified committed agent profile for product surface | External repo setup | External integrations | [Devin](vendors/devin.md) |
| GitHub Copilot | Full | `.github/copilot-instructions.md`, `.github/instructions/*`, `AGENTS.md` where supported | `.github/skills/*`, `.agents/skills/*`, `.claude/skills/*` | `.github/prompts/*`, custom agents | `.github/agents/*` | `.github/hooks/*` | MCP tools | [GitHub Copilot](vendors/github-copilot.md) |
| OpenCode | Full | `AGENTS.md`, `CLAUDE.md`, `opencode.json` instruction globs | `.opencode/skills/*`, `.agents/skills/*`, `.claude/skills/*` | `.opencode/commands/*`, `opencode.json` commands | `.opencode/agents/*`, `opencode.json` agents | permissions, plugin events | MCP, plugins, custom tools | [OpenCode](vendors/opencode.md) |
| Windsurf | Full except committed agents | `AGENTS.md`, `.windsurf/rules/*` | `.windsurf/skills/*`, `.agents/skills/*`, optional `.claude/skills/*` | `.windsurf/workflows/*` | No verified repo-committed agent profile | `.windsurf/hooks.json` | MCP | [Windsurf](vendors/windsurf.md) |

## Concept Docs

- [Design intent](design-intent.md): architecture, boundaries, canonical content
  model, and long-term direction.
- [Design intent review](design-intent-review.md): review findings and open
  design questions.
- [Vendor adapter capabilities](vendor-adapter-capabilities.md): shared feature
  vocabulary, rich profile, adapter degradation rules, and cross-vendor concept
  mapping.
- [Plugin models](plugin-models.md): shared vocabulary for direct configuration,
  module plugins, and installable plugin packages.
- [Distribution and install contract](distribution-install-plan.md): current
  one-distribution-per-vendor `dist/` contract and NPX installer behavior.
- [Activity skill backlog](activity-skill-backlog.md): implemented
  compositional activity skills and original batching rationale.

## Vendor Details

- [Vendor detail index](vendors/README.md)
- [Claude Code](vendors/claude-code.md)
- [Codex](vendors/codex.md)
- [Cursor](vendors/cursor.md)
- [Devin](vendors/devin.md)
- [GitHub Copilot](vendors/github-copilot.md)
- [OpenCode](vendors/opencode.md)
- [Windsurf](vendors/windsurf.md)

## Maintenance

When vendor behavior changes:

1. Verify current official documentation.
2. Update the relevant `vendors/*/capabilities.yaml` file.
3. Update the relevant `vendors/*/plugin-model.yaml` file if packaging or plugin
   behavior changed.
4. Update the matching `docs/vendors/*.md` page.
5. Update the table in this file only when the quick-reference answer changes.
6. Keep generated output under `dist/` in sync with adapter behavior.
