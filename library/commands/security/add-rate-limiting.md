---
id: add-rate-limiting
name: Add Rate Limiting
title: Add Rate Limiting to API Endpoints
description: >-
  Implement distributed API rate limiting with Redis-backed algorithms,
  tier-based policies, observability, and graceful failure handling.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - api
  - security
  - ratelimit
  - redis
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
          - name: add-rate-limiting
            file: add-rate-limiting.md
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

# Add Rate Limiting to API Endpoints

## Purpose

Establish robust rate limiting for APIs with production-safe defaults,
distributed counters, and clear client feedback when limits are exceeded.

## Core Capabilities

- algorithm selection guidance for token bucket, sliding window, and fixed window
- Redis-backed distributed enforcement for horizontally scaled services
- tier-aware limit strategies across anonymous, free, premium, and enterprise users
- endpoint-specific controls for expensive operations
- headers, retry guidance, and policy-driven error responses

## Operational Requirements

- graceful degradation on dependency failure to avoid full traffic outages
- instrumentation for blocked requests, limiter latency, and tier usage
- validation of key expiry and memory footprint to prevent Redis key leaks
