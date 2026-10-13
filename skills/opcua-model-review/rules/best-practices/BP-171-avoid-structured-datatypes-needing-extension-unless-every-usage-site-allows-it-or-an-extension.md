---
id: "BP-171"
title: "Avoid structured DataTypes needing extension unless every usage site allows it or an extension mechanism is built in"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-171 - Avoid structured DataTypes needing extension unless every usage site allows it or an extension mechanism is built in

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because subtyping Structured DataTypes is challenging or disallowed in several contexts, carefully consider whether extensibility is really required before designing it in. If it is required, either every usage location must be prepared to accept subtypes, or the structure should already embed its own extension mechanism (e.g., an array of key/value pairs)  -  noting that high-frequency transferred data should not be mixed with rarely-changing metadata in the same structure.

## Applicability

Structured DataType design anticipating future extension.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical (forward-looking design judgement).

**Document:** Review extensibility rationale for new Structured DataTypes.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
