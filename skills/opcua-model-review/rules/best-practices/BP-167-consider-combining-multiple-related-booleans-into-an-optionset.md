---
id: "BP-167"
title: "Consider combining multiple related Booleans into an OptionSet"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.9"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9"]
---

# BP-167 - Consider combining multiple related Booleans into an OptionSet

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If there are several Boolean values, consider combining them into a single OptionSet rather than modelling them as separate independent Booleans.

## Applicability

DataType/field design with multiple related Booleans.

## Exceptions and evidence limits

None stated; explicitly phrased as a soft "consider," weaker than "should."

## Audit

**NodeSet XML:** Flag a Structure/ObjectType with several sibling Boolean fields/Variables as a candidate for OptionSet consolidation (advisory).

**Document:** Review field design for scattered related Booleans.

**Assessment:** Static-checkable (candidate detection) / semantically reviewable (whether consolidation is actually warranted).

**Source wording:** MAY ("consider")

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
