---
id: "BP-185"
title: "Exception: writing an array may create/delete its exposed sub-variable entries"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.3"]
---

# BP-185 - Exception: writing an array may create/delete its exposed sub-variable entries

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

As a specific, narrower exception to BP-184, a Server may expose array elements as sub-variables (cross-ref clause 7.6/BP-158) such that writing the array causes creation/deletion of those sub-variables  -  using either the `ExposesItsArray` ModellingRule (as OPC 10000-5 does for diagnostics information) or `HasStructuredComponent` References.

## Applicability

Arrays exposed with individually-addressable sub-variable entries.

## Exceptions and evidence limits

This is itself the carve-out from BP-184's general discouragement.

## Audit

**NodeSet XML:** For such arrays, confirm the sub-variable exposure mechanism is one of `ExposesItsArray`/`HasStructuredComponent` (cross-ref BP-159's check).

**Document:** Review specification text describing array-write semantics.

**Assessment:** Static-checkable (mechanism presence).

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 8.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
