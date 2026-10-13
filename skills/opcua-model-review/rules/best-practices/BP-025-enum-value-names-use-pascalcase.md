---
id: "BP-025"
title: "Enum value names use PascalCase"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.3"]
---

# BP-025 - Enum value names use PascalCase

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Enum value names should use PascalCase (examples: `NoConfiguration`, `Running`).

## Applicability

Enumeration DataType value names.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag non-PascalCase enum value names.

**Document:** Review spec enumeration tables.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
