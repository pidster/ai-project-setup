# OpenCode Adapter

Renders canonical content into OpenCode surfaces.

Current outputs:

- `dist/opencode/AGENTS.md`
- `dist/opencode/.opencode/skills/*/SKILL.md`

Run:

```sh
python3 adapters/opencode/render.py
```

Check freshness:

```sh
python3 adapters/opencode/render.py --check
```

Future output may include `opencode.json`, `.opencode/commands/`,
`.opencode/agents/`, and `.opencode/plugins/`.
