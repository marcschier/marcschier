# OPC UA specification prose guidance

This reference is the prose-style authority for `opc-spec-review` and its
comprehension-review companion. It is part of this package; a separate style
skill cannot replace it. It governs specification prose, not technical
decisions, Markdown dialect, table-renderer behavior or publisher-owned
presentation. Applicable normative sources and approved working-group
decisions govern technical facts. The target repository's authoring contract
and pinned Publisher govern syntax and composition.

The examples below are original and synthetic. They illustrate the guidance;
they do not authorize a technical change. The numbered rules are concise
operational checks. Preserve the safeguards in the final section when applying
them: style review must not silently lose information, narrow a contract, or
make an unapproved normative decision.

## Optional editing companion

Before the first authorized specification prose edit, if the user has not
already made this choice, use `ask_user` once for the agreed edit scope: offer
**Use `opc-ua-writing-style`** or **Keep the existing editing workflow
(default)**. In comprehension review the coordinator asks and records the
choice for the editor. Skip the question in findings-only, planning and
removal-audit modes, and continue without the companion if the user declines
or no answer is available. The choice does not grant edit permission or
broaden the scope.

On explicit opt-in, resolve `opc-ua-writing-style` through the host's skill
mechanism for the agent making the edits. If it is unavailable, report that
the optional pass was skipped and continue with this guidance rather than
installing it automatically. Use it for voice, paragraph breaks and
punctuation in approved specification edits.
Keep an existing `claudism-killer` pass as a separate cleanup step; do not add
one just because the user opts in. This guidance and its preservation audit
still apply, and the implementer guide keeps its separate writing workflow.

## Sentence purpose and placement

For each sentence in a normative clause, identify its purpose:

- A testable requirement, permission or recommendation, placed with the Node,
  Method or EventType it constrains.
- A definition of a type, child, field or argument.
- Context needed by the specification's intended reader to understand those
  items, including an explanation of the technology being modelled.

Question sentences that only repeat a source, explain rationale, walk through a
standard service, preview another clause or restate a table. Remove or
condense them only after the preservation audit establishes that their useful
facts remain accessible and their scope is unchanged. Dense, testable rules
are not verbosity merely because they are long.
Apply the informative-context decision below before removing connecting
explanations, examples or diagrams; concision does not mean normative-only prose.

Place optionality in ModellingRules, Conformance Units and Profiles, not prose
labels. Put shared requirements in a canonical location with references; keep
their full scope when relocating them. The overview orients the reader; put
behavior in the applicable type or Method clause. Generated namespace, NodeId
and Profile content belongs to the repository's supported generated clauses.

### Clause shapes

- **ObjectType, VariableType, DataType and ReferenceType:** identify what the
  type represents; add behavior only when needed to explain a multi-child or
  non-obvious contract; introduce the formal definition table; explain
  declared children, not inherited or interface-owned members. A Structure
  fields table follows the type definition.
- **Method:** state its purpose; describe server and caller requirements,
  preconditions, effects, atomicity and security; provide signature and
  argument descriptions; list established result codes and their conditions;
  include any supported AddressSpace table.
- **EventType:** state what it represents or when it is raised; describe the
  raise condition and newly defined or constrained fields; provide the
  definition and field descriptions.
- **Scope:** state what the document defines and for whom, briefly. Put version
  alignment and release status in the repository's supported front matter or
  change history.
- **Overview:** explain the model and its main relationships; include only
  necessary requirements and detail, with figures governed by the template.

These shapes guide organization; they do not justify moving generated or
authored content into a location where it is lost, inaccessible or narrower in
meaning.

## Informative context

