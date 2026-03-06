---
id: error-handling-patterns
title: Error Handling Patterns Skill
description: >-
  Error handling skill for exception taxonomy, result-based flows, retry
  strategies, circuit breaking, and graceful degradation.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: reliability
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
  - error-handling
  - reliability
  - resilience
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
          - name: error-handling-patterns
            file: error-handling-patterns.md
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
  - implement-error-handling
conflicts: []
supersedes: []
---

# Error Handling Patterns Skill

## Purpose

Provide implementation guidance for resilient error handling across
language/runtime models, from local validation errors to distributed failures.

## Core Coverage

- exception hierarchy and contextual error propagation patterns
- result/option-style handling for predictable control flow
- retry and backoff strategies for transient dependency failures
- circuit-breaker and fallback patterns for service resilience
- aggregation and reporting techniques for multi-error workflows

## Integration Expectations

- no silent error swallowing in production paths
- actionable, typed error contracts at API boundaries
- structured logging with context for rapid incident diagnosis
