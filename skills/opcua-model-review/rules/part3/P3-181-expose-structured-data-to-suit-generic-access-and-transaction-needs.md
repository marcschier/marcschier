---
id: "P3-181"
title: "Expose structured data to suit generic access and transaction needs"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["A.4.3", "A.5"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-4-3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-5"]
---

# P3-181 - Expose structured data to suit generic access and transaction needs

## Rule

Prefer accessible component values; combine structured values with components when atomic bulk access is needed. Views can expose a purpose-specific subset.

## Audit

Review generic-client needs and atomicity. Passing opaque structured data can be appropriate when the Server cannot interpret it.

## Source

- [OPC 10000-3 v1.05.06, clause A.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-4-3)
- [OPC 10000-3 v1.05.06, clause A.5](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-5)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
