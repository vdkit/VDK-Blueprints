#!/usr/bin/env python3
import json
from pathlib import Path

root = Path('/Users/dominikospritis/DevFolder/My-Projects/VDK-Ecosystem')
shortlist = json.loads((root / 'VDK-Blueprints/library-snapshots/staging-promotion-candidates-latest.json').read_text())['selected']
tracker_lines = (root / 'VDK-Blueprints/docs/STAGING_PROMOTION_DEPRECATION_TRACKER.md').read_text().splitlines()

promoted_sources = set()
for line in tracker_lines:
    line = line.strip()
    if not line.startswith('|') or 'promoted' not in line:
        continue
    cols = [c.strip() for c in line.strip('|').split('|')]
    if len(cols) < 4:
        continue
    source = cols[1].strip('` ')
    status = cols[3].strip()
    if status == 'promoted' and source:
        promoted_sources.add(source)

missing = [item['path'] for item in shortlist if item['path'] not in promoted_sources]

staging = root / 'staging-blueprints'
shortlist_existing = [item['path'] for item in shortlist if (staging / item['path']).exists()]
shortlist_missing_files = [item['path'] for item in shortlist if not (staging / item['path']).exists()]

print(json.dumps({
    'shortlist_total': len(shortlist),
    'promoted_in_tracker_for_shortlist': len(shortlist) - len(missing),
    'missing_count': len(missing),
    'missing': missing[:20],
    'shortlist_source_files_existing': len(shortlist_existing),
    'shortlist_source_files_missing': len(shortlist_missing_files),
    'shortlist_source_files_missing_sample': shortlist_missing_files[:20]
}, indent=2))
