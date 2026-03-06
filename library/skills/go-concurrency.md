---
id: go-concurrency
title: Go Concurrency
description: >-
  Go concurrency patterns including goroutine lifecycle management, channel usage, mutex handling, and sync primitives. Use when writing concurrent Go code, spawning goroutines, working with channels, or documenting thread-safety guarantees. Based on Google and Uber Go Style Guides.
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
          - name: go-concurrency
            file: go-concurrency.md
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


# Go Concurrency

## Purpose

Go concurrency patterns including goroutine lifecycle management, channel usage, mutex handling, and sync primitives. Use when writing concurrent Go code, spawning goroutines, working with channels, or documenting thread-safety guarantees. Based on Google and Uber Go Style Guides.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `go/golang-skills/skills/go-concurrency/SKILL.md`
- canonical id: `go-concurrency`
