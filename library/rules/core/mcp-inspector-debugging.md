---
id: mcp-inspector-debugging
title: Mcp Inspector Debugging
description: >-
  Debugging and verifying MCP servers using the MCP Inspector UI with Playwright automation
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
  - mcp-inspector-debugging
  - mcp
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
          - name: mcp-inspector-debugging
            file: mcp-inspector-debugging.md
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
          - name: mcp-inspector-debugging
            file: mcp-inspector-debugging.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Mcp Inspector Debugging

## Purpose

Debugging and verifying MCP servers using the MCP Inspector UI with Playwright automation

## Activation Guidance

- apply when repository context matches the rule domain
- prefer deterministic checks over implicit assumptions
- document deviations when constraints require exceptions

## Source Mapping

- staging source: `mcp-inspector-debugging.mdc`
- canonical id: `mcp-inspector-debugging`
