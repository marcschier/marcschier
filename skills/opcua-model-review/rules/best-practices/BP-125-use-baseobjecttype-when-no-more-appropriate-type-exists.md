---
id: "BP-125"
title: "Use BaseObjectType when no more appropriate type exists"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2"]
---

# BP-125 - Use BaseObjectType when no more appropriate type exists

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When there is no more appropriate ObjectType to derive from, `BaseObjectType` shall be used as the base.

## Applicability

New ObjectType design decisions with no suitable existing supertype.

## Exceptions and evidence limits

None  -  this is the mandatory fallback.

## Audit

**NodeSet XML:** For any ObjectType whose supertype is not a more specific existing type by design rationale, confirm its supertype chain terminates appropriately at `BaseObjectType` (ns=0;i=58) rather than some other unrelated/ad hoc arrangement  -  full verification requires the semantic judgement of BP-123.

**Document:** Review specification rationale.

**Assessment:** Static-checkable (that the fallback, when used, is literally BaseObjectType) combined with semantically reviewable (whether the fallback was appropriately triggered).

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 7.2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
