---
id: ai-monitoring-setup
name: AI Monitoring Setup
title: AI Monitoring Setup
description: >-
  Set up comprehensive LLM monitoring, cost tracking, and observability
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: automation
tags:
  - command
  - packages
  - ai
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
          - name: ai-monitoring-setup
            file: ai-monitoring-setup.md
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


# AI Monitoring Setup

## Purpose

Set up comprehensive LLM monitoring, cost tracking, and observability

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/ai-ml-engineering-pack/plugins/04-ai-safety/commands/ai-monitoring-setup.md`
- canonical id: `ai-monitoring-setup`
