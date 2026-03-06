---
id: paypal-integration
title: PayPal Integration Skill
description: >-
  Payment integration skill for PayPal checkout, capture flows, subscriptions,
  IPN/webhook handling, dispute response, and refund operations.
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
  - paypal
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
          - name: paypal-integration
            file: paypal-integration.md
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
  - payment-integration
  - pci-compliance
conflicts: []
supersedes: []
---

# PayPal Integration Skill

## Purpose

Provide implementation guidance for PayPal payment workflows, from checkout and
capture to asynchronous notifications and refund handling.

## Core Coverage

- smart button and server-orchestrated checkout patterns
- order creation and capture lifecycle
- subscription and recurring billing flows
- IPN/webhook verification and idempotent processing
- refund, dispute, and chargeback handling patterns

## Integration Expectations

- no direct storage of sensitive payment card data
- backend verification before order fulfillment
- auditable payment status transitions