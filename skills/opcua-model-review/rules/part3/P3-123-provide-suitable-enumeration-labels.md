---
id: "P3-123"
title: "Provide suitable enumeration labels"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.2", "5.8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3"]
---

# P3-123 - Provide suitable enumeration labels

## Rule

Enumeration DataTypes provide EnumStrings or EnumValues; nonzero-based or sparse values use EnumValues. These Properties do not describe unrelated DataTypes.

## Audit

Compare integer values and label representation. Do not confuse a UInteger OptionSet with an Enumeration.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2)
- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
