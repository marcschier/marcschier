---
id: "BP-221"
title: "A Mandatory deprecated Node still requires permanent Server support"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["14.3.1"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1"]
---

# BP-221 - A Mandatory deprecated Node still requires permanent Server support

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If the deprecated Node is Mandatory (rather than Optional), Servers must continue supporting the old, deprecated mechanism indefinitely, even if no Client actually uses it anymore  -  because BP-076 still requires the Node to remain, and it being Mandatory means every conformant instance must still carry it.

## Applicability

Mandatory Nodes marked deprecated within an existing NamespaceUri.

## Exceptions and evidence limits

None stated  -  this is presented as an inescapable consequence.

## Audit

**NodeSet XML:** For a Mandatory Node marked `IsDeprecated`, confirm it remains Mandatory (not silently demoted to Optional, which would itself be a separate BP-topic breaking change) in subsequent versions.

**Document:** Review deprecation notices for Mandatory Nodes.

**Assessment:** Static-checkable (cross-ref BP-076/BP-108's general attribute-change caution).

**Source wording:** MUST (consequence)

## Source notes

This is a direct corollary of BP-076 (cannot remove) applied to the Mandatory+deprecated combination specifically; recorded separately because the consequence ("Server must support it forever") is explicitly called out at this location.

## Source

- [OPC 11030 v1.03.03, clause 14.3.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/14.3.1)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
