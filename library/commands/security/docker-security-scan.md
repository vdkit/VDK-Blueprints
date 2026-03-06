---
id: docker-security-scan
name: Docker Security Scan
title: Docker Security Scan
description: >-
  Scans Docker containers and images for security vulnerabilities
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: security
tags:
  - command
  - packages
  - docker
author: VDK
lastUpdated: '2026-03-02'
schemaVersion: '3.0'
kind: command
specificityLayer: L3
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
          - name: docker-security-scan
            file: docker-security-scan.md
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


# Docker Security Scan

## Purpose

Scans Docker containers and images for security vulnerabilities

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/security-pro-pack/plugins/04-infrastructure-security/commands/docker-security-scan.md`
- canonical id: `docker-security-scan`
