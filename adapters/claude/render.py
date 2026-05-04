#!/usr/bin/env python3
"""Render canonical content into Claude-oriented generated output."""

from __future__ import annotations

import argparse
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
OUTPUT_ROOT = REPO_ROOT / "dist" / "claude"
CLAUDE_OUTPUT = OUTPUT_ROOT / "CLAUDE.md"
SKILLS_OUTPUT = OUTPUT_ROOT / ".claude" / "skills"
RENDERER = "adapters/claude/render.py"


def render_claude_md(items) -> str:
    rules = sorted([item for item in items if item.kind == "rule"], key=lambda item: item.item_id)
    source_ids = ", ".join(f"`{item.item_id}`" for item in rules)
    lines = [
        generated_header(RENDERER),
        "",
        "# Claude Instructions",
        "",
        "This generated file adapts canonical repository rules for Claude Code.",
        "Canonical policy and procedure remain in `core/`.",
        "",
        f"Sources: {source_ids}",
        "",
    ]
    for item in rules:
        lines.extend(
            [
                f"## {title(item)}",
                "",
                f"Source: `{item.item_id}`",
                "",
                body_without_title(item.body),
                "",
            ]
        )
    lines.append("Generated skills are under `.claude/skills/<name>/SKILL.md`.")
    return "\n".join(lines).rstrip() + "\n"


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


def rendered_outputs() -> dict[Path, str]:
    items = canonical_items(REPO_ROOT)
    outputs = {CLAUDE_OUTPUT: render_claude_md(items)}
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
    print(f"{rel(REPO_ROOT, OUTPUT_ROOT)} is up to date")
    return 0


def write_outputs(outputs: dict[Path, str]) -> None:
    if SKILLS_OUTPUT.exists():
        shutil.rmtree(SKILLS_OUTPUT)
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
