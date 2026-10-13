---
id: "BP-066"
title: "Adding argument metadata is permitted without changing mandatory/optional status"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.11"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11"]
---

# BP-066 - Adding argument metadata is permitted without changing mandatory/optional status

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

It is allowed to add metadata to an existing Method argument (worked example: an `EngineeringUnits` Property via a `HasArgumentDescription` Reference, as illustrated in clause 5). This does not extend to changing an argument from mandatory to optional or vice versa.

## Applicability

Existing Method Arguments.

## Exceptions and evidence limits

Explicitly excludes mandatory/optional status changes.

## Audit

**NodeSet XML:** Confirm a `HasArgumentDescription`-referenced metadata Node was added without any change to the Argument's own entry in `InputArguments`/`OutputArguments`.

**Document:** Review spec text for added per-argument metadata descriptions.

**Assessment:** Static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.11](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.11)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
