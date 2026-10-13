---
id: "P3-002"
title: "Keep the standard Attribute set"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["3.3.2", "4.4.3", "5.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.9"]
---

# P3-002 - Keep the standard Attribute set

## Rule

Companion models, Clients, and Servers cannot define new standard Attributes. Additional characteristics belong in Properties or other model Nodes.

## Audit

Compare proposed Attributes with the NodeClass definitions. Distinguish NodeSet serialization metadata from AddressSpace Attributes.

## Source

- [OPC 10000-3 v1.05.06, clause 3.3.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/3.3.2)
- [OPC 10000-3 v1.05.06, clause 4.4.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.4.3)
- [OPC 10000-3 v1.05.06, clause 5.9](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.9)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
