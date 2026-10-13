---
id: "BP-062"
title: "An inserted DataType supertype must not add new textual constraints"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.10"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10"]
---

# BP-062 - An inserted DataType supertype must not add new textual constraints

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

For all DataTypes, no new constraints (written as specification text) should be added by an inserted supertype  -  however, an existing constraint already common to all its subtypes may be relocated/added to the new supertype. The document separately notes that abstract DataTypes and simple DataTypes (subtypes of a Built-in DataType) carry no further additional rules beyond this.

## Applicability

Conditional on BP-061's carve-out; applies across all DataType categories, with Enumeration (BP-063) and Structured (BP-064) DataTypes carrying extra specific constraints.

## Exceptions and evidence limits

Constraints already common to every existing subtype may be promoted onto the new supertype.

## Audit

**NodeSet XML:** Not structurally checkable (prose-level constraints).

**Document:** Compare constraint text.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD NOT (source phrasing: "should not be added") with an explicit allowance

## Source

- [OPC 11030 v1.03.03, clause 3.2.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
