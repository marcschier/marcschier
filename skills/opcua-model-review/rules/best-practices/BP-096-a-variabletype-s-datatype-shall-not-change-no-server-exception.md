---
id: "BP-096"
title: "A VariableType's DataType shall not change (no Server exception)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-096 - A VariableType's DataType shall not change (no Server exception)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A VariableType's own DataType shall not change. Unlike the Variable case (BP-094), the table gives a flat "No" for "Change in Server allowed?"  -  there is no instance-level carve-out, because a VariableType itself is never instantiated as a Server "instance" in the same sense.

## Applicability

VariableType Nodes.

## Exceptions and evidence limits

None.

## Audit

**NodeSet XML:** Diff `DataType` across versions for a given VariableType.

**Document:** Compare VariableType DataType columns across versions.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Contrast deliberately preserved against BP-094 (Variable case), where the table does give a narrower Server-level exception.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
