---
id: "BP-150"
title: "Define a VariableType mainly for reusable semantics, not for ObjectType-scoped Variables"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.4"]
---

# BP-150 - Define a VariableType mainly for reusable semantics, not for ObjectType-scoped Variables

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

VariableTypes are used to define a Variable's substructure, semantic, and DataType (worked example: `AnalogItemType` providing `EngineeringUnits`/`InstrumentRange`). It can make sense to define one purely to capture semantics intended for reuse across multiple places (worked example: a generic "SetPoints" VariableType). Conversely, a Variable whose semantic is already fully defined by its owning ObjectType does not need its own dedicated VariableType.

## Applicability

New VariableType design decisions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag a custom VariableType used in exactly one place whose semantic duplicates its sole owning ObjectType's already-defined semantic (advisory).

**Document:** Review rationale for new VariableType definitions.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD / SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 7.3.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
