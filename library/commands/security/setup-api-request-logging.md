---
id: setup-api-request-logging
name: Set Up API Request Logging
title: Set Up API Request Logging
description: >-
  Configure structured API request logging with correlation IDs, PII redaction,
  response timing, and centralized log shipping integration.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - api
  - logging
  - observability
  - security
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
          - name: setup-api-request-logging
            file: setup-api-request-logging.md
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
  - add-rate-limiting
conflicts: []
supersedes: []
---

# Set Up API Request Logging

## Purpose

Provide a robust logging implementation blueprint for API services with strong
debuggability, compliance-aware sanitization, and operational visibility.

## Core Capabilities

- structured JSON log emission with consistent schema fields
- request correlation identifiers propagated across service boundaries
- request/response timing and status instrumentation
- sensitive-field redaction and configurable data minimization policies
- compatibility with centralized aggregation pipelines and retention policies

## Operational Requirements

- non-blocking logging strategy for request-path performance safety
- log rotation and storage controls for sustained production operation
- compliance alignment for data retention and access control