Before removing material that connects normative clauses or explains the
modelled technology, give the user an explicit retention choice through the
host's question tool. Show located before/after excerpts, the reading gap the
removal would create, and proposed subsection placement. Ask one decision at a
time: retain the connecting material in an informative subsection of the
specification, or move suitable implementation teaching to the companion guide
when the specification remains understandable without it. Record the chosen
policy and its scope; apply an already approved policy without asking again
unless a materially different case falls outside it. Silence, unavailable
input or general rewrite approval is not consent to remove the material:
leave it unchanged and record the pending choice.

An informative subsection keeps the specification's existing audience.
It explains concepts, relationships and the modelled technology at the depth
that reader needs; it does not adopt the developer-booklet audience or writing
companions used for `implementer-guide.md`. Include supporting examples and
diagrams when they bridge understanding, not only when a requirement is
ambiguous. Keep these connected to the surrounding normative clauses rather
than collecting them in a distant appendix or relying on the guide.

Place the explanation before or alongside the first dependent concept, with
clear transitions back to the contract. Mark the subsection informative using
the repository's supported authoring convention and preserve example/diagram
captions, links and reading order. If the template or pinned Publisher cannot
express that distinction, report the conflict and seek a decision; do not
invent markup or delete the explanation to satisfy a layout rule.

Separate explanation from obligations in mixed passages. Required definitions,
conditions, exceptions, negative guarantees and other normative facts retain
their normative force and accessible normative homes; labelling a subsection
informative must not downgrade them. The informative-context decision takes
precedence over concision, placement and example-removal rules below, including
D1-D7, but never over technical authority or edit permission.

Reread the resulting specification forward, including each informative
subsection, example and diagram, without the implementer guide. Verify that
the intended reader can follow the normative contract and that no transition,
needed premise or normative fact was lost. Record the decision, exact retained
homes, publication evidence and any reading gap in the preservation audit.

## A. Terms and typography

### A1. Distinguish names, terms and literals

Use the target specification's semantic emphasis convention consistently for
defined terms and model names, including mentions in table cells. Reserve code
font for literal syntax or expressions, not merely for a name. Render Boolean
values as the spelling required by the applicable syntax.

**Example:** For a defined `Status` Property containing a Boolean, distinguish
the name (*Status*) from the literal `TRUE`; do not render the Property name
like a source-code token.

### A2. Keep defined-term spelling stable

Use one established spelling for each defined term throughout the edition.
Follow the target specification's glossary convention; do not silently change
an established term's casing or spacing.

**Example:** If the glossary defines “SourceIdentity”, use that same form in
later clauses rather than alternating among “source identity” and
“sourceIdentity”.

### A3. Make definitions name the concept

A glossary entry should identify the concept as a noun phrase. Put behavior or
requirements in the clause where they apply.

**Example:** Prefer “identifier assigned to a data source” as a definition
over “A SourceIdentity is the identifier assigned to a data source.”

### A4. Resolve terms before relying on them

Check that terms, identifiers and abbreviations are defined in the glossary,
table, or cited specification before readers need them. Reconcile every
definition with its normative uses, including scope and distinctions from
similar concepts.

**Example:** Define “ReplicaId” before a requirement uses it; if two roles have
different authority, define both rather than merging their entries.

### A5. Cite clauses without a section sign

Use the target's supported clause reference format. Do not insert a section
symbol as a substitute for a clause citation.

**Example:** Write “see 6.4” rather than “see §6.4”.

### A6. Give tables and figures stable, usable references

Ensure every table and figure has a caption and a text reference under the
target's publishing contract. Prefer supported generated-number references to
hard-coded numbers or positional phrases.

**Example:** In a fenced Publisher-Markdown sample, show
`listed in [](#tbl-example-definition)` as literal syntax; verify that the
actual target anchor exists before using it as a live document link.

### A7. Do not use italics only for emphasis

Use italics according to the specification's term and model-name convention,
not as general stress.

**Example:** Emphasize a defined *TransferMode* name consistently, but do not
italicize “only” in “The Client may only select a supported mode” to add
editorial emphasis.

## B. Normative language

### B1. Keep conformance labels out of headings

