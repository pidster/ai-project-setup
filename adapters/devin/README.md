# Devin Adapter

Renders canonical content into Devin product and Devin for Terminal surfaces.

Current outputs:

- `dist/devin/AGENTS.md`
- `dist/devin/.agents/skills/*/SKILL.md`
- `dist/devin/.devin/config.json`
- `dist/devin/.devin/skills/*/SKILL.md`
- `dist/devin/.devin/agents/*/AGENT.md`
- `dist/devin/.devin/hooks.v1.json`

Run:

```sh
python3 adapters/devin/render.py
```

Check freshness:

```sh
python3 adapters/devin/render.py --check
```
