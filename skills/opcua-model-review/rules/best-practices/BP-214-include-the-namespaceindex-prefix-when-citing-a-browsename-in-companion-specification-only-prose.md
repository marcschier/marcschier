---
id: "BP-214"
title: "Include the NamespaceIndex prefix when citing a BrowseName in Companion-Specification-only prose"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["13.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.2"]
---

# BP-214 - Include the NamespaceIndex prefix when citing a BrowseName in Companion-Specification-only prose

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Companion Specification defines a table assigning NamespaceIndex values to NamespaceUris (analogous to a Server's own NamespaceArray). When citing a BrowseName in the specification's own prose text (not inside a UANodeSet), the NamespaceIndex should be included (worked example: `0:EngineeringUnits`) to avoid ambiguity.

## Applicability

Companion Specification prose text, not UANodeSet content.

## Exceptions and evidence limits

See clause 13.3 (BP-215/BP-216) for the different rule applying to text that ends up inside a UANodeSet.

## Audit

**NodeSet XML:** N/A (prose-only rule).

**Document:** Review specification prose for BrowseName citations lacking a NamespaceIndex prefix.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 13.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
