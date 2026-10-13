---
id: "BP-195"
title: "New InstanceDeclarations may always be added optionally, anywhere in the structure"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.1"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.1"]
---

# BP-195 - New InstanceDeclarations may always be added optionally, anywhere in the structure

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

InstanceDeclarations (Variables, Methods, Objects) can be added optionally at any point in an existing TypeDefinition's structure without creating a Subtype  -  this includes adding a new InstanceDeclaration directly on a TypeDefinition, or nested under an existing InstanceDeclaration of that TypeDefinition (without needing to change the TypeDefinition of the owning InstanceDeclaration itself).

## Applicability

Existing TypeDefinitions and their InstanceDeclarations, within the same NamespaceUri.

## Exceptions and evidence limits

Does not cover making the addition mandatory  -  see BP-196.

## Audit

**NodeSet XML:** Diff two NodeSet versions; confirm new Optional/OptionalPlaceholder InstanceDeclarations (at any nesting depth within a TypeDefinition's structure) are an expected non-violation (restates BP-034 with explicit nested-placement scope).

**Document:** N/A.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

This clause restates BP-034 (clause 3.2.2) with the added explicit clarification that nested placement (under another InstanceDeclaration) is included.

## Source

- [OPC 11030 v1.03.03, clause 11.2.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
