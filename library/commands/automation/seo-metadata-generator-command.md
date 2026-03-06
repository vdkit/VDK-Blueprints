---
id: seo-metadata-generator-command
name: SEO Metadata Generator Command
title: SEO Metadata Generator Command
description: >-
  Generate SEO-optimized metadata for YouTube, blogs, and social platforms with keyword research and ranking strategies
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: automation
tags:
  - command
  - packages
  - seo
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
          - name: seo-metadata-generator-command
            file: seo-metadata-generator-command.md
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


# SEO Metadata Generator Command

## Purpose

Generate SEO-optimized metadata for YouTube, blogs, and social platforms with keyword research and ranking strategies

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/creator-studio-pack/plugins/content-strategy/seo-metadata-generator/commands/metadata.md`
- canonical id: `seo-metadata-generator-command`
