---
id: dockerfile-generator
name: Dockerfile Generator
title: Dockerfile Generator
description: >-
  Generate optimized Dockerfile with multi-stage builds
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: devops
tags:
  - command
  - packages
  - dockerfile
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
          - name: dockerfile-generator
            file: dockerfile-generator.md
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


# Dockerfile Generator

## Purpose

Generate optimized Dockerfile with multi-stage builds

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/devops-automation-pack/plugins/03-docker/commands/dockerfile-generate.md`
- canonical id: `dockerfile-generator`
