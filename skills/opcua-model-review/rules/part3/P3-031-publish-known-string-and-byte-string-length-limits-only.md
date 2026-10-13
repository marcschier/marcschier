---
id: "P3-031"
title: "Publish known string and byte-string length limits only"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.6.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4"]
---

# P3-031 - Publish known string and byte-string length limits only

## Rule

Do not expose MaxStringLength, MaxCharacters, or MaxByteStringLength when the Server has no such limit or cannot determine it.

## Audit

Compare the specification's advertised limits with the implementation contract; the XML Property value alone cannot establish whether a real limit exists.

## Source

- [OPC 10000-3 v1.05.06, clause 5.6.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.6.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
