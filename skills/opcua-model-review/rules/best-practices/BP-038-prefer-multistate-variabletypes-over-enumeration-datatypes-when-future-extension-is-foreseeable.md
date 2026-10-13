---
id: "BP-038"
title: "Prefer MultiState VariableTypes over Enumeration DataTypes when future extension is foreseeable"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4"]
---

# BP-038 - Prefer MultiState VariableTypes over Enumeration DataTypes when future extension is foreseeable

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If it is foreseeable that a future specification version (or a derived Companion Specification) will need to add or remove enumeration-like values, one of the MultiState VariableTypes should be used instead of an Enumeration DataType.

## Applicability

New discrete-value designs anticipating extension.

## Exceptions and evidence limits

None stated; this is forward-looking design advice, not a retrofit rule.

## Audit

**NodeSet XML:** None directly (a design-time choice); cannot be verified after the fact without knowing original intent.

**Document:** Review design rationale in specification text where discrete values are introduced.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

Cross-referenced in detail at clause 7.12 (BP-177-BP-180).

## Source

- [OPC 11030 v1.03.03, clause 3.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