Do not label headings with parenthetical mandatory or optional status. State
normative force using the authorized model and conformance mechanisms.

**Example:** Use “Event Reporting”, not “Event Reporting (optional)”; express
support through the applicable Facet and Conformance Unit.

### B2. Model optional features through conformance

Express optional functionality in the applicable Conformance Unit and Profile,
not an informal prose label.

**Example:** Put the optional notification feature in its optional Facet
rather than adding “notifications are optional” to the type description.

### B3. Put conditional obligations in the relevant Facet

When support for a Facet makes a feature mandatory, express that condition in
the Facet's conformance definition. Do not make a declaration itself sound
unconditionally mandatory.

**Example:** Keep a Property's declaration Optional and list its required
behavior in the Facet that requires it.

### B4. Place requirements with the constrained element

Put a requirement in the clause for the Node or Method it constrains. For
genuinely cross-cutting behavior, use one canonical home and references
without reducing its scope.

**Example:** Put the access precondition for `ResetCache` in that Method's
clause; retain a common security rule in its shared home when it covers several
Methods.

### B5. Make requirements verifiable

A requirement needs an observable criterion, such as a CTT check or inspection
of the specified AddressSpace. If its test is unclear, flag the gap rather
than inventing a test.

**Example:** “The Server shall expose the configured limit in the
MaxItems Property” is inspectable; “The Server shall provide a robust
configuration” is not.

### B6. Avoid statements that merely disclaim an obligation

A sentence that says a feature is not required may be redundant when the
conformance model already settles it. Before removing it, check whether it also
states an implementer-relevant absence, prohibition, error result or scope
condition; preserve such facts in accessible published text.

**Example:** A redundant “AuditDetails is not required by Facet A” may be
removed only if the Facet definitions fully resolve the question; retain a
separate requirement that an error leaves the AddressSpace unchanged.

### B7. Prefer direct definitions, but preserve meaningful negatives

Define what an entity is rather than relying on an unhelpful comparison.
Negative wording may nevertheless state a real contract, such as a
prohibition, absence semantic or no-state-change guarantee; do not delete that
meaning.

**Example:** Define a Token as “the identifier for one active lease”; retain
“The Server shall not change the lease on failure” when that is the required
error behavior.

### B8. Describe established Method result codes in the result table

For each established result code, give the condition that produces it in the
Method Result Codes table. Do not invent a status code to fill a gap; mark a
suggested code as a proposal for a technical decision.

**Example:** Map an already specified `Bad_Timeout` to its timeout condition;
put a newly suggested code in a review flag, not the normative table.

### B9. Preserve the force of normative verbs

Use the specification's established distinction among shall, should, may and
can. Do not turn capability or description into obligation, or use an
unauthorized synonym that changes force.

**Example:** If the source says a Client “can query” a value, do not rewrite it
as “shall query” without an approved technical decision.

### B10. Name the actor

Prefer active sentences that identify the responsible Server, Client or other
actor.

**Example:** Prefer “The Server shall reject the request” over “The request
shall be rejected”.

### B11. Flag unobservable implementation constraints

Requirements about internal persistence, caching or repair may not be
verifiable through the specified interface. Flag them for an editor or
working-group decision. Do not delete them or disguise them as testable
behavior.

**Example:** If the Server's private retry queue cannot be observed through any
specified interface, flag the clause and explain the evidence gap rather than
rewriting its internals as a visible guarantee.

### B12. Keep proposals out of normative text

Do not strengthen or weaken a requirement while editing. If behavior or a
result code is unspecified, mark the proposed wording clearly in the review
record and seek a technical decision. Preserve descriptive wording when its
normative intent is unresolved.

**Example:** Keep “The Server associates the snapshot with the session” as
descriptive text and flag its intended force; do not change it to “shall
associate”.

## C. Modelling flags

These are questions for the editor or modeller, not permission to change the
NodeSet or type structure.

