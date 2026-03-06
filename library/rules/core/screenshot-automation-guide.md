---
id: screenshot-automation-guide
title: Screenshot Automation Guide
description: >-
  Reusable AppleScript patterns for automated screenshot capture for documentation and testing
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
  - screenshot-automation
  - screenshot
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
          - name: screenshot-automation-guide
            file: screenshot-automation-guide.md
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
          - name: screenshot-automation-guide
            file: screenshot-automation-guide.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Screenshot Automation Guide

## Purpose

Reusable AppleScript patterns for automated screenshot capture for documentation and testing

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `screenshot-automation.mdc`
- canonical id: `screenshot-automation-guide`
