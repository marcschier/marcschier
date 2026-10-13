---
id: "BP-076"
title: "Never remove a previously-defined Node from a Companion Specification's Information Model"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.16"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.16"]
---

# BP-076 - Never remove a previously-defined Node from a Companion Specification's Information Model

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to remove any Node that has been defined before  -  this explicitly includes DataTypes, VariableTypes, ObjectTypes, and standardized Instances or InstanceDeclarations, including optional ones. The Information Model definition itself must retain every such Node permanently once released.

## Applicability

The Companion Specification's own Information Model definition (its UANodeSet/type library), across versions sharing a NamespaceUri.

## Exceptions and evidence limits

None at the specification-definition level. See BP-077 for the distinct, narrower Server-level allowance.

## Audit

**NodeSet XML:** Diff two NodeSet versions of the same NamespaceUri; flag any Node present in the old version but absent in the new version.

**Document:** Compare the specification's full Node inventory/tables across versions.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source notes

Rationale given: prevents a NodeId/BrowseName from being silently repurposed for something different in a later version.

## Source

- [OPC 11030 v1.03.03, clause 3.2.16](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.16)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
