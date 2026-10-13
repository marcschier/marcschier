---
id: "BP-173"
title: "Avoid recursive structures when possible"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.10"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10"]
---

# BP-173 - Avoid recursive structures when possible

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Recursive structures (an ObjectType, VariableType, or DataType directly or indirectly containing an InstanceDeclaration/field of itself) should be avoided when creating DataTypes, ObjectTypes, or VariableTypes.

## Applicability

New ObjectType/VariableType/DataType design.

## Exceptions and evidence limits

The clause itself acknowledges recursive structures are "sometimes... helpful and cannot be avoided"  -  see BP-174/BP-175 for the rules that then apply.

## Audit

**NodeSet XML:** Detect self-referencing type chains (an ObjectType/VariableType containing, directly or via nested InstanceDeclarations, a member typed as itself or an ancestor; a Structure field typed as its own DataType or containing it indirectly).

**Document:** Review type designs for unavoidable recursion.

**Assessment:** Static-checkable (detection of recursion itself); "was it avoidable" is semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
