# Composed-edition review

The manifest and include tree define the publication. Inventory authored clauses,
generated references, terminology, profiles, conformance units (CUs), NodeSet
tables, annexes, examples and official figures. Include complete HTML and every
other shipped format that the review contract covers.

## Coverage ledger

Give every composed clause a row, including generated clauses and annexes.
Track figures separately so an uninspected image cannot disappear inside a
completed chapter. Map each row to its source or generator and current output.
Read the part number and title inside each artifact before its evidence joins a
row; file names and output folders can point at another part.

| Spec / clause | Source or generator | Render revision / hash | Route | Structure | Detail | Words | Evidence / findings |
|---|---|---|---|---|---|---|---|
| Synthetic Part A / 4 | Authored source | Recorded artifact hash | Pending | Pending | Pending | Pending | Not yet read |

Use pending, reviewed or blocked for each level; a blocked cell needs a reason.
Record not-applicable only when the content and scope justify it. The levels
mean:

1. **Route:** skim the complete edition and establish its reading route,
   prerequisites and cross-part responsibilities.
2. **Structure:** assess section hierarchy, order and teaching progression.
   Determine whether definitions arrive before use and responsibilities before
   protocol detail.
3. **Detail:** read every paragraph, table, snippet and annex in context,
   including generated content. Reread generated bibliography and glossary
   entries in each shipped format after a contract correction. Follow
   pagination and fetch omitted ranges; truncated reads do not count as
   coverage.
4. **Words:** check terminology, qualifications, normative force and consistency
   at word level against the technical sources and other parts.

A search assists these passes but does not replace them. Scan results and
delegate reports are candidates until confirmed in the composed artifact.
Record the exact covered range and remaining gap after interrupted reading;
require each delegate to return the same two facts, and reopen a delegate whose
gap its own inputs could close. Reopen affected cells after source changes or
regeneration; complete only when their evidence matches the current output.

## Explanation and reading order

Assess whether the publication teaches the mechanism around its precise
contracts. Prefer causal explanatory prose where the reader must understand
why a rule exists. Retain signatures, enumerations, option sets, actual
algorithms and profile matrices. Bullet count alone is not a quality measure.
Preserve strong chapters and revise proportionately.

At difficult boundaries, trace a concrete successful interaction and a relevant
failure. Check identity and authority, inputs and outputs, omitted or default
values, lifecycle transitions, rollback, retirement, retry, partial failure and
diagnostics where applicable. These are questions to apply to the model, not
mandatory headings or an instruction to invent unsupported behavior.

Evaluate examples and figures at the points where readers must make difficult
decisions. Check technical accuracy by executing each example the toolchain can
run, or by validating it against the model or schema it illustrates; a failing
example can expose a model defect that reading misses. Check distribution as
well: a large example count cannot compensate for a missing explanation at an
interoperability boundary. Keep examples distinguishable from normative
requirements.

## Contract reconciliation

Compare prose and figures with normative models, schemas, vocabularies,
profiles, CU definitions, tests and cited base standards. Trace producer and
consumer responsibilities across parts. Resolve apparent contradictions using
the actual predicates and lifecycle levels: candidate versus invocation,
precommit versus activation, active versus exact versus default identity.

Preserve conditional obligations and Optional qualifications. An obligation
under an existing Optional ancestor is different from requiring that ancestor.
Terminology alone does not establish a contradiction. Record competing
interpretations and their evidence; obtain a technical decision where the
sources do not settle it. Editorial work cannot choose a new contract.

The publisher assigns annex letters and clause, table and figure numbers when
it composes the edition. A source heading that repeats the annex letter doubles
it, and a reference written as a fixed letter goes stale when annexes move.
Search authored sources, generators, generated model descriptions such as
NodeSet `Description` text, and publication checks for hard-coded numbers, and
compare each with the composed numbering. Correct the generator and the check
with the source, then regenerate.

For model questions, use `opcua-model-review` and reconcile its complete ledger
with the publication findings. Load the base NodeSet whose version matches the
pinned dependency before confirming a missing inherited Mandatory member;
without it, the finding remains a candidate. Static checks do not establish
runtime behavior.
Keep unexecuted tests, unavailable implementations and unverified deployment
assumptions visible in the runtime-evidence category.

