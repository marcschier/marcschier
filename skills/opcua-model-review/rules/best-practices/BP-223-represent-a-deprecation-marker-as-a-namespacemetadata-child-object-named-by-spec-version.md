---
id: "BP-223"
title: "Represent a deprecation marker as a NamespaceMetadata child Object named by spec+version"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.3.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.2"]
---

# BP-223 - Represent a deprecation marker as a NamespaceMetadata child Object named by spec+version

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When marking Nodes deprecated in a Companion Specification, it is recommended to create an Object as a child of the Namespace's `NamespaceMetadata` Object, and point to it from the deprecated Node(s) using the `IsDeprecated` ReferenceType. The marker Object's BrowseName should indicate the deprecation and the deprecating version (worked example pattern: `<SpecName>Version1_02`; a cited real-world instance is OPC 40501-1 version 1.02).

## Applicability

Companion Specifications marking Nodes as deprecated.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm a child Object of `NamespaceMetadata` exists with a BrowseName following the `<SpecName>Version<Major>_<Minor>` pattern, and that deprecated Nodes reference it via `IsDeprecated`.

**Document:** Review deprecation notices for this structural pattern.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 14.3.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
