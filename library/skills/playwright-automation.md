---
id: playwright-automation
title: Playwright Browser Automation Skill
description: >-
  Browser automation skill for functional checks, UI regression scripts,
  responsive validation, and interaction testing using Playwright.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: testing
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L2
author: VDK
tags:
  - skill
  - playwright
  - browser-testing
  - automation
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      skills:
        type: claude-skill
        enabled: true
        location: .claude/skills/
        manifests:
          - name: playwright-automation
            file: playwright-automation.md
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
          - name: playwright-automation
            file: playwright-automation.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests:
  - code-quality
conflicts: []
supersedes: []
---

# Playwright Browser Automation

## Purpose

Use Playwright for repeatable browser automation, including page checks,
interaction flows, responsive verification, and screenshot capture.

## Workflow

1. Detect active local servers when target is localhost.
2. Create script in a temporary location.
3. Keep URLs parameterized.
4. Execute and collect output artifacts (screenshots/logs).
5. Report pass/fail observations with reproducible steps.

## Core Guidelines

- Prefer explicit waits (`waitForSelector`, `waitForURL`) over arbitrary sleep.
- Include error handling in scripts for deterministic failures.
- Validate critical user journeys (auth, forms, checkout, key navigation).
- Verify desktop and mobile viewport behavior for UI-sensitive pages.

## Typical Use Cases

- smoke testing newly implemented pages
- login and form submission validation
- responsive layout verification
- visual checkpoint screenshots for review
