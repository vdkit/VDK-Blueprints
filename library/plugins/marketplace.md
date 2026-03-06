---
id: marketplace
title: Marketplace
description: >-
  Imported plugin-distribution blueprint from staging source swift/swift-patterns-skill/.claude-plugin/marketplace.json.
version: 1.0.0
lastUpdated: '2026-03-02'
category: plugin
subcategory: distribution
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: plugin-distribution
specificityLayer: L3
author: VDK
tags:
  - plugin
  - distribution
  - imported
  - plugin-distribution
  - swift
  - marketplace
platforms:
  claude-code:
    compatible: true
    enabled: true
    components:
      distribution:
        type: claude-plugin
        enabled: true
        location: .claude-plugin/plugin.json
        manifests:
          - name: marketplace
            file: plugin.json
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests: []
conflicts: []
supersedes: []
---


# Marketplace

## Purpose

Imported plugin-distribution blueprint from staging source swift/swift-patterns-skill/.claude-plugin/marketplace.json.

## Included Focus Areas

- packaged guidance scope and distribution intent
- installation and activation compatibility boundaries
- expected integration surfaces across supported tools

## Source Mapping

- staging source: `swift/swift-patterns-skill/.claude-plugin/marketplace.json`
- canonical id: `marketplace`
