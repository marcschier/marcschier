---
id: "BP-176"
title: "Standardized server-bound Variables must be marked non-static in NamespaceMetadata"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.11"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.11"]
---

# BP-176 - Standardized server-bound Variables must be marked non-static in NamespaceMetadata

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

Most instances in an OPC UA Server depend on its configuration and are based on TypeDefinitions, but Companion Specifications sometimes define standardized Instances outright. Some of these are static entry points (e.g., the base specification's `Root`/`Objects` folders, or the Devices specification's `DeviceSet`). Others are standardized but server-bound Variables (e.g., the capability/diagnostic Variables defined in OPC 10000-5) that are not static. To work correctly when aggregated by another Server, these non-static standardized Variables/Nodes must be marked as such in the `NamespaceMetadata` Object of their Namespace.

## Applicability

Standardized, server-bound (non-fixed) Instances/Variables defined by a Companion Specification.

## Exceptions and evidence limits

Genuinely static entry-point Instances (e.g., fixed folders) are not subject to this marking requirement.

## Audit

**NodeSet XML:** For Nodes documented as server-bound/non-static standardized instances, confirm they are listed in the owning Namespace's `NamespaceMetadata` Object's non-static Node list/Property.

**Document:** Review specification text identifying which standardized Instances are server-bound versus fixed.

**Assessment:** Static-checkable (given the documented static/non-static classification).

**Source wording:** MUST

## Source

- [OPC 11030 v1.03.03, clause 7.11](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.11)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
