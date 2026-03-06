---
id: codeql-security-analysis
title: CodeQL Security Analysis Workflow
description: >-
  Workflow blueprint for selecting CodeQL packs, model packs, threat models,
  executing analysis, and triaging result outputs.
version: 1.0.0
lastUpdated: '2026-03-02'
category: workflow
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: workflow
specificityLayer: L2
author: VDK
tags:
  - workflow
  - security
  - codeql
  - static-analysis
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
          - name: codeql-security-analysis
            file: codeql-security-analysis.md
  windsurf:
    compatible: true
    enabled: true
    components:
      workflows:
        type: windsurf-workflow
        enabled: true
        location: .windsurf/workflows/
        manifests:
          - name: codeql-security-analysis
            file: codeql-security-analysis.yaml
            trigger:
              - manual
requires: []
suggests:
  - security-reviewer
conflicts: []
supersedes: []
---

# CodeQL Security Analysis Workflow

## Objective

Run reproducible CodeQL analysis with explicit pack/model/threat selection and
produce triage-ready findings.

## Workflow Stages

1. select target database and language
2. resolve installed query and model packs
3. select threat model scope
4. run analysis and export SARIF
5. summarize findings by severity and rule

## Output Contract

- selected analysis configuration (packs and threat model)
- SARIF output path
- severity summary and top findings
