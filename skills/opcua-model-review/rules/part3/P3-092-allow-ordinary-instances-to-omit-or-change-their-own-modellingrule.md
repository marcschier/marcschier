---
id: "P3-092"
title: "Allow ordinary instances to omit or change their own ModellingRule"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.4.4.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.3"]
---

# P3-092 - Allow ordinary instances to omit or change their own ModellingRule

## Rule

A normal instantiated Node may have no ModellingRule or any ModellingRule independently of its source declaration's rule.

## Audit

Still verify the original type's instantiation obligations. Do not confuse a normal instance with a new declaration inside another type.

## Source

- [OPC 10000-3 v1.05.06, clause 6.4.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
