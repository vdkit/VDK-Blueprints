#!/usr/bin/env python3
"""Bulk-promote shortlist entries from staging-blueprints into canonical library.

This script:
1) Loads shortlist candidates JSON
2) Detects already promoted staging sources from tracker
3) Generates canonical markdown blueprints for remaining entries
4) Appends promotion + deprecation mapping section to tracker
5) Writes a JSON report for validation and auditing
"""

from __future__ import annotations

import json
import re
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Dict, List, Tuple

ROOT = Path("/Users/dominikospritis/DevFolder/My-Projects/VDK-Ecosystem")
VDK_BLUEPRINTS = ROOT / "VDK-Blueprints"
STAGING = ROOT / "staging-blueprints"
SHORTLIST_JSON = VDK_BLUEPRINTS / "library-snapshots" / "staging-promotion-candidates-latest.json"
TRACKER = VDK_BLUEPRINTS / "docs" / "STAGING_PROMOTION_DEPRECATION_TRACKER.md"
REPORT = VDK_BLUEPRINTS / "library-snapshots" / "bulk-promotion-wave4-report.json"

TODAY = date.today().isoformat()
WAVE_LABEL = f"Wave 4 (bulk) ({TODAY})"


def slugify(value: str) -> str:
    value = (value or "").lower()
    value = re.sub(r"[^a-z0-9]+", "-", value).strip("-")
    value = re.sub(r"-{2,}", "-", value)
    return value


def title_case_slug(slug: str) -> str:
    return " ".join(part.capitalize() for part in slug.split("-") if part)


def parse_tracker_promoted_sources(text: str) -> set[str]:
    pattern = re.compile(r"\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*promoted\s*\|")
    return {m.group(1) for m in pattern.finditer(text)}


def extract_frontmatter_description(source_text: str) -> str | None:
    if not source_text.startswith("---\n"):
        return None
    end = source_text.find("\n---", 4)
    if end == -1:
        return None
    fm = source_text[4:end]
    m = re.search(r"^description:\s*(.+)$", fm, flags=re.MULTILINE)
    if not m:
        return None
    value = m.group(1).strip().strip('"').strip("'")
    return value if value else None


def extract_h1(source_text: str) -> str | None:
    m = re.search(r"^#\s+(.+)$", source_text, flags=re.MULTILINE)
    if not m:
        return None
    return m.group(1).strip()


def resolve_source_path(src_rel: str, item_id: str, dedupe_key: str, md_files: List[Path]) -> Tuple[str, Path, str]:
    """Resolve renamed staging source files when exact shortlist paths no longer exist.

    Returns: (resolved_rel_path, resolved_abs_path, resolution_mode)
    resolution_mode: direct | parent-match | global-match | missing
    """
    direct_abs = STAGING / src_rel
    if direct_abs.exists():
        return src_rel, direct_abs, "direct"

    src_parent = direct_abs.parent
    key_tokens = [slugify(item_id), slugify(dedupe_key), slugify(Path(src_rel).stem)]
    key_tokens = [t for t in key_tokens if t]

    def score(path: Path) -> int:
        s = 0
        stem = slugify(path.stem)
        name = path.name.lower()
        if name == "skill.md":
            s += 2
        for t in key_tokens:
            if t and t in stem:
                s += 6
        return s

    # 1) Prefer markdown files in original parent directory.
    if src_parent.exists():
        parent_md = [p for p in src_parent.glob("*.md") if p.is_file()]
        if parent_md:
            best = sorted(parent_md, key=lambda p: (score(p), -len(p.name)), reverse=True)[0]
            rel = best.relative_to(STAGING).as_posix()
            return rel, best, "parent-match"

    # 2) Fallback to global fuzzy match by tokens.
    scored = []
    for p in md_files:
        stem = slugify(p.stem)
        if any(t and t in stem for t in key_tokens):
            scored.append((score(p), p))
    if scored:
      best = sorted(scored, key=lambda x: (x[0], -len(x[1].name)), reverse=True)[0][1]
      rel = best.relative_to(STAGING).as_posix()
      return rel, best, "global-match"

    return src_rel, direct_abs, "missing"


@dataclass
class Candidate:
    kind: str
    source: str
    source_abs: Path
    dedupe_key: str
    id: str
    target_rel: str
    target_abs: Path
    title: str
    description: str


