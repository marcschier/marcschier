---
id: "BP-028"
title: "Companion-spec NamespaceUri template pattern"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.5"]
---

# BP-028 - Companion-spec NamespaceUri template pattern

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The Companion Specification template already suggests the NamespaceUri pattern `http://opcfoundation.org/UA/<short name>/`; this is cited as the general recommended pattern.

## Applicability

New Companion Specification NamespaceUris.

## Exceptions and evidence limits

None stated beyond this being the template default.

## Audit

**NodeSet XML:** Check `NamespaceUris` entries for companion namespaces against this pattern.

**Document:** Review the specification's namespace declaration.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source notes

This clause explicitly defers detailed NamespaceUri rules to OPC 10000-3 ("OPC 10000-3 defines rules for NamespaceUris")  -  that detail is out of scope for this extraction (Part 3).

## Source

- [OPC 11030 v1.03.03, clause 2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
