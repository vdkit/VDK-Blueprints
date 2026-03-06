---
id: implement-event-driven-api
name: Implement Event-Driven API
title: Implement Event-Driven API
description: >-
  Implement event-driven API architecture using message brokers, publisher and
  subscriber patterns, idempotent handlers, and dead-letter processing.
target: claude-code
commandType: custom-slash
version: 1.0.0
scope: project
category: command
tags:
  - api
  - events
  - messaging
  - microservices
author: VDK
lastUpdated: '2026-03-02'
schemaVersion: '3.0'
kind: command
specificityLayer: L2
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
          - name: implement-event-driven-api
            file: implement-event-driven-api.md
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
  - add-rate-limiting
  - implement-error-handling
conflicts: []
supersedes: []
---

# Implement Event-Driven API

## Purpose

Provide a production-safe blueprint for event-driven API architecture across
publishers, consumers, broker setup, retry semantics, and failure isolation.

## Core Capabilities

- message-broker strategy guidance (RabbitMQ, Kafka, SQS/SNS, Redis)
- event schema design with versioning and backward-compatibility expectations
- publisher implementation with delivery confirmation and durability controls
- subscriber implementation with idempotency checks and DLQ routing
- support patterns for outbox, CQRS, and saga orchestration

## Operational Requirements

- mandatory observability for event lag, retry volume, and DLQ growth
- correlation identifiers for end-to-end traceability
- replay-safe handlers and schema validation before processing
