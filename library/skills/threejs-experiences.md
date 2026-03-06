---
id: threejs-experiences
title: Three.js Interactive Experiences Skill
description: >-
  Skill for building Three.js scenes, interaction mechanics, rendering setup,
  animation loops, and responsive 3D experiences.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: frontend
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
  - threejs
  - webgl
  - 3d
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
          - name: threejs-experiences
            file: threejs-experiences.md
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
          - name: threejs-experiences
            file: threejs-experiences.mdc
            globs:
              - '**/*'
            activation: manual
requires: []
suggests: []
conflicts: []
supersedes: []
---

# Three.js Interactive Experiences

## Purpose

Provide a structured approach for implementing performant, interactive 3D scenes
with consistent render setup, camera configuration, object composition, and user
interaction patterns.

## Core Practices

- initialize scene, camera, and renderer deterministically
- add animation loops with `requestAnimationFrame`
- include resize handling and viewport adaptation
- use explicit lighting strategy for non-basic materials
- apply interaction patterns (raycasting, pointer handling) intentionally

## Typical Outputs

- interactive 3D components
- animated scene demos
- responsive visual prototypes
