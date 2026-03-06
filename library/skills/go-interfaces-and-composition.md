---
id: go-interfaces-and-composition
title: Go Interfaces and Composition
description: >-
  Go interfaces, type assertions, type switches, and embedding from Effective Go. Covers implicit interface satisfaction, comma-ok idiom, generality through interface returns, interface and struct embedding for composition. Use when defining or implementing interfaces, using type assertions/switches, or composing types through embedding.
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
          - name: go-interfaces-and-composition
            file: go-interfaces-and-composition.md
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


# Go Interfaces and Composition

## Purpose

Go interfaces, type assertions, type switches, and embedding from Effective Go. Covers implicit interface satisfaction, comma-ok idiom, generality through interface returns, interface and struct embedding for composition. Use when defining or implementing interfaces, using type assertions/switches, or composing types through embedding.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `go/golang-skills/skills/go-interfaces/SKILL.md`
- canonical id: `go-interfaces-and-composition`
