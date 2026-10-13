---
id: "P3-042"
title: "Reserve ObjectType Create Methods for creation"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.4"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.4"]
---

# P3-042 - Reserve ObjectType Create Methods for creation

## Rule

An ObjectType Method named Create should not perform an unrelated operation instead of creating an Object of that type.

## Audit

Review Method semantics, not just its BrowseName. AddNodes-based creation remains valid without a Create Method.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
