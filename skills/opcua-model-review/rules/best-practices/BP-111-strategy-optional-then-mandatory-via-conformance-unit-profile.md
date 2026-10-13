---
id: "BP-111"
title: "Strategy: optional-then-mandatory via Conformance Unit/Profile"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3"]
---

# BP-111 - Strategy: optional-then-mandatory via Conformance Unit/Profile

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A second strategy: add new components as Optional on the existing types, then make them mandatory via Conformance Units/Profiles  -  avoiding the need to create Subtypes at all. Old Clients work with new Servers; new Clients may work with old Servers if they do not require the new mandatory-by-profile things.

## Applicability

Companion Specification evolution strategy.

## Exceptions and evidence limits

N/A.

## Audit

**NodeSet XML:** Confirm new elements are Optional at the type level, with a Conformance Unit/Profile requiring their presence.

**Document:** Review the specification's conformance-unit/profile definitions.

**Assessment:** Semantically reviewable.

**Source wording:** MAY (recommended strategy)

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source

- [OPC 11030 v1.03.03, clause 3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
