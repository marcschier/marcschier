---
id: "P3-011"
title: "Validate qualified BrowseNames"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.2.4", "8.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.3"]
---

# P3-011 - Validate qualified BrowseNames

## Rule

Resolve the namespace of a BrowseName and keep its name within 512 characters, without C0/C1 control characters.

## Audit

Validate the qualified name after XML decoding and namespace resolution. A namespace prefix is not part of the 512-character name.

## Source

- [OPC 10000-3 v1.05.06, clause 5.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.2.4)
- [OPC 10000-3 v1.05.06, clause 8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
