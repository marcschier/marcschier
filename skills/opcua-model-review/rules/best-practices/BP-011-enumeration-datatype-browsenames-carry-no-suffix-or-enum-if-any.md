---
id: "BP-011"
title: "Enumeration DataType BrowseNames carry no suffix (or \"Enum\" if any)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-011 - Enumeration DataType BrowseNames carry no suffix (or "Enum" if any)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Enumeration DataTypes (subtypes of the Enumeration DataType) should not have a naming suffix; if a suffix is used anyway, it should be "Enum" (examples of the no-suffix default: `NodeClass`, `ServerState`).

## Applicability

DataType NodeClass Nodes that are subtypes of Enumeration.

## Exceptions and evidence limits

None beyond the stated "Enum" fallback.

## Audit

**NodeSet XML:** For `UADataType` nodes whose supertype chain includes Enumeration (ns=0;i=29), flag BrowseNames ending in any suffix other than "Enum".

**Document:** Scan spec Enumeration tables.

**Assessment:** Static-checkable.

**Source wording:** SHOULD NOT (carry a suffix, as the default) / SHOULD ("Enum" specifically, if a suffix is used at all)

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
