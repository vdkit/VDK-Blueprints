---
id: sql-optimization-patterns
title: SQL Optimization Patterns
description: >-
  Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow queries. Use when debugging slow queries, designing database schemas, or optimizing application performance.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: database
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
  - developer-essentials
  - sql
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
          - name: sql-optimization-patterns
            file: sql-optimization-patterns.md
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


# SQL Optimization Patterns

## Purpose

Master SQL query optimization, indexing strategies, and EXPLAIN analysis to dramatically improve database performance and eliminate slow queries. Use when debugging slow queries, designing database schemas, or optimizing application performance.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `developer-essentials/skills/sql-optimization-patterns/SKILL.md`
- canonical id: `sql-optimization-patterns`
