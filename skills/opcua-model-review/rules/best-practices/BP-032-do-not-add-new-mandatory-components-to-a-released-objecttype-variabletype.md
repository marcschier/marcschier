---
id: "BP-032"
title: "Do not add new mandatory components to a released ObjectType/VariableType"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.1"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.1"]
---

# BP-032 - Do not add new mandatory components to a released ObjectType/VariableType

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is not allowed to add new mandatory InstanceDeclarations (ModellingRule `Mandatory` or `MandatoryPlaceholder`) to an ObjectType or VariableType that has already been released under an existing NamespaceUri.

## Applicability

Only binds when the new version is intended to reuse the existing NamespaceUri (per clause 3.1). Applies to ObjectType and VariableType Nodes.

## Exceptions and evidence limits

See BP-033 for the sanctioned alternative patterns.

## Audit

**NodeSet XML:** Diff two NodeSet versions sharing a NamespaceUri; for each ObjectType/VariableType present in both, flag any child InstanceDeclaration whose ModellingRule is `Mandatory`/`MandatoryPlaceholder` in the new version but was absent in the old version.

**Document:** Compare successive specification revisions' AddressSpace tables for newly-mandatory rows on existing types.

**Assessment:** Impossible without dependencies for a single NodeSet snapshot (requires the *prior released version* for comparison); static-checkable given both versions.

**Source wording:** MUST NOT

## Source notes

The rationale given is explicitly interoperability-directed: a new-version-aware Client could otherwise expect a mandatory feature an old Server does not provide.

## Source

- [OPC 11030 v1.03.03, clause 3.2.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
