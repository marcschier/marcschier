---
id: "BP-008"
title: "ObjectType BrowseNames end in \"Type\""
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-008 - ObjectType BrowseNames end in "Type"

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

ObjectType BrowseNames should be suffixed "Type" (examples given: `ServerType`, `NamespaceMetadataType`, `BaseEventType`).

## Applicability

ObjectType NodeClass BrowseNames.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For every `UAObjectType/@BrowseName`, confirm it ends with the literal substring "Type".

**Document:** Scan spec ObjectType tables for the same.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
