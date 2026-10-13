---
id: "BP-152"
title: "An ObjectType may define class Methods with no ModellingRule"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.4"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.4"]
---

# BP-152 - An ObjectType may define class Methods with no ModellingRule

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

ObjectTypes may also have Methods without a ModellingRule at all  -  such a Method is a "class Method" called on the ObjectType itself (not on instances). Cross-reference: clause 8.4.1 gives an example where such a class Method constructs instances of the ObjectType.

## Applicability

ObjectType design for type-level (non-instance) operations.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** Confirm Methods intended as class Methods are attached directly to the `UAObjectType` Node (not propagated via a ModellingRule to instances).

**Document:** Review specification text describing class-Method behavior.

**Assessment:** Static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Detailed further at clause 8.4.1 (BP-190).

## Source

- [OPC 11030 v1.03.03, clause 7.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
