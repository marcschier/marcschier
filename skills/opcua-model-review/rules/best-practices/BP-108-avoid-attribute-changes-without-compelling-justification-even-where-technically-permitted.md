---
id: "BP-108"
title: "Avoid attribute changes without compelling justification, even where technically permitted"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17"]
---

# BP-108 - Avoid attribute changes without compelling justification, even where technically permitted

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Beyond the per-attribute table, the clause's general framing states that, after a Node is published, modifying attributes is a breaking change for some attributes and not for others, but "in general, changes to attributes should be avoided unless there is a compelling justification"  -  i.e., even a technically-permitted change (per BP-081/BP-082/BP-083/BP-085/BP-087/BP-099/BP-101/BP-102/BP-103) should not be made gratuitously.

## Applicability

All Node Attributes, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

Overridden by an explicit "compelling justification"  -  not mechanically defined.

## Audit

**NodeSet XML:** None directly (this is a change-management discipline, not a structural property).

**Document:** Review version-to-version change rationale/release notes for unjustified attribute churn.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
