# Source notes and adjudication limits

Read these notes before turning a search hit or apparent source conflict into
a violation. Source notes are evidence limits, not permission to silently
pick whichever wording makes a check pass.

## ModellingRule placeholder transitions

Part 3 v1.05.06 [6.4.4.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.2)
Table 21 permits OptionalPlaceholder-to-MandatoryPlaceholder promotion.
The Object/Variable text in
[6.4.4.4.4](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/6.4.4.4.4)
says an overriding OptionalPlaceholder remains OptionalPlaceholder.
Methods have their own explicitly different transitions. Preserve this
distinction in P3-091 and P3-102; uncertain Object/Variable promotion requires
source clarification, not a universal transition matrix.

## Refinement and subtype-restriction bits

The NoSubDataTypes passages in
[5.8.5.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.5.2)
and the example in
[5.8.6.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.6.1)
need careful comparison with its general definition in
[8.58](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.58).
Do not infer a bit-level violation from an isolated example where the stated
abstract-type behavior conflicts with the general subtype-exclusion meaning.
The structural restrictions on context, owner count, exact DataType matching,
rank, and allowed variants are still assessed independently.

## StructureField length metadata

[8.51](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/8.51)
mentions LocalizedText in MaxStringLength applicability but its subsequent
exclusion sentence mentions only String/ByteString. Keep the precise evidence
and seek clarification before rejecting a LocalizedText length restriction.

## General Reference rules and explicit standard extensions

The general HasComponent endpoint list in
[7.7](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/7.7)
must be read with the explicit Method-to-Variable metadata extension in
[5.7.2](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.7.2).
Likewise, the general DataType outgoing-Reference restrictions in
[5.8.3](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/5.8.3)
must account for the refinement relationships introduced later in Part 3.
Apply the specific standard definition; do not treat these as a permission for
custom ReferenceTypes to relax inherited constraints.

## Multiple inheritance

Part 3
[4.10.1](https://reference.opcfoundation.org/specs/OPC-10000-3/v1.05.06/4.10.1)
explicitly states that it does not restrict ObjectType hierarchies to single
inheritance, but defines only single-inheritance semantics. OPC 11030
[7.2.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.2.4)
uses a stronger single-inheritance premise for its composition recommendation.
BP-128 is advice; it is not a blanket ObjectType prohibition. P3-055's
ReferenceType single-inheritance requirement remains normative.

## PropertyType source attribution

The explicit no-subtyping requirement is in
[OPC 10000-5 v1.05.06, 7.3](https://reference.opcfoundation.org/specs/OPC-10000-5/v1.05.06/7.3).
Part 3 requires exact PropertyType on Properties; OPC 11030
[7.3.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.3.2)
restates the prohibition. Use P5-001 for its normative provenance.

## OPC 11030 authority and inferred examples

OPC 11030 [1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/1)
identifies the entire document as a non-mandatory whitepaper. Preserve the
wording and conditional scope of its individual rules without treating every
"must" as an independent normative OPC UA requirement.

The literal `Status` argument naming pattern in BP-120 is inferred from the
worked example in
[5.2](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/5.2),
not an explicit naming prohibition. A MAY alternative such as file transfer
or a deletion-Method pattern cannot require every model to use that alternative.

## OPC 11030 limits and underspecified guidance

DisplayName naming recommendations are deferred by the guide itself in
[2.1.1](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.1);
do not invent a missing convention. Part 3's separate length and localization
rules still apply.

BP-019's cross-namespace name avoidance in
[2.1.4](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/2.1.4)
is explicitly best-effort, not global name uniqueness.

BP-075's "inside the hierarchy" restriction in
[3.2.15](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/3.2.15)
is less precisely scoped than the neighboring hierarchy-insertion clauses.
Review it against the actual old/new hierarchy rather than inventing an
unconditional leaf-subtype ban.

BP-172's 32-optional-field statement in
[7.9](https://reference.opcfoundation.org/specs/OPC-11030/v1.03.03/7.9)
does not cite its originating encoding constraint. Verify the applicable
Part 6 encoding before reporting it as a normative encoding violation.
The same clause distinguishes optional-field and subtyped-value StructureTypes:
its statement is not a ban on the BaseDataType/Structure field mechanisms
explicitly allowed by Part 3 and BP-170.

The broad writable-Attribute rationale in BP-148 must not override explicit
read-only Attributes such as Part 3's UserRolePermissions. BP-018 uses a broad
type-naming category; Part 3's defined term TypeDefinitionNode means ObjectType
or VariableType, not a DataType usable as a HasTypeDefinition target.

## Official publication precedence

These summaries follow the linked HTML editions retrieved on 2026-10-13.
The publisher states that its official publication controls if it differs from
the website. No independent PDF equivalence is claimed. Consult the official
publication or published errata before resolving a material discrepancy.
