---
id: codebase-analyst-skill
title: Codebase Analyst Skill
description: >-
  Reusable skill blueprint for structured codebase analysis, dependency mapping,
  and targeted snippet extraction before implementation work.
version: 1.0.0
lastUpdated: '2026-02-25'
category: skill
subcategory: analysis
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
  - analysis
  - discovery
  - codebase
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
          - name: codebase-analyst
            file: codebase-analyst.md
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
          - name: codebase-analyst
            file: codebase-analyst.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---

# Codebase Analyst Skill

## Purpose

Provide a repeatable analysis workflow before implementation so changes are made
against real call sites, existing conventions, and verified dependencies.

## Core Behavior

1. Start with semantic search for relevant symbols and concepts.
2. Confirm usage paths with exact-text search and symbol references.
3. Read target files end-to-end before editing.
4. Map dependencies and side effects before proposing changes.
5. Produce concise findings with concrete file-level evidence.

## Output Contract

- Relevant files list with why each file matters.
- Key symbols and call paths.
- Risks and integration considerations.
- Recommended implementation entry points.
