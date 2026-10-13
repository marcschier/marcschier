---
id: "BP-144"
title: "Option 3: Optional grouping + OptionalPlaceholder subcomponent, to preserve subtype flexibility"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.8"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8"]
---

# BP-144 - Option 3: Optional grouping + OptionalPlaceholder subcomponent, to preserve subtype flexibility

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

"Option 3": when the model is built to be extended and a Subtype may add its own additional functionality to the grouping Object, defining the subcomponent as `OptionalPlaceholder` (with the grouping Object Optional) allows a Subtype to independently change the grouping Object's own ModellingRule (e.g., to Mandatory) without being forced to also require a placeholder subcomponent.

## Applicability

Grouping Objects anticipated to gain independent functionality in future Subtypes.

## Exceptions and evidence limits

This is the forward-compatibility-oriented alternative to BP-143.

## Audit

**NodeSet XML:** For a grouping Object explicitly documented as extensible by Subtypes, confirm its placeholder child uses `OptionalPlaceholder` rather than `MandatoryPlaceholder`.

**Document:** Review stated extensibility intent for the grouping Object.

**Assessment:** Semantically reviewable (the "is extensibility anticipated" judgement); static-checkable once the pattern is declared.

**Source wording:** MAY (conditional)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 7.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
