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

The distribution build should read
`vendors/<vendor>/plugin-model.yaml` to determine which install modes are
supported by the vendor. The relevant source fields are:

- `plugin_model`: the vendor's overall plugin model category.
- `plugin_config_surfaces`: plugin package or module surfaces.
- `marketplace_surfaces`: marketplace or registry surfaces.
- `direct_config_surfaces`: direct repository configuration surfaces.
- `confidence`, `last_reviewed`, `sources`, and `notes`: review metadata and
  caveats used by validation and human review.

`docs/plugin-models.md` remains the vocabulary reference. The vendor YAML files
remain the structured facts. Adapter code renders those facts into `dist/`
artifacts.

Vendor support does not by itself mean this project has a generated or published
artifact for that mode. Generated `install-manifest.yaml` files must distinguish:

- `vendor_supported`: the vendor has a verified surface for the mode.
- `artifact_available`: this project generated or published the artifact needed
  for the mode.
- `installable_by_cli`: the installer can complete the mode using only
  repository-local writes.

Default mode selection may consider only modes where `vendor_supported`,
`artifact_available`, and `installable_by_cli` are all true. Modes that require
user-level configuration, global tool state, marketplace publication,
package-registry publication, or external repo setup may be listed as available
artifacts or manual follow-up steps, but they are not fully installable by the
CLI unless the action remains inside the target repository.

## Install Modes

The distribution system has three install modes.

`marketplace` is the preferred mode when
`vendors/<vendor>/plugin-model.yaml` declares one or more
`marketplace_surfaces` and this project has generated or published the matching
marketplace artifact. This mode should prepare marketplace or registry artifacts
under `dist/<vendor>/marketplace/`. If vendor tooling requires user-level
enablement, global configuration, package-registry publication, or marketplace
selection, the manifest must model that as a `manual_step` or
`external_package` action rather than a repository write.

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

Expected vendor behavior:

- Vendors with package manifests can consume packaged plugin artifacts, but
  installing or enabling those packages may be a user-level or marketplace
  operation outside the target repository.
- OpenCode consumes local JavaScript or TypeScript plugin modules and npm
  package plugins through `opencode.json`; repo-local `opencode.json` updates
  are installable by the CLI, while npm publication or package installation is
  external.
- Cursor, Devin, and Windsurf currently use direct repository configuration for
  this project's purposes. Devin product repo setup outside version control is a
  manual or external action, not a repository write.

## `dist/` Contract

Every vendor distribution directory must include:

```text
dist/<vendor>/install-manifest.yaml
```

Optional mode-specific directories are generated only when the corresponding
artifact is available:

```text
dist/<vendor>/marketplace/
dist/<vendor>/plugin/
dist/<vendor>/repo-files/
```

`install-manifest.yaml` is the installer's contract. It should describe:

- Vendor ID and display name.
- Source plugin model data used to identify vendor-supported modes.
- Mode availability, including `vendor_supported`, `artifact_available`, and
  `installable_by_cli`.
- Default install mode and fallback reasons for modes that are skipped.
- Ordered install actions for each mode.
- Source URLs, review date, confidence, and generation metadata.

The manifest should be generated from canonical content, vendor capabilities,
vendor plugin model data, and adapter output. It must not become an independent
source of policy.

Manifest actions should use a small allowlisted vocabulary:

`copy_file` copies one generated file to one target path under the target
repository. Required fields: `source`, `target`, and `on_conflict`.

`copy_tree` copies a generated directory tree to a target directory under the
target repository. Required fields: `source`, `target`, `include`, `exclude`,
and `on_conflict`.

`merge_structured_file` updates a structured repository file such as JSON, YAML,
or TOML without replacing unrelated keys. Required fields: `source`, `target`,
`format`, `merge_strategy`, and `on_conflict`.

`external_package` records a package or marketplace artifact that exists outside
the target repository. Required fields: `surface`, `package`, `version`, and
`manual`.

`manual_step` records a human action needed for user-level configuration,
marketplace selection, package publication, package installation, or vendor
setup outside version control. Required fields: `summary` and `instructions`.

Only `copy_file`, `copy_tree`, and `merge_structured_file` may write during
`install`, and all of their targets must remain inside the target repository.
`external_package` and `manual_step` must be reported by `plan` and `install`,
but the installer must not execute them.

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

`plan <vendor>` prints the selected mode, fallback reasons, target repository,
planned repository writes, external package references, manual steps, skipped
writes, and warnings. It performs no writes.

`install <vendor>` applies the repository-local write actions from the selected
plan. By default it should use the current working directory as the target
repository unless `--repo <path>` is provided. It must still print external
package references and manual steps, but it must not mutate user-level tool
configuration, global package state, registries, marketplace records, or vendor
repo setup outside version control.

## Default Mode Selection

When `--mode` is omitted, the installer chooses the first default-eligible mode
in this order:

1. `marketplace`
2. `plugin`
3. `repo_files`

The generated `install-manifest.yaml` must record the default mode and the
reason each higher-priority mode is unavailable. `plan` should print those
reasons so users can review why a fallback was selected.

For default selection, default-eligible means the manifest marks the mode with
all of `vendor_supported: true`, `artifact_available: true`, and
`installable_by_cli: true`. If a higher-priority mode has a generated artifact
but needs only external or manual actions, it may be shown as available but must
not become the default install mode.

When `--mode` is provided, the installer must fail clearly if that mode is not
vendor-supported or if this project has no artifact available for that mode. If
the requested mode is available but not fully installable by the CLI, `plan` and
`install` must report the external package references and manual steps without
falling back to another mode.

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

Installer implementations must not execute arbitrary commands from manifests.
External commands, package-manager commands, marketplace operations, user-config
edits, and vendor product setup belong in `manual_step` text unless a later
review explicitly adds a narrowly validated action type.

## Validation Expectations

Validation should check:

- Every manifest source exists.
- Every manifest target path is relative and cannot escape the repository root.
- Every vendor has a complete `dist/<vendor>/install-manifest.yaml`.
- Mode `vendor_supported` values match `vendors/<vendor>/plugin-model.yaml`.
- Mode `artifact_available` values match generated or published project
  artifacts.
- Mode `installable_by_cli` values are false when every action is external or
  manual.
- The default install mode follows marketplace, plugin, then repo-files order
  among modes installable by the CLI.
- Marketplace output exists only when marketplace surfaces are present.
- Plugin output exists only when package manifest or module plugin packaging is
  present.
- Direct repo-file output exists for direct configuration installation.
- Manifest actions use only allowlisted action types.
- Write actions use relative, repository-contained targets.
- `external_package` and `manual_step` actions are never executed by the
  installer.
- Generated outputs are fresh relative to canonical content, vendor
  capabilities, plugin model data, and adapter templates.

For invariants not covered by tooling, review generated manifests manually
against this plan before publishing.

## Review Checklist

- Does the plan preserve the separation between capabilities and plugin models?
- Does marketplace, plugin, and repo-files fallback behavior match each vendor's
  verified model?
- Does default mode selection consider project artifact availability as well as
  vendor support?
- Are user-level, global, marketplace, registry, and external repo setup actions
  represented as non-executed manual or external actions?
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
