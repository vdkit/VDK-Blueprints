---
id: package
title: Package
description: >-
  Imported plugin-distribution blueprint from staging source devops/sugar/mcp-server/package.json.
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
  - devops
  - package
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
          - name: package
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


# Package

## Purpose

Imported plugin-distribution blueprint from staging source devops/sugar/mcp-server/package.json.

## Included Focus Areas

- packaged guidance scope and distribution intent
- installation and activation compatibility boundaries
- expected integration surfaces across supported tools

## Source Mapping

- staging source: `devops/sugar/mcp-server/package.json`
- canonical id: `package`
