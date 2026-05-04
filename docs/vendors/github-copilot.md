# GitHub Copilot

Status: verified from current GitHub Docs.

## Sources

- Custom instructions:
  <https://docs.github.com/en/copilot/how-tos/configure-custom-instructions/add-repository-instructions>
- Response customization:
  <https://docs.github.com/en/copilot/concepts/prompting/response-customization>
- Custom-instruction support matrix:
  <https://docs.github.com/en/copilot/reference/custom-instructions-support>
- Agent skills:
  <https://docs.github.com/en/copilot/concepts/agents/about-agent-skills>
- Custom agents:
  <https://docs.github.com/en/copilot/concepts/agents/copilot-cli/about-custom-agents>
- Custom-agent configuration:
  <https://docs.github.com/en/copilot/reference/custom-agents-configuration>
- Hooks:
  <https://docs.github.com/en/copilot/concepts/agents/coding-agent/about-hooks>
- MCP for coding agent:
  <https://docs.github.com/en/copilot/concepts/coding-agent/mcp-and-coding-agent>

## Surfaces

- `.github/copilot-instructions.md`: repository-wide custom instructions.
- `.github/instructions/**/*.instructions.md`: path-specific instructions with
  `applyTo` frontmatter.
- `AGENTS.md`: agent instructions where supported.
- Root `CLAUDE.md` or `GEMINI.md`: accepted as agent-instruction alternatives in
  some contexts.
- `.github/prompts/**/*.prompt.md`: reusable prompt files where supported.
- `.github/skills/<skill>/SKILL.md`: project agent skills. Copilot also scans
  `.claude/skills/` and `.agents/skills/`.
- `.github/agents/<custom-agent-name>.md`: repository custom agent profiles.
- `.github/hooks/*.json`: lifecycle hooks for supported Copilot agent surfaces.
- MCP servers can extend Copilot coding agent with tools.

## Adapter Notes

- Use `.github/copilot-instructions.md` for compact repository-wide summaries.
- Use `.github/instructions/` for path-scoped guidance.
- Treat prompt files as manually selected workflow prompts.
- Use `.github/skills/` for Copilot-specific skills and `.agents/skills/` for
  cross-vendor reuse.
- Use custom agents for role-specific execution profiles, not canonical policy.
- Avoid relying solely on `AGENTS.md`, because support varies by surface.
