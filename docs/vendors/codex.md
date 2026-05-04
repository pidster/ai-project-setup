# Codex

Status: verified from current OpenAI Codex docs.

## Sources

- AGENTS.md: <https://developers.openai.com/codex/guides/agents-md>
- Rules: <https://developers.openai.com/codex/rules>
- Skills: <https://developers.openai.com/codex/skills>
- Subagents: <https://developers.openai.com/codex/subagents>
- Hooks: <https://developers.openai.com/codex/hooks>
- Config reference: <https://developers.openai.com/codex/config-reference>
- Plugins: <https://developers.openai.com/codex/plugins>

## Surfaces

- `AGENTS.md`: scoped agent instructions.
- `AGENTS.override.md`: overrides same-directory `AGENTS.md` where present.
- Nested `AGENTS.md`: directory-specific guidance.
- Fallback instruction filenames can be configured.
- `.agents/skills/<skill>/SKILL.md`: repository skills.
- `.codex/agents/*.toml`: custom agent profiles for subagents.
- `.codex/config.toml`: project-scoped configuration loaded only for trusted
  projects.
- `.codex/rules/*.rules`: trusted project execution policy rules. These are
  deterministic command execution rules, not prompt-policy rule files.
- Hooks can be configured, including `PreToolUse` and `PostToolUse`, behind the
  `codex_hooks` feature.
- MCP servers, approvals, sandbox behavior, connector apps, and plugins are
  configured through Codex surfaces.
- No current official committed repo format found for custom slash-command
  prompt files comparable to `.claude/commands/` or `.opencode/commands/`.

## Adapter Notes

- Use `AGENTS.md` as the primary Codex output.
- Use nested `AGENTS.md` files for directory-specific guidance.
- Use `.agents/skills/` for Codex-consumable skills.
- Use `.codex/agents/` for Codex custom agent profiles when rendering agent
  outputs.
- Treat `.codex/config.toml`, `.codex/rules/`, hooks, and MCP settings as
  runtime adapters, not canonical prompt policy.

## Plugin Model

Codex has a verified installable plugin package model. See
[plugin-model.yaml](../../vendors/codex/plugin-model.yaml) for structured
details.