def infer_command_subcategory(source: str, item_id: str) -> str:
    source_l = source.lower()
    item_l = item_id.lower()

    if any(k in source_l or k in item_l for k in ["security", "sast", "crypto", "cryptography", "audit"]):
        return "security"
    if any(k in source_l or k in item_l for k in ["terraform", "docker", "kubernetes", "helm", "cloudformation", "devops", "deployment", "ci-cd"]):
        return "devops"
    if any(k in source_l or k in item_l for k in ["zapier", "webhook", "integration", "api"]):
        return "api"
    if any(k in source_l or k in item_l for k in ["automation", "template", "prompt", "seo", "title", "monitor", "creator-studio"]):
        return "automation"
    return "development"


def map_target(kind: str, item_id: str, source: str = "") -> str:
  if kind == "command":
    subcategory = infer_command_subcategory(source, item_id)
    return f"library/commands/{subcategory}/{item_id}.md"
  if kind == "skill":
    return f"library/skills/{item_id}.md"
  if kind == "agent":
    return f"library/agents/{item_id}.md"
  if kind == "workflow":
    return f"library/workflows/{item_id}.md"
  if kind == "plugin-distribution":
    return f"library/plugins/{item_id}.md"
  if kind == "conditional-rule":
    return f"library/rules/core/{item_id}.md"
  return f"library/misc/{item_id}.md"


def build_content(c: Candidate) -> str:
    kind = c.kind

    if kind == "command":
        subcategory = Path(c.target_rel).parent.name
        return f"""---
id: {c.id}
name: {c.title}
title: {c.title}
description: >-
  {c.description}
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: {subcategory}
tags:
  - command
author: VDK
lastUpdated: '{TODAY}'
schemaVersion: '3.0'
kind: command
specificityLayer: L3
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      commands:
        type: claude-command
        enabled: true
        location: .claude/commands/
        manifests:
          - name: {c.id}
            file: {c.id}.md
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

## Purpose

{c.description}

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""

    if kind == "skill":
        return f"""---
id: {c.id}
title: {c.title}
description: >-
  {c.description}
version: 1.0.0
lastUpdated: '{TODAY}'
category: skill
subcategory: imported
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L3
author: VDK
tags:
  - skill
  - imported
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      skills:
        type: claude-skill
        enabled: true
        location: .claude/skills/
        manifests:
          - name: {c.id}
            file: {c.id}.md
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

## Purpose

{c.description}

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""

    if kind == "agent":
        return f"""---
id: {c.id}
name: {c.title}
title: {c.title}
description: >-
  {c.description}
version: 1.0.0
type: agent
author: VDK
lastUpdated: '{TODAY}'
schemaVersion: '3.0'
kind: agent
specificityLayer: L3
category: assistant
tags:
  - agent
  - imported
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      agents:
        type: claude-agent
        enabled: true
        location: .claude/agents/
        manifests:
          - name: {c.id}
            file: {c.id}.md
  openai-codex:
    compatible: true
    enabled: true
    components:
      agents:
        type: agents-md
        enabled: true
        location: AGENTS.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

You are responsible for `{c.id}` guidance and implementation quality.

## Core Behaviors

- apply domain-aligned implementation patterns
- preserve production readiness and integration quality
- expose explicit constraints and handoff expectations

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""

    if kind == "workflow":
        return f"""---
id: {c.id}
title: {c.title}
description: >-
  {c.description}
version: 1.0.0
lastUpdated: '{TODAY}'
category: workflow
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: workflow
specificityLayer: L3
author: VDK
tags:
  - workflow
  - imported
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      commands:
        type: claude-command
        enabled: true
        location: .claude/commands/
        manifests:
          - name: {c.id}
            file: {c.id}.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

## Objective

{c.description}

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""

    if kind == "plugin-distribution":
        return f"""---
id: {c.id}
title: {c.title}
description: >-
  {c.description}
version: 1.0.0
lastUpdated: '{TODAY}'
category: plugin
subcategory: distribution
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: plugin-distribution
specificityLayer: L3
author: VDK
tags:
  - plugin
  - distribution
  - imported
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      distribution:
        type: claude-plugin
        enabled: true
        location: .claude-plugin/plugin.json
        manifests:
          - name: {c.id}
            file: plugin.json
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

## Purpose

{c.description}

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""

    # conditional-rule and fallback
    return f"""---
id: {c.id}
title: {c.title}
description: >-
  {c.description}
