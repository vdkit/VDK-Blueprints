---
id: context-prime
title: Context Prime
description: >-
  Imported conditional-rule blueprint from staging source context-prime.mdc.
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
  - context-prime
  - context
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
          - name: context-prime
            file: context-prime.md
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
          - name: context-prime
            file: context-prime.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Context Prime

## Purpose

Imported conditional-rule blueprint from staging source context-prime.mdc.

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `context-prime.mdc`
- canonical id: `context-prime`
