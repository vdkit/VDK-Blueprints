---
id: wordpress-content
title: WordPress Content
description: >-
  WordPress content operations skill for editorial workflows, taxonomy design,
  publishing quality controls, and SEO-aware authoring.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: cms
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
  - wordpress
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
          - name: wordpress-content
            file: wordpress-content.md
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


# WordPress Content

## Purpose

Provide structured guidance for managing WordPress content lifecycle from draft
through publication with consistency and governance.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `wordpress/skills/wordpress-content/SKILL.md`
- canonical id: `wordpress-content`
