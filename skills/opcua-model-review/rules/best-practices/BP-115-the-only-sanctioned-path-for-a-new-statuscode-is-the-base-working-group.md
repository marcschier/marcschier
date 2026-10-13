---
id: "BP-115"
title: "The only sanctioned path for a new StatusCode is the base working group"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["4"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/4"]
---

# BP-115 - The only sanctioned path for a new StatusCode is the base working group

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

In very rare cases a Companion Specification may need an additional StatusCode (worked example: FDI needed to indicate a value was currently being edited by a specific Client). In that case, the Companion Specification authors shall contact the base OPC UA working group, and the needed StatusCode will be added to the base specification  -  this is described as the only legitimate route, not a design choice left to the companion spec itself.

## Applicability

Companion Specifications with a demonstrated, rare need for a new StatusCode.

## Exceptions and evidence limits

N/A  -  this is itself the exception path to BP-114.

## Audit

**NodeSet XML:** N/A (organizational process, not a NodeSet artifact).

**Document:** If a specification claims a new StatusCode is needed, confirm it documents engagement with the base working group rather than self-defining one.

**Assessment:** Semantically reviewable (organizational/process compliance, not structural).

**Source wording:** MUST (procedural, conditional)

## Source

- [OPC 11030 v1.03.03, clause 4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
