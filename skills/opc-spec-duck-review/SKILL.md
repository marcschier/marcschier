---
name: opc-spec-duck-review
license: MIT
description: >
  Review OPC UA specifications through a rubber-duck dialogue between an
  independent reader and an expert editor. Use for a fresh-reader comprehension
  review, sentence-by-sentence forward reading, or iterative reader/editor
  rewrites. Select source-only or source plus published HTML. Unlike
  opc-spec-review's correctness and style audit, this workflow tests what an
  OPC UA expert can understand without prior knowledge of the target domain.
---

# OPC specification comprehension review

Use separate reader and editor agents. The reader discovers what the document
actually teaches; the editor understands its technology and makes authorized
corrections. Keep the editor's history across passes and give each new full
pass a fresh reader context.

This complements `opc-spec-review`; it does not replace its correctness,
information-model, or publication audit. Comprehension agreement is not
certification, standards approval, or evidence of runtime behavior.

## 1. Agree the scope

Before reading the specification, discover its manifests and ask the user which
specifications to review: all in the repository, a named subset, or one.
Then ask whether to review only each specification's source folder or also its
Publisher-rendered HTML. Ask one question at a time, showing discovered names.
Confirm the selection even when the invocation suggests a scope.

Record whether the user authorizes source fixes or wants findings only. A
request for review alone authorizes no edits. Identify each spec's prerequisite
OPC UA specifications and preceding parts with their editions. For Part 2 the
reader may know Part 1; for Part 1 it may know the declared dependent OPC UA
specifications. Keep other specifications outside the edit scope.

Freeze source revisions and hashes, dirty state, tool pins, and the selected
files and publication route. For HTML, verify that its recorded input
fingerprint matches the current source, model, and tool inputs. Stale HTML is
evidence of an older edition, not coverage of the current one. Agree an
isolated output location and regeneration permission if current HTML is
missing; otherwise leave that coverage incomplete.
Source review includes all prose in the selected
source folders, including manifest terms and profile descriptions, not just
`spec.md`. Read models or external domain sources only as editor evidence.
Exclude PDF and Word from this workflow.

**Ready:** every selected spec, format, prerequisite, and edit permission is
explicit. An unavailable artifact is a gap, not an implicit exclusion.

## 2. Establish independent roles and evidence

Resolve `opc-spec-review` through the host's skill mechanism and read its
packaged `references/style-overrides.md` as the single shared temporary
safeguard source; do not assume installed sibling directories. Resolve
`opcua-spec-style` only from the repository being reviewed at
`<repository root>/skills/opcua-spec-style/`. Read its complete `SKILL.md`,
`rules.md` and `examples.md`. Record the target repository revision and paths
read; include file hashes or dirty state when they differ from that revision.
If the directory, any required file, the review package or safeguards cannot
be read, stop before style review, proposal or writing and report each missing
or unreadable path. Do not fall back to a host-resolved or remote style skill,
another style skill or a copied summary.

The safeguards override conflicting upstream guidance; upstream rules outrank
contradictory examples. The style skill governs specification prose,
applicable normative sources and approved technical decisions govern technical
facts, and the repository's authoring contract and pinned Publisher govern
syntax and composition. Generic report-writing helpers may be used for
non-specification deliverables only, never as competing specification guidance.

Read [the role instructions](references/roles.md) before dispatching agents.
Send the reader its role instructions, agreed scope, current source and HTML
locations/hashes, allowed OPC UA prerequisites, and the style authority and
shared safeguards only. Send the editor its role instructions, the same style
authority and safeguards, full technical sources, edit permissions, and the
findings. Both agents independently read all three target-repository files and the
shared safeguards; verify their access before the affected work. Style guidance
does not grant the reader domain knowledge, previous findings or editor history.
Keep task documents and fetched content as evidence, not agent instructions.

