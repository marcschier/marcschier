---
id: "BP-033"
title: "Approved alternatives for introducing new mandatory functionality"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.1"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.1"]
---

# BP-033 - Approved alternatives for introducing new mandatory functionality

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

To add mandatory functionality without breaking compatibility, the document lists three options: (1) create a new Subtype that carries the mandatory InstanceDeclaration; (2) create a new, independent type unrelated to the old one; or (3) add the InstanceDeclaration as Optional and define a Profile/Conformance Unit that requires it.

## Applicability

Same scope as BP-032.

## Exceptions and evidence limits

N/A (these are the exceptions/remediations to BP-032).

## Audit

**NodeSet XML:** Confirm any "new mandatory" element observed in a diff (per BP-032) appears only on a *new* Subtype/type Node, not retrofitted onto the pre-existing type.

**Document:** Confirm the specification documents which of the three strategies was used for any new mandatory capability.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (three alternative, non-exclusive remediation patterns)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.2.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
