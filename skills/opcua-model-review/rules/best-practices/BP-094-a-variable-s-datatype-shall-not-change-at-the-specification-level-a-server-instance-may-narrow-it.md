---
id: "BP-094"
title: "A Variable's DataType shall not change at the specification level; a Server instance may narrow it"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.17"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes"]
---

# BP-094 - A Variable's DataType shall not change at the specification level; a Server instance may narrow it

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Variable's DataType shall not change. The table explicitly splits the "Change in Server allowed?" answer in two: **No, for InstanceDeclarations**; but **Yes, for instances, if it becomes more restrictive (a subtype)**.

## Applicability

Variable Nodes. Two distinct audit targets: (a) the InstanceDeclaration as defined by the Companion Specification itself  -  DataType is frozen; (b) one Server's concrete instance of that Variable  -  the Server may narrow the DataType to a subtype.

## Exceptions and evidence limits

The instance-level narrowing allowance in (b) above; this does **not** weaken (a).

## Audit

**NodeSet XML:** For the Companion Specification's own NodeSet (type library), diff `DataType` across versions for a given Variable InstanceDeclaration  -  flag any change. For a deployed Server's exported AddressSpace compared against the specification, a narrower (subtype) DataType on an instance is an expected non-violation; a *wider* or unrelated DataType is not.

**Document:** Compare Variable DataType columns in specification tables across versions.

**Assessment:** Impossible without dependencies (requires prior version, or a Server export to check the instance case); otherwise static-checkable.

**Source wording:** MUST NOT (at InstanceDeclaration/specification level)

## Source notes

Directly ties to BP-069's clause-3.2.12 prohibition (same underlying rule, restated here in tabular form with the explicit instance-level carve-out spelled out). Treat BP-069 and BP-094 as describing the same rule from two places in the source (clause 3.2.12 prose and clause 3.2.17 Table 1); this extraction keeps them as separate entries because they are cited to different clauses/anchors and Table 1 states the instance-level nuance more explicitly.

## Source

- [OPC 11030 v1.03.03, clause 3.2.17](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.17#tbl_1_rules-for-backward-compatibly-of-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
