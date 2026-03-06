---
id: api-design-principles
title: API Design Principles Skill
description: >-
  API design skill covering REST and GraphQL architecture, versioning,
  pagination, error contracts, and resolver performance patterns.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: backend
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L2
author: VDK
tags:
  - skill
  - api
  - rest
  - graphql
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
          - name: api-design-principles
            file: api-design-principles.md
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
  - implement-error-handling
conflicts: []
supersedes: []
---

# API Design Principles Skill

## Purpose

Provide durable API design guidance for REST and GraphQL systems that remain
intuitive, scalable, and maintainable over long product lifecycles.

## Core Coverage

- resource-oriented REST modeling and HTTP method semantics
- GraphQL schema-first design with typed queries, mutations, and pagination
- consistent error response contracts and status semantics
- versioning and deprecation strategy for breaking evolution
- resolver efficiency patterns including batching and N+1 mitigation

## Integration Expectations

- stable public contracts with explicit compatibility boundaries
- predictable pagination/filter/search behavior across endpoints
- documentation and design review gates before implementation rollout