## Figures and shipped formats

This review covers what each shipped format says, not how its pages look.
Dark-mode theming and PDF or print layout, including pagination, page breaks,
clipped tables and wrapped identifiers, are outside its scope. Do not inspect
them or record them as findings unless the user expands the scope. Opening a
renderer for a content check does not bring its layout into scope.

Inspect every official figure in full, including labels, arrows, legend,
caption, surrounding explanation and cross-references. Record each figure's
source, rendered evidence, disposition and any unreadable region. Use the
actual artwork rather than inferring it from a filename or nearby prose. Take
the figure inventory from the composed intermediate, such as the STS XML,
counted per part, and reconcile it with the ledger before stating a count; an
HTML scan or an estimate can miscount. For browser captures, disable smooth
scrolling and confirm the element's bounding box lies inside the viewport
before recording the capture as evidence.

Inspect complete HTML at wide and narrow widths, its navigation and anchors.
Distinguish an embedded preview's overrides from the shipped publication. If a
`file://` preview cannot load assets, verify through a task-owned loopback
static server before reporting a missing asset. Bind locally, verify readiness
and stop the specific task-owned process after inspection. A static link scan
lists candidates: confirm each failure in a browser, because the publication's
script rewrites some links when served over HTTP. A render from a dirty tree
omits source-edit links; judge them from a clean committed publication, or
record that limit.

Inspect other shipped formats as agreed. Before reporting a renderer or tool as
unavailable, probe how the host registers it, not only `PATH`, and name each
probe in the report. State which formats still could not be opened and how that
limits the release assessment. Never turn an inaccessible figure or format into
an implicit pass.

### Word documents

A DOCX holds its cross-references, contents, lists of figures and tables and
generated bibliography as fields. Word computes their text when it updates
them, so DOCX XML inspection shows which fields exist, not what a reader sees.
Review the resolved text through Word.

Office installations normally leave `WINWORD.EXE` off `PATH`, so a failed
command lookup proves nothing. On Windows, create the `Word.Application` COM object, or
read the `App Paths\WINWORD.EXE` registry key. Report Word as unavailable only
when both fail. LibreOffice can resolve fields when Word is absent; record that
its field engine differs from Word's.

Run Word so that neither the artifact nor the host changes:

1. Point `TEMP` and `TMP` at the user's authorized temporary location before
   starting Word, because Word and its exports write temporary files there.
2. Set `AutomationSecurity` to force-disable macros. Open each DOCX read-only,
   invisible and without adding it to the recent-file list.
3. Update all fields, then every table of contents and table of figures.
4. Read the resolved text through Word, or export a PDF and extract its text.
   Search it for Word's error results, such as "Error! Reference source not
   found." and "Error! Bookmark not defined.", in Word's interface language.
   Compare contents and figure-list entries with the composed headings and
   captions, and reread the generated bibliography.
5. Close each document without saving and quit Word. Confirm that no Word
   process the task started remains, and stop a leftover only by its process ID.

An exported PDF here is a vehicle for text extraction; its layout stays outside
the review scope.

## External dependencies and publication closure

For each normative external dependency, verify the pinned edition,
authoritative status, accessibility, date and current proposal or release
state. Record evidence and the date checked. Compare every edition number cited
in prose, tables and generated descriptions with the manifest pin; a chapter
can cite a newer edition than the one pinned. Resolve each pinned versioned URL
and record its HTTP status. Local parts may form a valid
simultaneous co-release; assess the coordinated release set rather than
requiring every local part to have been published independently.

A merged change or GitHub release flag does not establish standards approval.
An immutable draft pin preserves identity, not final status. Preserve draft
labels and actual identifiers; record approval or availability blockers rather
than manufacturing final identities. Ask for the release-state policy once, as
one decision covering whether pinned drafts count as approved dependencies,
which document status the release carries and which identifiers it uses. Record
the exact answer, quote it when a later question touches it, and re-audit
earlier edits when a later answer narrows it.

Distinguish source-edit links and history chrome from normative dependencies
on PRs, commit IDs or mutable branches. Check that edition-stable publication
links resolve models, schemas, contexts and examples as well as document pages.
Report a broken publication dependency with its consumer and consequence,
not merely a count of links.
