---
id: codeql-build-database
title: CodeQL Build Database Workflow
description: >-
  Workflow blueprint for building high-quality CodeQL databases across
  interpreted and compiled languages with fallback build strategies and
  quality validation.
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
  - database-build
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
          - name: codeql-build-database
            file: codeql-build-database.md
  windsurf:
    compatible: true
    enabled: true
    components:
      workflows:
        type: windsurf-workflow
        enabled: true
        location: .windsurf/workflows/
        manifests:
          - name: codeql-build-database
            file: codeql-build-database.yaml
            trigger:
              - manual
requires: []
suggests:
  - codeql-security-analysis
conflicts: []
supersedes: []
---

# CodeQL Build Database Workflow

## Purpose

Create a CodeQL database with reproducible build and logging steps, including
language detection, build-strategy fallback, and quality assessment.

## Core Stages

1. detect primary language and build system characteristics
2. configure exclusions for interpreted languages when applicable
3. run build sequence with fallback methods
4. apply remediation for failed or low-quality extraction
5. assess database quality and record final build command

## Build Strategy Order

- interpreted languages: single-pass `database create`
- compiled languages:
  1. autobuild
  2. explicit build command
  3. trace-command multi-step flow
  4. no-build fallback for partial analysis

## Output Contract

- selected language and build mode
- created database path
- build log path and remediation notes
- quality assessment summary