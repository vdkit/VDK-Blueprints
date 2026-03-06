---
id: design-system-setup
name: Design System Setup
title: Design System Setup
description: >-
  Initialize a design system with token scales, color modes, typography,
  spacing, and output formats for consistent UI implementation.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - design-system
  - ui
  - tokens
  - frontend
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
          - name: design-system-setup
            file: design-system-setup.md
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
  - ui-designer
conflicts: []
supersedes: []
---

# Design System Setup

## Purpose

Create a structured design system foundation that supports multi-theme UI work,
token governance, and predictable component styling.

## Core Capabilities

- interactive configuration for preset depth and design constraints
- token generation for color, typography, spacing, and radius scales
- support for light/dark/system-aware color mode strategies
- output generation in CSS variables, Tailwind, JSON, or multi-format bundles
- optional component guideline generation for reusable UI patterns

## Output Contract

- generated token definitions
- selected output artifacts by format
- setup state summary for reproducible updates