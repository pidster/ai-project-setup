# Copilot Adapter

Renders canonical content into GitHub Copilot surfaces.

Current outputs:

- `dist/copilot/.github/copilot-instructions.md`
- `dist/copilot/.github/skills/*/SKILL.md`

Run:

```sh
python3 adapters/copilot/render.py
```

Check freshness:

```sh
python3 adapters/copilot/render.py --check
```

Future output may include `.github/instructions/`, `.github/prompts/`,
`.github/agents/`, and `.github/hooks/`.
