# Upstream writing analysis

This analysis covers **`xregistry/spec` upstream `main`**, pinned on
2026-10-26 to [`4ccfe859b2a04859dadd7a0632af23c1495efe4d`][source]. The fork's
main branch and open PRs are not style evidence here.

All 14 files named `spec.md` or `primer.md` were accounted for. Nine are
substantive documents, including two domain working drafts. One is an
unfinished Primer plan, and four are link-check fixtures. The nine documents
contain 13,143 source lines; all matches together contain 13,360. These are
coverage measurements, not document-size targets.

## Corpus and document families

Paths in this table are relative to the pinned upstream repository.

| File | Lines | Role and distinguishing style |
| --- | ---: | --- |
| `core/spec.md` | 5,512 | Normative reference for client/server implementers; entity definitions, attribute constraints, ordered processing and named errors |
| `core/primer.md` | 1,663 | Explicitly non-normative introduction and rationale; REST-literate reader, running examples, direct address and answered design questions |
| `endpoint/spec.md` | 1,122 | Domain mapping and protocol options; Group/Resource relationships, property tables and constraints |
| `message/spec.md` | 1,420 | Metadata and protocol reference; definitions, composition explanation, protocol tables and one relationship diagram |
| `schema/spec.md` | 681 | Domain/versioning explanation followed by model and attribute/format reference |
| `cloudevents/spec.md` | 490 | Integration walkthrough; combines existing domain specifications using substantial JSON examples |
| `pagination/spec.md` | 319 | Short, direct protocol reference; client parameters, response attributes and HTTP examples |
| `workingdrafts/models/openusd/spec.md` | 854 | Domain draft with more motivation and emphasis; identity construction, dependencies and security consequences |
| `workingdrafts/models/wot/spec.md` | 1,082 | Domain draft; identity, metadata/document distinctions, lookup and explicit informative relationships |
| `todos/primer.md` | 200 | WIP Discovery/Subscription outline with unfinished sections; not a finished prose exemplar |
| `tools/fake-docs/myspec/spec.md` | 4 | Link/title-check fixture, not a specification |
| `tools/fake-docs/yourspec/spec.md` | 7 | Deliberately inconsistent title fixture, not an editorial model |
| `tools/fake-docs/languages/my-lang/myspec/spec.md` | 3 | Translation/title-check fixture |
| `tools/fake-docs/languages/your-lang/myspec/spec.md` | 3 | Deliberately inconsistent translation/title fixture |

The established references share conventions, but not a single outline. Core
uses unnumbered headings; the Primer and both domain drafts use numbered
sections. CloudEvents teaches composition rather than defining another Core.
Pagination begins with its purpose and operations without a long preamble.

The newer domain drafts contain more bold emphasis, em dashes and causal
explanation than the established normative references. Use them to learn
domain mapping and scope distinctions, not to impose their emphasis density on
Core or every README.

## Audience and register

The [Primer's opening][primer-purpose] explicitly separates explanation and
design rationale from normative technical detail. Its [quick
introduction][quick] assumes ordinary REST operations and JSON, then teaches
the Registry hierarchy and reading/writing operations. Its [Epoch
discussion][why-epoch] is an example of an answered design question, not a
normative attribute definition.

The [Core notation and terminology][notation] establish the language used by
implementers. Attribute names are literals; Registry, Group, Resource and
Version denote distinct entities. The style avoids making a reader infer which
actor performs a step or which entity an attribute belongs to.

Domain material defines domain concepts and explains their relation to Core.
The [Schema overview][schema-overview] explains the domain before its
reference material; the [CloudEvents overview][cloudevents-overview] combines
existing domain models instead of introducing another Registry hierarchy. The
[WoT overview][wot-overview] distinguishes TDs from TMs and describes what the
registry does and does not enforce. Its [document-store section][wot-views]
separates the metadata view from document retrieval with concrete URL
consequences. These distinctions justify detail; generic product positioning
does not.

**Derived guidance:** use an implementation-oriented register for
specifications and a teaching/rationale register for Primers. For supporting
documents, choose the nearest role rather than copying the entire
specification outline.

## Detail and structure

The [Core identifier and self attributes][cards] show the recurring Type /
Description / Constraints / Examples structure. The [epoch rules][epoch] carry
condition-dependent update and concurrency behavior close to the attribute
definition. The [Resource processing algorithm][processing] gives an explicit
sequence where order determines the outcome.

The [Endpoint protocol tables][endpoint-tables] add usage-role columns where
the role changes an option's applicability. The [Message HTTP
options][message-http] use a simpler property/type/description table followed
by the constraints that cannot be expressed by a type label alone. The
[Pagination attributes][pagination-cards] use reference cards even though the
document has no long introductory outline.

Details are not uniformly expanded. A short value example can be enough for an
attribute. A branching operation needs its conditions and failure results. The
[WoT format and inheritance clauses][wot-formats] refer to Core and other
standards instead of reproducing all of their rules. The [OpenUSD identifier
construction][usd-identifiers] needs an algorithm and a mapping table because
the transformation itself is the subject.

Brief local explanations occur inside specifications. Extended justification
belongs in the Primer; this is a separation of purpose, not a ban on
explaining why a normative rule matters.

**Derived guidance:** size a clause by the number of distinct decisions a
reader has to implement. A word limit or compulsory edge-case paragraph would
not capture the corpus's approach.

