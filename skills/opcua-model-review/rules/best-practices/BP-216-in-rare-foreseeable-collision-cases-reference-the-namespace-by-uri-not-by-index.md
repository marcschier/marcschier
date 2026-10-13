---
id: "BP-216"
title: "In rare foreseeable-collision cases, reference the Namespace by URI, not by index"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["13.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.3"]
---

# BP-216 - In rare foreseeable-collision cases, reference the Namespace by URI, not by index

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

In the rare case where it can be foreseen that the same Name string will or may be used by two different Namespaces in a context where that would be ambiguous, the text should explicitly reference the Namespace by its URI (not by NamespaceIndex, since that value is context-dependent)  -  worked example given in the source: "...specified by 'http://opcfoundation.org/UA/'".

## Applicability

UANodeSet text with a foreseeable cross-Namespace name collision.

## Exceptions and evidence limits

This is the narrow carve-out from BP-215's general omit-the-index rule.

## Audit

**NodeSet XML:** For UANodeSet text documented as addressing a foreseeable collision, confirm it references a NamespaceUri string rather than a NamespaceIndex number.

**Document:** N/A.

**Assessment:** Static-checkable (given the documented collision scenario) / semantically reviewable (was the collision risk correctly identified).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 13.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/13.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
