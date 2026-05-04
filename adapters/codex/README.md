# Codex Adapter

Renders canonical content into a Codex marketplace package.

Current output:

- `dist/codex/marketplace/.agents/plugins/marketplace.json`
- `dist/codex/marketplace/plugins/ai-project-setup/.codex-plugin/plugin.json`
- `dist/codex/marketplace/plugins/ai-project-setup/skills/*/SKILL.md`

Native install command:

```sh
codex plugin marketplace add dist/codex/marketplace
```

Run:

```sh
python3 adapters/codex/render.py
```

Check freshness:

```sh
python3 adapters/codex/render.py --check
```

Future plugin output may include `.mcp.json`, `.app.json`, hooks, assets, and
other plugin-root files when they can be generated from canonical content
without redefining policy.
