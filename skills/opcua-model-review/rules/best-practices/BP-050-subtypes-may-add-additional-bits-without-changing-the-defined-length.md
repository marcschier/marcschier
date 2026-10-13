---
id: "BP-050"
title: "Subtypes may add additional bits without changing the defined length"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.8"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8"]
---

# BP-050 - Subtypes may add additional bits without changing the defined length

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a specification intends to extend an OptionSet-DataType-based OptionSet, it needs to define Subtypes with additional bits; the initially-defined bit length cannot be changed in any Subtype.

## Applicability

Same as BP-047.

## Exceptions and evidence limits

The bit-length constraint (BP-052) bounds this permission.

## Audit

**NodeSet XML:** Confirm a Subtype OptionSet DataType's declared length (per its `DataTypeDefinition`) matches its supertype's length, while its additional `OptionSetValues` entries occupy only previously-unused bit positions.

**Document:** Review spec text describing the subtype's extension.

**Assessment:** Static-checkable.

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.8](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.8)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
