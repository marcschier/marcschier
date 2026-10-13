---
id: "BP-183"
title: "Avoid relying on the generic NodeManagement Services for configuration-driven AddressSpace changes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.2"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.2"]
---

# BP-183 - Avoid relying on the generic NodeManagement Services for configuration-driven AddressSpace changes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The OPC 10000-4 NodeManagement Services (AddNodes/DeleteNodes/AddReferences/DeleteReferences) might seem an obvious fit for AddressSpace configuration changes, but the document identifies three practical problems: they require specifying every Attribute per the strict OPC UA meta-model (unsuitable if the Server needs extra non-AddressSpace configuration data, e.g. a fieldbus address); they provide no transactional context (separate calls per Node/Reference add/remove, unsuitable when a change needs atomicity); and they carry no information about *where* it is actually allowed to add/remove Nodes (fully generic, no placement restrictions). Therefore, using the NodeManagement Services is, in most cases, not the best approach.

## Applicability

AddressSpace configuration-change mechanism design.

## Exceptions and evidence limits

None stated; "in most cases" leaves room for cases where none of the three problems apply, though no such case is detailed.

## Audit

**NodeSet XML:** Not directly checkable from a static NodeSet (this concerns which *mechanism* a Server chooses to expose/rely on for runtime configuration, not the reference NodeSet's own structure).

**Document:** Review specification text for the configuration-change mechanism it recommends/specifies; flag reliance on bare NodeManagement Services for anything beyond trivial generic tooling.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD NOT

## Source

- [OPC 11030 v1.03.03, clause 8.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
