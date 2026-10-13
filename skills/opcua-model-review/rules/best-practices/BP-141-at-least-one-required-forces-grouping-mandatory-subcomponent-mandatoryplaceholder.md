---
id: "BP-141"
title: "\"At least one required\" forces grouping-Mandatory + subcomponent-MandatoryPlaceholder"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.8"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8"]
---

# BP-141 - "At least one required" forces grouping-Mandatory + subcomponent-MandatoryPlaceholder

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When an ObjectType needs to guarantee at least one subcomponent of a given type (exposed via a Placeholder ModellingRule, typically under a grouping Object), the grouping Object must be Mandatory and the subcomponent must use `MandatoryPlaceholder`.

## Applicability

ObjectType design requiring a guaranteed-present set member of unspecified cardinality/name.

## Exceptions and evidence limits

None  -  this is the one combination that guarantees "at least one," per the document.

## Audit

**NodeSet XML:** For a grouping Object intended to guarantee at least one member, confirm the grouping Object's own ModellingRule is Mandatory and its placeholder-typed child uses `MandatoryPlaceholder`.

**Document:** Review the specification's stated cardinality intent against the ModellingRule combination used.

**Assessment:** Static-checkable (given the documented intent).

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 7.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
