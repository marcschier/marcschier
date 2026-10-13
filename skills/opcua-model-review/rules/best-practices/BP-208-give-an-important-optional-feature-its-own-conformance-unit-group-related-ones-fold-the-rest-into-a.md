---
id: "BP-208"
title: "Give an important optional feature its own Conformance Unit; group related ones; fold the rest into a broader unit"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["12.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1"]
---

# BP-208 - Give an important optional feature its own Conformance Unit; group related ones; fold the rest into a broader unit

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If an optional feature is important enough that a Client needs to know whether it specifically is supported, it should get an individual Conformance Unit. Several optional components that belong together should be grouped into one Conformance Unit; otherwise, fold them into an overall Conformance Unit. Worked example: an ObjectType with ten optional Variables could have one Conformance Unit for the whole type (not preferred), one per optional Variable, or three related ones grouped together  -  any approach may be appropriate depending on the Variables.

## Applicability

Conformance Unit granularity decisions for optional model elements.

## Exceptions and evidence limits

None stated; explicitly acknowledges multiple valid granularities depending on context.

## Audit

**NodeSet XML:** N/A.

**Document:** Review Conformance Unit granularity against the importance/relatedness of the optional elements covered.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (stated as "the recommendation")

## Source

- [OPC 11030 v1.03.03, clause 12.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/12.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
