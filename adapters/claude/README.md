# Claude Adapter

Renders canonical content into Claude Code surfaces.

Current outputs:

- `dist/claude/plugin/ai-project-setup/.claude-plugin/plugin.json`
- `dist/claude/plugin/ai-project-setup/skills/*/SKILL.md`

Run:

```sh
python3 adapters/claude/render.py
```

Check freshness:

```sh
python3 adapters/claude/render.py --check
```

Future plugin output may include `commands/`, `agents/`, and plugin hooks.
