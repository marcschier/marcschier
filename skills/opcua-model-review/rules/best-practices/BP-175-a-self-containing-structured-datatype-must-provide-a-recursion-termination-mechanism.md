---
id: "BP-175"
title: "A self-containing Structured DataType must provide a recursion-termination mechanism"
spec: "OPC 11030"
version: "1.03.03"
clauses: ["7.10"]
strength: "MUST"
targets: ["nodeset", "document"]
check: "manual"
authority: "guidance"
sources: ["https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10"]
---

# BP-175 - A self-containing Structured DataType must provide a recursion-termination mechanism

**Authority:** OPC 11030 is a non-mandatory whitepaper. Its own wording is retained below; a deviation is advisory unless a normative specification or an explicitly adopted policy establishes a requirement.

## Rule

If a Structured DataType contains itself in a field (direct self-reference by DataType is not possible; only indirect containment, e.g., via an array, is), it must provide a way to end the recursion: either an optional field, an array of the (potentially indirectly) recursive DataType that is allowed to be empty, or a mandatory field whose DataType permits a NULL value. Implementations constructing such values must guard against infinite construction loops, and recipients of potentially recursive values should cap the recursion depth they support. The document separately notes that a self-containing Structured DataType lacking such an indirection (and not also allowing subtypes) will cause code-generation problems.

## Applicability

Structured DataTypes that unavoidably contain themselves (directly or indirectly) in a field.

## Exceptions and evidence limits

None stated beyond providing one of the listed termination mechanisms.

## Audit

**NodeSet XML:** For a Structure field whose DataType is (indirectly) the enclosing Structure itself, confirm the field is optional, is an empty-allowed array, or is a NULL-permitting mandatory field.

**Document:** Review self-containing structure definitions for the termination mechanism used.

**Assessment:** Static-checkable (termination mechanism presence); the depth-guarding recommendation is Runtime-only.

**Source wording:** MUST (termination mechanism) / SHOULD (implementation-side depth guarding)

## Source

- [OPC 11030 v1.03.03, clause 7.10](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.10)

Apply the [assessment policy](../README.md#assessment-policy). Permissions, examples, and conditional guidance are not unconditional prohibitions.