### C1. Consider an Interface for a shared contract

When several types repeat the same Properties or behavior, assess whether an
Interface is appropriate. Record the model evidence; do not introduce one
through prose editing.

**Example:** Three unrelated types expose the same identity Properties; flag
the repeated contract for model review instead of asserting an Interface was
added.

### C2. Resolve the namespace for identifier-derived BrowseNames

When a rule derives a BrowseName from an identifier, determine the
NamespaceUri source. A BrowseName is a QualifiedName, not just a String.

**Example:** A request identifier supplies the Name portion; flag the clause
if it does not establish which NamespaceUri supplies the QualifiedName.

### C3. Declare well-known BrowseNames in the type

Check that a claimed well-known BrowseName is declared with its applicable
ModellingRule, rather than established only by prose.

**Example:** A clause calls `CurrentJob` a standard child but has no matching
declaration; flag the model gap instead of inventing a Node.

### C4. Check text-valued Properties for localization needs

Assess whether a human-readable Property needs LocalizedText rather than
String. This is a modelling question requiring evidence.

**Example:** A Property contains a translated operator-facing label; flag its
DataType for review rather than changing the NodeSet during copyediting.

### C5. Reconcile generated namespace data and release disclosures

Namespace URI and NodeId assignments may be defined by generated annexes.
Check the publication route before proposing duplicate prose. Do not use this
as authority to remove a provisional identifier, registration or release
status disclosure; retain it in a persistent appropriate location.

**Example:** If Annex A publishes the assigned NodeId, avoid a second
unnecessary assignment statement, but preserve a distinct notice that the
identifier is provisional for this release.

## D. Size and shape

### D1. Keep Scope concise

Use Scope for what the document defines and for whom, not for extended domain
background or release history.

**Example:** Replace several paragraphs of context with a short statement of
the model's subject and intended users, while preserving unique contract facts
in their proper clauses.

### D2. Keep the overview orienting

Use the overview to introduce the model and its main relationships. Keep
requirements and detailed behavior with the relevant types and Methods.
Retain user-approved connecting explanation in informative subsections under
the informative-context decision rather than stripping the overview to names.

**Example:** Show the relation between a Controller and its Channels in the
overview; put the Channel's timeout requirement in the Channel clause.

### D3. Do not tutorialize standard service sequences

Refer to the applicable standard when the behavior is already defined there.
Retain the additional behavior this specification defines, including any
observable lifecycle or failure contract.
An external citation alone may not supply the modelled-technology context
needed by this specification's audience; apply the informative-context decision.

**Example:** Cite the standard file-reading operation instead of listing every
call; retain the unique rule that binds an open handle to a selected revision.

### D4. Use examples to resolve real ambiguity

Use examples that clarify rules or connect the modelled technology to the
normative contract. Keep examples distinguishable from normative text and
proportionate to the specification audience. Apply the informative-context
decision before removing a useful example or diagram.

**Example:** Show one boundary value to clarify whether a range endpoint is
inclusive; omit an example that merely repeats an obvious table value.

### D5. Separate rationale from implementer contracts

Offer the informative-context choice for rationale that connects the model
to its normative contract. Retain developer-specific rationale in the companion
guide under the [guide workflow](implementer-guide.md) when it is not needed
for the specification's reading flow. Working-group-only deliberation belongs
in an authorized review artifact. Do not delete factual consequences or
requirements merely because their explanation includes rationale.

**Example:** Move a comparison of rejected architectures out of a normative
clause, but retain the resulting supported transport requirement.

### D6. Avoid clause previews and summaries

Do not spend normative-clause space narrating the chapter structure or
repeating the clause's contents.
Distinguish empty previews from transitions that connect concepts; retain
needed connective explanation under the informative-context decision.

**Example:** Replace “This clause first describes the Controller and then
lists its operations” with the actual explanation needed to understand the
Controller.

