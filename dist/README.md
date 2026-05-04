# Generated Output

Generated vendor artifacts will be written under this directory.

Each vendor should have exactly one generated distribution artifact directory
alongside `dist/<vendor>/install-manifest.yaml`.

Repository-local install artifacts live under `dist/<vendor>/repo-files/`.
Vendor plugin package artifacts live under `dist/<vendor>/plugin/`.
Marketplace artifacts live under `dist/<vendor>/marketplace/`.

Do not hand-author canonical policy in `dist/`. Change canonical content in
`core/`, then regenerate vendor outputs.

`generated-output-manifest.yaml` records generated files, renderer markers, and
canonical source IDs for reviewability.
