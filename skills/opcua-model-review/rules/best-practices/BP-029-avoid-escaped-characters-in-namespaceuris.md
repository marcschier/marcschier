---
id: "BP-029"
title: "Avoid %-escaped characters in NamespaceUris"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.5"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.5"]
---

# BP-029 - Avoid %-escaped characters in NamespaceUris

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The use of %-escaped characters in a NamespaceUri is strongly discouraged  -  stated as a general recommendation applying to both Companion Specification and vendor-specific NamespaceUris.

## Applicability

Any NamespaceUri (companion or vendor).

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Scan `NamespaceUris` entries for `%XX` percent-encoded sequences.

**Document:** Review the specification's namespace declaration text.

**Assessment:** Static-checkable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 2.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
