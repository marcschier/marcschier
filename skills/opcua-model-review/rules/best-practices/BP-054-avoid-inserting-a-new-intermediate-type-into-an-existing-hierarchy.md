---
id: "BP-054"
title: "Avoid inserting a new intermediate type into an existing hierarchy"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-054 - Avoid inserting a new intermediate type into an existing hierarchy

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not recommended to insert a new type inside an existing ObjectType/VariableType hierarchy (i.e., as a new supertype positioned between two existing types). The document illustrates this with Figure 1, where a hypothetical `NewType` is inserted as a new supertype of `Subtype_B` and `Subtype_C`.

## Applicability

ObjectType/VariableType hierarchies, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

If judged "absolutely necessary," the insertion is not forbidden outright but becomes subject to the hard constraints in BP-055-BP-057.

## Audit

**NodeSet XML:** Diff two NodeSet versions; flag any pre-existing type whose immediate `HasSubtype` parent changed between versions (indicating a type was spliced into its ancestry).

**Document:** Review Figure 1 and surrounding text when evaluating a proposed hierarchy change: https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9#fig_1_example-of-adding-types-inside-an-existing-type-hierarchy

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
