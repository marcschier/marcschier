---
id: "BP-205"
title: "A new breaking-change Namespace requires new Conformance Units and Profiles"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3"]
---

# BP-205 - A new breaking-change Namespace requires new Conformance Units and Profiles

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When a new Namespace is created for a breaking change, new Conformance Units and Profiles must also be created, since the existing ones reference the old Namespace.

## Applicability

Companion Specifications minting a new NamespaceUri per BP-203.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Confirm new Conformance Unit/Profile definitions reference the new NamespaceUri (not merely reusing the old ones).

**Document:** Review the specification's Conformance Unit/Profile definitions.

**Assessment:** Static-checkable (given access to the CU/Profile registry) / semantically reviewable.

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 11.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
