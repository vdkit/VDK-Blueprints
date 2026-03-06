---
id: accessibility-audit
name: Accessibility Audit
title: Accessibility Audit
description: >-
  Audit UI code against WCAG 2.1/2.2 criteria with issue severity reporting,
  remediation guidance, and optional guided fix workflow.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - accessibility
  - wcag
  - ui
  - audit
author: VDK
lastUpdated: '2026-03-02'
schemaVersion: '3.0'
kind: command
specificityLayer: L3
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
          - name: accessibility-audit
            file: accessibility-audit.md
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
  - design-system-setup
  - ui-designer
conflicts: []
supersedes: []
---

# Accessibility Audit

## Purpose

Provide a complete accessibility audit workflow for UI code with WCAG
compliance checks, severity-scored findings, and implementation-ready fixes.

## Core Capabilities

- target scoping for component, route, directory, app-wide, or recent changes
- WCAG level selection support (A, AA, AAA) with optional focus areas
- static checks for semantics, keyboard support, forms, ARIA, and contrast
- issue classification into critical, serious, moderate, and minor severities
- generation of structured audit output and guided remediation flow

## Output Contract

- audit state artifact for resumable execution
- markdown report with findings, criteria mapping, and code-level fixes
- prioritized remediation queues and test recommendations
