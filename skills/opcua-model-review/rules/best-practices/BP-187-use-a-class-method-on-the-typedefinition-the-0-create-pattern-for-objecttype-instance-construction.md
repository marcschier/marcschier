---
id: "BP-187"
title: "Use a class Method on the TypeDefinition (the \"0:Create\" pattern) for ObjectType instance construction"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.4.1"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.1"]
---

# BP-187 - Use a class Method on the TypeDefinition (the "0:Create" pattern) for ObjectType instance construction

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

One pattern: the TypeDefinition itself provides Methods to add/remove instances. Because Methods only apply to Objects/ObjectTypes, this only works for ObjectTypes, not VariableTypes. The base specification (OPC 10000-3) already standardizes the BrowseName `0:Create` as a class Method called on the ObjectType to construct a new instance; its Arguments should specify where to place the new Object (e.g. the parent NodeId) and how to configure it (e.g. which optional components to include).

## Applicability

ObjectType instance-construction design.

## Exceptions and evidence limits

Not applicable to VariableTypes.

## Audit

**NodeSet XML:** For an ObjectType exposing instance-construction, confirm the Method is attached to the `UAObjectType` itself (class Method, no ModellingRule, cross-ref BP-152) and is named `Create` in namespace 0, with Arguments covering placement and configuration.

**Document:** Review the Method's documented Arguments for placement/configuration completeness.

**Assessment:** Static-checkable.

**Source wording:** MAY (recommended pattern where applicable)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 8.4.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.4.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
