---
id: "BP-014"
title: "ReferenceType BrowseNames are verb-based with no suffix"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-014 - ReferenceType BrowseNames are verb-based with no suffix

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

ReferenceType BrowseNames should carry no suffix and should describe the source->target relationship, typically as a verb; where a noun is used instead, it should be prefixed with a verb such as "Has" (examples: `HasComponent`, `HasEffect`, `HasChild`, `Organizes`, `Aggregates`).

## Applicability

ReferenceType NodeClass BrowseNames.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag ReferenceType BrowseNames ending in "Type" (suffix should be absent); verb/noun-form correctness is not mechanically decidable.

**Document:** Review spec ReferenceType tables for naming style.

**Assessment:** Partially static-checkable (suffix absence); verb-vs-noun semantic correctness is semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
