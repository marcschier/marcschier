---
id: "P3-124"
title: "Restrict inherited Enumeration values without changing labels"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.14"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.14"]
---

# P3-124 - Restrict inherited Enumeration values without changing labels

## Rule

Enumerations derive from Enumeration. A subtype of a custom Enumeration can remove values but cannot add values or alter their associated text.

## Audit

Compare complete inherited integer/label pairs, not just a field count.

## Source

- [OPC 10000-3 v1.05.06, clause 8.14](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.14)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
