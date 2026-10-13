---
id: "P3-079"
title: "Preserve similarity when overriding or instantiating declarations"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["6.2.4", "6.2.7", "6.3.3.3", "6.4.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "inheritance"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.7", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.1"]
---

# P3-079 - Preserve similarity when overriding or instantiating declarations

## Rule

A similar Node preserves NodeClass and BrowseName; Object/Variable types are unchanged or narrowed to subtypes. Method similarity also preserves the allowed argument contract.

## Audit

Compare corresponding fully inherited BrowsePaths, not NodeIds; an override may have a new NodeId.

## Source

- [OPC 10000-3 v1.05.06, clause 6.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.4)
- [OPC 10000-3 v1.05.06, clause 6.2.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.2.7)
- [OPC 10000-3 v1.05.06, clause 6.3.3.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.3.3.3)
- [OPC 10000-3 v1.05.06, clause 6.4.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.1)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
