---
id: "BP-168"
title: "Explicitly declare subtype-permission when a structured field's DataType must allow subtypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-168 - Explicitly declare subtype-permission when a structured field's DataType must allow subtypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

By default, if a field in a Structured DataType uses a concrete Structured DataType (or an abstract DataType other than `BaseDataType`/`Structure`), it is not allowed to use a subtype of that field's DataType there, because doing so would break the encoding. The specification provides a mechanism to explicitly state that subtypes are allowed for such a field (changing how the value is encoded, akin to how an abstract Structure field is encoded via an extension Object). If subtype flexibility is needed for such a field, this mechanism must be used.

## Applicability

Structured DataType field design where a concrete/non-wildcard field DataType needs subtype flexibility.

## Exceptions and evidence limits

`BaseDataType`/`Structure`-typed fields already permit any subtype by nature and need no special declaration.

## Audit

**NodeSet XML:** For a `StructureField` whose `DataType` is a concrete Structured DataType (or a non-BaseDataType/Structure abstract type) and which is documented as needing subtype flexibility, confirm the "allow subtypes" flag/mechanism is set on that field.

**Document:** Review field definitions for documented subtype-extensibility intent versus the actual flag.

**Assessment:** Static-checkable (given documented intent).

**Source wording:** MUST (conditional on wanting subtype flexibility)

## Source notes

Encoding mechanics ("how" the alternate encoding works) are described only at a high level in 11030; detailed semantics are base-specification territory (out of scope).

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
