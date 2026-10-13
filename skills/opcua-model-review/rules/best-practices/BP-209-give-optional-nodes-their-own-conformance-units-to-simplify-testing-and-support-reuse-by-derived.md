---
id: "BP-209"
title: "Give optional Nodes their own Conformance Units to simplify testing and support reuse by derived models"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1"]
---

# BP-209 - Give optional Nodes their own Conformance Units to simplify testing and support reuse by derived models

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Providing separate Conformance Units for optional Nodes simplifies testing and better supports reuse of Information Models: a model derived from/reusing this one may need to require one of its optional items; if that optional item lacks its own unique Conformance Unit, the derived model would be forced to define a new Conformance Unit for functionality it did not itself originate.

## Applicability

Conformance Unit design anticipating reuse by other (derived) Companion Specifications.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** N/A.

**Document:** Review whether optional, individually-reusable Nodes have their own Conformance Unit.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source

- [OPC 11030 v1.03.03, clause 12.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
