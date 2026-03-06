---
id: codeql-data-extensions
title: CodeQL Data Extensions Workflow
description: >-
  Workflow blueprint for discovering missing source/sink models, generating
  data extension packs, and validating security analysis coverage improvements.
version: 1.0.0
lastUpdated: '2026-03-02'
category: workflow
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: workflow
specificityLayer: L3
author: VDK
tags:
  - workflow
  - security
  - codeql
  - data-extensions
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
          - name: codeql-data-extensions
            file: codeql-data-extensions.md
  windsurf:
    compatible: true
    enabled: true
    components:
      workflows:
        type: windsurf-workflow
        enabled: true
        location: .windsurf/workflows/
        manifests:
          - name: codeql-data-extensions
            file: codeql-data-extensions.yaml
            trigger:
              - manual
requires:
  - codeql-build-database
suggests:
  - codeql-security-analysis
conflicts: []
supersedes: []
---

# CodeQL Data Extensions Workflow

## Purpose

Improve CodeQL result quality by identifying project-specific sources, sinks,
and summaries that default model packs do not cover.

## Core Stages

1. detect existing in-repo and installed model packs
2. query current known sources and sinks from the database
3. map project API surface against known model inventory
4. create data extension files for identified gaps
5. rerun analysis and validate expected coverage improvements

## Early Exit Logic

- exit when existing extensions already satisfy the project scope
- exit when no meaningful modeling gaps are found

## Output Contract

- extension pack path(s)
- list of newly modeled sources/sinks/summaries
- before/after analysis comparison notes