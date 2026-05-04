# Copilot Adapter

Renders canonical content into a GitHub Copilot CLI marketplace package.

Current outputs:

- `.github/plugin/marketplace.json`
- `dist/copilot/marketplace/plugins/ai-project-setup/plugin.json`
- `dist/copilot/marketplace/plugins/ai-project-setup/skills/*/SKILL.md`

Native install commands:

```sh
copilot plugin marketplace add pidster/ai-project-setup
copilot plugin install ai-project-setup@ai-project-setup
```

Run:

```sh
python3 adapters/copilot/render.py
```

Check freshness:

```sh
python3 adapters/copilot/render.py --check
```

Future output may include `agents/`, hooks, MCP, and LSP configuration when they
can be generated from canonical content without redefining policy.
