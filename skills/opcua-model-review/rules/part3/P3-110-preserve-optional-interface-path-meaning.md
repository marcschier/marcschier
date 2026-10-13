---
id: "P3-110"
title: "Preserve optional Interface path meaning"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["4.10.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "interfaces"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2"]
---

# P3-110 - Preserve optional Interface path meaning

## Rule

An absent Optional Interface member's path cannot be reused by the implementing type or its subtypes for an incompatible Node.

## Audit

Check reserved paths and any present matching member. Providing all optional Interface declarations is separately a recommendation.

## Source

- [OPC 10000-3 v1.05.06, clause 4.10.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.2)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
