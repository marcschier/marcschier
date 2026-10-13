---
id: "BP-015"
title: "InverseName applies only to asymmetric ReferenceTypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-015 - InverseName applies only to asymmetric ReferenceTypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A ReferenceType's InverseName should only be provided for asymmetric References.

## Applicability

ReferenceType NodeClass Nodes.

## Exceptions and evidence limits

Symmetric ReferenceTypes are implicitly excluded (not an "exception" so much as the rule's own scope boundary).

## Audit

**NodeSet XML:** For `UAReferenceType` nodes with `Symmetric="true"`, flag presence of a distinct `InverseName`; for `Symmetric="false"`, confirm `InverseName` is present.

**Document:** Review spec ReferenceType tables.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
