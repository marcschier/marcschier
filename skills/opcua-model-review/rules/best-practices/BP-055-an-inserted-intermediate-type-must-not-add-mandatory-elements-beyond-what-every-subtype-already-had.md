---
id: "BP-055"
title: "An inserted intermediate type must not add mandatory elements beyond what every subtype already had"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["3.2.9"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9"]
---

# BP-055 - An inserted intermediate type must not add mandatory elements beyond what every subtype already had

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a new intermediate type is inserted anyway (per BP-054's "absolutely necessary" carve-out), it shall not add mandatory InstanceDeclarations unless those had already been defined (as mandatory) on every one of its new subtypes beforehand.

## Applicability

Conditional on choosing to insert an intermediate type per BP-054.

## Exceptions and evidence limits

None beyond the stated precondition.

## Audit

**NodeSet XML:** For an inserted type, confirm every Mandatory/MandatoryPlaceholder child it defines was already present (and Mandatory) on all of its subtypes in the prior version.

**Document:** Compare the inserted type's mandatory members against what each subtype already required.

**Assessment:** Impossible without dependencies (requires prior version); otherwise static-checkable.

**Source wording:** MUST NOT

## Source

- [OPC 11030 v1.03.03, clause 3.2.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.9)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
