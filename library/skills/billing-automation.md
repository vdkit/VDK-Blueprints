---
id: billing-automation
title: Billing Automation Skill
description: >-
  Billing automation skill for recurring invoices, subscription lifecycle,
  proration, dunning, and tax-aware billing operations.
version: 1.0.0
lastUpdated: '2026-03-02'
category: skill
subcategory: payments
complexity: complex
scope: project
audience: developer
maturity: stable
schemaVersion: '3.0'
kind: skill
specificityLayer: L3
author: VDK
tags:
  - skill
  - billing
  - subscriptions
  - invoicing
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
          - name: billing-automation
            file: billing-automation.md
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
  - stripe-integration
  - paypal-integration
  - pci-compliance
conflicts: []
supersedes: []
---

# Billing Automation Skill

## Purpose

Define robust automation patterns for billing engines, from invoice generation
to payment recovery and compliance-aware taxation.

## Core Coverage

- subscription state transitions including trial, active, past-due, and canceled
- recurring cycle execution with deterministic invoice lifecycle handling
- dunning policy orchestration with retries, notifications, and account gating
- proration models for plan, seat, and interval transitions
- tax/VAT/GST calculation strategies by jurisdiction

## Integration Expectations

- complete billing event audit trail and immutable financial records
- customer communication hooks for all payment and renewal states
- resilient retry and recovery flows that balance revenue and user experience
