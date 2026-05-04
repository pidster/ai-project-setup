# Windsurf

Status: verified from current Windsurf docs.

## Sources

- AGENTS.md: <https://docs.windsurf.com/windsurf/cascade/agents-md>
- Memories and rules: <https://docs.windsurf.com/windsurf/cascade/memories>
- Skills: <https://docs.windsurf.com/windsurf/cascade/skills>
- Workflows: <https://docs.windsurf.com/windsurf/cascade/workflows>
- Hooks: <https://docs.windsurf.com/windsurf/cascade/hooks>

## Surfaces

- `AGENTS.md` or `agents.md`: location-scoped instructions. Root files are
  always on; subdirectory files auto-scope to that subtree.
- `.windsurf/rules/*.md`: workspace rules with `trigger` frontmatter.
- Rule triggers: `always_on`, `glob`, `model_decision`, and `manual`.
- Rules can include `description` and `globs`.
- `.windsurf/workflows/*.md`: manually invoked slash-command workflows.
- `.windsurf/skills/<skill-name>/SKILL.md`: workspace skills with supporting
  files and progressive disclosure.
- Windsurf also discovers `.agents/skills/` and optionally `.claude/skills/`.
- `.windsurf/hooks.json`: workspace hooks.
- Memories exist outside version control and should not be treated as durable
  project policy.
- No current official Windsurf docs found for repo-committed custom subagent
  profiles.

## Adapter Notes

- Use root `AGENTS.md` for the simplest always-on project guidance.
- Use `.windsurf/rules/` for explicit activation control.
- Use `glob` rules for path-scoped guidance.
- Use skills for complex procedures with supporting files.
- Use workflows for manual slash-command runbooks.
- Use hooks for enforcement, logging, validation, and lifecycle automation.
