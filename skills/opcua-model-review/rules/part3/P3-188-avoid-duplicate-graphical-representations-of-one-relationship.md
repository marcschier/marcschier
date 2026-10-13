---
id: "P3-188"
title: "Avoid duplicate graphical representations of one relationship"
spec: "OPC 10000-3"
version: "1.05.06"
clauses: ["C.2.3"]
strength: "MUST NOT"
targets: ["document"]
check: "manual"
sources: ["https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-3"]
---

# P3-188 - Avoid duplicate graphical representations of one relationship

## Rule

A Node cannot show both an inline TypeDefinition shortcut and a HasTypeDefinition edge; a Property cannot be both inline and a separate Node in that same representation.

## Audit

Inspect diagrams using Annex C's extended notation; different figures may legitimately show the same Node differently.

## Source

- [OPC 10000-3 v1.05.06, clause C.2.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/c-2-3)

Apply the [assessment policy](../README.md#assessment-policy); a static check is only candidate evidence, not a complete rule verdict.
