---
id: "BP-220"
title: "Prefer a new NamespaceUri over deprecation-plus-new-mechanism, except for small changes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.3.1"]
strength: "SHOULD"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1"]
---

# BP-220 - Prefer a new NamespaceUri over deprecation-plus-new-mechanism, except for small changes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Marking a Node deprecated within a Companion Specification is less useful there than in the base specification, because a deprecated Node in an already-released NamespaceUri can never actually be removed (cross-ref BP-076). A Companion Specification may still define a new mechanism for some functionality and deprecate the old one without a breaking change  -  giving Clients a hint of a better path  -  but Clients must still be able to use the old (deprecated) mechanism if they need to support older Companion Specification versions, and a Server may need to support both to serve old Clients (if the deprecated Node is Mandatory, see BP-221). Creating a new NamespaceUri instead (cross-ref clause 3.3/clause 11.3) more cleanly signals exactly what a given Server/Client supports, at the cost of a transition period where a product may need to support both NamespaceUris. For Companion Specifications, it is therefore recommended to create a new NamespaceUri with the new mechanism rather than deprecating in place  -  **except** for small changes, such as deprecating a single optional InstanceDeclaration (and any DataTypes/ObjectTypes/VariableTypes used only by that InstanceDeclaration).

## Applicability

Companion Specifications introducing a replacement mechanism for existing functionality.

## Exceptions and evidence limits

Explicitly stated: small changes (a single optional InstanceDeclaration and its exclusively-used supporting types) may still use in-place deprecation rather than a new NamespaceUri.

## Audit

**NodeSet XML:** For a documented new-mechanism-replaces-old-mechanism change, check whether its scope matches the "small change" exception (single optional InstanceDeclaration + exclusively-used types) to determine whether in-place deprecation or a new NamespaceUri was the expected approach.

**Document:** Review the specification's stated rationale for choosing deprecation vs. a new NamespaceUri.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD, with an explicit stated exception

## Source

- [OPC 11030 v1.03.03, clause 14.3.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
