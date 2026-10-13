---
id: "BP-204"
title: "Construct the new NamespaceUri by appending a major-version suffix"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3"]
---

# BP-204 - Construct the new NamespaceUri by appending a major-version suffix

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is recommended to construct the new NamespaceUri by extending the old one with `V<VersionNumber>/` (e.g. `V2/` for version 2), using only the major version number, since only major-version changes should indicate a breaking change.

## Applicability

Companion Specifications minting a new NamespaceUri per BP-203.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For a breaking-change release, confirm the new NamespaceUri equals the old one with a `V<N>/` suffix appended, where N is an integer major version.

**Document:** Review the specification's namespace declaration.

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 11.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
