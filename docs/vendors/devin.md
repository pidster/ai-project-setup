# Devin

Status: verified from current Devin docs.

This page covers both Devin product and Devin for Terminal. The product surfaces
are not identical.

## Sources

- AGENTS.md: <https://docs.devin.ai/onboard-devin/agents-md>
- Repository setup: <https://docs.devin.ai/onboard-devin/new-repo-setup>
- Product skills: <https://docs.devin.ai/product-guides/skills>
- Terminal extensibility: <https://cli.devin.ai/docs/extensibility>
- Terminal rules: <https://cli.devin.ai/docs/extensibility/rules>
- Terminal skills: <https://cli.devin.ai/docs/extensibility/skills/overview>
- Terminal custom subagents: <https://cli.devin.ai/docs/subagents>
- Terminal hooks: <https://cli.devin.ai/docs/extensibility/hooks/overview>
- Terminal configuration: <https://cli.devin.ai/docs/extensibility/configuration>

## Surfaces

- `AGENTS.md`: project instructions for Devin.
- Devin for Terminal also reads `AGENT.md` and `CLAUDE.md` as equivalent
  always-on rules.
- Devin for Terminal loads supported rule files at session start and discovers
  subdirectory rule files lazily.
- Devin for Terminal imports `.cursor/rules/*.md`, `.cursorrules`, and
  `.windsurf/rules/*.md` when enabled.
- No current official Devin docs found for a committed `.devin/rules/`
  directory.
- `.agents/skills/<skill-name>/SKILL.md`: recommended repo skill location for
  Devin product sessions.
- Devin also scans `.github/skills/<skill-name>/SKILL.md` and
  `.claude/skills/<skill-name>/SKILL.md`.
- `.devin/skills/<skill-name>/SKILL.md`: Devin for Terminal skills.
- `.devin/agents/<agent-name>/AGENT.md`: Devin for Terminal custom subagents.
- `.agents/agents/<agent-name>/AGENT.md`: alternate Terminal subagent location.
- `.devin/config.json`: Terminal permissions, MCP servers, imports, and hooks.
- `.devin/hooks.v1.json`: Terminal lifecycle hooks.
- Repo setup fields outside the repository configure upkeep, dependency
  maintenance, lint commands, test commands, and repo-specific knowledge.

## Adapter Notes

- Use `AGENTS.md` as the portable committed instruction file.
- Do not emit `.devin/rules/` unless official Devin docs add that committed
  surface.
- Use `.agents/skills/` for Devin product sessions.
- Use `.devin/skills/`, `.devin/agents/`, `.devin/hooks.v1.json`, and
  `.devin/config.json` for Devin for Terminal.
- Treat Devin repo setup as external environment configuration, not committed
  canonical policy.
- Document any imported vendor config explicitly to avoid hidden policy
  duplication.
