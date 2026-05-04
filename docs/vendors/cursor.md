# Cursor

Status: verified from current Cursor docs.

## Sources

- Rules: <https://docs.cursor.com/en/context/rules>
- Custom commands: <https://docs.cursor.com/en/agent/chat/commands>
- Modes: <https://docs.cursor.com/agent>
- CLI MCP: <https://docs.cursor.com/cli/mcp>

## Surfaces

- `.cursor/rules/*.mdc`: project rules with MDC frontmatter.
- Rule activation types are represented by `description`, `globs`, and
  `alwaysApply`.
- Nested `.cursor/rules/` directories can scope rules to subdirectories.
- `AGENTS.md`: supported as a simple alternative to `.cursor/rules`.
- Cursor CLI also reads root `AGENTS.md` and `CLAUDE.md`.
- `.cursor/commands/*.md`: project custom commands.
- Custom modes exist in the product, but current docs do not define a
  repo-committed custom mode file format.
- MCP servers are supported for Cursor CLI through the same MCP configuration
  used by the editor.
- `.cursorrules`: legacy and deprecated.
- No current official Cursor docs found for repo-native `SKILL.md` agent skills.
- No current official Cursor docs found for repo-native event hooks comparable
  to richer vendors.

## Adapter Notes

- Use `.cursor/rules/*.mdc` for full-fidelity scoped rules.
- Use `alwaysApply: true` only for short project-wide instructions.
- Use `globs` for path-scoped guidance.
- Use `description` for agent-requested rules.
- Use `.cursor/commands/` for manually invoked workflows.
- Do not project canonical skills into Cursor as `SKILL.md` unless Cursor adds
  native skill support.

## Plugin Model

Cursor currently has direct configuration surfaces, with no verified repo-native
plugin package model. See
[plugin-model.yaml](../../vendors/cursor/plugin-model.yaml) for structured
details.
