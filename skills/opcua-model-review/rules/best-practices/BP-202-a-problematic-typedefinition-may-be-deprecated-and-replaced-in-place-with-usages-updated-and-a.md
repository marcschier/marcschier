---
id: "BP-202"
title: "A problematic TypeDefinition may be deprecated and replaced in-place, with usages updated and a numbered successor name"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.6"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.6"]
---

# BP-202 - A problematic TypeDefinition may be deprecated and replaced in-place, with usages updated and a numbered successor name

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

When an old model has missing base functionality or wrongly-mandatory functionality, it may be necessary to deprecate an old TypeDefinition and define a new one instead  -  even though this could be considered a breaking change (cross-ref clause 11.3/BP-203), it can also be resolved within the existing Namespace by deprecating the old TypeDefinition (cross-ref clause 14) and defining a new one. When exactly one old TypeDefinition is replaced by exactly one new one, it is recommended to reuse the same name with an appended version number (e.g. "2"). This approach requires that all usages of the old TypeDefinition be replaced with the new one, which may itself cascade into needing new versions of other TypeDefinitions that used the old one.

## Applicability

Companion Specifications needing to replace a flawed TypeDefinition without changing the NamespaceUri.

## Exceptions and evidence limits

None stated beyond the one-old-for-one-new scope of the naming recommendation (a different cardinality of replacement is not addressed).

## Audit

**NodeSet XML:** Confirm the old TypeDefinition is retained (cross-ref BP-076) and marked deprecated (cross-ref clause 14), the new one uses the numbered-name convention, and no other retained Node still references the old TypeDefinition where the new one was intended to replace it.

**Document:** Review the specification's migration narrative and naming.

**Assessment:** Static-checkable (retention/naming) / semantically reviewable (completeness of the cascade).

**Source wording:** MAY (deprecate-and-replace as a strategy) / SHOULD (naming pattern) / MUST (replace all usages)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Closely related to clause 3.3's "parallel numbered type" strategy (BP-113); clause 3.3 and clause 11.2.6 describe the same naming pattern from two locations (clause 3.3 frames it as a last-resort breaking-change-avoidance strategy; clause 11.2.6 frames it as the concrete "how" for replacing one TypeDefinition).

## Source

- [OPC 11030 v1.03.03, clause 11.2.6](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.6)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
