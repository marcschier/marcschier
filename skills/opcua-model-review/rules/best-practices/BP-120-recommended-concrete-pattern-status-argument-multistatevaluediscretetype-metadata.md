---
id: "BP-120"
title: "Recommended concrete pattern: \"Status\" argument + MultiStateValueDiscreteType metadata"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["5.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_2_somemethod-method-arguments", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_3_somemethod-method-addressspace-definition", "https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_4_sometype-additional-attributes"]
---

# BP-120 - Recommended concrete pattern: "Status" argument + MultiStateValueDiscreteType metadata

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The worked example names this trailing Argument literally `Status` (not an angle-bracketed placeholder, unlike `<SomeInput>`/`<SomeOutput>`, implying "Status" is the recommended literal name) and documents its possible values by attaching, via a `HasArgumentDescription` Reference, a Mandatory Variable typed `MultiStateValueDiscreteType` whose `EnumValues` Property enumerates each code as `{value, displayName, description}` (e.g. `0/OK/Everything is OK`, `-1/E_FirstError/...`).

## Applicability

Methods implementing the BP-116 pattern, at the point of documenting the status argument's possible values.

## Exceptions and evidence limits

None stated; this is a worked example, not a separately phrased "shall"/"should" sentence, so the literal-naming inference ("Status") is based on the angle-bracket convention from clause 2.1.2 (BP-005) rather than an explicit naming statement in clause 5 itself  -  flagged as an inference, not a direct quote.

## Audit

**NodeSet XML:** For Methods following this pattern, confirm: (a) a Variable named `Status` referenced via `HasArgumentDescription` from the Method; (b) its `TypeDefinition` is `MultiStateValueDiscreteType`; (c) it carries Mandatory ModellingRule; (d) an `EnumValues` Property enumerates the codes.

**Document:** Review Method documentation tables for this structure (cf. Tables 2-4 in the source).

**Assessment:** Static-checkable.

**Source wording:** SHOULD

## Source notes

The inference that "Status" is a literal recommended name (not a placeholder) is based on the angle-bracket convention documented elsewhere (clause 2.1.2) and contextual contrast within the same example, not an explicit standalone statement in clause 5. Recorded as a reasoned inference, flagged accordingly.

## Source

- [OPC 11030 v1.03.03, clause 5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_2_somemethod-method-arguments)
- [OPC 11030 v1.03.03, clause 5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_3_somemethod-method-addressspace-definition)
- [OPC 11030 v1.03.03, clause 5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2#tbl_4_sometype-additional-attributes)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