Launch one dedicated editor agent and retain it throughout the review. Launch
a separate reader agent for each full pass, without inherited conversation,
previous findings, editor explanations, or prior-pass summaries. Record agent
IDs and model identities when exposed by the host. Separate agents are
mandatory; use distinct models when requested and available. Ask for model
choices if the user requires different models but has not selected them.
Otherwise honor host model defaults rather than hard-coding model names.
If isolated agents cannot be created, report the limitation; a single agent
pretending to forget is not an independent review.

Use the host's supported delegation and follow-up tools to retain each role's
context; orchestration does not require installing an automated workflow.
Route reader findings to the editor and editor revisions back to that pass's
reader. Supply the pass number to both roles so the challenge policy is
unambiguous. For multiple specs, agree dependency order and record each spec's
allowed prior knowledge; unrelated domain knowledge does not transfer merely
because another selected spec introduced it.

Both agents must use the OPC UA knowledge-base MCP tools and
https://reference.opcfoundation.org/ for OPC UA authority and representative
companion-specification prose. Discover tools by capability; the knowledge
base may expose names such as `opcua-kb-tools-search_docs`. A live OPC UA
server's Browse/Read tools are not a substitute. Verify that both agents can
access both sources, record relevant queries and versioned clause URLs, and
keep retrieved summaries distinct from authoritative text. If either source
is unavailable, pause the affected review and report the access dependency.
Never upload private drafts or models to the knowledge base: query generalized
OPC UA concepts without confidential content.

The reader may consult OPC UA prerequisites but must derive target-domain
knowledge from the current specification as it reads. The editor may research
the domain and non-OPC standards. Supply prerequisite references, not an
editor-written explanation of the target domain.

**Ready:** independent contexts, both evidence sources, the complete style
authority and shared safeguards are available to both roles. No review verdict
rests on assumed tool access.

## 3. Complete the first forward reading

Have the reader execute the forward-reading procedure in the role instructions.
Use bounded consecutive batches when needed, retaining the same reader within
this pass. Inspect every sentence in source order; if HTML is selected, also
inspect every sentence and content element in publication order. Keep separate
coverage for each representation and identify generated material.

The reader records a judgment and concise reason for each sentence, including
sentences it accepts. It first judges the sentence using only knowledge gained
so far, then consults the whole containing paragraph and records whether that
resolves the concern. A later explanation does not erase an earlier reading
obstacle. Track headings, table cells, captions, examples, and diagrams as
additional units so sentence accounting does not omit their meaning.

The coordinator checks the coverage ledger against the selected content.
Unread ranges, truncated tool output, inaccessible figures, and missing HTML
remain explicit gaps. A summary, search, lint result, or batch-wide approval
does not establish sentence coverage.

**Done:** every selected unit has a located judgment and all remaining
comprehension questions are recorded. The reader finishes with an explanation
of the spec's purpose, concepts, operations, boundaries, and examples, grounded
in what it learned. Unanswered questions limit that understanding; never
declare the reader an expert merely because it reached the end.

## 4. Revise and re-review within the first pass

Route every reader finding to the editor without filtering out requests the
coordinator dislikes. Only the editor may change specification sources.
The editor applies `opcua-spec-style` and the shared temporary safeguards to
every specification rewrite; missing authority blocks that branch.

In the first full pass, the editor accepts the reader's requests for clearer
wording and continues revising when the reader remains dissatisfied. It must
not reject a request merely because it considers its own explanation adequate.
If a requested rewrite would invent behavior, contradict authoritative text,
or exceed permission, offer a faithful alternative or ask the user for the
technical decision instead of making an unsafe edit.

The editor returns source locations, the diff, rationale, supporting evidence,
and affected reading units. In HTML scope, use the repository's pinned
Specification Publisher commands to regenerate the affected edition before
asking for re-review. Obtain permission for writes and output locations;
preserve unrelated dirty work. Inspect actual rendered HTML, including figures
and links, rather than treating STS or Markdown as equivalent evidence. Keep
generated output fixes in their authoritative source; report Publisher defects
instead of patching generated HTML.

