---
id: "BP-164"
title: "Represent a TypeDefinition's key structural aspects with hierarchical References"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.8"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.8"]
---

# BP-164 - Represent a TypeDefinition's key structural aspects with hierarchical References

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

OPC UA distinguishes hierarchical from non-hierarchical ReferenceTypes; for TypeDefinitions, the key aspects of the model's structure are represented using hierarchical References.

## Applicability

TypeDefinition substructure design.

## Exceptions and evidence limits

None stated (non-structural relationships naturally use non-hierarchical References instead, by implication, though not spelled out further here).

## Audit

**NodeSet XML:** Confirm a TypeDefinition's primary substructure (InstanceDeclarations) is reached via hierarchical ReferenceTypes (e.g., `HasComponent`, `HasProperty`, `Organizes`), not exclusively non-hierarchical ones.

**Document:** Review TypeDefinition substructure diagrams.

**Assessment:** Static-checkable.

**Source wording:** SHOULD / Informative

## Source

- [OPC 11030 v1.03.03, clause 7.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
