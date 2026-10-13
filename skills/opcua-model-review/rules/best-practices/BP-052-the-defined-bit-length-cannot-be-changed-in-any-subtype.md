---
id: "BP-052"
title: "The defined bit-length cannot be changed in any subtype"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-052 - The defined bit-length cannot be changed in any subtype

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The initially-defined length of an OptionSet-DataType-based OptionSet cannot be changed in any Subtype (the document notes this point is itself detailed in OPC 10000-3).

## Applicability

Same as BP-047.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Compare declared length across a supertype/subtype OptionSet DataType pair; flag mismatches.

**Document:** Review spec subtype definitions.

**Assessment:** Static-checkable.

**Source wording:** MUST NOT

## Source notes

Mechanics/definition of "length" sourced to Part 3; out of scope for detail here.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
