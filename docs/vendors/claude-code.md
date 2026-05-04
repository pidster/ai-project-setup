# Claude Code

Status: verified from current Claude Code docs.

## Sources

- Claude Code memory and rules:
  <https://code.claude.com/docs/en/memory>
- Claude Code settings:
  <https://docs.claude.com/en/docs/claude-code/settings>
- Claude Code slash commands:
  <https://docs.claude.com/en/docs/claude-code/slash-commands>
- Claude Code subagents:
  <https://docs.claude.com/en/docs/claude-code/subagents>
- Claude Code skills:
  <https://docs.claude.com/en/docs/claude-code/skills>
- Claude Code hooks:
  <https://docs.claude.com/en/docs/claude-code/hooks>
- Claude Code plugins:
  <https://docs.claude.com/en/docs/claude-code/plugins>

## Surfaces

- `CLAUDE.md` or `.claude/CLAUDE.md`: project instructions.
- `CLAUDE.local.md`: local personal project instructions; should not be
  committed.
- `.claude/rules/**/*.md`: modular project rules. Rules without `paths`
  frontmatter load at launch; rules with `paths` load when matching files are
  read.
- `~/.claude/rules/**/*.md`: user-level rules.
- `@path` imports inside `CLAUDE.md`.
- `.claude/skills/<skill>/SKILL.md`: project skills with optional supporting
  files.
- `.claude/commands/**/*.md`: project slash commands.
- `.claude/agents/*.md`: project subagents with YAML frontmatter.
- `.claude/settings.json`: shared project settings, including permissions,
  environment variables, hooks, sandbox settings, MCP server settings, and
  exclusions.
- Hooks configured through settings.
- Plugins that can include commands, agents, hooks, skills, and MCP servers.

## Adapter Notes

- Use root `CLAUDE.md` as the compact entry point.
- Import `AGENTS.md` from `CLAUDE.md` when sharing cross-tool instructions.
- Use `.claude/rules/` for path-scoped rules.
- Use `.claude/skills/` for rich capabilities with supporting files.
- Use `.claude/commands/` for manually invoked workflows.
- Treat settings, hooks, MCP, and plugins as runtime adapters, not canonical
  prompt policy.
