---
id: cryptography-audit
name: Cryptography Audit
title: Cryptography Audit
description: >-
  Reviews cryptographic implementations for security vulnerabilities
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: security
tags:
  - command
  - packages
  - cryptography
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
          - name: cryptography-audit
            file: cryptography-audit.md
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


# Cryptography Audit

## Purpose

Reviews cryptographic implementations for security vulnerabilities

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/security-pro-pack/plugins/03-cryptography/commands/crypto-audit.md`
- canonical id: `cryptography-audit`
