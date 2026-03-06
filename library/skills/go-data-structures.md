---
id: go-data-structures
title: Go Data Structures
description: >-
  Go data structures including allocation with new vs make, arrays, slices, maps, printing with fmt, and constants with iota. Use when working with Go's built-in data structures, memory allocation, or formatted output.
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
          - name: go-data-structures
            file: go-data-structures.md
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


# Go Data Structures

## Purpose

Go data structures including allocation with new vs make, arrays, slices, maps, printing with fmt, and constants with iota. Use when working with Go's built-in data structures, memory allocation, or formatted output.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `go/golang-skills/skills/go-data-structures/SKILL.md`
- canonical id: `go-data-structures`
