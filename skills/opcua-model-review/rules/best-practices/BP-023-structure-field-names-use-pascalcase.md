---
id: "BP-023"
title: "Structure field names use PascalCase"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.2"]
---

# BP-023 - Structure field names use PascalCase

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Structure field names should use PascalCase (examples: `Offset`, `DaylightSavingInOffset`).

## Applicability

Structured DataType field definitions.

## Exceptions and evidence limits

Specification **prose** legitimately shows lower camelCase for the same fields in many Companion Specifications and in the base specification itself; the source explicitly notes this is expected ("However, in many Companion Specifications, and in the base OPC UA specifications, lower camel case ... is used in the specification. However, the UANodeSet uses PascalCase"). A reviewer must not flag lowerCamelCase in **prose tables** as a defect  -  only the actual `StructureDefinition`/NodeSet field names are expected to be PascalCase.

## Audit

**NodeSet XML:** Flag `Field/@Name` values not in PascalCase.

**Document:** Do **not** flag lowerCamelCase field names appearing in specification prose/tables as a defect; only the NodeSet XML is normative for this casing rule.

**Assessment:** Static-checkable (XML); the prose exception is semantically reviewable context, not itself a violation.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
