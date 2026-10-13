---
id: "P3-195"
title: "Use concrete DataTypes for concrete values"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.2", "5.8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-195 - Use concrete DataTypes for concrete values

## Rule

Although DataType Attributes may name an abstract DataType, actual values use a permitted concrete subtype with its appropriate wire encoding.

## Audit

Inspect value and encoding identities rather than rejecting an abstract DataType Attribute itself.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
