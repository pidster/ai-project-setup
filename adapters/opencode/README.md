# OpenCode Adapter

Renders canonical content into OpenCode surfaces.

Current outputs:

- `dist/opencode/repo-files/AGENTS.md`
- `dist/opencode/repo-files/.opencode/skills/*/SKILL.md`

This adapter intentionally selects repo files. OpenCode plugins are JavaScript
or TypeScript runtime modules, while the current ai-project-setup deliverable is
canonical rules plus native OpenCode skills.

Run:

```sh
python3 adapters/opencode/render.py
```

Check freshness:

```sh
python3 adapters/opencode/render.py --check
```

Future output may include `opencode.json`, `.opencode/commands/`, or
`.opencode/agents/` when canonical content exists for those surfaces. Generate
`.opencode/plugins/` only for runtime hooks or custom tools.