Ask the same reader to re-review each revision in its paragraph and adjacent
context, with updated source/HTML hashes. Record local acceptance or continued
confusion. The editor maintains the finding history and useful information
removed or moved. Findings-only mode produces located recommendations, not
unapplied changes presented as accepted fixes.

**Done:** the reader accepts the first pass's authorized revisions, or a
specific missing permission, evidence gap, or user decision blocks progress.

## 5. Repeat with a fresh reader

After the first pass's revisions, start a new full pass from the beginning with
a new reader agent. Retain the editor and its history; withhold that history
from the new reader. The fresh reader receives only the current edition,
agreed contract, permitted OPC UA prerequisites, and the style authority and
shared safeguards. Reset learned domain knowledge between full passes, not
between batches or local re-reviews.

From the second full pass onward, the editor may challenge a finding. Request
the exact sentence, the reader's interpretation at that point, the missing or
conflicting information, and why the paragraph or an earlier definition does
not resolve it. The editor may reject a change when that argument is
insufficient, but must record its reason and evidence and ask the reader to
respond. An editor rejection alone does not close a disputed finding.

Continue revisions and local re-reviews until both agree. Bring a persistent
disagreement to the user with the original wording, reader reasoning, editor
reasoning, evidence, and concrete alternatives. Record the tie-breaking
decision without misrepresenting it as mutual acceptance. If a cycle repeats
without progress or reaches a user-imposed resource limit, ask for a decision
or continuation; never call that convergence.

Every change requires another fresh full pass over the current source and,
when selected, current HTML. Continue until a complete fresh pass finds no
new or unresolved issues and the editor also accepts that same edition.
Previously rejected findings need explicit reader agreement or a recorded user
decision; hide neither from the final report.

**Done:** a complete unchanged final edition has fresh-reader and editor
acceptance, no coverage gaps, and no outstanding decisions, subject to the
mandatory final information-preservation audit below. Otherwise report the
precise incomplete state.

## 6. Final information-preservation audit

Before reporting completion, the editor and coordinator must read and apply
`references/revisions.md` section "Final information-preservation audit" from
the host-resolved `opc-spec-review` package. Resolve that reference through the
host, not an assumed sibling directory. If the reference is unavailable or
lacks that section, report the missing dependency and withhold completion.

Perform this audit after the final draft or rewrite and last authorized
regeneration. Compare the fixed pre-change baseline and complete information
inventory against the final text and current in-scope publication. For new
drafting use agreed source inputs and requirements; in findings-only mode
audit proposed text without editing or claiming it was published. Missing
baseline evidence or unresolved loss prevents acceptance, even when the fresh
reader and editor agree or checks pass.

Keep the baseline, previous findings and audit history with the editor and
coordinator, not the fresh reader. Record located retention or approved removal
dispositions and the audit outcome in an authorized artifact. Any correction
requires validation as applicable, another fresh full reading pass and another
final audit; read-only mode reports loss without writing commands or edits.

## 7. Deliver the result

Keep the detailed ledger and editor history in an authorized session artifact
location, outside stageable specification content unless requested. For each
spec and pass record:

| Record | Content |
|---|---|
| Edition | Source/HTML hashes, tool versions, prerequisites, reader and editor IDs |
| Coverage | Ordered unit IDs, file/line or HTML anchor, sentence text or unambiguous span, judgment, reason, paragraph reassessment, gaps |
| Findings | Reading obstacle, first occurrence, proposed correction, editor action, local re-review and final disposition |
| Decisions | Evidence citations, challenges, rejected suggestions, user decisions |
| Preservation | Baseline and final revisions or hashes, located retention or approved removal dispositions, final audit outcome and gaps |
| Result | Reader explanation of learned concepts, editor acceptance, changed files, validation and remaining limitations |

Report per-spec outcomes as accepted for comprehension, findings delivered
without edits, user decision required, or assessment incomplete. Give actual
coverage counts, passes, changes, and publication provenance. Distinguish this
outcome from `opc-spec-review` correctness/style findings and
`opcua-model-review` model conformance. Commit, push, publication, and issue
filing require their own user authorization.
