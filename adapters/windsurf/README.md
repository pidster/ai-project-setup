# Windsurf Adapter

Renders canonical content into Windsurf surfaces.

Current outputs:

- `dist/windsurf/repo-files/AGENTS.md`
- `dist/windsurf/repo-files/.windsurf/rules/*.md`
- `dist/windsurf/repo-files/.windsurf/skills/*/SKILL.md`
- `dist/windsurf/repo-files/.windsurf/workflows/*.md`
- `dist/windsurf/repo-files/.windsurf/hooks.json`

Run:

```sh
python3 adapters/windsurf/render.py
```

Check freshness:

```sh
python3 adapters/windsurf/render.py --check
```
