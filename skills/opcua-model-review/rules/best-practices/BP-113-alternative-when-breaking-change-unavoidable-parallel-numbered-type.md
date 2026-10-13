---
id: "BP-113"
title: "Alternative when breaking change unavoidable: parallel numbered type"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.3"]
strength: "MAY"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3"]
---

# BP-113 - Alternative when breaking change unavoidable: parallel numbered type

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

As an alternative to minting a new Namespace, new types may be created independent of the old ones when needed (worked example: `DeviceType2` alongside `DeviceType`), which also allows removing mandatory elements that proved problematic. The document notes this may cascade: depending how many types are exchanged, old Clients may or may not do anything reasonable with a new Server, and new Clients may need to support both the old and new type if old Servers must still be supported.

## Applicability

Companion Specifications facing an unavoidable breaking change, preferring to stay within the existing NamespaceUri.

## Exceptions and evidence limits

N/A (alternative to BP-112, not a sub-case of it).

## Audit

**NodeSet XML:** Confirm the new parallel type is additive (old type retained per BP-076) rather than a modification of the old one.

**Document:** Review the specification's description of the new type's relationship to the old one.

**Assessment:** Static-checkable (retention of old type) / semantically reviewable (overall strategy soundness).

**Source wording:** MAY

**Permission guard:** This is an allowed option, not a requirement to choose it. Check its stated conditions only when the model uses the option; its absence is not a deviation.

## Source notes

Closely related to clause 11.2.6's TypeDefinition-replacement guidance (BP-206); clause 3.3 and clause 11.2.6 describe the same naming pattern from two locations.

## Source

- [OPC 11030 v1.03.03, clause 3.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
