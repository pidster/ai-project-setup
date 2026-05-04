#!/usr/bin/env python3
"""Render canonical content into a GitHub Copilot CLI marketplace package."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import shutil
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from render_support import (  # noqa: E402
    body_without_title,
    canonical_items,
    generated_header,
    rel,
    skill_name,
    title,
)


REPO_ROOT = Path(__file__).resolve().parents[2]
PUBLIC_MARKETPLACE_MANIFEST_OUTPUT = REPO_ROOT / ".github" / "plugin" / "marketplace.json"
MARKETPLACE_ROOT = REPO_ROOT / "dist" / "copilot" / "marketplace"
PLUGIN_ROOT = MARKETPLACE_ROOT / "plugins" / "ai-project-setup"
PLUGIN_MANIFEST_OUTPUT = PLUGIN_ROOT / "plugin.json"
SKILLS_OUTPUT = PLUGIN_ROOT / "skills"
OBSOLETE_REPO_FILES_ROOT = REPO_ROOT / "dist" / "copilot" / "repo-files"
OBSOLETE_PLUGIN_ROOT = REPO_ROOT / "dist" / "copilot" / "plugin"
RENDERER = "adapters/copilot/render.py"


def render_skill(item) -> str:
    name = skill_name(item.item_id)
    return (
        "---\n"
        f"name: {name}\n"
        f"description: {item.summary}\n"
        f"source_id: {item.item_id}\n"
        "---\n"
        "\n"
        f"{generated_header(RENDERER)}\n"
        "\n"
        f"# {title(item)}\n"
        "\n"
        "Canonical policy and procedure remain in `core/`.\n"
        "\n"
        f"Source: `{item.item_id}`\n"
        "\n"
        f"{body_without_title(item.body)}\n"
    )


def render_plugin_manifest() -> str:
    manifest = {
        "name": "ai-project-setup",
        "description": "Canonical repository guidance and workflows for AI project setup.",
        "version": "0.1.0",
        "author": {
            "name": "ai-project-setup",
        },
        "skills": "skills/",
        "category": "Productivity",
    }
    return json.dumps(manifest, indent=2, sort_keys=False) + "\n"


def render_marketplace_manifest() -> str:
    manifest = {
        "name": "ai-project-setup",
        "owner": {
            "name": "ai-project-setup",
        },
        "metadata": {
            "description": "Canonical repository guidance and workflows for AI project setup.",
            "version": "0.1.0",
        },
        "plugins": [
            {
                "name": "ai-project-setup",
                "description": "Canonical repository guidance and workflows for AI project setup.",
                "version": "0.1.0",
                "source": "dist/copilot/marketplace/plugins/ai-project-setup",
                "category": "Productivity",
            }
        ],
    }
    return json.dumps(manifest, indent=2, sort_keys=False) + "\n"


def rendered_outputs() -> dict[Path, str]:
    items = canonical_items(REPO_ROOT)
    outputs = {
        PUBLIC_MARKETPLACE_MANIFEST_OUTPUT: render_marketplace_manifest(),
        PLUGIN_MANIFEST_OUTPUT: render_plugin_manifest(),
    }
    for item in sorted([candidate for candidate in items if candidate.kind == "skill"], key=lambda i: i.item_id):
        outputs[SKILLS_OUTPUT / skill_name(item.item_id) / "SKILL.md"] = render_skill(item)
    return outputs


def check_outputs(outputs: dict[Path, str]) -> int:
    for path, rendered in sorted(outputs.items()):
        if not path.exists():
            print(f"{rel(REPO_ROOT, path)}: missing generated output", file=sys.stderr)
            return 1
        if path.read_text(encoding="utf-8") != rendered:
            print(f"{rel(REPO_ROOT, path)}: generated output is stale", file=sys.stderr)
            return 1
    for obsolete_root in (OBSOLETE_REPO_FILES_ROOT, OBSOLETE_PLUGIN_ROOT):
        if obsolete_root.exists():
            print(f"{rel(REPO_ROOT, obsolete_root)}: obsolete generated artifact", file=sys.stderr)
            return 1
    print(f"{rel(REPO_ROOT, MARKETPLACE_ROOT)} is up to date")
    return 0


def write_outputs(outputs: dict[Path, str]) -> None:
    if MARKETPLACE_ROOT.exists():
        shutil.rmtree(MARKETPLACE_ROOT)
    for obsolete_root in (OBSOLETE_REPO_FILES_ROOT, OBSOLETE_PLUGIN_ROOT):
        if obsolete_root.exists():
            shutil.rmtree(obsolete_root)
    for path, rendered in sorted(outputs.items()):
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(rendered, encoding="utf-8")
        print(f"wrote {rel(REPO_ROOT, path)}")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="check generated output freshness")
    args = parser.parse_args()
    outputs = rendered_outputs()
    if args.check:
        return check_outputs(outputs)
    write_outputs(outputs)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
