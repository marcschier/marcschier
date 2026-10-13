---
id: "BP-024"
title: "Enum value names must be unique"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.3"]
---

# BP-024 - Enum value names must be unique

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Each possible value of an Enum DataType must have a unique name.

## Applicability

Enumeration DataType value definitions (EnumStrings/EnumValues).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag duplicate `EnumValueType/DisplayName` (or `EnumStrings` entries) within one Enumeration DataType.

**Document:** Review spec enumeration-value tables for duplicate names.

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
