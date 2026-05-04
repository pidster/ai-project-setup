# Cursor

Status: provisional. Cursor's direct rule surfaces are verified, but the plugin
and marketplace model changed after the previous review and needs a follow-up
schema review before adapter changes.

## Sources

- Rules: <https://docs.cursor.com/en/context/rules>
- Custom commands: <https://docs.cursor.com/en/agent/chat/commands>
- Modes: <https://docs.cursor.com/agent>
- CLI MCP: <https://docs.cursor.com/cli/mcp>
- Plugin announcement: <https://cursor.com/blog/marketplace>
- Marketplace: <https://cursor.com/marketplace/>
- Marketplace plugin example: <https://cursor.com/marketplace/skills/plugin-builder>
- Verified plugin source example: <https://github.com/runlayer/plugins>

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
- Cursor Marketplace plugins now exist. Cursor states that plugins can bundle
  MCP servers, skills, subagents, rules, and hooks.
- Marketplace pages expose user-facing install affordances such as
  `/add-plugin <plugin>`.
- Verified public examples use root `.cursor-plugin/marketplace.json`.
- Verified public examples put plugin package metadata at
  `<plugin>/.cursor-plugin/plugin.json`.
- Marketplace entries can point `source` at a plugin subdirectory.
- Cursor CLI 3.0.16 does not expose plugin management commands. The verified
  user-facing install surface is still Cursor's marketplace `/add-plugin`
  command.
- Public marketplace submission and non-marketplace repository install flows are
  not yet verified.

## Adapter Notes

- Use `.cursor/rules/*.mdc` for full-fidelity scoped rules.
- Use `alwaysApply: true` only for short project-wide instructions.
- Use `globs` for path-scoped guidance.
- Use `description` for agent-requested rules.
- Use `.cursor/commands/` for manually invoked workflows.
- Keep the current generated output as `.cursor/rules/*.mdc` until we decide
  whether to target public Cursor Marketplace listing or a repo-hosted plugin
  source.
- A future Cursor plugin renderer should generate a root
  `.cursor-plugin/marketplace.json` only if we can support a valid public
  install path.
- A future Cursor plugin package should use `.cursor-plugin/plugin.json` inside
  the plugin payload and may include generated `skills/`, `commands/`, `rules/`,
  and `hooks/` once each schema is verified.

## Plugin Model

Cursor now has marketplace plugins, so the previous `direct_config_only` model is
stale. The structured model is marked provisional because package paths are now
verified but public submission and non-marketplace repository install flows still
need confirmation. See [plugin-model.yaml](../../vendors/cursor/plugin-model.yaml)
for details.

## Open Questions

- Can a plugin be installed from a public repository path, or only through the
  Cursor Marketplace?
- Is `/add-plugin <plugin>` the only supported user-facing install command?
- What is the public marketplace submission or publication process?
- What are the exact schemas for plugin-packaged rules, skills, subagents,
  hooks, commands, and MCP declarations?
