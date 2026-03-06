---
id: wordpress-elementor
title: WordPress Elementor
description: >-
  WordPress Elementor skill for component-driven page composition, responsive
  layout patterns, and maintainable content architecture.
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
          - name: wordpress-elementor
            file: wordpress-elementor.md
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


# WordPress Elementor

## Purpose

Define robust Elementor implementation patterns for scalable page building,
style consistency, and editable content workflows.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `wordpress/skills/wordpress-elementor/SKILL.md`
- canonical id: `wordpress-elementor`
