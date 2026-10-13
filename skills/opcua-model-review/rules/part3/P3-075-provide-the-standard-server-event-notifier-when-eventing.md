---
id: "P3-075"
title: "Provide the standard Server event notifier when eventing"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.7.1", "5.4"]
strength: "MUST"
targets: ["document", "runtime"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4"]
---

# P3-075 - Provide the standard Server event notifier when eventing

## Rule

An eventing Server exposes an EventNotifier through the standard Server Object. An eventing View supplies Events of its contained notifiers and its ModelChangeEvents.

## Audit

Review event capability and delivery context. A disconnected underlying event source is not required to invent Events.

## Source

- [OPC 10000-3 v1.05.06, clause 4.7.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.1)
- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
