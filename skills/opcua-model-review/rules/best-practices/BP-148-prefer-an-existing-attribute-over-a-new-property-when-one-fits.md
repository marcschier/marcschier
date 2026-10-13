---
id: "BP-148"
title: "Prefer an existing Attribute over a new Property when one fits"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.3"]
---

# BP-148 - Prefer an existing Attribute over a new Property when one fits

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Before defining a new Property, check whether an existing base-specification Node Attribute is already suitable (worked example: use the `Description` Attribute rather than defining a custom "Description" Property). Since all Attributes are allowed to be writable, even a requirement for a writeable description does not justify a separate Property.

## Applicability

New descriptive-data design decisions for a Node.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** Flag custom Properties whose BrowseName/semantic duplicates an existing Attribute name (e.g., a Property literally named "Description").

**Document:** Review rationale for new Property definitions against the Attribute set.

**Assessment:** Static-checkable (name-collision heuristic) / semantically reviewable (true semantic duplication).

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
