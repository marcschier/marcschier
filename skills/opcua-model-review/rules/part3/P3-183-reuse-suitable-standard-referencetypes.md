---
id: "P3-183"
title: "Reuse suitable standard ReferenceTypes"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["A.7"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-7"]
---

# P3-183 - Reuse suitable standard ReferenceTypes

## Rule

Define a new ReferenceType only when an existing one does not express the needed relationship, and choose the most suitable supertype.

## Audit

Review proposed semantics against standard References without replacing a genuinely distinct domain relation.

## Source

- [OPC 10000-3 v1.05.06, clause A.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/a-7)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
