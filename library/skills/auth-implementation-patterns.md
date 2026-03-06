---
id: auth-implementation-patterns
title: Auth Implementation Patterns Skill
description: >-
  Authentication and authorization skill for JWT/session/OAuth flows, RBAC,
  permission checks, and resource-ownership enforcement.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: security
complexity: complex
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L2
author: VDK
tags:
  - skill
  - auth
  - authorization
  - security
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
          - name: auth-implementation-patterns
            file: auth-implementation-patterns.md
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
  - build-auth-system
  - add-rate-limiting
conflicts: []
supersedes: []
---

# Auth Implementation Patterns Skill

## Purpose

Define secure implementation patterns for authentication and authorization
systems that scale across APIs, web applications, and multi-service platforms.

## Core Coverage

- JWT and refresh-token lifecycle management patterns
- session-based authentication with secure cookie controls
- OAuth and third-party identity provider integration flows
- role- and permission-based authorization middleware patterns
- resource ownership enforcement and privileged-access safeguards

## Integration Expectations

- strict credential handling with hardened secret management
- explicit server-side authorization checks on protected resources
- security event logging and brute-force protection for auth endpoints
