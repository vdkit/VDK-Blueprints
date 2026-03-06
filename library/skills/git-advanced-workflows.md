---
id: git-advanced-workflows
title: Git Advanced Workflows
description: >-
  Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from any situation. Use when managing complex Git histories, collaborating on feature branches, or troubleshooting repository issues.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: version-control
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
  - developer-essentials
  - git
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
          - name: git-advanced-workflows
            file: git-advanced-workflows.md
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


# Git Advanced Workflows

## Purpose

Master advanced Git workflows including rebasing, cherry-picking, bisect, worktrees, and reflog to maintain clean history and recover from any situation. Use when managing complex Git histories, collaborating on feature branches, or troubleshooting repository issues.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `developer-essentials/skills/git-advanced-workflows/SKILL.md`
- canonical id: `git-advanced-workflows`
