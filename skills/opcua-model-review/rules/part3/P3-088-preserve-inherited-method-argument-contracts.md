---
id: "P3-088"
title: "Preserve inherited Method argument contracts"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.4", "6.3.3.3"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3"]
---

# P3-088 - Preserve inherited Method argument contracts

## Rule

An override cannot remove existing Method arguments, alter concrete argument DataTypes, or add required arguments. Abstract argument types may be specialized and optional inputs appended.

## Audit

Compare ordered arguments, optional-input metadata, and original abstract/concrete DataTypes.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.4)
- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
