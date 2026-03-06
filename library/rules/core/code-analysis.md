---
id: code-analysis
title: Code Analysis
description: >-
  Imported conditional-rule blueprint from staging source code-analysis.mdc.
version: 1.0.0
lastUpdated: '2026-03-02'
category: core
subcategory: rule
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: conditional-rule
specificityLayer: L3
author: VDK
tags:
  - rule
  - imported
  - conditional-rule
  - code-analysis
  - code
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      rules:
        type: claude-rule
        enabled: true
        location: .claude/rules/
        manifests:
          - name: code-analysis
            file: code-analysis.md
  cursor:
    compatible: true
    enabled: true
    components:
      rules:
        type: cursor-rule
        enabled: true
        location: .cursor/rules/
        format: mdc
        manifests:
          - name: code-analysis
            file: code-analysis.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Code Analysis

## Purpose

Imported conditional-rule blueprint from staging source code-analysis.mdc.

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `code-analysis.mdc`
- canonical id: `code-analysis`
