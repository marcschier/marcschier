---
id: "P3-003"
title: "Honor NodeClass attribute and reference cardinality"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["3.3.2", "5.9"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.9"]
---

# P3-003 - Honor NodeClass attribute and reference cardinality

## Rule

Provide each mandatory NodeClass Attribute and observe each specified Reference cardinality: exactly one, at most one, or unrestricted.

## Audit

Apply the NodeClass tables to the reconstructed model, accounting for NodeSet XML defaults and export omissions; XML attribute absence alone is not a runtime violation.

## Source

- [OPC 10000-3 v1.05.06, clause 3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2)
- [OPC 10000-3 v1.05.06, clause 5.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.9)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
