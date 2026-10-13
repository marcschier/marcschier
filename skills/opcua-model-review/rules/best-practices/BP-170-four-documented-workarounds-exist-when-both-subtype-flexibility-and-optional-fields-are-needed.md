---
id: "BP-170"
title: "Four documented workarounds exist when both subtype-flexibility and optional fields are needed"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-170 - Four documented workarounds exist when both subtype-flexibility and optional fields are needed

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When a Structured DataType needs both subtype flexibility and optional-field flexibility, four options are documented: (1) define default values  -  including NULL where available  -  for all optional fields instead of marking them optional; (2) split into two nested sub-structures, one with all optional fields and one with all subtype-allowing fields, conventionally named `OptionalFields` and `SubtypableFields`; (3) type the field as `BaseDataType` (any DataType) or `Structure` (any Structured DataType) wherever subtyping is wanted, optionally still defining a concrete DataType for implementations that don't need the subtype; (4) replace an optional scalar field with a length-0-or-1 array (a variant of option 1 with a well-defined "absent" representation). Each option has acknowledged weaknesses: (1) unclear default values for types with no natural "unset" value; (2) extra nesting; (3) no type safety; (4) decreased readability from using arrays for scalars.

## Applicability

Structured DataType design needing both capabilities simultaneously.

## Exceptions and evidence limits

None stated; all four are presented as valid but imperfect.

## Audit

**NodeSet XML:** For a DataType documented as needing both capabilities, confirm one of the four patterns was actually used (structural detection varies by option).

**Document:** Review the design rationale/trade-off discussion for the chosen option.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (choose one of the documented options)

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
