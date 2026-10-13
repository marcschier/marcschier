---
id: "BP-022"
title: "Structure field names must be unique"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.2"]
---

# BP-022 - Structure field names must be unique

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Each field of a Structured DataType must have a unique name.

## Applicability

Structured DataType field definitions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Within a `StructureDefinition`, flag duplicate `Field/@Name` values.

**Document:** Review spec structure-field tables for duplicate names.

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source notes

Attributed by the source to the base OPC UA specification ("as defined in the base OPC UA specification"); recorded as it appears in 11030 clause 2.2.

## Source

- [OPC 11030 v1.03.03, clause 2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
