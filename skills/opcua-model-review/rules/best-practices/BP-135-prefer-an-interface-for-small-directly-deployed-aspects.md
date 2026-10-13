---
id: "BP-135"
title: "Prefer an Interface for small, directly-deployed aspects"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.6"]
---

# BP-135 - Prefer an Interface for small, directly-deployed aspects

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is recommended to use an Interface when something relatively small and simple is being defined (described as "maybe a handful of Variables and Methods") that should potentially be deployable directly on an ObjectType without a grouping Object. The document notes an Interface is, by base-specification design, intentionally simple/limited (cross-ref OPC 10000-3, out of scope for detail), so not every composition need can be expressed as an Interface.

## Applicability

Composition design choice between Interface and AddIn.

## Exceptions and evidence limits

Bounded by the base-specification's Interface construct's limitations (detail out of scope, Part 3).

## Audit

**NodeSet XML:** For small (few-member) composed substructures deployed via `HasInterface` without an intervening grouping Object, this is an expected-compliant pattern; flag the inverse (large substructures crammed into an Interface) as a candidate for reconsideration.

**Document:** Review the size/complexity of Interface definitions.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 7.2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
