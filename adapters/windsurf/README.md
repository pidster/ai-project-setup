# Windsurf Adapter

Renders canonical content into Windsurf surfaces.

Current outputs:

- `dist/windsurf/AGENTS.md`
- `dist/windsurf/.windsurf/rules/*.md`
- `dist/windsurf/.windsurf/skills/*/SKILL.md`
- `dist/windsurf/.windsurf/workflows/*.md`
- `dist/windsurf/.windsurf/hooks.json`

Run:

```sh
python3 adapters/windsurf/render.py
```

Check freshness:

```sh
python3 adapters/windsurf/render.py --check
```
