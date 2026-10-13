---
id: "P3-010"
title: "Respect NodeId identifier bounds"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["8.2.3", "8.2.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "identity"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.3", "https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.4"]
---

# P3-010 - Respect NodeId identifier bounds

## Rule

String NodeId identifiers are at most 4,096 characters and contain no C0/C1 control characters. Opaque identifiers are at most 4,096 bytes; identifiers must match their declared kind.

## Audit

Validate decoded identifier values, not the length of base64 text or the XML-escaped representation.

## Source

- [OPC 10000-3 v1.05.06, clause 8.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.3)
- [OPC 10000-3 v1.05.06, clause 8.2.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.2.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
