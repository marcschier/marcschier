---
id: "P3-179"
title: "Use reusable types for reusable semantic structures"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["A.1", "A.2", "A.3", "A.4.1"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-1", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-4-1"]
---

# P3-179 - Use reusable types for reusable semantic structures

## Rule

Prefer ObjectTypes for reusable object/group structures and VariableTypes for reusable value semantics, not a new VariableType that merely duplicates a DataType.

## Audit

Review expected reuse and extensibility. Annex A is informative; these recommendations do not make an otherwise valid model nonconformant.

## Source

- [OPC 10000-3 v1.05.06, clause A.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-1)
- [OPC 10000-3 v1.05.06, clause A.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-2)
- [OPC 10000-3 v1.05.06, clause A.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-3)
- [OPC 10000-3 v1.05.06, clause A.4.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-4-1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
