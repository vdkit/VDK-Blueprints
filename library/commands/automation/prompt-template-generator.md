---
id: prompt-template-generator
name: Prompt Template Generator
title: Prompt Template Generator
description: >-
  Generate reusable prompt templates with variables and best practices
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: automation
tags:
  - command
  - packages
  - prompt
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
          - name: prompt-template-generator
            file: prompt-template-generator.md
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


# Prompt Template Generator

## Purpose

Generate reusable prompt templates with variables and best practices

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/ai-ml-engineering-pack/plugins/01-prompt-engineering/commands/prompt-template-gen.md`
- canonical id: `prompt-template-generator`
