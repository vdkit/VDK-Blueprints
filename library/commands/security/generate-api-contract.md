---
id: generate-api-contract
name: Generate API Contract
title: Generate API Contract
description: >-
  Generate API contracts for consumer-driven testing with Pact, Spring Cloud
  Contract, or OpenAPI outputs and CI verification hooks.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - api
  - contracts
  - testing
  - openapi
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
          - name: generate-api-contract
            file: generate-api-contract.md
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
  - api-design-principles
  - implement-error-handling
conflicts: []
supersedes: []
---

# Generate API Contract

## Purpose

Define standardized API contract generation for service boundaries, enabling
safe evolution through consumer-provider compatibility validation.

## Core Capabilities

- framework targeting for Pact, Spring Cloud Contract, and OpenAPI formats
- generation of interaction-level expectations and validation rules
- provider verification scaffolding with state setup patterns
- CI-ready contract publishing and compatibility gate configuration
- versioning workflow for controlled contract evolution

## Output Contract

- contract artifacts and test harness stubs by selected framework
- schema assets for shared validation and reuse
- documentation output for cross-team consumption
