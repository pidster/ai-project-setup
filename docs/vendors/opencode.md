# OpenCode

Status: verified from current OpenCode docs.

## Sources

- Rules: <https://opencode.ai/docs/rules>
- Config: <https://opencode.ai/docs/config/>
- Agents: <https://opencode.ai/docs/agents/>
- Commands: <https://opencode.ai/docs/commands/>
- Skills: <https://opencode.ai/docs/skills/>
- Plugins: <https://opencode.ai/docs/plugins/>
- Ecosystem: <https://opencode.ai/docs/ecosystem/>
- Custom tools: <https://opencode.ai/docs/custom-tools/>
- Permissions: <https://opencode.ai/docs/permissions>

## Surfaces

- `AGENTS.md`: primary project rules.
- `CLAUDE.md`: project fallback when `AGENTS.md` is absent.
- `opencode.json`: project config.
- `opencode.json` `instructions`: local, globbed, or remote instruction files.
- `.opencode/commands/*.md` and `opencode.json` `command`: custom commands.
- `opencode.json` `agent`: primary and subagent configuration.
- `.opencode/agents/*.md`: Markdown agent definitions.
- `.opencode/skills/<name>/SKILL.md`: project skills loaded on demand.
- OpenCode also scans `.claude/skills/` and `.agents/skills/`.
- `.opencode/plugins/*.js` or `.opencode/plugins/*.ts`: project plugins.
- `opencode plugin <module>`: installs an npm plugin module and updates
  OpenCode config.
- `.opencode/tools/`: custom tools callable by the model.
- `opencode.json` `mcp`: MCP server configuration.
- `opencode.json` `permission`: action approvals and loop-safety controls.

## Adapter Notes

- Use `AGENTS.md` as the baseline rule output.
- Use `opencode.json` when composing multiple instruction files without
  duplicating content.
- Use `.opencode/commands/` for manual workflows.
- Use OpenCode agents for role-specific behavior, not canonical policy.
- Use `.opencode/skills/` for native skills and `.agents/skills/` for
  cross-vendor skills.
- Represent executable integration behavior in canonical rules or skills before
  enforcing it in runtime hooks or plugins.
- Do not generate an OpenCode plugin module unless the deliverable needs runtime
  hooks or custom tools. The current canonical guidance maps directly to
  `AGENTS.md` and `.opencode/skills/`.

## Plugin Model

OpenCode has a verified module plugin model rather than a manifest package
model. Local plugins are JavaScript or TypeScript files, and npm plugins can be
installed with `opencode plugin <module>`.

That command is not the selected install path for ai-project-setup today because
our generated artifact is rules and skills, not an executable npm plugin module.
The selected distribution remains `dist/opencode/repo-files/` until a published
OpenCode plugin package builder is intentionally added.

See [plugin-model.yaml](../../vendors/opencode/plugin-model.yaml) for structured
details.
