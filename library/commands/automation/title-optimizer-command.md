---
id: title-optimizer-command
name: Title Optimizer Command
title: Title Optimizer Command
description: >-
  A/B test video titles for maximum CTR using proven formulas and psychological triggers
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: automation
tags:
  - command
  - packages
  - title
author: VDK
lastUpdated: '2026-03-02'
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
          - name: title-optimizer-command
            file: title-optimizer-command.md
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


# Title Optimizer Command

## Purpose

A/B test video titles for maximum CTR using proven formulas and psychological triggers

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/creator-studio-pack/plugins/content-strategy/title-optimizer/commands/optimize-title.md`
- canonical id: `title-optimizer-command`
