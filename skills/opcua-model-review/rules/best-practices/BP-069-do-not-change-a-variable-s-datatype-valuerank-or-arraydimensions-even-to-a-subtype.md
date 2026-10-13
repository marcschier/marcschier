---
id: "BP-069"
title: "Do not change a Variable's DataType, ValueRank, or ArrayDimensions, even to a subtype"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.12"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.12"]
---

# BP-069 - Do not change a Variable's DataType, ValueRank, or ArrayDimensions, even to a subtype

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to change the DataType, ValueRank, or ArrayDimensions of a Variable  -  this applies equally to an InstanceDeclaration and to a standardized Variable (worked example given: `ServerStatus`). The document is explicit that even narrowing the DataType to a subtype is still considered a breaking change at this (specification/InstanceDeclaration) level, because a new Client connecting to an old Server would expect the subtype but might receive the supertype instead.

## Applicability

Variable InstanceDeclarations and standardized Variables, across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None at the specification/InstanceDeclaration level. **Important scope distinction:** Table 1 (clause 3.2.17, BP-094/BP-095 below) separately states that an actual Server **instance** (not the InstanceDeclaration on the type) may narrow a Variable's DataType/ValueRank to a subtype for its own deployed Nodes. This rule (BP-069) and Table 1's instance-level allowance are not in conflict  -  they describe two different audit targets (the Companion Specification's own type-level declaration vs. one Server's concrete instance), and both must be checked separately.

## Audit

**NodeSet XML:** Diff a Variable InstanceDeclaration's `DataType`/`ValueRank`/`ArrayDimensions` across two versions of the **type-defining** NodeSet; flag any change, including narrowing.

**Document:** Compare Variable DataType tables across specification versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

This is one of the most consequential scope distinctions in the whole document for an automated checker: do not conflate "the Companion Specification redefining an InstanceDeclaration's DataType" (forbidden, this rule) with "one Server instance exposing a narrower DataType for its own copy of that Variable" (permitted, see BP-094/BP-095). Exact source locations: clause 3.2.12 and Table 1 at clause 3.2.17.

## Source

- [OPC 11030 v1.03.03, clause 3.2.12](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.12)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
