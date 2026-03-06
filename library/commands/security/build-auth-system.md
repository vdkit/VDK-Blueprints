---
id: build-auth-system
name: Build API Authentication System
title: Build API Authentication System
description: >-
  Generate API authentication and authorization architecture including token
  strategy, middleware, role controls, and security hardening patterns.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - auth
  - security
  - api
author: VDK
lastUpdated: '2026-03-02'
schemaVersion: '3.0'
kind: command
specificityLayer: L2
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
          - name: build-auth-system
            file: build-auth-system.md
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests:
  - security-audit
conflicts: []
supersedes: []
---

# Build API Authentication System

## Purpose

Provide structured implementation guidance for API authentication and
authorization, including JWT/session/API key options and role/permission
controls.

## Scope

- auth method selection by system constraints
- secure user credential flows
- token/session lifecycle management
- role-based authorization middleware design
- endpoint protection strategy and error responses

## Quality Gates

- no plaintext credential handling
- security headers and rate limiting in place
- predictable auth and authorization error format
- auditable access decisions