### D7. Avoid duplicating tables in prose

Do not restate attributes or inheritance that a table already expresses.
Retain any distinct explanation needed by implementers and verify that table
facts survive publication.

**Example:** Do not list a type's inherited Name and State Properties in prose
when the definition table already presents them; keep the unique rule for how
State changes.

### D8. Consolidate type definitions only when the authoring pipeline supports it

The intended model is one logical definition containing attributes, direct
references and Conformance Units. Before consolidating source tables, reconcile
the target repository's AUTHORING contract, validators, generator ownership
and pinned Publisher. If composition loses content or scope, report the
dependency and seek a decision; do not rewrite contracts or drop tables.

**Example:** A validator requires separate authored tables and the pinned
composer drops a reference row from a consolidated table; record the conflict
instead of merging tables until the owner resolves it.

### D9. Represent Interface members without duplicating their definition

Use the repository's supported pattern to show the HasInterface relation and
applied members with the implementing type's ModellingRules. If the table must
be kept from Publisher composition, verify the rule and persistence through
outer generators too.

**Example:** Show one Interface member group under an “Applied from” row; do
not repeat the member's explanation in each implementing type. A `table=keep`
caption alone does not protect the table from an outer generator.

### D10. Check Structure table organization and every field fact

Follow the publisher's supported type row and field ordering, while checking
all field names, descriptions, types, ranks, dimensions, encodings and
semantics. A generated table or a successful build is not proof of semantic
completeness.

**Example:** A Structure table has the right field order but omits an encoding
reference and a reserved-bit meaning; report both even if composition succeeds.

### D11. Check merged Method and Interface table cells against the actual pin

Use the repository's documented representation for Method and HasInterface
rows, including merged cells and clause references. Verify against the
repository-approved Publisher version; do not impose a version floor from an
example or silently change the pin.

**Example:** If the pinned Publisher rejects a merged Method row, report the
authoring/tooling dependency and preserve the source contract; do not upgrade
the toolchain solely to match an illustrative example.

## Procedures

### Drafting

Shape the clause for its type or operation. Test each sentence for purpose,
placement, evidence and normative force. Check terminology and typography in
prose and table cells. Verify syntax against the target repository's authoring
contract.

### Tightening an existing draft

1. Inventory all requirements, permissions, recommendations, definitions,
   mappings, examples and other useful implementer facts with source locations.
2. Identify the proper persistent home for each item. Move or merge only when
   the destination is equivalent in meaning and scope. Obtain the user's
   informative-context choice for connecting material before removing it.
3. Remove only material that is genuinely redundant or approved for removal.
4. Compare the inventory with the proposed text and publication. Record each
   retained, moved, merged, superseded or intentionally removed item; no useful
   information disappears silently.
5. Flag model issues for the editor or modeller. Do not change the NodeSet or
   type structure as a prose edit.
6. Before removing a heading or anchor, search repository-wide references,
   including sibling specifications, annexes, CTT material, Profiles,
   manifests, includes, tests and validators.
7. Record moved requirements at both source and destination until the source
   occurrence is removed in an authorized edit.

When result codes, normative strength or technical behavior are unresolved,
keep proposals in the review record, not normative text. Preserve renderer,
generator and release dependencies as explicit findings.

Keep user-selected connecting context in the specification's informative
subsections. For useful implementation teaching not needed there, apply the
[implementer guide workflow](implementer-guide.md) and retain it in the adjacent
guide. Normative contract facts still require a normative published home;
guide-only retention cannot authorize their removal.

## Review record

Return revised wording with the evidence needed to assess it:

- **Dropped:** every removed item, with evidence of a genuinely equivalent
  published home or approved removal reason.
- **Moved:** source and exact destination, including scope and verification.
- **Flags:** unresolved model questions, undefined terms, unobservable
  requirements, proposed normative wording, broken references, publication
  dependencies and conflicts needing an owner or working-group decision.

