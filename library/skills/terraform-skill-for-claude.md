---
id: terraform-skill-for-claude
title: Terraform Skill for Claude
description: >-
  Terraform infrastructure as code best practices
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
  - terraform-skill
  - terraform
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
          - name: terraform-skill-for-claude
            file: terraform-skill-for-claude.md
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


# Terraform Skill for Claude

## Purpose

Terraform infrastructure as code best practices

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `terraform-skill/SKILL.md`
- canonical id: `terraform-skill-for-claude`
