---
id: "BP-198"
title: "Remediation for needing new Enumeration values: deprecate-and-replace (ideally with an extensible pattern instead)"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.3"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.3"]
---

# BP-198 - Remediation for needing new Enumeration values: deprecate-and-replace (ideally with an extensible pattern instead)

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Adding new Enumeration DataType values is not allowed (cross-ref clause 3.2.4/BP-036). Ideally, an extensible approach per clause 7.12 (BP-178-BP-180) would already have been used, avoiding the problem. If not, the only remaining option is to deprecate the old Enumeration (and all its usages across Variables, Method signatures, Structured DataTypes, etc.) and define a new Enumeration (preferably using an extensible approach this time)  -  explicitly flagged as "very cumbersome," especially where the DataType has been used in many places.

## Applicability

Companion Specifications needing to extend an already-released, non-extensible Enumeration DataType.

## Exceptions and evidence limits

None stated; this is the fallback when extensibility was not designed in from the start.

## Audit

**NodeSet XML:** Not independently mechanical; confirm (if this path is taken) that the old Enumeration is marked deprecated (cross-ref clause 14) rather than silently mutated.

**Document:** Review the specification's migration narrative for the deprecated/replacement Enumeration pair.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD (remediation guidance)

## Source

- [OPC 11030 v1.03.03, clause 11.2.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
