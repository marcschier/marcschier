---
id: "BP-184"
title: "Avoid implying AddressSpace changes via writing a count/number Variable"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["8.3"]
strength: "SHOULD NOT"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.3"]
---

# BP-184 - Avoid implying AddressSpace changes via writing a count/number Variable

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

A Server could expose, e.g., a `NumberOfSubmodules` Variable plus one Object per submodule, such that writing the count implicitly adds/removes submodule Objects. This is limited: it's unclear which instance should be deleted when the count decreases, and newly-added instances lack any configuration (so need default values and likely later adjustment). In general, this approach is not recommended.

## Applicability

AddressSpace configuration-change mechanism design.

## Exceptions and evidence limits

See BP-185 for the one documented carve-out.

## Audit

**NodeSet XML:** Flag a Variable whose documented semantic is "count of X" sitting alongside a matching set of X-typed Objects, where writing the count is the stated mechanism for adding/removing those Objects.

**Document:** Review specification text for this pattern.

**Assessment:** Semantically reviewable.

**Source wording:** SHOULD NOT (implied default; the document calls this "in general... not recommended")

## Source

- [OPC 11030 v1.03.03, clause 8.3](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/8.3)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
