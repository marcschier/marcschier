---
id: "BP-215"
title: "Omit the NamespaceIndex when BrowseName text appears inside UANodeSet content"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["13.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.3"]
---

# BP-215 - Omit the NamespaceIndex when BrowseName text appears inside UANodeSet content

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Text that ends up inside a UANodeSet (e.g. a `Description` Attribute's text) will appear in deployed Servers' AddressSpaces, where the actual NamespaceIndex very likely differs from the one used in the Companion Specification's own table. Therefore, it is recommended to omit the NamespaceIndex in such text and use just the Name part (worked example: "The unit is defined in the EngineeringUnits property."). In almost all cases there will not be two same-named BrowseNames from different Namespaces plausibly meant in that Description's context.

## Applicability

Text embedded in a UANodeSet (Description Attributes, etc.), contrasted with BP-214's prose-only rule.

## Exceptions and evidence limits

See BP-216 for the rare-collision case.

## Audit

**NodeSet XML:** Flag `Description` (and similar) Attribute text containing an explicit `N:Name` NamespaceIndex-qualified reference, as a likely violation (the index would be wrong/meaningless once deployed).

**Document:** N/A (this concerns NodeSet content, not specification prose).

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 13.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
