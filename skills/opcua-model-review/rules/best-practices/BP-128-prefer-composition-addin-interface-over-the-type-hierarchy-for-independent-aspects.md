---
id: "BP-128"
title: "Prefer composition (AddIn/Interface) over the type hierarchy for independent aspects"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.2.4"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.4"]
---

# BP-128 - Prefer composition (AddIn/Interface) over the type hierarchy for independent aspects

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The document recommends creating common base ObjectTypes for shared semantics/substructure, but cautions against very deep type hierarchies. As its stated premise, it says an ObjectType can be derived from only one supertype, so the type hierarchy "can only be organized by one aspect." Its consequent recommendation: subtyping should be used to refine an ObjectType's main characteristic, while additional, independent aspects should instead be added via composition  -  either an **AddIn** (a sub-Object of a standardized type attached under a defined `DefaultInstanceBrowseName`) or an **Interface** (a substructure deployed directly on the ObjectType without a grouping Object). Worked example: a `SensorType`/`TemperatureSensorType`/`FlowSensorType` subtype chain for the device-kind "aspect," with an independent "lockable" aspect added via an AddIn/Interface rather than a second supertype.

## Applicability

ObjectType design when more than one independent aspect needs to be expressed.

## Exceptions and evidence limits

See BP-129 for the further nuance when two or more independently-composable capabilities must coexist on one instance.

## Audit

**NodeSet XML:** Not mechanically checkable as a single structural test; a reviewer can flag ObjectTypes whose documentation describes two unrelated "aspects" being handled purely through subtyping as a candidate for using composition instead.

**Document:** Review whether independent aspects are modelled via AddIn/Interface rather than forced into the single-supertype chain.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD

## Source notes

**Accuracy-sensitive item (flagged per parent instruction).** clause 7.2.4 states, as its own premise/justification for this recommendation: "OPC UA only supports single inheritance (multiple inheritance is not supported), thus an ObjectType can be derived from only one supertype" (and later in the same clause: "even the above-mentioned example can lead to problems without multiple inheritance"). This extraction reports that sentence strictly as **OPC 11030's own stated premise, scoped to ObjectTypes, at clause 7.2.4**  -  it is explicitly **not** independently verified here against OPC 10000-3 (out of scope for this extraction per task instructions), and per guidance received, OPC 10000-3 is understood to define inheritance *semantics* specifically for the single-inheritance case rather than necessarily issuing a general ban elsewhere. Accordingly, **the extracted rule (BP-128) is framed as an 11030-original SHOULD-level composition recommendation**, not as a restated MUST-NOT prohibition on multiple inheritance  -  this file does not assert "OPC UA prohibits multiple inheritance" as an independently-confirmed fact. Exact source location for the quoted premise: clause 7.2.4, paragraph 2 and paragraph 6.

Part 3 clause 4.10.1 explicitly does not impose a general multiple-inheritance prohibition. Keep this composition recommendation separate from ReferenceType single inheritance in [P3-055](../part3/P3-055-use-single-inheritance-for-referencetypes.md).

## Source

- [OPC 11030 v1.03.03, clause 7.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