Keep the original inventory, decisions and final information-preservation
audit in the authorized review artifact. A chat flag is not an approval record.

## Information-preservation safeguards

Apply these safeguards alongside every rule above. They protect against
semantic loss from editing, table composition, generators and publication.
They do not authorize writes or technical changes.

### Ownership and persistence

- Identify complete `BEGIN GENERATED MODEL REFERENCE` through
  `END GENERATED MODEL REFERENCE` regions and bound table cells. Do not edit
  generator-owned regions or relocate authored requirements into them.
  `table=keep` may protect from compose but not from an outer generator.
  Propose a generator-input change or persistent authored home; do not casually
  alter frozen NodeSet descriptions. In approved isolation, verify survival
  with the repository's regeneration and determinism checks. Read-only work
  runs no writing commands.
- "Already in the NodeSet" is not sufficient. Identify accessible rendered
  specification text, a table or an exact applicable normative reference with
  equivalent meaning and scope. Preserve useful facts without forcing
  duplicate prose where an equivalent published home genuinely exists. A
  compose check or build does not prove semantic completeness.

### Meaning and technical scope

- Inventory definitions and every term used normatively, including newly
  introduced names, first-use resolution, scope and distinctions between
  similar roles. Reconcile each definition and use; do not discard a
  distinction as rationale.
- Preserve prohibitions, no-state-change-on-error guarantees, absence
  semantics, and operation or ordering limits when they express facts. Do not
  let B6 or B7 erase these contracts. A shared requirement may have one
  canonical cross-cutting home with references; relocation must not narrow its
  scope.
- Preserve provisional identifier, registration and release-status disclosures
  in an appropriate persistent location. C5 is a modelling flag, not deletion
  authority.
- Before merging mapping tables, inventory every external member or key, row,
  field and value, encoding, omitted or not-mapped case; reconcile treatment
  and scope.
- Do not convert descriptive or illustrative statements into new `shall`
  requirements or mandatory status codes. Keep proposals outside normative
  text until a technical decision is secured. Persist Dropped, Moved and Flags
  in authorized review artifacts, correlate affected CTT expectations, and do
  not treat transient chat text as approval.

### Publication dependencies

- Before heading, table or layout changes, inventory repository-wide inbound
  references, including sibling specifications, hard-coded clause numbers,
  manifests, includes, Profiles, tests, validators and annexes. In read-only
  review report impacts; for approved edits update allowed dependencies or flag
  out-of-scope fixes. Use the actual repository baseline and compare after
  validation.
- Reconcile table facts, including ReferenceType InverseName and Symmetric,
  Structure encoding references, field order, dimensions, ModellingRules and
  reserved-bit semantics. An equivalent published home can suffice; do not
  blindly restore redundant rows. Publisher omissions are dependencies, not
  authority to delete content or edit tooling outside scope.
- For D8 consolidation, reconcile the target AUTHORING contract, validators
  and generator ownership. Report conflicts and seek a decision rather than
  rewriting contracts or dropping tables. Assess consistency within the agreed
  release set; do not initiate an unrequested repository-wide migration.
- Use the repository-approved pinned toolchain and validate restore and
  validator compatibility. Do not impose a version floor from examples,
  silently substitute a version or change pins.

### Examples and retirement

Examples illustrate rules but never override them. In particular, do not
promote descriptive text to `shall`, omit a required child name and kind, or
prefer code formatting over the applicable semantic convention because an
example does so. Do not adopt an example's editorial ordering as policy.
Placeholder anchors in examples must appear as literal syntax in code or
fenced samples, not as broken actionable links.

The safeguards address risks observed in prior reviews; they are preventive
and do not imply that style guidance caused every loss. Retire a safeguard
individually only after reviewing the corrected behavior and verifying its
matching synthetic regression scenario. Record the revision and evidence for
each retirement; keep all other safeguards until separately verified.
