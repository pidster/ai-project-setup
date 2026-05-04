# Devin Adapter

Renders canonical content into Devin product and Devin for Terminal surfaces.

Current outputs:

- `dist/devin/repo-files/AGENTS.md`
- `dist/devin/repo-files/.agents/skills/*/SKILL.md`
- `dist/devin/repo-files/.devin/config.json`
- `dist/devin/repo-files/.devin/skills/*/SKILL.md`
- `dist/devin/repo-files/.devin/agents/*/AGENT.md`
- `dist/devin/repo-files/.devin/hooks.v1.json`

Run:

```sh
python3 adapters/devin/render.py
```

Check freshness:

```sh
python3 adapters/devin/render.py --check
```
