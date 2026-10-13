---
id: "BP-110"
title: "Strategy: compatible mandatory additions via subtype + new Conformance Unit/Profile"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3"]
---

# BP-110 - Strategy: compatible mandatory additions via subtype + new Conformance Unit/Profile

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

One strategy to avoid breaking changes while still adding mandatory elements: create Subtypes carrying the new mandatory elements, and create new Conformance Units/Profiles that require use of those Subtypes. An old Client still works with a new Server; a new Client may additionally be designed to accept the old types too, or may choose not to support old Servers  -  a Client-developer decision. The document notes that subtyping one type may cascade into needing to change other types that use it.

## Applicability

Companion Specification evolution strategy.

## Exceptions and evidence limits

N/A (this is itself one of the approved alternatives referenced at BP-033).

## Audit

**NodeSet XML:** Confirm new mandatory elements only appear on new Subtypes, with corresponding new Conformance Units/Profiles defined.

**Document:** Review the specification's conformance-unit/profile definitions for the new Subtype.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (recommended strategy, one of several)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
