---
id: linkerd-patterns
title: Linkerd Patterns
description: >-
  Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking with minimal overhead.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: devops
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
  - cloud-infrastructure
  - linkerd
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
          - name: linkerd-patterns
            file: linkerd-patterns.md
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


# Linkerd Patterns

## Purpose

Implement Linkerd service mesh patterns for lightweight, security-focused service mesh deployments. Use when setting up Linkerd, configuring traffic policies, or implementing zero-trust networking with minimal overhead.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `cloud-infrastructure/skills/linkerd-patterns/SKILL.md`
- canonical id: `linkerd-patterns`
