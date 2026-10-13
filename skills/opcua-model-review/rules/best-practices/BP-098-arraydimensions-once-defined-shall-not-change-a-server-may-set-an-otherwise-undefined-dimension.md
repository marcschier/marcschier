---
id: "BP-098"
title: "ArrayDimensions, once defined, shall not change; a Server may set an otherwise-undefined dimension"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-098 - ArrayDimensions, once defined, shall not change; a Server may set an otherwise-undefined dimension

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

ArrayDimensions is typically not defined by the specification; where it is defined, it shall not change. "Change in Server allowed?" = **Yes, if not defined (per dimension)**  -  i.e., a Server may supply a concrete value for any dimension the specification itself left unconstrained, on a per-dimension basis. This identical rule recurs for both Variable and VariableType.

## Applicability

Variable and VariableType Nodes.

## Exceptions and evidence limits

The per-dimension, only-if-previously-undefined Server allowance above.

## Audit

**NodeSet XML:** Diff `ArrayDimensions` across versions where the specification defines a concrete (non-zero/non-wildcard) value per dimension; flag changes to any dimension that was already concretely specified.

**Document:** Compare ArrayDimensions columns across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT (once defined by the specification)

## Source notes

Two table rows merged (identical content for Variable and VariableType).

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
