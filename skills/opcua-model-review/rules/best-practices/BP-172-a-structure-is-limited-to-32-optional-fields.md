---
id: "BP-172"
title: "A Structure is limited to 32 optional fields"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-172 - A Structure is limited to 32 optional fields

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The number of optional fields in a Structure is limited to 32 per Structure.

## Applicability

Structured DataType design using optional fields.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Count fields marked optional within one `StructureDefinition`; flag if count > 32.

**Document:** Review structure field tables for optional-field counts.

**Assessment:** Static-checkable.

**Source wording:** MUST NOT (exceed 32 optional fields)

## Source notes

This reads as a hard platform/encoding ceiling rather than an 11030-original policy recommendation; 11030 states the number at clause 7.9 but does not itself explain the encoding mechanism behind the limit (presumably a base-specification/Part-6 encoding constraint, out of scope here). Recorded exactly as stated, without asserting its ultimate normative source.

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
