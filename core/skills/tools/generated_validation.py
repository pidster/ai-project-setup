#!/usr/bin/env python3
"""Validate generated vendor output freshness."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

CHECKS = (
    ("claude", "adapters/claude/render.py"),
    ("codex", "adapters/codex/render.py"),
    ("copilot", "adapters/copilot/render.py"),
    ("cursor", "adapters/cursor/render.py"),
    ("devin", "adapters/devin/render.py"),
    ("opencode", "adapters/opencode/render.py"),
    ("windsurf", "adapters/windsurf/render.py"),
)
MANIFEST_CHECK = "core/skills/tools/generated_manifest.py"


def main() -> int:
    failures: list[str] = []

    for vendor, renderer in CHECKS:
        command = [sys.executable, renderer, "--check"]
        print(f"checking {vendor}: {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if result.returncode != 0:
            failures.append(vendor)

    command = [sys.executable, MANIFEST_CHECK, "--check"]
    print(f"checking generated manifest: {' '.join(command)}", flush=True)
    result = subprocess.run(command, cwd=REPO_ROOT, check=False)
    if result.returncode != 0:
        failures.append("generated manifest")

    if failures:
        print("generated validation failed", file=sys.stderr)
        for vendor in failures:
            print(f"- {vendor}", file=sys.stderr)
        return 1

    print("generated validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
