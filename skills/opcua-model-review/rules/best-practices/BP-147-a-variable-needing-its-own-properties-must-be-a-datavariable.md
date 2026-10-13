---
id: "BP-147"
title: "A Variable needing its own Properties must be a DataVariable"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.2"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.2"]
---

# BP-147 - A Variable needing its own Properties must be a DataVariable

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a Variable needs its own Properties (worked example: an engineering unit), it must be modelled as a DataVariable  -  even when the Variable's semantic would otherwise suggest it should be a Property.

## Applicability

Any Variable that itself requires attached Properties.

## Exceptions and evidence limits

None  -  this overrides the semantic-fit guidance in BP-146 whenever it applies.

## Audit

**NodeSet XML:** For any `UAVariable` with outgoing `HasProperty` References, confirm its own `TypeDefinition` is not `PropertyType` (which structurally cannot have such references per BP-146, so this is close to self-enforcing, but worth checking directly for malformed NodeSets).

**Document:** Review whether Variables documented as needing sub-Properties are correctly typed as DataVariables.

**Assessment:** Static-checkable.

**Source wording:** MUST ("you have to use a DataVariable")

## Source

- [OPC 11030 v1.03.03, clause 7.3.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
