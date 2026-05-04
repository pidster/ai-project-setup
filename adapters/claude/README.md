# Claude Adapter

Renders canonical content into Claude Code surfaces.

Current outputs:

- `dist/claude/CLAUDE.md`
- `dist/claude/.claude/skills/*/SKILL.md`

Run:

```sh
python3 adapters/claude/render.py
```

Check freshness:

```sh
python3 adapters/claude/render.py --check
```

Future output may include `.claude/rules/`, `.claude/commands/`, and
`.claude/agents/`.
