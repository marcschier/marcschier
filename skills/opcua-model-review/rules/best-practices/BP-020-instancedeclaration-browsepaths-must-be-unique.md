---
id: "BP-020"
title: "InstanceDeclaration BrowsePaths must be unique"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4"]
---

# BP-020 - InstanceDeclaration BrowsePaths must be unique

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For InstanceDeclarations, the BrowsePath shall be unique.

## Applicability

InstanceDeclarations (Objects/Variables/Methods declared under a TypeDefinition).

## Exceptions and evidence limits

None stated here.

## Audit

**NodeSet XML:** Within one TypeDefinition's declared substructure, compute BrowsePaths (sequences of BrowseNames from the TypeDefinition root) and flag duplicates.

**Document:** N/A.

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source notes

As with BP-018, this clause attributes the "shall" to the base specification; recorded as it appears in 11030 clause 2.1.4.

## Source

- [OPC 11030 v1.03.03, clause 2.1.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
