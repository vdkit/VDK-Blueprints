---
id: go-documentation
title: Go Documentation
description: >-
  Guidelines for Go documentation including doc comments, package docs, godoc formatting, runnable examples, and signal boosting. Use when writing or reviewing documentation for Go packages, types, functions, or methods.
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
          - name: go-documentation
            file: go-documentation.md
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


# Go Documentation

## Purpose

Guidelines for Go documentation including doc comments, package docs, godoc formatting, runnable examples, and signal boosting. Use when writing or reviewing documentation for Go packages, types, functions, or methods.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `go/golang-skills/skills/go-documentation/SKILL.md`
- canonical id: `go-documentation`
