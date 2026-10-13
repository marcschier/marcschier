---
id: "BP-009"
title: "VariableType BrowseNames end in \"Type\" (or \"VariableType\" if ambiguous)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3"]
---

# BP-009 - VariableType BrowseNames end in "Type" (or "VariableType" if ambiguous)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

VariableType BrowseNames should be suffixed "Type"; if that would be ambiguous with another Node, the suffix "VariableType" should be used instead (examples: `PropertyType`, `BaseDataVariableType`).

## Applicability

VariableType NodeClass BrowseNames.

## Exceptions and evidence limits

The "VariableType" suffix is itself the documented exception/fallback when plain "Type" would be ambiguous; the source does not define a mechanical ambiguity test.

## Audit

**NodeSet XML:** For every `UAVariableType/@BrowseName`, confirm it ends with "Type" or "VariableType".

**Document:** Scan spec VariableType tables.

**Assessment:** Static-checkable for suffix presence; "is it ambiguous, hence which suffix" is semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 2.1.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
