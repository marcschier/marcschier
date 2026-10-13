---
id: "BP-163"
title: "Define a new ReferenceType only for a semantic not already covered"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.8"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.8"]
---

# BP-163 - Define a new ReferenceType only for a semantic not already covered

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a relationship semantic needs to be exposed that is not already defined (the base specification, OPC 10000-5, and OPC 10000-23 already define many ReferenceTypes), a new ReferenceType should be created.

## Applicability

New relationship-semantic modelling decisions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Not independently mechanical (requires a semantic survey of existing ReferenceTypes).

**Document:** Review rationale for introducing a new ReferenceType versus reusing an existing one.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

Detailed base/Part-5/Part-23 ReferenceType catalogues are out of scope here.

## Source

- [OPC 11030 v1.03.03, clause 7.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
