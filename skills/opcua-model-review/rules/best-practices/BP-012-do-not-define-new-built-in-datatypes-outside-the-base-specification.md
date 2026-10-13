---
id: "BP-012"
title: "Do not define new Built-in DataTypes outside the base specification"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-012 - Do not define new Built-in DataTypes outside the base specification

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Built-in DataTypes "can only be defined by the base OPC UA specification"  -  Companion Specifications and vendor models must not attempt to define new Built-in DataTypes, and (descriptively) such types carry no naming suffix (examples: `String`, `Int32`, `Byte`).

## Applicability

Companion Specification and vendor information models.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag any non-base (`NamespaceIndex != 0`) `UADataType` that structurally mimics a Built-in DataType registration (this is inherently a rare/implementation-level check; typically surfaced via DataTypeDefinition/encoding irregularities rather than a simple attribute).

**Document:** Review spec prose for any claim of defining a new Built-in DataType.

**Assessment:** Semantically reviewable (the violation pattern is organizational/registration-level, not a single attribute).

**Source wording:** MUST NOT

## Source notes

The naming-convention half of this clause (no suffix) is not independently actionable for companion-spec authors since they do not name Built-in DataTypes; retained here only as descriptive context.

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
