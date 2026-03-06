---
id: safari-automation-guide
title: Safari Automation Guide
description: >-
  Patterns and best practices for automating Safari browser interactions for web UI automation and testing
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
  - safari-automation
  - safari
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
          - name: safari-automation-guide
            file: safari-automation-guide.md
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
          - name: safari-automation-guide
            file: safari-automation-guide.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Safari Automation Guide

## Purpose

Patterns and best practices for automating Safari browser interactions for web UI automation and testing

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `safari-automation.mdc`
- canonical id: `safari-automation-guide`
