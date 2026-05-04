# Codex Adapter

Renders canonical content into Codex surfaces.

Current output:

- `dist/codex/AGENTS.md`

Run:

```sh
python3 adapters/codex/render.py
```

Check freshness:

```sh
python3 adapters/codex/render.py --check
```

Future output may include `.agents/skills/*/SKILL.md`, `.codex/agents/*.toml`,
`.codex/rules/*.rules`, and project-scoped `.codex/config.toml` where those
runtime outputs can be generated from canonical content without redefining
policy.
