---
id: vscode-ai-productivity-pack
title: VS Code AI Productivity Pack Distribution
description: >-
  Plugin distribution blueprint defining a curated VS Code extension pack for
  AI-assisted development workflows and repository onboarding.
version: 1.0.0
lastUpdated: '2026-02-25'
category: plugin
subcategory: distribution
complexity: simple
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: plugin-distribution
specificityLayer: L1
author: VDK
tags:
  - plugin
  - distribution
  - vscode
  - extensions
platforms:
  vscode:
    compatible: true
    enabled: true
    components:
      distribution:
        type: vscode-extension-pack
        enabled: true
        location: .vscode/extensions.json
        manifests:
          - name: vscode-ai-productivity-pack
            file: extensions.json
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

# VS Code AI Productivity Pack

## Purpose

Define a reusable plugin distribution profile for repositories that standardize
AI-centric VS Code developer experience.

## Recommended Extensions

- `github.copilot`
- `github.copilot-chat`
- `esbenp.prettier-vscode`
- `dbaeumer.vscode-eslint`

## Distribution Artifact

The target artifact is `.vscode/extensions.json` with a curated
`recommendations` list and optional `unwantedRecommendations` guardrails.
