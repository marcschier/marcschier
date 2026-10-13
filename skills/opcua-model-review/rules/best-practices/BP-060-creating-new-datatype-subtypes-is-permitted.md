---
id: "BP-060"
title: "Creating new DataType subtypes is permitted"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.10"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10"]
---

# BP-060 - Creating new DataType subtypes is permitted

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to create new subtypes of existing DataTypes.

## Applicability

DataType hierarchies, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Diff two NodeSet versions; new leaf DataType subtypes are an expected non-violation.

**Document:** N/A.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
