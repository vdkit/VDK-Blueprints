---
id: stripe-integration
title: Stripe Integration Skill
description: >-
  Payment integration skill for Stripe checkout flows, subscriptions,
  webhook verification, disputes, and refund orchestration.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: payments
complexity: medium
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L3
author: VDK
tags:
  - skill
  - stripe
  - payments
  - subscriptions
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
          - name: stripe-integration
            file: stripe-integration.md
  github-copilot:
    compatible: true
    enabled: true
    components:
      repo-level:
        type: copilot-repo
        enabled: true
        location: .github/copilot-instructions.md
requires: []
suggests:
  - billing-automation
  - pci-compliance
conflicts: []
supersedes: []
---

# Stripe Integration Skill

## Purpose

Provide implementation guidance for secure Stripe payment systems covering
checkout UX, recurring billing, and backend event-driven correctness.

## Core Coverage

- checkout session and payment intent integration paths
- subscription lifecycle design and customer portal patterns
- webhook signature verification and idempotent event processing
- refund and dispute handling workflows
- test-mode validation and production rollout controls

## Integration Expectations

- server-side fulfillment decisions sourced from webhook truth
- strict secret management and no raw card handling in app backends
- traceable metadata linking payment provider records to domain entities
