---
id: "BP-199"
title: "Remediation for needing new Structure fields: Subtype, conditioned on subtype-permission at every usage site"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["11.2.4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.4"]
---

# BP-199 - Remediation for needing new Structure fields: Subtype, conditioned on subtype-permission at every usage site

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Adding new fields directly to a Structured DataType is not allowed (cross-ref clause 3.2.5/BP-039). A Subtype can be created with the additional fields, but whether it is actually usable depends on where the DataType is used: if used as a field inside another Structured DataType that does not state subtypes are allowed, the Subtype cannot be used there (cross-ref clause 7.9/BP-168); for a Variable, it depends on whether subtypes of the Variable's DataType are declared allowed; for a Method argument, the metadata may or may not permit subtypes, but an existing Method cannot be changed to *require* the Subtype (cross-ref clause 3.2.11/BP-065). Ideally, the structure would already have a built-in extension mechanism (cross-ref clause 7.9/BP-171). If not, a new Subtype must be created and all its usages replaced  -  again flagged as potentially very cumbersome.

## Applicability

Companion Specifications needing to extend an already-released Structured DataType.

## Exceptions and evidence limits

Depends entirely on the subtype-permission state of every usage site, as described above.

## Audit

**NodeSet XML:** For a proposed Subtype-based field addition, check each usage site's subtype-permission flag (cross-ref BP-169) before treating the Subtype as viable there.

**Document:** Review the specification's migration narrative.

**Assessment:** Semantically reviewable.

**Source wording:** MUST NOT (direct addition) / MAY (Subtype, conditionally)

## Source notes

This rule combines/cross-references clause 3.2.5, clause 7.9, and clause 3.2.11; recorded once here as the consolidated "how to extend" guidance, with component rules cited separately where they were first introduced.

## Source

- [OPC 11030 v1.03.03, clause 11.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/11.2.4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
