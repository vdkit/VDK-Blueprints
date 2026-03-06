# VDK Blueprints

Canonical, curated blueprint library for the VDK ecosystem.

This repository is the source of truth for blueprint content consumed by `VDK-CLI`, surfaced in `VDK-Hub`, and documented in `VDK-Wiki`.

## What this repository is

`VDK-Blueprints` stores reusable AI-context blueprints in the AI Context Schema v3 format. Blueprints are designed for deterministic deployment and cross-platform adaptation through the canonical `kind` taxonomy.

### Canonical kind taxonomy

Every blueprint must declare one canonical `kind`:

- `project-memory`
- `conditional-rule`
- `skill`
- `command`
- `workflow`
- `agent`
- `hook`
- `mcp-integration`
- `plugin-distribution`

`category` is optional and used for editorial grouping/browsing.

## Curation model (generic ➜ specific)

The library is intentionally curated to balance broad usefulness with project precision:

- **L0**: universal baseline blueprints
- **L1**: language-level blueprints
- **L2**: framework/tool blueprints
- **L3**: project-context blueprints
- **L4**: provenance/variant blueprints (excluded from default retrieval)

Default CLI retrieval blends `L0-L3` and excludes `L4` unless explicitly requested (`--include-l4` or provenance audit).

## Repository structure

```text
library/
  agents/
  commands/
  rules/
  skills/
  workflows/

blueprints/
  (legacy/reference materials used by migration and analysis workflows)

scripts/
  (migration and maintenance utilities)
```

## How this integrates with the ecosystem

- **ai-context-schema**: defines schema + validation contract
- **VDK-Blueprints**: curated content source
- **VDK-CLI**: retrieval, scoring, dedupe, and deployment engine (authoritative runtime semantics)
- **VDK-Hub**: web distribution + operational surfaces synchronized to CLI semantics
- **VDK-Wiki**: user and operator documentation synchronized to schema + CLI behavior

### Integration order (required)

1. `ai-context-schema`
2. `VDK-Blueprints`
3. `VDK-CLI`
4. `VDK-Hub`
5. `VDK-Wiki`

Blueprint authoring should assume this order and avoid introducing metadata or behavior that cannot be interpreted deterministically by `VDK-CLI`.

## Using this library through VDK CLI

Typical flow:

1. Search curated blueprints by kind/specificity/platform.
2. Inspect compatibility and adaptation equivalence.
3. Deploy selected blueprint into project integrations.

Example commands:

- `vdk search --kind skill --platform claude-code`
- `vdk search --query nextjs --specificity L2`
- `vdk deploy <blueprint-id>`

## Contract linting and normalization

This repository enforces blueprint frontmatter contract checks with Oxlint + `@vdk/oxlint-plugin-blueprints`.

- `pnpm run lint` — run contract lint checks across `library/**`
- `pnpm run lint:blueprints:dry` — preview deterministic normalization changes
- `pnpm run lint:blueprints:fix` — apply deterministic normalization for frontmatter
- `pnpm run check` — repository gate (currently lint)

Normalization currently covers:

- `schemaVersion` alignment (`3.0`)
- required `kind`
- required semver `version`
- `id` normalization to kebab-case

## Contribution standards

When adding or updating blueprints:

1. Keep frontmatter schema-valid (v3.0).
2. Use canonical `kind` values only.
3. Preserve cross-platform intent in `platforms.components`.
4. Avoid duplicate near-identical variants unless provenance requires an `L4` representation.

## License

MIT — see `LICENSE`.