---
id: "BP-056"
title: "An inserted intermediate type must not add new textual constraints"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-056 - An inserted intermediate type must not add new textual constraints

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

An inserted intermediate type shall not define additional constraints (i.e., prose-stated rules in the specification text) unless those constraints were already valid for all of its subtypes beforehand. In summary, the inserted type must not impose on the subtypes anything that could not already have been added to them directly.

## Applicability

Conditional on BP-054's carve-out.

## Exceptions and evidence limits

None beyond the stated precondition.

## Audit

**NodeSet XML:** Not structurally checkable (constraints are prose-level); requires reading both the new type's documented constraints and each subtype's pre-existing documented constraints.

**Document:** Compare constraint text added by the new intermediate type against pre-existing per-subtype constraint text.

**Assessment:** Semantically reviewable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
