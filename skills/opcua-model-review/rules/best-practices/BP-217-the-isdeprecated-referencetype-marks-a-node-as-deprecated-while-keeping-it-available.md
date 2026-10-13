---
id: "BP-217"
title: "The IsDeprecated ReferenceType marks a Node as deprecated while keeping it available"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.2"]
strength: "INFORMATIVE"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.2"]
---

# BP-217 - The IsDeprecated ReferenceType marks a Node as deprecated while keeping it available

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

OPC UA defines a mechanism to mark a Node as deprecated using the `IsDeprecated` ReferenceType, pointing from the deprecated Node to information identifying when it was first deprecated. The general purpose: mark Nodes that should no longer be used (usually because a replacement exists) while keeping them available so Clients built against an older Information Model version keep working; new Clients (or new configurations of old Clients) should not use the deprecated Nodes, since future Information Model versions will not retain them (cross-ref clause 3.2.16/BP-076's permanent-retention rule only applies within one NamespaceUri  -  this describes an orderly *transition*, not a contradiction of BP-076).

## Applicability

Any Node a Companion Specification wishes to mark as superseded, within the base-specification mechanism's terms.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** Confirm an `IsDeprecated` Reference exists from the deprecated Node to its deprecation-identifying target.

**Document:** Review specification text identifying deprecated Nodes and their replacements.

**Assessment:** Static-checkable (reference presence).

**Source wording:** Informative (describes a base-specification mechanism) / MAY (its use is optional)

**Context guard:** Informative framing does not independently establish a conformance violation.

## Source

- [OPC 11030 v1.03.03, clause 14.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
