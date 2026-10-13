---
id: "BP-155"
title: "Use a Methods-based approach when extra context is needed or the Client should trigger (re)calculation"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.5.7", "7.5.5"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.5"]
---

# BP-155 - Use a Methods-based approach when extra context is needed or the Client should trigger (re)calculation

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The Methods-based approach (one Method to read combined data, another to change it, clause 7.5.5) makes sense when additional data should be supplied with the request, or when the Client should explicitly trigger a server-side calculation rather than relying on passive sampling. Trade-off: Clients cannot subscribe to changes this way, only poll via repeated calls  -  the document explicitly judges this approach not well suited to the IP-configuration running example.

## Applicability

Structured-data modelling decisions where request-time parameters or explicit triggering matter.

## Exceptions and evidence limits

None stated beyond the trade-off description.

## Audit

**NodeSet XML:** Not independently mechanical.

**Document:** Review rationale for choosing a Methods-based approach.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (conditional recommendation)

## Source notes

The Method signature itself may use a structured DataType instead of individual Arguments (noted in clause 7.5.5 as a further sub-choice, not separately atomized here).

## Source

- [OPC 11030 v1.03.03, clause 7.5.7](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.7)
- [OPC 11030 v1.03.03, clause 7.5.5](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.5.5)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
