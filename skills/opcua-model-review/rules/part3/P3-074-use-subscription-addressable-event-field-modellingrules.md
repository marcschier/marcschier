---
id: "P3-074"
title: "Use subscription-addressable Event field ModellingRules"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.7.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.2"]
---

# P3-074 - Use subscription-addressable Event field ModellingRules

## Rule

Only EventType components using Mandatory or Optional can be returned through an Event Subscription.

## Audit

Check proposed EventFields and their fully inherited declarations; do not promise placeholder-based fields as selectable fixed BrowsePaths.

## Source

- [OPC 10000-3 v1.05.06, clause 4.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.7.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
