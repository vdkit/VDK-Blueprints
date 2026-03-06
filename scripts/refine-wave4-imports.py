#!/usr/bin/env python3
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path('/Users/dominikospritis/DevFolder/My-Projects/VDK-Ecosystem')
TRACKER = ROOT / 'VDK-Blueprints/docs/STAGING_PROMOTION_DEPRECATION_TRACKER.md'
LIB_ROOT = ROOT / 'VDK-Blueprints'
REPORT = ROOT / 'VDK-Blueprints/library-snapshots/wave4-refinement-report.txt'


def slug(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    s = re.sub(r'-{2,}', '-', s).strip('-')
    return s


def classify_subcategory(kind: str, source: str, bp_id: str) -> str | None:
    s = f"{source} {bp_id}".lower()
    if kind == 'skill':
        if any(k in s for k in ['python', 'pytest', 'uv']):
            return 'python'
        if any(k in s for k in ['go-', '/go/', 'golang']):
            return 'go'
        if any(k in s for k in ['wordpress']):
            return 'cms'
        if any(k in s for k in ['shopify', 'ecommerce']):
            return 'ecommerce'
        if any(k in s for k in ['security', 'auth', 'gdpr', 'mtls']):
            return 'security'
        if any(k in s for k in ['react', 'next', 'frontend', 'ui']):
            return 'frontend'
        if any(k in s for k in ['terraform', 'cloud', 'devops', 'kubernetes', 'docker', 'linkerd']):
            return 'devops'
        if any(k in s for k in ['market', 'social', 'business']):
            return 'business'
        return 'imported'
    if kind == 'command':
        if any(k in s for k in ['security', 'auth', 'sast', 'scan', 'audit']):
            return 'security'
        if any(k in s for k in ['api', 'contract', 'event', 'logging']):
            return 'api'
        if any(k in s for k in ['terraform', 'docker', 'helm', 'cloudformation']):
            return 'devops'
        return 'automation'
    if kind == 'workflow':
        return 'automation'
    if kind == 'plugin-distribution':
        return 'distribution'
    if kind == 'conditional-rule':
        return 'rule'
    if kind == 'agent':
        return 'assistant'
    return None


def derive_domain_tag(source: str) -> str:
    if '/' not in source:
        return slug(source.split('.')[0])
    first = source.split('/')[0]
    return slug(first)


def parse_frontmatter(text: str) -> tuple[str, str, str]:
    if not text.startswith('---\n'):
        return '', '', text
    end = text.find('\n---\n', 4)
    if end == -1:
        return '', '', text
    fm = text[4:end]
    body = text[end + 5 :]
    return '---\n', fm, body


def update_or_insert_scalar(fm_lines: list[str], key: str, value: str) -> list[str]:
    pattern = re.compile(rf'^{re.escape(key)}:\s*')
    replaced = False
    out = []
    for line in fm_lines:
        if pattern.match(line):
            out.append(f'{key}: {value}')
            replaced = True
        else:
            out.append(line)
    if not replaced:
        insert_at = 0
        for i, line in enumerate(out):
            if line.startswith('category:') or line.startswith('subcategory:'):
                insert_at = i + 1
        out.insert(insert_at, f'{key}: {value}')
    return out


def update_tags_block(fm: str, required_tags: list[str]) -> str:
    lines = fm.splitlines()
    tag_start = None
    for i, ln in enumerate(lines):
        if ln.strip() == 'tags:':
            tag_start = i
            break

    if tag_start is None:
        # insert before platforms
        insert_at = next((i for i, ln in enumerate(lines) if ln.startswith('platforms:')), len(lines))
        block = ['tags:'] + [f'  - {t}' for t in required_tags]
        lines[insert_at:insert_at] = block
        return '\n'.join(lines)

    # collect existing tag block
    tag_end = tag_start + 1
    while tag_end < len(lines) and lines[tag_end].startswith('  - '):
        tag_end += 1
    existing = [ln.strip()[2:].strip() for ln in lines[tag_start + 1 : tag_end] if ln.strip().startswith('- ')]

    merged = []
    for t in existing + required_tags:
        if t and t not in merged:
            merged.append(t)

    new_block = ['tags:'] + [f'  - {t}' for t in merged]
    lines[tag_start:tag_end] = new_block
    return '\n'.join(lines)


def ensure_section(body: str, section_title: str, content: str, before: str = '## Source Mapping') -> str:
    if section_title in body:
        return body
    if before in body:
        return body.replace(before, f'{section_title}\n\n{content}\n\n{before}')
    return body.rstrip() + f'\n\n{section_title}\n\n{content}\n'


def refine_body(kind: str, body: str, bp_id: str, source: str) -> str:
    if kind == 'command':
        content = '\n'.join([
            '- interactive scoping for repository and target context',
            '- implementation guidance aligned with existing architecture constraints',
            '- output expectations for repeatable execution and reviewability',
        ])
        body = ensure_section(body, '## Core Capabilities', content)
    elif kind == 'skill':
        coverage = '\n'.join([
            '- architecture and implementation patterns for the domain',
            '- quality, reliability, and maintainability guardrails',
            '- practical execution guidance for production usage',
        ])
        expect = '\n'.join([
            '- preserve integration contracts and existing interfaces',
            '- surface operational constraints and validation requirements',
            '- prioritize testability and observability in implementations',
        ])
        body = ensure_section(body, '## Core Coverage', coverage)
        body = ensure_section(body, '## Integration Expectations', expect)
    elif kind == 'workflow':
        stages = '\n'.join([
            '1. establish scope and prerequisites',
            '2. execute ordered workflow steps with checkpoints',
            '3. produce outputs and summarize validation state',
        ])
        body = ensure_section(body, '## Workflow Stages', stages)
    elif kind == 'plugin-distribution':
        included = '\n'.join([
            '- packaged guidance scope and distribution intent',
            '- installation and activation compatibility boundaries',
            '- expected integration surfaces across supported tools',
        ])
        body = ensure_section(body, '## Included Focus Areas', included)
    elif kind == 'conditional-rule':
        guidance = '\n'.join([
            '- apply when repository context matches the rule domain',
            '- prefer deterministic checks over implicit assumptions',
            '- document deviations when constraints require exceptions',
        ])
        body = ensure_section(body, '## Activation Guidance', guidance)
    elif kind == 'agent':
        deliverables = '\n'.join([
            '- scoped implementation plan and execution constraints',
            '- quality criteria and acceptance checks',
            '- explicit outputs and handoff notes',
        ])
        body = ensure_section(body, '## Deliverables', deliverables)

    # normalize trailing whitespace
    body = re.sub(r'\n{3,}', '\n\n', body).rstrip() + '\n'
    return body


def parse_wave4_rows(tracker_text: str) -> list[tuple[str, str, str]]:
    # rows: | kind | `source` | `target` | promoted |
    in_wave4 = False
    rows: list[tuple[str, str, str]] = []
    for line in tracker_text.splitlines():
        if line.startswith('## Wave 4 (bulk)'):
            in_wave4 = True
            continue
        if in_wave4 and line.startswith('## ') and not line.startswith('## Wave 4 (bulk)'):
            break
        if not in_wave4:
            continue
        m = re.match(r"\|\s*([^|]+?)\s*\|\s*`([^`]+)`\s*\|\s*`([^`]+)`\s*\|\s*promoted\s*\|", line)
        if m:
            kind = m.group(1).strip()
            source = m.group(2).strip()
            target = m.group(3).strip()
            rows.append((kind, source, target))
    return rows


def main() -> None:
    tracker_text = TRACKER.read_text()
    rows = parse_wave4_rows(tracker_text)
    if not rows:
        REPORT.write_text('No Wave 4 rows found.\n')
        print('No Wave 4 rows found.')
        return

    updated = 0
    skipped = 0
    missing = 0
    missing_files: list[str] = []

    for kind, source, target in rows:
        path = LIB_ROOT / target
        if not path.exists():
            missing += 1
            missing_files.append(target)
            continue

        text = path.read_text()
        _, fm, body = parse_frontmatter(text)
        if not fm:
            skipped += 1
            continue

        fm_lines = fm.splitlines()

        id_match = re.search(r'^id:\s*([^\n]+)$', fm, flags=re.MULTILINE)
        bp_id = id_match.group(1).strip() if id_match else slug(Path(target).stem)

        # subcategory normalization
        subcategory = classify_subcategory(kind, source, bp_id)
        if subcategory:
            fm_lines = update_or_insert_scalar(fm_lines, 'subcategory', subcategory)

        # tags normalization
        domain_tag = derive_domain_tag(source)
        required = [
            kind if kind != 'plugin-distribution' else 'plugin-distribution',
            'imported',
            domain_tag,
        ]
        # add id-root tag
        id_root = bp_id.split('-')[0] if '-' in bp_id else bp_id
        if id_root and id_root not in required:
            required.append(id_root)

        new_fm = update_tags_block('\n'.join(fm_lines), [slug(t) for t in required if t])
        new_body = refine_body(kind, body, bp_id, source)

        new_text = f"---\n{new_fm}\n---\n\n{new_body}"
        if new_text != text:
            path.write_text(new_text)
            updated += 1

    report_lines = [
        f'Wave4 rows scanned: {len(rows)}',
        f'Updated files: {updated}',
        f'Skipped (no frontmatter parse): {skipped}',
        f'Missing target files: {missing}',
    ]
    if missing_files:
        report_lines.append('Missing list:')
        report_lines.extend(f'- {m}' for m in missing_files)

    REPORT.write_text('\n'.join(report_lines) + '\n')
    print('\n'.join(report_lines))


if __name__ == '__main__':
    main()