version: 1.0.0
lastUpdated: '{TODAY}'
category: core
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: conditional-rule
specificityLayer: L3
author: VDK
tags:
  - rule
  - imported
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      rules:
        type: claude-rule
        enabled: true
        location: .claude/rules/
        manifests:
          - name: {c.id}
            file: {c.id}.md
  cursor:
    compatible: true
    enabled: true
    components:
      rules:
        type: cursor-rule
        enabled: true
        location: .cursor/rules/
        format: mdc
        manifests:
          - name: {c.id}
            file: {c.id}.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---

# {c.title}

## Purpose

{c.description}

## Source Mapping

- staging source: `{c.source}`
- canonical id: `{c.id}`
"""


def main() -> None:
    shortlist_data = json.loads(SHORTLIST_JSON.read_text())
    selected = shortlist_data["selected"]
    tracker_text = TRACKER.read_text()
    already_promoted_sources = parse_tracker_promoted_sources(tracker_text)
    md_files = [p for p in STAGING.rglob("*.md") if p.is_file()]

    candidates: List[Candidate] = []
    resolution_stats: Dict[str, int] = {"direct": 0, "parent-match": 0, "global-match": 0, "missing": 0}
    for item in selected:
        src_rel = item["path"]
        if src_rel in already_promoted_sources:
            continue

        item_id = slugify(item.get("dedupeKey") or Path(src_rel).stem)
        resolved_rel, src_abs, resolution_mode = resolve_source_path(
          src_rel=src_rel,
          item_id=item_id,
          dedupe_key=item.get("dedupeKey", ""),
          md_files=md_files,
        )
        target_rel = map_target(item["kind"], item_id, resolved_rel)
        target_abs = VDK_BLUEPRINTS / target_rel
        resolution_stats[resolution_mode] = resolution_stats.get(resolution_mode, 0) + 1

        source_text = src_abs.read_text() if src_abs.exists() else ""
        h1 = extract_h1(source_text) or title_case_slug(item_id)
        description = extract_frontmatter_description(source_text) or f"Imported {item['kind']} blueprint from staging source {resolved_rel}."
        description = re.sub(r"\s+", " ", description).strip()

        candidates.append(
            Candidate(
                kind=item["kind"],
                source=resolved_rel,
                source_abs=src_abs,
                dedupe_key=item.get("dedupeKey", ""),
                id=item_id,
                target_rel=target_rel,
                target_abs=target_abs,
                title=h1,
                description=description,
            )
        )

    created: List[Tuple[str, str, str, str]] = []
    skipped_existing: List[Tuple[str, str]] = []

    for c in candidates:
        if c.target_abs.exists():
            skipped_existing.append((c.source, c.target_rel))
            continue
        c.target_abs.parent.mkdir(parents=True, exist_ok=True)
        c.target_abs.write_text(build_content(c))
        created.append((c.kind, c.source, c.target_rel, c.id))

    if created:
        lines: List[str] = []
        lines.append("")
        lines.append(f"## {WAVE_LABEL}")
        lines.append("")
        lines.append("### Promoted")
        lines.append("")
        lines.append("| Kind | Staging Source | Canonical Target | Status |")
        lines.append("|---|---|---|---|")
        for kind, source, target_rel, _id in created:
            lines.append(f"| {kind} | `{source}` | `{target_rel}` | promoted |")
        lines.append("")
        lines.append("### Deprecation Mapping (staging scope)")
        lines.append("")
        lines.append("| Staging Source | Replaced By | State |")
        lines.append("|---|---|---|")
        for _kind, source, target_rel, _id in created:
            lines.append(f"| `{source}` | `{target_rel}` | deprecated-in-staging |")

        TRACKER.write_text(tracker_text.rstrip() + "\n" + "\n".join(lines) + "\n")

    report = {
        "wave": WAVE_LABEL,
        "shortlist_selected": len(selected),
        "already_promoted_sources": len(already_promoted_sources),
        "remaining_candidates_seen": len(candidates),
        "created_count": len(created),
        "skipped_existing_count": len(skipped_existing),
        "source_resolution": resolution_stats,
        "created_by_kind": {},
        "created": [
            {
                "kind": kind,
                "source": source,
                "target": target,
                "id": bp_id,
            }
            for kind, source, target, bp_id in created
        ],
        "skipped_existing": [
            {
                "source": source,
                "target": target,
            }
            for source, target in skipped_existing
        ],
    }

    by_kind: Dict[str, int] = {}
    for kind, *_ in created:
        by_kind[kind] = by_kind.get(kind, 0) + 1
    report["created_by_kind"] = by_kind

    REPORT.write_text(json.dumps(report, indent=2))
    print(json.dumps(report, indent=2))


if __name__ == "__main__":
    main()
