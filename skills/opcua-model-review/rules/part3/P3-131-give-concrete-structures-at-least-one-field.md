---
id: "P3-131"
title: "Give concrete Structures at least one field"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.32"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.32"]
---

# P3-131 - Give concrete Structures at least one field

## Rule

A non-abstract Structure has at least one field, declared locally or inherited.

## Audit

Resolve inherited definitions before declaring a locally empty subtype invalid.

## Source

- [OPC 10000-3 v1.05.06, clause 8.32](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.32)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
