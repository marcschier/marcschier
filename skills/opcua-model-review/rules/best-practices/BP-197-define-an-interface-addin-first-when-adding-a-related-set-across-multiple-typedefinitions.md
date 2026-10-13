---
id: "BP-197"
title: "Define an Interface/AddIn first when adding a related set across multiple TypeDefinitions"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.2"]
---

# BP-197 - Define an Interface/AddIn first when adding a related set across multiple TypeDefinitions

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a grouped set of InstanceDeclarations (not just one) that belongs together should be added to potentially several TypeDefinitions, an Interface or AddIn should be defined first and then applied uniformly at each location.

## Applicability

Adding a related set of new capabilities across multiple existing TypeDefinitions.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For a documented new capability appearing across multiple TypeDefinitions, confirm it is expressed via a shared `HasInterface`/AddIn component rather than independently duplicated per type.

**Document:** Review the new capability's definition mechanism.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 11.2.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
