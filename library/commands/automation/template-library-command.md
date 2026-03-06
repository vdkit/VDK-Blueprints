---
id: template-library-command
name: Template Library Command
title: Template Library Command
description: >-
  Save and reuse successful video templates including scripts, thumbnails, titles, and editing styles
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: automation
tags:
  - command
  - packages
  - template
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
          - name: template-library-command
            file: template-library-command.md
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


# Template Library Command

## Purpose

Save and reuse successful video templates including scripts, thumbnails, titles, and editing styles

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/creator-studio-pack/plugins/workflow-optimization/template-library/commands/template.md`
- canonical id: `template-library-command`
