---
id: helm-chart-generator
name: Helm Chart Generator
title: Helm Chart Generator
description: >-
  Generate Helm chart for Kubernetes application
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: devops
tags:
  - command
  - packages
  - helm
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
          - name: helm-chart-generator
            file: helm-chart-generator.md
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


# Helm Chart Generator

## Purpose

Generate Helm chart for Kubernetes application

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/devops-automation-pack/plugins/04-kubernetes/commands/k8s-helm-chart.md`
- canonical id: `helm-chart-generator`
