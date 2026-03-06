---
id: sast-security-plugin
name: SAST Security Plugin
title: SAST Security Plugin
description: >-
  Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: security
tags:
  - command
  - security-scanning
  - sast
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
          - name: sast-security-plugin
            file: sast-security-plugin.md
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


# SAST Security Plugin

## Purpose

Static Application Security Testing (SAST) for code vulnerability analysis across multiple languages and frameworks

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `security-scanning/commands/security-sast.md`
- canonical id: `sast-security-plugin`
