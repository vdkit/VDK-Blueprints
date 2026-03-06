---
id: terraform-plan-analyzer
name: Terraform Plan Analyzer
title: Terraform Plan Analyzer
description: >-
  Analyze terraform plan output for risks and cost impact
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
          - name: terraform-plan-analyzer
            file: terraform-plan-analyzer.md
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


# Terraform Plan Analyzer

## Purpose

Analyze terraform plan output for risks and cost impact

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/devops-automation-pack/plugins/05-terraform/commands/terraform-plan-analyze.md`
- canonical id: `terraform-plan-analyzer`
