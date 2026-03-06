---
id: nx-workspace-patterns
title: Nx Workspace Patterns
description: >-
  Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: monorepo
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
  - nx
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
          - name: nx-workspace-patterns
            file: nx-workspace-patterns.md
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


# Nx Workspace Patterns

## Purpose

Configure and optimize Nx monorepo workspaces. Use when setting up Nx, configuring project boundaries, optimizing build caching, or implementing affected commands.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `developer-essentials/skills/nx-workspace-patterns/SKILL.md`
- canonical id: `nx-workspace-patterns`
