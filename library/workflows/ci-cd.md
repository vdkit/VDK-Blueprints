---
name: CI/CD Pipeline
description: Standard CI/CD workflow
version: 1.0.0
type: workflow
tags:
  - devops
  - ci-cd
schemaVersion: '3.0'
id: ci-cd-pipeline
title: CI/CD Pipeline
kind: workflow
specificityLayer: L2
category: workflow
platforms:
  windsurf:
    compatible: true
    enabled: true
    components:
      workflows:
        type: windsurf-workflow
        enabled: true
        location: .windsurf/workflows/
        manifests:
          - name: ci-cd-pipeline
            file: ci-cd-pipeline.yaml
            trigger:
              - manual
  claude-code:
    compatible: true
    enabled: true
    components:
      commands:
        type: claude-command
        enabled: true
        location: .claude/commands/
        manifests:
          - name: ci-cd-pipeline
            file: ci-cd-pipeline.md
requires: []
suggests: []
conflicts: []
supersedes: []
---

# CI/CD Pipeline

1. **Build**: Run component build.
2. **Test**: Run unit and integration tests.
3. **Lint**: Check code quality.
4. **Deploy**: Deploy to staging if successful.
