---
id: "BP-213"
title: "Generic/reusable Companion Specifications should expose Facets rather than only full Profiles"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.2"]
---

# BP-213 - Generic/reusable Companion Specifications should expose Facets rather than only full Profiles

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Generic Companion Specifications designed to be used by others may define only Facets (or bare Conformance Units) rather than full Profiles, so that other Companion Specifications can more easily reuse the grouping inside their own Profiles. If a group of functionality is expected to be reused by other specifications, defining it as a Facet is recommended to ease that reuse; such Facets can then be included within an overall Profile defined by a (domain-specific) Companion Specification.

## Applicability

Generic/reusable Companion Specifications.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A.

**Document:** Review whether reusable functionality groups are exposed as Facets.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 12.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
