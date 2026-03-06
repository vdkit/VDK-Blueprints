---
id: cursor-rules-meta-guide
title: Cursor Rules Meta Guide
description: >-
  Guidelines for creating and maintaining Cursor rules to ensure consistency and effectiveness.
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
  - cursor-rules-meta-guide
  - cursor
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
          - name: cursor-rules-meta-guide
            file: cursor-rules-meta-guide.md
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
          - name: cursor-rules-meta-guide
            file: cursor-rules-meta-guide.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Cursor Rules Meta Guide

## Purpose

Guidelines for creating and maintaining Cursor rules to ensure consistency and effectiveness.

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `cursor-rules-meta-guide.mdc`
- canonical id: `cursor-rules-meta-guide`
