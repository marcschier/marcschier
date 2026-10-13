---
id: "P3-140"
title: "Map field-description Variables to real distinct fields"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.5.2", "7.25"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.25"]
---

# P3-140 - Map field-description Variables to real distinct fields

## Rule

Field descriptions identify existing fields, with at most one description per field. They use compatible BaseDataVariableType-derived Variables and the prescribed field name/namespace.

## Audit

Use the declaring DataType's namespace; ignore namespace only for the specified client comparison of a field's string name.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
- [OPC 10000-3 v1.05.06, clause 7.25](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.25)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
