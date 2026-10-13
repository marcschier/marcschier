---
id: "BP-203"
title: "A required breaking change must use a new NamespaceUri"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.3"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3"]
---

# BP-203 - A required breaking change must use a new NamespaceUri

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When it is required or desirable to create a version of a Companion Specification independent of the old model (worked example: something fundamental was modelled badly, hindering adoption), a new NamespaceUri has to be used.

## Applicability

Companion Specifications needing an unavoidable breaking change.

## Exceptions and evidence limits

None  -  this is the mandatory consequence once a breaking change is accepted as necessary (cross-ref clause 3.3/BP-112 for the decision to go this route at all, vs. BP-113's parallel-type alternative).

## Audit

**NodeSet XML:** Confirm a distinct NamespaceUri is used for the breaking-change release.

**Document:** Review the specification's namespace declaration.

**Assessment:** Static-checkable.

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 11.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
