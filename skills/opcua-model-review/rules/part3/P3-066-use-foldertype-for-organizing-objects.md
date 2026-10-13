---
id: "P3-066"
title: "Use FolderType for organizing Objects"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.5.3", "7.11"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.11"]
---

# P3-066 - Use FolderType for organizing Objects

## Rule

An Object used as an Organizes source should instantiate FolderType or a subtype.

## Audit

Resolve Object type ancestry and consider its semantic purpose. This is not a MUST ban on other Object types.

## Source

- [OPC 10000-3 v1.05.06, clause 5.5.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.5.3)
- [OPC 10000-3 v1.05.06, clause 7.11](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.11)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
