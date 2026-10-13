---
id: "BP-037"
title: "Restricting an Enumeration via a value-subset Subtype is permitted"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.4"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4"]
---

# BP-037 - Restricting an Enumeration via a value-subset Subtype is permitted

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to limit enumeration values by creating a Subtype DataType with a subset of the values defined by its supertype.

## Applicability

Enumeration DataType hierarchies.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm a Subtype Enumeration DataType's values are a subset (not superset or disjoint set) of its supertype's values.

**Document:** Review spec text describing the subtype's restricted value set.

**Assessment:** Static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
