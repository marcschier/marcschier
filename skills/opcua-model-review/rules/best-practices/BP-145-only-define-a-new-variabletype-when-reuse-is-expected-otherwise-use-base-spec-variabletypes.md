---
id: "BP-145"
title: "Only define a new VariableType when reuse is expected; otherwise use base-spec VariableTypes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.1"]
---

# BP-145 - Only define a new VariableType when reuse is expected; otherwise use base-spec VariableTypes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Defining a new VariableType only makes sense when it is expected to be used several times. Since a Variable's semantic is typically already defined by its owning ObjectType, the base specification's existing VariableTypes (notably OPC 10000-8's range/engineering-unit-bearing types) are often already sufficient, and no new VariableType needs to be defined.

## Applicability

New VariableType design decisions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag single-use custom VariableTypes as a candidate for replacement by an existing base-spec VariableType (advisory; requires semantic judgement to confirm).

**Document:** Review rationale for introducing a new VariableType versus reusing an existing one.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.3.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
