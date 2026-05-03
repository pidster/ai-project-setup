#!/usr/bin/env python3
"""Run all implemented repository validators."""

from __future__ import annotations

from pathlib import Path
import subprocess
import sys


REPO_ROOT = Path(__file__).resolve().parents[3]

VALIDATORS = (
    "core/skills/tools/canonical_validation.py",
    "core/skills/tools/vendor_validation.py",
    "core/skills/tools/adapter_validation.py",
    "core/skills/tools/generated_validation.py",
)


def main() -> int:
    failures: list[str] = []

    for validator in VALIDATORS:
        command = [sys.executable, validator]
        print(f"running {' '.join(command)}", flush=True)
        result = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if result.returncode != 0:
            failures.append(validator)

    if failures:
        print("validation failed", file=sys.stderr)
        for validator in failures:
            print(f"- {validator}", file=sys.stderr)
        return 1

    print("validation passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
