---
id: "BP-070"
title: "Changing an InstanceDeclaration's TypeDefinition is restricted to non-constraining subtypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.13"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.13"]
---

# BP-070 - Changing an InstanceDeclaration's TypeDefinition is restricted to non-constraining subtypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Changing the TypeDefinition of an InstanceDeclaration is not allowed unless the replacement is a Subtype of the already-specified TypeDefinition, and even then only if that Subtype does not add any mandatory InstanceDeclaration or constraint, and (for a Variable) does not refine/narrow the DataType.

## Applicability

InstanceDeclarations, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

Retargeting to a "safe" Subtype as defined above is the sole permitted exception.

## Audit

**NodeSet XML:** Diff an InstanceDeclaration's `TypeDefinition` reference across versions; if changed, confirm the new TypeDefinition is a Subtype of the old one, contributes no new Mandatory/MandatoryPlaceholder members, and (if a Variable) has an unchanged DataType.

**Document:** Compare InstanceDeclaration TypeDefinition columns across specification versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT (with a narrow conditional exception)

## Source notes

This rule's Variable/DataType clause interacts with BP-069's absolute DataType-change prohibition; read together, retargeting an InstanceDeclaration's TypeDefinition to a VariableType Subtype is permitted only when that Subtype does not itself imply a different (narrower) DataType for the Variable.

## Source

- [OPC 11030 v1.03.03, clause 3.2.13](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.13)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
