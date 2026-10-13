---
id: "BP-194"
title: "Prefer composition over inheritance when depending on another Companion Specification's types"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["10.2"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.2"]
---

# BP-194 - Prefer composition over inheritance when depending on another Companion Specification's types

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Because clause 3's backward-compatibility rules guarantee that a depended-upon Companion Specification's future versions won't break existing consumers, depending on another Companion Specification is generally safe. However, if the upstream specification later adds a useful feature by creating a Subtype, a dependent model that reused the original type via **inheritance** (defining its own Subtype of the reused type) cannot easily pick up that new upstream Subtype's feature, because its own Subtype is still derived from the original (non-extended) type (illustrated in Figure 9). If the dependent model instead reuses the upstream type via **composition** (embedding it as a component, illustrated in Figure 10), any instance of the dependent model's type can use the new upstream Subtype (and thus the new feature) without any change to the dependent model at all; the dependent model could also optionally define its own Subtype that specifically requires the new upstream Subtype as its component. Therefore, composition is recommended over subtyping when reusing concepts from another Companion Specification, where feasible.

## Applicability

Any model (Companion Specification or vendor) reusing types defined by a separate, independently-evolving Companion Specification.

## Exceptions and evidence limits

The document notes composition does not perfectly solve this in every case  -  e.g., when the reused type is also used elsewhere in the same dependent model and the new feature should be available there too, composition would require inverse-browsing to reach back to the instance that has the new capability, which is awkward.

## Audit

**NodeSet XML:** Flag a model's TypeDefinition that uses `HasSubtype` against an externally-defined (different-Namespace) Companion Specification type, as a candidate for reconsideration toward a composition (component-Reference) based design instead.

**Document:** Review the specification's stated reuse mechanism (inheritance vs. composition) for externally-defined types.

**Assessment:** Static-checkable (detecting cross-Namespace `HasSubtype` usage) / semantically reviewable (whether composition was feasible/preferable in context).

**Source wording:** SHOULD

## Source notes

Figure references: https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.2#fig_9_reusing-extended-companion-specifications-by-inheritance (Figure 9) and https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.2#fig_10_reusing-extended-companion-specifications-by-composition (Figure 10).

## Source

- [OPC 11030 v1.03.03, clause 10.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/10.2)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
