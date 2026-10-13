---
id: "BP-196"
title: "Mandatory additions require a Subtype or an Optional-plus-Conformance-Unit pattern"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.1"]
---

# BP-196 - Mandatory additions require a Subtype or an Optional-plus-Conformance-Unit pattern

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If InstanceDeclarations need to be added as mandatory, either a Subtype must be created carrying the mandatory InstanceDeclaration, or the InstanceDeclaration is added only as Optional and a new Conformance Unit is defined requiring its presence.

## Applicability

Same as BP-195, mandatory-addition case.

## Exceptions and evidence limits

None  -  these are the two sanctioned paths.

## Audit

**NodeSet XML:** Same diff approach as BP-032/BP-033.

**Document:** Confirm the specification documents which path was used.

**Assessment:** Impossible without dependencies; otherwise static-checkable.

**Source wording:** MUST (one of two exclusive remediation paths)

## Source notes

This rule mirrors BP-032/BP-033 (clause 3.2.1), restated at clause 11.2.1 in the context of "how to extend."

## Source

- [OPC 11030 v1.03.03, clause 11.2.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
