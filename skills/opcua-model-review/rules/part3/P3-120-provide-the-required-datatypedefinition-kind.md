---
id: "P3-120"
title: "Provide the required DataTypeDefinition kind"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.8.3", "8.47", "8.48", "8.50"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.47", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.50"]
---

# P3-120 - Provide the required DataTypeDefinition kind

## Rule

Structured/Union types provide StructureDefinition; Enumeration and OptionSet types provide EnumDefinition, including UInteger subtypes representing OptionSets.

## Audit

Interpret NodeSet Definition according to Part 6 rather than demanding a literal DataTypeDefinition XML Attribute.

## Source

- [OPC 10000-3 v1.05.06, clause 5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
- [OPC 10000-3 v1.05.06, clause 8.47](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.47)
- [OPC 10000-3 v1.05.06, clause 8.48](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.48)
- [OPC 10000-3 v1.05.06, clause 8.50](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.50)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
