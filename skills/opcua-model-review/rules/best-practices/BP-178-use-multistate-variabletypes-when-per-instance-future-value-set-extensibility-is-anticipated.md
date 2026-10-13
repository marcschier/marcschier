---
id: "BP-178"
title: "Use MultiState VariableTypes when per-instance/future value-set extensibility is anticipated"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.12.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.3"]
---

# BP-178 - Use MultiState VariableTypes when per-instance/future value-set extensibility is anticipated

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

`MultiStateDiscreteType`/`MultiStateValueDiscreteType` behave like an enumeration but allow a different value set per instance, which many Companion Specifications use specifically to let future versions and vendors extend the allowed values. Because (purely from the model) vendors could otherwise substitute entirely different value sets, the specification choosing this pattern must explicitly state in text which predefined values are expected to be used. This approach inherently requires Clients to inspect the instance's own enumeration values rather than relying on built-in knowledge, and is therefore appropriate specifically when extensibility is expected.

## Applicability

Discrete-value design anticipating future/vendor extensibility.

## Exceptions and evidence limits

None stated.

## Audit

**NodeSet XML:** For Variables typed `MultiStateDiscreteType`/`MultiStateValueDiscreteType`, confirm an `EnumStrings`/`EnumValues` default value set is present and that specification text documents the expected predefined values.

**Document:** Review specification text for the required explicit statement of expected predefined values.

**Assessment:** Static-checkable (type/value-set presence) combined with semantically reviewable (documentation adequacy).

**Source wording:** SHOULD (pattern choice) / MUST (companion documentation obligation once chosen)

## Source

- [OPC 11030 v1.03.03, clause 7.12.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.12.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
