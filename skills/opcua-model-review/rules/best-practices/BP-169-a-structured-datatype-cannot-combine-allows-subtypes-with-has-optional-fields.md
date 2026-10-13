---
id: "BP-169"
title: "A Structured DataType cannot combine \"allows subtypes\" with \"has optional fields\""
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-169 - A Structured DataType cannot combine "allows subtypes" with "has optional fields"

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Structured DataType may have optional fields (fields that need not be provided), which must also be explicitly declared  -  but the "allows subtypes" capability and "has optional fields" cannot both be used on the same structure at once.

## Applicability

Structured DataType design.

## Exceptions and evidence limits

None  -  stated as a flat incompatibility. See BP-170 for workaround patterns when both are wanted.

## Audit

**NodeSet XML:** Flag any `StructureDefinition` that simultaneously declares itself to allow subtypes and to have one or more optional fields.

**Document:** Review structured DataType definitions for this combination.

**Assessment:** Static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