## Example granularity

The corpus uses two different kinds of large block: a reference grammar and a
worked integration example. Neither implies that every example needs to be
large.

| Purpose | Evidence and observed scale |
| --- | --- |
| Hierarchy reference | Core's [serialization specimen][core-shape] spans 252 lines inside its fence and uses declared pseudo-JSON notation |
| Introductory use | The Primer's 15 fenced blocks range from 1 to 18 content lines, including an ASCII hierarchy and short requests |
| Domain model reference | OpenUSD's specimen spans 111 content lines; WoT's spans 145, with annotations and explicit omissions |
| Composition walkthrough | The [CloudEvents examples][cloudevents-examples] include JSON blocks of 84 and 140 content lines |
| A single relationship | WoT's [TD-to-TM link example][wot-link] uses a 12-line JSON fragment beside the explanation |
| A direct operation | The [Pagination HTTP binding][pagination-http] illustrates requests, response links and traversal with short HTTP fragments |

Fence-content lengths exclude the opening and closing fences. They describe
this snapshot, not quotas for future work.

The [Core notation][notation] explains placeholders, permitted omissions and
repeated members. The [WoT Group example][wot-group-example] marks omitted
common attributes. Such ellipses are intentional abstraction, unlike the
unfinished sections of `todos/primer.md`.

**Derived guidance:** preserve enough state, identity and representation to
make the demonstrated result unambiguous. Use valid concrete JSON for copyable
JSON examples; use declared pseudo-JSON for a model grammar.

## Diagram granularity

All four images linked from the [Core overview][core-figures] were inspected:

- `core/xregbasicmodel.png`: four levels, from Registry to Versions.
- `core/xregfullmodel.png`: the same hierarchy expanded into two Groups and
  four Resource-type collections.
- `core/xregsample.png`: a concrete Endpoint/Message and Schema mapping,
  including the reference from Message Definitions to Schemas.
- `core/xregurlmapping.png`: URL path components aligned with the corresponding
  nested document keys.

These figures progress from concepts to instances to representation. They do
not depict server internals or deployment infrastructure.

The [Message reuse section][message-diagram] has one Mermaid relationship
diagram for derived and base definitions. The Primer has a small ASCII
hierarchy. The other six specifications in the substantive corpus have no
figures. Thus neither a diagram per section nor a particular drawing format is
an upstream convention.

**Derived guidance:** choose one relationship or abstraction level per figure.
Use prose to establish meaning and a text equivalent for readers who cannot
see it. Accessible descriptions and maintainable source are delivery
practices, not claims that every existing image already satisfies them.

## Conventions to preserve, defects to avoid

[CONTRIBUTING][contributing] explicitly asks for 80-column wrapping when
practical, RFC2119 requirements, valid links, spelling checks and no Markdown
tabs. Preserve local headings, anchors, literal identifiers and the
established division between normative and explanatory material.

Repeated rule cards, precise technical repetition and qualified sentences
serve reference readers. Do not flatten them into uniformly short prose or
replace defined terms with synonyms to avoid repetition.

Do not elevate unfinished notes, malformed markup, inconsistent examples,
unsupported generalizations or technical contradictions into style rules.
Resolve technical questions from the governing specification, not by imitating
a selected sentence.

The detailed [WoT relationship boundary][wot-boundary] explicitly marks
informative clauses. An informative label is not permission to add obligations
during a style rewrite. Conversely, requirement strength is not cosmetic.

## Limits of this skill

The skill supplies an authoring process and a review checklist. It cannot
guarantee that a model will follow every instruction, replace editorial
judgment, or prove specification conformance. The repository instruction
points agents to it for documentation work; the checklist makes departures
reviewable.

No source specification, Primer, fixture or generated schema was rewritten to
create this analysis. The corpus remains the upstream version identified
above; new behavior requires its own technical decision.

[source]: https://github.com/xregistry/spec/tree/4ccfe859b2a04859dadd7a0632af23c1495efe4d
[primer-purpose]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/primer.md#L6-L15
[quick]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/primer.md#L99-L177
[why-epoch]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/primer.md#L1117-L1155
[notation]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L112-L242
[cards]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L1042-L1127
[epoch]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L1213-L1255
[processing]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L2590-L2702
[core-shape]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L406-L666
[core-figures]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/core/spec.md#L62-L110
[schema-overview]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/schema/spec.md#L38-L160
[cloudevents-overview]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/cloudevents/spec.md#L10-L46
[cloudevents-examples]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/cloudevents/spec.md#L110-L350
[endpoint-tables]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/endpoint/spec.md#L826-L880
[message-http]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/message/spec.md#L1064-L1099
[message-diagram]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/message/spec.md#L229-L271
[pagination-cards]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/pagination/spec.md#L41-L93
[pagination-http]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/pagination/spec.md#L200-L319
[wot-overview]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L64-L118
[wot-views]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L150-L183
[wot-formats]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L534-L590
[wot-group-example]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L444-L475
[wot-link]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L904-L946
[wot-boundary]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/wot/spec.md#L896-L902
[usd-identifiers]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/workingdrafts/models/openusd/spec.md#L648-L701
[contributing]: https://github.com/xregistry/spec/blob/4ccfe859b2a04859dadd7a0632af23c1495efe4d/docs/CONTRIBUTING.md#L116-L134
