---
id: "BP-188"
title: "Instance deletion may be an instance Method or a class Method taking an identifier"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.4.1"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.1"]
---

# BP-188 - Instance deletion may be an instance Method or a class Method taking an identifier

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Deleting an Object may be modelled as an ordinary instance Method called directly on the instance to be deleted, or alternatively as a class Method on the TypeDefinition that takes the target instance's identification as an input Argument.

## Applicability

ObjectType instance-deletion design.

## Exceptions and evidence limits

None  -  both are presented as equally valid alternatives.

## Audit

**NodeSet XML:** Confirm the deletion Method matches one of these two shapes (instance-attached with no identifying argument, or class-attached with an identifying argument).

**Document:** Review the deletion Method's design.

**Assessment:** Static-checkable.

**Source wording:** MAY (two accepted alternatives)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 8.4.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
