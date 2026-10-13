---
id: "P3-132"
title: "Give Structure and Enum fields distinct valid names"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.51", "8.52"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.52"]
---

# P3-132 - Give Structure and Enum fields distinct valid names

## Rule

StructureField names are unique within StructureDefinition, at most 512 characters, and contain no C0/C1 controls. EnumField names are unique within EnumDefinition.

## Audit

Compare the complete semantic definition, accounting for the NodeSet representation of inherited fields.

## Source

- [OPC 10000-3 v1.05.06, clause 8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)
- [OPC 10000-3 v1.05.06, clause 8.52](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.52)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
