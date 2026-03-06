---
id: terraform-module-generator
name: Terraform Module Generator
title: Terraform Module Generator
description: >-
  Generate reusable Terraform modules with best practices
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: devops
tags:
  - command
  - packages
  - terraform
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
          - name: terraform-module-generator
            file: terraform-module-generator.md
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


# Terraform Module Generator

## Purpose

Generate reusable Terraform modules with best practices

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/devops-automation-pack/plugins/05-terraform/commands/terraform-module-create.md`
- canonical id: `terraform-module-generator`
