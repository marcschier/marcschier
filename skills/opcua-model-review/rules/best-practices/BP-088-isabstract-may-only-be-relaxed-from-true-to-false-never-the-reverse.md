---
id: "BP-088"
title: "IsAbstract may only be relaxed from true to false, never the reverse"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-088 - IsAbstract may only be relaxed from true to false, never the reverse

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The IsAbstract attribute may be changed from true to false across versions, but never from false to true. This identical rule recurs in the table for four NodeClasses: ReferenceType, ObjectType, VariableType, and DataType.

## Applicability

ReferenceType, ObjectType, VariableType, and DataType Nodes.

## Exceptions and evidence limits

Change in Server allowed? = No, for all four NodeClasses.

## Audit

**NodeSet XML:** Diff `IsAbstract` across versions for matched Nodes; flag any false->true transition; true->false is an expected non-violation.

**Document:** Compare type tables' Abstract column across versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MAY (true->false) / MUST NOT (false->true)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Four distinct table rows merged into one rule here since the stated behavior is textually identical across all four NodeClasses.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
