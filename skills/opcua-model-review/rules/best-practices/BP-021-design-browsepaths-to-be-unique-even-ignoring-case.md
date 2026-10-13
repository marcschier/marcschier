---
id: "BP-021"
title: "Design BrowsePaths to be unique even ignoring case"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.4"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4"]
---

# BP-021 - Design BrowsePaths to be unique even ignoring case

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because OPC UA Servers are permitted to treat BrowseNames case-insensitively, Information Models should not rely on case sensitivity to make BrowsePaths unique; BrowsePaths should be designed so that they remain unique even when case is ignored (worked example: do not use sibling Properties "Id" and "ID" on the same parent  -  instead use distinguishing names like "NetworkId" and "DeviceId").

## Applicability

Any set of sibling InstanceDeclarations/TypeDefinition members sharing a parent.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Within each parent Node's set of declared children, lower-case all BrowseNames and flag collisions that only exist due to case differences.

**Document:** Review spec substructure tables for same-parent names differing only by case.

**Assessment:** Static-checkable.

**Source wording:** SHOULD NOT (rely on case sensitivity) / SHOULD (design case-insensitively-unique paths)

## Source notes

The permission "OPC UA Servers are allowed to treat BrowseNames in a case-insensitive manner" and "OPC UA Clients shall consider case sensitivity" are server/client runtime-behavior statements included by the source only as rationale for this modelling rule; they are not separately extracted as standalone modelling rules since they describe application behavior rather than Information Model design (see exact text at clause 2.1.4).

## Source

- [OPC 11030 v1.03.03, clause 2.1.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
