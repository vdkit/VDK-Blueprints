---
id: go-naming-conventions
title: Go Naming Conventions
description: >-
  Go naming conventions for packages, functions, methods, variables, constants, and receivers from Google and Uber style guides. Use when naming any identifier in Go code—choosing names for types, functions, methods, variables, constants, or packages—to ensure clarity, consistency, and idiomatic style.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: go
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L3
author: VDK
tags:
  - skill
  - imported
  - go
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
          - name: go-naming-conventions
            file: go-naming-conventions.md
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


# Go Naming Conventions

## Purpose

Go naming conventions for packages, functions, methods, variables, constants, and receivers from Google and Uber style guides. Use when naming any identifier in Go code—choosing names for types, functions, methods, variables, constants, or packages—to ensure clarity, consistency, and idiomatic style.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `go/golang-skills/skills/go-naming/SKILL.md`
- canonical id: `go-naming-conventions`
