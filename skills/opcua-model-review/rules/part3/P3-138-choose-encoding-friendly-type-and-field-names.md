---
id: "P3-138"
title: "Choose encoding-friendly type and field names"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.2", "8.51", "8.52"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.52"]
---

# P3-138 - Choose encoding-friendly type and field names

## Rule

DataType BrowseName strings and Structure/Enum field names start with a letter and otherwise contain letters, digits, or underscore.

## Audit

Flag deviations as recommendations: the mappings can transform other names, so this is not a universal validity prohibition.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.2)
- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)
- [OPC 10000-3 v1.05.06, clause 8.52](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.52)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
