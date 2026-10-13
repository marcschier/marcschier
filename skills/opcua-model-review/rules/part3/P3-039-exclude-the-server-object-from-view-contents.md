---
id: "P3-039"
title: "Exclude the Server Object from View contents"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["5.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4"]
---

# P3-039 - Exclude the Server Object from View contents

## Rule

The standard Server Object cannot be part of a View's contents, because it supplies all Server Events.

## Audit

Inspect View membership rather than assuming every organizational Reference represents membership.

## Source

- [OPC 10000-3 v1.05.06, clause 5.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.4)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
