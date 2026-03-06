---
id: wordpress-setup
title: WordPress Setup
description: >-
  WordPress setup skill for installation, baseline configuration, environment
  hardening, and deployment readiness workflows.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: cms
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
  - wordpress
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
          - name: wordpress-setup
            file: wordpress-setup.md
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


# WordPress Setup

## Purpose

Provide implementation guidance for initializing and configuring WordPress
projects with secure defaults and repeatable setup conventions.

## Core Coverage

- architecture and implementation patterns for the domain
- quality, reliability, and maintainability guardrails
- practical execution guidance for production usage

## Integration Expectations

- preserve integration contracts and existing interfaces
- surface operational constraints and validation requirements
- prioritize testability and observability in implementations

## Source Mapping

- staging source: `wordpress/skills/wordpress-setup/SKILL.md`
- canonical id: `wordpress-setup`
