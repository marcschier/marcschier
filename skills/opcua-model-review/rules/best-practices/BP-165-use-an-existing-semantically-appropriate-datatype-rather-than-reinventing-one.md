---
id: "BP-165"
title: "Use an existing, semantically-appropriate DataType rather than reinventing one"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-165 - Use an existing, semantically-appropriate DataType rather than reinventing one

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Use appropriate existing DataTypes rather than reinventing equivalent data with a generic structure (worked example: use the existing `DateTime` DataType rather than a custom Structure of Integer values).

## Applicability

New DataType/field design decisions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not mechanically checkable (requires semantic comparison against the existing DataType catalogue).

**Document:** Review new DataType/field definitions for unnecessary reinvention of existing semantics.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
