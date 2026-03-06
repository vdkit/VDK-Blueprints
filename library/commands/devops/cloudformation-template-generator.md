---
id: cloudformation-template-generator
name: CloudFormation Template Generator
title: CloudFormation Template Generator
description: >-
  Convert Terraform to CloudFormation or generate CFN templates
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
subcategory: devops
tags:
  - command
  - packages
  - cloudformation
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
          - name: cloudformation-template-generator
            file: cloudformation-template-generator.md
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


# CloudFormation Template Generator

## Purpose

Convert Terraform to CloudFormation or generate CFN templates

## Core Capabilities

- interactive scoping for repository and target context
- implementation guidance aligned with existing architecture constraints
- output expectations for repeatable execution and reviewability

## Source Mapping

- staging source: `packages/devops-automation-pack/plugins/05-terraform/commands/cloudformation-generate.md`
- canonical id: `cloudformation-template-generator`
