---
id: "BP-158"
title: "Expose array entries as sub-variables when individual referencing or metadata is needed"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.6"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6"]
---

# BP-158 - Expose array entries as sub-variables when individual referencing or metadata is needed

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When individual array entries need to be referenced from elsewhere, or need their own additional information (e.g., Properties), expose them as sub-variables  -  retaining all the advantages of the plain-array approach. Two mechanisms are available: the ModellingRule `ExposesItsArray` (keeps a sub-variable's identity independent of its position in the array) or the `HasStructuredComponent` ReferenceType (ties a sub-variable to the array's order, so if the order changes, what is referenced changes too). The choice depends on whether entry-identity or entry-order is what matters.

## Applicability

Set/list modelling needing individually-referenceable or individually-annotatable entries.

## Exceptions and evidence limits

None stated beyond the identity-vs-order selection criterion.

## Audit

**NodeSet XML:** Confirm array-exposing sub-variables use exactly one of `ExposesItsArray` or `HasStructuredComponent` consistent with the documented identity/order intent.

**Document:** Review which mechanism was chosen and whether it matches the stated identity/order requirement.

**Assessment:** Static-checkable (mechanism used) / semantically reviewable (correct choice for intent).

**Source wording:** SHOULD

## Source notes

Detailed mechanics of the two ModellingRule/ReferenceType options are deferred to OPC 10000-3 ("OPC 10000-3 describes the differences"), out of scope here.

## Source

- [OPC 11030 v1.03.03, clause 7.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
