# Vendor Capability Data

This directory contains declarative vendor capability and plugin-model data used
by adapters. These files describe verified product surfaces; they should not
contain rendering logic or canonical project policy.

Use [docs/README.md](../docs/README.md) for the quick compatibility table and
[docs/vendors/README.md](../docs/vendors/README.md) for source-backed vendor
details.

## Capability Maps

- [Claude Code](claude/capabilities.yaml) and
  [plugin model](claude/plugin-model.yaml)
- [Codex](codex/capabilities.yaml) and
  [plugin model](codex/plugin-model.yaml)
- [Cursor](cursor/capabilities.yaml) and
  [plugin model](cursor/plugin-model.yaml)
- [Devin](devin/capabilities.yaml) and
  [plugin model](devin/plugin-model.yaml)
- [GitHub Copilot](copilot/capabilities.yaml) and
  [plugin model](copilot/plugin-model.yaml)
- [OpenCode](opencode/capabilities.yaml) and
  [plugin model](opencode/plugin-model.yaml)
- [Windsurf](windsurf/capabilities.yaml) and
  [plugin model](windsurf/plugin-model.yaml)

## Maintenance

When vendor behavior changes, verify the current official documentation before
editing capability or plugin-model data. Update the matching `docs/vendors/*.md`
page, then update the `docs/README.md` compatibility table only when the
quick-reference answer changes.
