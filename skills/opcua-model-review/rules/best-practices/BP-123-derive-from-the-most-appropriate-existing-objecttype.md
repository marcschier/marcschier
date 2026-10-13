---
id: "BP-123"
title: "Derive from the most appropriate existing ObjectType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2"]
---

# BP-123 - Derive from the most appropriate existing ObjectType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When defining an ObjectType, consider whether an already-appropriate ObjectType exists to derive from  -  judged by both its defined semantic and its defined substructure  -  looking not only at the base specification but also at ObjectTypes defined in existing Companion Specifications (discoverable via the Online Reference).

## Applicability

New ObjectType design decisions.

## Exceptions and evidence limits

See BP-125 (fallback to BaseObjectType).

## Audit

**NodeSet XML:** Not mechanically checkable (requires cross-model semantic judgement); a tool could at best suggest candidate existing types with overlapping substructure for human review.

**Document:** Review specification rationale for the chosen supertype.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
