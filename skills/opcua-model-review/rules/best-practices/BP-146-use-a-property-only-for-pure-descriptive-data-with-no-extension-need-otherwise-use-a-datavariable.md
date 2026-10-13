---
id: "BP-146"
title: "Use a Property only for pure descriptive data with no extension need; otherwise use a DataVariable"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.3.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.2"]
---

# BP-146 - Use a Property only for pure descriptive data with no extension need; otherwise use a DataVariable

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

OPC UA distinguishes lightweight Properties from DataVariables. Properties describe the Node they belong to, are always typed `PropertyType`, are referenced via `HasProperty`, have their semantic defined by their BrowseName, and are leaves of the hierarchy (cannot source further hierarchical References, so cannot themselves carry Properties). Property values typically change rarely and are usually read once rather than subscribed to. DataVariables (typed `BaseDataVariableType` or a subtype) carry none of these restrictions. The recommendation: use a Property when it is semantically clear the Variable merely describes characteristics of its owning Node, with no need to add further information to it (including as an extensibility mechanism in vendor models or other Companion Specifications); otherwise use a DataVariable.

## Applicability

Any Variable-design decision between Property and DataVariable framing.

## Exceptions and evidence limits

See BP-147 (a Variable that itself needs Properties must be a DataVariable regardless of semantic fit).

## Audit

**NodeSet XML:** For any `UAVariable` reached via a `HasProperty` Reference, confirm its `TypeDefinition` is `PropertyType` (ns=0;i=68) and that it has no outgoing hierarchical References (including no `HasProperty` of its own).

**Document:** Review the semantic rationale for Property-vs-DataVariable choices in specification text.

**Assessment:** Static-checkable (the structural leaf/TypeDefinition facts); the "was this the right semantic choice" judgement is semantically reviewable.

**Source wording:** SHOULD

## Source notes

**Accuracy-sensitive item (flagged per parent instruction).** clause 7.3.2 states, as a parenthetical: Properties "are always of VariableType PropertyType (**which is not allowed to be subtyped**)." This extraction reports that claim exactly as it appears, cited precisely to clause 7.3.2, and does **not** independently confirm (nor deny) which base-specification clause (Part 3 and/or Part 5, per the parent's own separate verification) normatively establishes PropertyType's non-subtypability  -  that determination is explicitly out of scope here. The mechanical XML check above ("is there any `UAVariableType` claiming `PropertyType` as its supertype via `HasSubtype`") is independent of resolving that sourcing question: it only tests the observable structural claim 11030 makes, not its ultimate normative basis. Exact source location: clause 7.3.2, paragraph 2.

The normative PropertyType-subtyping prohibition is independently verified in [P5-001](../supplement/P5-001-do-not-subtype-propertytype.md).

## Source

- [OPC 11030 v1.03.03, clause 7.3.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
