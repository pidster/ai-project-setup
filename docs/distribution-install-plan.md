# Distribution and Install Plan

Status: planning
Last reviewed: 2026-05-04

This document defines the planned distribution and installation contract for
generated vendor artifacts. It is an implementation plan, not a replacement for
the plugin model vocabulary or per-vendor source-backed data.

Use [Plugin models](plugin-models.md) for shared vocabulary. Use
`vendors/<vendor>/plugin-model.yaml` as the structured source of truth for each
vendor's install and packaging model.

## Goals

- Generate predictable `dist/` output from canonical content and vendor plugin
  model data.
- Let users install vendor-specific repository setup with one familiar command:
  `npx ai-project-setup install <vendor>`.
- Prefer the most native install surface available for a vendor while keeping a
  safe fallback path for vendors that only support direct repository files.
- Keep vendor capability data, plugin model data, adapter rendering, and
  installer behavior separate.

## Non-Goals

- Implement the NPX package in this planning step.
- Add generated `dist/` output in this planning step.
- Create a second vendor compatibility table outside
  [Documentation Index](README.md).
- Redefine canonical policy in generated vendor artifacts or install manifests.

## Source Data

The installer and distribution build should read
`vendors/<vendor>/plugin-model.yaml` to determine which install modes are
available. The relevant source fields are:

- `plugin_model`: the vendor's overall plugin model category.
- `plugin_config_surfaces`: plugin package or module surfaces.
- `marketplace_surfaces`: marketplace or registry surfaces.
- `direct_config_surfaces`: direct repository configuration surfaces.
- `confidence`, `last_reviewed`, `sources`, and `notes`: review metadata and
  caveats used by validation and human review.

`docs/plugin-models.md` remains the vocabulary reference. The vendor YAML files
remain the structured facts. Adapter code renders those facts into `dist/`
artifacts.

## Install Modes

The distribution system has three install modes.

`marketplace` is the preferred mode when
`vendors/<vendor>/plugin-model.yaml` declares one or more
`marketplace_surfaces`. This mode should prepare marketplace or registry
artifacts under `dist/<vendor>/marketplace/` and direct the installer to select
or enable the published package when that is possible.

`plugin` is the fallback mode for vendors with `plugin_model:
package_manifest` or `plugin_model: module_plugin` when marketplace
installation is unavailable or not selected. This mode should prepare plugin
package or module artifacts under `dist/<vendor>/plugin/`.

`repo_files` is the fallback mode for vendors with `plugin_model:
direct_config_only`, and the final fallback for vendors whose marketplace or
plugin packaging cannot be used. This mode should prepare direct per-repository
configuration files under `dist/<vendor>/repo-files/`.

The internal mode name is `repo_files`. The CLI flag uses `repo-files` to match
normal command-line spelling.

Mode selection must not infer plugin packaging from skills, hooks, MCP,
commands, or agents alone. It must follow the vendor plugin model data.

## `dist/` Contract

Every vendor distribution directory must include:

```text
dist/<vendor>/install-manifest.yaml
```

Optional mode-specific directories are generated only when supported:

```text
dist/<vendor>/marketplace/
dist/<vendor>/plugin/
dist/<vendor>/repo-files/
```

`install-manifest.yaml` is the installer's contract. It should describe:

- Vendor ID and display name.
- Source plugin model data used to choose supported modes.
- Supported install modes and default install mode.
- Fallback reasons for modes that are skipped.
- Files or package artifacts to install for each mode.
- Target paths relative to the target repository root.
- Conflict behavior for each target.
- Required warnings, manual steps, or external commands.
- Source URLs, review date, confidence, and generation metadata.

The manifest should be generated from canonical content, vendor capabilities,
vendor plugin model data, and adapter output. It must not become an independent
source of policy.

## CLI Contract

The user-facing entrypoint is:

```bash
npx ai-project-setup <command>
```

Planned commands:

```bash
npx ai-project-setup list
npx ai-project-setup plan <vendor>
npx ai-project-setup install <vendor>
```

Planned flags:

```bash
--repo <path>
--mode marketplace|plugin|repo-files
--dry-run
--yes
--force
```

`list` prints available vendors, supported install modes, default mode, and
review confidence.

`plan <vendor>` prints the selected mode, fallback reason, target repository,
planned writes, skipped writes, manual steps, and warnings. It performs no
writes.

`install <vendor>` applies the selected plan. By default it should use the
current working directory as the target repository unless `--repo <path>` is
provided.

## Default Mode Selection

When `--mode` is omitted, the installer chooses the first supported mode in this
order:

1. `marketplace`
2. `plugin`
3. `repo_files`

The generated `install-manifest.yaml` must record the default mode and the
reason each higher-priority mode is unavailable. `plan` should print those
reasons so users can review why a fallback was selected.

When `--mode` is provided, the installer must fail clearly if that mode is not
supported for the vendor. It must not silently fall back to another mode after a
user explicitly selected a mode.

## Installer Safety

The installer must write only inside the target repository.

Target paths in manifests must be relative paths. They must not be absolute,
empty, contain parent-directory traversal, or resolve outside the target repo
after normalization.

Existing files must not be overwritten by default. If a target exists, the plan
should report the conflict and `install` should fail unless `--force` is
provided.

`--dry-run` must perform no writes and should report the same plan that a real
install would execute.

`--yes` may skip interactive confirmation, but it must not imply `--force`.

`--force` may replace files that are part of the selected install plan, but it
must still obey repository-boundary checks.

## Validation Expectations

Validation should check:

- Every manifest source exists.
- Every manifest target path is relative and cannot escape the repository root.
- Every vendor has a complete `dist/<vendor>/install-manifest.yaml`.
- Supported modes match `vendors/<vendor>/plugin-model.yaml`.
- The default install mode follows marketplace, plugin, then repo-files order.
- Marketplace output exists only when marketplace surfaces are present.
- Plugin output exists only when package manifest or module plugin packaging is
  present.
- Direct repo-file output exists for direct configuration installation.
- Generated outputs are fresh relative to canonical content, vendor
  capabilities, plugin model data, and adapter templates.

For invariants not covered by tooling, review generated manifests manually
against this plan before publishing.

## Review Checklist

- Does the plan preserve the separation between capabilities and plugin models?
- Does marketplace, plugin, and repo-files fallback behavior match each vendor's
  verified model?
- Is `npx ai-project-setup install <vendor>` simple enough for users?
- Are destructive writes prevented by default?
- Is the manifest schema sufficient for validation and future installers?

## Implementation Sequence

1. Review and approve this planning document.
2. Define the `install-manifest.yaml` schema.
3. Teach adapters to emit install manifests and mode-specific `dist/`
   directories.
4. Add validation for manifests, target paths, mode selection, and generated
   freshness.
5. Implement the NPX package commands.
6. Add end-to-end dry-run and install tests against fixture repositories.

## Planning-Step Test Plan

For this planning step, run:

```bash
python3 core/skills/tools/validate_all.py
git diff --check
```

No generated `dist/` changes should be added during this step.
