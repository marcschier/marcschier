---
id: "P3-091"
title: "Do not weaken inherited ModellingRules"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.2", "6.4.4.4.4", "6.4.4.4.5"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5"]
---

# P3-091 - Do not weaken inherited ModellingRules

## Rule

Mandatory remains Mandatory; Optional may remain Optional or become Mandatory. Placeholder transitions require their class-specific rules as well as Table 21.

## Audit

Check declaration overrides, not ordinary instance ModellingRules. Table 21 and the Object/Variable OptionalPlaceholder prose differ on promotion; flag that source tension instead of applying a universal transition matrix.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.2)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4)
- [OPC 10000-3 v1.05.06, clause 6.4.4.4.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
