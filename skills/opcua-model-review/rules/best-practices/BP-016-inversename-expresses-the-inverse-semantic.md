---
id: "BP-016"
title: "InverseName expresses the inverse semantic"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-016 - InverseName expresses the inverse semantic

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The InverseName text should express the inverse of the relationship named by the BrowseName (worked example: `ComponentOf` as the inverse of `HasComponent`).

## Applicability

Asymmetric ReferenceTypes (see BP-015).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** None purely mechanical; a tool could flag suspicious non-inverse-looking pairs (e.g., InverseName identical to BrowseName) as a weak heuristic.

**Document:** Review spec ReferenceType tables for semantic plausibility.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
