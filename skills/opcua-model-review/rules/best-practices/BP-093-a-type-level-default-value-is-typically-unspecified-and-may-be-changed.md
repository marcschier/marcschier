---
id: "BP-093"
title: "A type-level default Value is typically unspecified and may be changed"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-093 - A type-level default Value is typically unspecified and may be changed

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The Value attribute is typically not defined by the specification (at the type/InstanceDeclaration level) and may be changed. This identical rule recurs for both Variable and VariableType NodeClasses.

## Applicability

Variable and VariableType Nodes.

## Exceptions and evidence limits

Change in Server allowed? = Yes (both).

## Audit

**NodeSet XML:** Low value (typically absent/server-set at runtime).

**Document:** N/A.

**Assessment:** Static-checkable (typically a non-finding) / Runtime-only for actual deployed values.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Two table rows merged (identical content for Variable and VariableType).

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
