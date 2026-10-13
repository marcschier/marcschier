---
id: "BP-114"
title: "Do not define additional StatusCodes"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["4"]
strength: "MUST NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/4"]
---

# BP-114 - Do not define additional StatusCodes

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

The base OPC UA specification defines the complete set of StatusCodes. It is not allowed for Companion Specifications or vendors to define additional StatusCodes. For more specific per-attribute/per-value status detail, OPC UA provides the DiagnosticInfo mechanism (OPC 10000-4).

## Applicability

Companion Specifications and vendor information models, generally  -  this is **not** conditioned on NamespaceUri reuse/versioning the way clause 3's rules are; it applies even to a brand-new Namespace/version.

## Exceptions and evidence limits

See BP-115 (the sole sanctioned path to get a genuinely new StatusCode).

## Audit

**NodeSet XML:** Not directly checkable from NodeSet XML alone (StatusCodes are returned at runtime/in Method call results, not declared as Nodes); review would need to inspect any custom status-code constant definitions in accompanying source/SDK artifacts, which are outside a NodeSet file.

**Document:** Scan specification prose for any table purporting to define new, non-base StatusCodes.

**Assessment:** Semantically reviewable (prose); impossible without dependencies for a NodeSet-only audit (StatusCode usage is not itself an XML-declared construct in the same way Nodes are).

**Source wording:** MUST NOT

## Source notes

Distinct in character from clause 3's rules: this is a general prohibition against inventing a *fixed OPC UA mechanism* (the StatusCode value space itself), not a backward-compatibility rule about not breaking an existing release.

## Source

- [OPC 11030 v1.03.03, clause 4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/4)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
