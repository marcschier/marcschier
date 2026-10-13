---
id: "BP-007"
title: "Prefixes in BrowseNames are permitted, not mandated or prohibited"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["2.1.2"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2"]
---

# BP-007 - Prefixes in BrowseNames are permitted, not mandated or prohibited

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The document states there is no recommendation on using prefixes in BrowseNames, and explicitly notes Companion Specifications may use a prefix where it suits their model (worked example: a "Vision" prefix for Vision-Companion-Specification types, e.g. `VisionStateMachineType`).

## Applicability

Any BrowseName, any Companion Specification.

## Exceptions and evidence limits

N/A  -  this is itself a stated non-restriction.

## Audit

**NodeSet XML:** None  -  a reviewer/tool must **not** flag prefixed BrowseNames as a naming violation; this entry exists specifically to prevent that false positive (per task instruction not to convert a permission into a prohibition).

**Document:** None.

**Assessment:** Static-checkable only in the negative sense (absence of a violation to raise).

**Source wording:** MAY (explicit permission; this document states there is no recommendation either way)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Recorded primarily as a guardrail against over-strict automated naming checks.

## Source

- [OPC 11030 v1.03.03, clause 2.1.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
