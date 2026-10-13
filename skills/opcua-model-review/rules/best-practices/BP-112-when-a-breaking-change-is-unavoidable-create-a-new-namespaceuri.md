---
id: "BP-112"
title: "When a breaking change is unavoidable, create a new NamespaceUri"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3"]
---

# BP-112 - When a breaking change is unavoidable, create a new NamespaceUri

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When something must break from an existing specification version, one option is to create a new NamespaceUri, defining  -  conceptually  -  an entirely new Information Model (detailed versioning pattern at clause 11.3, BP-203-BP-205). The document calls this "on one hand the cleanest solution," while noting it is "a completely incompatible change of the model": no old Client will directly work with a new Server and vice versa.

## Applicability

Companion Specifications facing an unavoidable breaking change.

## Exceptions and evidence limits

See BP-113 for the alternative (parallel-type) strategy.

## Audit

**NodeSet XML:** Confirm a distinct NamespaceUri was minted (cross-check against clause 11.3's versioning pattern, BP-208).

**Document:** Review the specification's namespace declaration and version history.

**Assessment:** Static-checkable (presence of new NamespaceUri) / semantically reviewable (was it actually warranted).

**Source wording:** SHOULD (recommended, as "the cleanest solution")

## Source

- [OPC 11030 v1.03.03, clause 3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
