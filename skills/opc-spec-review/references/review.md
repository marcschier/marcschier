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
When a model or other render input changes, compare a fresh publication with
the reviewed output before reusing earlier evidence. Record both revisions and
hashes. Carry forward coverage only for unchanged content and figures; reopen
the affected cells where the output differs.

Before a bulk ledger refinement, preflight the selected rows and their existing
rule-specific reasons. Select by stable row identity and applicable rule, not
by a generic subject alone: rows about the same subject can have different
obligations or evidence. Preserve each existing reason unless the refinement
explicitly accounts for its replacement. Check the proposed before/after rows
before writing, and verify afterward that unrelated reasons remain unchanged;
leave ambiguous matches untouched for investigation.

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

Check primary and RequiredModel metadata separately against the Part 6 edition
the model uses. When that edition requires `XmlSchemaUri` or associated XML and
binary schemas, reconcile their identities, annotations, imports and definitions
with the NodeSet. An XML schema namespace determines encoded QNames; do not
infer it from the NodeId namespace or assign one without an owner decision.
Validate generated schemas against their dependencies: a generator's output or
exit status alone does not establish that the schemas compile.

## Figures and shipped formats

This review covers what each shipped format says. Dark-mode behavior and PDF
layout/rendering, including pagination, page breaks, clipped tables and wrapped
identifiers in PDF or print exports, are outside this skill's scope. Do not
inspect them or record them as findings. Word visual pagination review is a
separate, explicitly agreed branch described below. Opening a renderer for a
content check does not bring its layout into scope.

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
generated bibliography as fields. Distinguish field instructions from stored
field results: the current Publisher output may already contain populated
results in the DOCX XML. Inspect those results before deciding that Word must
compute them. Field instructions alone do not establish resolved text, and
populated results do not prove that the fields are correct or current.

Before using DOCX or Word evidence, record the absolute artifact path, SHA-256
hash and source/model/tool input revision or hashes from the isolated Publisher
run. Match the part number and title inside the document to the ledger. For an
open Word window, verify its document's full path and compare the file hash
with that recorded output; a matching filename or window title is insufficient.
If the open document has unsaved edits, its disk hash does not identify the
displayed content. Do not save, close or replace the user's document; open the
verified output separately, read-only. If the review contract permits a saved,
field-updated evidence copy, create a task-owned copy in the authorized review
location. Verify its initial hash against the Publisher artifact, update and
save only that copy, and record its new hash. Recheck identity after
regeneration. Word being installed does not make an already-open document
current: an older DOCX may show empty fields while the current isolated output
has populated results. Withdraw that hypothesis when the current artifact
disproves it.

A changed DOCX hash requires comparison before earlier Word observations can
be reused. Resolve relationship IDs to their targets and compare the package
parts that affect rendering, including fields, used styles and their
inheritance, page settings, fonts, media, headers and footers. Account for
fields whose updated results depend on the filename or environment. Record
the renderer and its version, the differences and the pages actually inspected.
Compare non-list text before and after field updates as well. A `FILENAME`
result can change from the template name to the task-owned copy's name after
`FieldsUpdate`. Identify each changed field by its instruction and location,
record its before/after result and attribute a legitimate change to the copy's
identity or evaluation environment. Do not treat every difference as an authored
edit, exclude all field results from comparison or report all non-list text as
unchanged when a field result changed. Keep unexplained differences open.
If layout-affecting equivalence is not established, inspect the new artifact;
matching body text alone does not establish equivalent pagination.

Two pre-field-update DOCX ZIPs can differ only because image or hyperlink
relationship IDs were regenerated. Record both package SHA-256 hashes, compare
ZIP member sets and each member's uncompressed bytes, and enumerate every
difference. For differing document XML, compare element structure, text and
non-relationship attributes at corresponding locations. Resolve every changed
relationship ID through its owning part's relationship file and require the
same relationship type, target and target mode at that location; do not simply
strip IDs. Compare relationship-attribute multisets within each relationship
file with only `Id` excluded, preserving duplicate counts and all other
attributes. A matching multiset
alone cannot detect targets swapped between document locations.
Require all other members to be byte-identical; unexplained differences,
missing relationships or changed targets prevent an ID-only equivalence
conclusion. This establishes only the compared pre-update package content,
not field-update results or visual pagination. The copy filename, environment
and later Word actions can affect those results; verify them separately.

Compare non-list field results by instruction and document location across both
DOCX representations: simple fields (`w:fldSimple` with `w:instr`) and complex
fields (`w:fldChar` begin/separate/end with `w:instrText`). Reconstruct split
instructions and result runs within the correct field boundaries, respecting
nested fields. Match corresponding fields across representations; an XML form
change alone is not a text change, and an ambiguous match remains unresolved.
A publisher-generated `REF` field for an internal table link can replace a
custom display label with the table number when updated, changing technical
text even though the link still resolves. Do not assume a field update
preserved link labels. Record the original label and updated result with the
instruction, target bookmark and location, then investigate unexpected changes
against the source link and composed table. Distinguish the update-induced
change from the Publisher's original stored result; a legitimate `FILENAME`
change does not justify accepting unrelated `REF` changes.

Separate content evidence from visual evidence in the ledger. DOCX XML can
establish stored field-result text, including reference errors, but cannot
establish Word's pagination or how a page looks. Record whether text came from
stored results or a Word field update. Compare contents and figure-list entries
with the composed headings and captions, and reread the generated bibliography.
When results are missing, ambiguous or require Word evaluation, use Word to
resolve them; do not mark unresolved fields as reviewed.

Word's "Update Table of Contents" ribbon action can update only the contents
while the separate lists of figures and tables remain placeholders, even in a
current CI DOCX. Update and verify each list separately, then check the remaining
fields, including cross-references and bibliography. Record which fields
resolved and which remain placeholders or errors. A successful contents update
does not establish that all fields were updated or that pagination was visually
reviewed.

If a focused `F9` dispatch fails through UI automation, place the caret inside
the figures or tables placeholder and use References > Captions > Update Table.
The control's UIA ID is `TableOfFiguresUpdate`; find it in a fresh accessibility
state and act through its current node index. This route has resolved both
figures and tables placeholders into entries through separate invocations,
with the caret inside the respective field. It is distinct from References >
Table of Contents > Update Table, which updates the contents list. Reread the
selected field to verify the result; command completion alone is insufficient.
Update and verify figures and tables separately; one invocation does not
establish that both lists were updated. Keep contents, remaining fields and
visual pagination coverage independent.

Office installations normally leave `WINWORD.EXE` off `PATH`, so a failed
command lookup proves nothing. On Windows, probe the `Word.Application` COM
registration or the `App Paths\WINWORD.EXE` registry key. For content automation,
try creating the COM object and record any activation error. Report Word as
unavailable only when both discovery routes fail. A registered executable with
failed COM activation is an automation blocker, not proof that Word is absent.
LibreOffice can resolve fields when Word is absent; record that its field
engine differs from Word's and that it does not establish Word visual coverage.

A task-started Word process does not establish that every document in it is
task-owned. In one observed launch, `WINWORD.EXE /n` with `TEMP` and `TMP` set
to `D:\temp` and no filename passed showed at least three visible `OpusApp`
windows with `_WwG` document-view children. Their document identities were not
inspected; their contents and the cause remain unknown. Only the task-started
PID was closed/stopped. Do not infer document ownership from the PID, window
classes, launch arguments or temporary-directory settings.

Before updating fields or quitting an instance, enumerate its documents and
windows and verify each affected document's identity and task ownership.
If unexpected documents appear or an identity cannot be verified, stop
automation against them, report the uncertainty and leave them unchanged.
Do not save or close an unidentified document, or quit an instance containing
one. Distinguish a task-started PID from verified document ownership in cleanup
records; stop only that specific PID when termination is authorized, never
other Word processes.

For content-automation process identification, obtain the handle from a
verified Word window's [`Window.Hwnd`](https://learn.microsoft.com/en-us/office/vba/api/word.window.hwnd),
then resolve that handle to its process ID and compare it with the recorded
task-started PID. Word exposes this property on `Window`, not
`Application.Hwnd`; the attempted application property returned no handle.
Do not assume an empty application has a usable document window. If no verified
window or handle is available, report process identity as unverified rather
than substituting another Word window. A handle-to-PID match does not establish
ownership of every document in that process.

Consult Microsoft's [Office command-line-switch documentation](https://support.microsoft.com/en-us/office/lifecycle/command-line-switches-for-microsoft-office-products)
before relying on a launch option. It describes `/n` as starting a new instance
with no document open, and `/x` as responding to only one Dynamic Data Exchange
(DDE) request, not as a separate-process guarantee. Starting Office with multiple
switches is unsupported. Do not recommend `/x`, combined switches or `/n`
as a guarantee that only task-owned documents are present; verify the actual
document inventory. These observations do not authorize shell launch or focus
workarounds in the Computer Use workflow below.

For content-only field evaluation without a saved copy, keep the Publisher
artifact unchanged:

1. Point `TEMP` and `TMP` at the user's authorized temporary location before
   starting Word, because Word and its exports write temporary files there.
2. Set `AutomationSecurity` to force-disable macros. Open each DOCX read-only,
   invisible and without adding it to the recent-file list.
3. Record the stored results before updating all fields, then every table of
   contents and table of figures. Keep the original artifact unchanged and
   distinguish update-induced changes from the Publisher's stored results.
4. Read the resolved text through Word, or export a PDF and extract its text.
   Search it for Word's error results, such as "Error! Reference source not
   found." and "Error! Bookmark not defined.", in Word's interface language.
   Compare contents and figure-list entries with the composed headings and
   captions, and reread the generated bibliography.
5. Close only verified task-owned documents without saving and quit Word only
   after verifying that the instance contains no other documents. Confirm
   whether a Word process the task started remains; report any ownership or
   cleanup uncertainty instead of assuming it is safe to terminate. Stop an
   authorized leftover only by its recorded process ID.
   Quit only a task-owned instance; never quit a pre-existing user instance.

An exported PDF here is a vehicle for text extraction; its layout stays outside
the review scope. Record its origin and the DOCX hash rather than treating an
export as independent evidence of the original field results.

### Word visual inspection and UI blockers

Use the available Computer Use accessibility workflow when Word visual
inspection is explicitly in scope. Discover its tool schemas through the host,
then use `list_apps` on Windows to select the Word app/window pair and
`get_window_state` to read it. If Word is not running, discover its launch target
with `list_apps(include_launchable=true)` and use `start_app`; do not launch or
focus it through shell or window-manager workarounds during this UI workflow.
Open the verified DOCX read-only through the UI, or use an authorized
task-owned copy as described above. Confirm the full path and artifact hash
before recording evidence, and distinguish a saved field-updated copy from the
Publisher original.

After an Open-dialog action, wait for the actual document window rather than
equating command completion with a completed open. A split Open control can
expand its menu; Return in the filename field can dismiss that menu, and a
subsequent Return can report completion while the dialog is briefly still
visible. These observations are not a prescribed keystroke sequence. Before
retrying an apparently unchanged dialog, let the state settle, enumerate Word
windows again with `list_apps` and read the candidate with `get_window_state`;
the requested document may have opened in a separate window. Re-verify its
full path, artifact hash, part number and title before continuing. Retry only
after fresh state confirms the intended document is not open and the dialog
still targets that artifact. If the Computer Use transport closes, record the
last confirmed window state and exact transport failure, leave unperformed
field and pagination checks unreviewed, and resume with window discovery and
identity verification when the transport is available; an open document alone
does not establish inspection or a publication defect.

For a selected main-story field update, use a task-owned current DOCX copy
whose update and save are authorized by the review contract. In Word Options >
Quick Access Toolbar, set Choose commands from to All Commands and add the
command named `Update` for this document only, not for all documents. Its UIA ID
is `FieldsUpdate`. Before adding or applying a customization, verify that the
document-specific customization target names the intended task-owned copy.
Opening Quick Access Toolbar > More Commands from a background Word window
does not establish the active document: Word Options can offer another open
copy as its target. If the target differs or cannot be verified, cancel without
applying changes and report the intended copy and offered target as a UI
limitation. Re-establish document identity before retrying; do not customize the
other document or assume the targeted window determines the active document.

Use Home > Select > Select All and record the selected and
total word counts from the current state; do not assume selection from command
completion alone.

Dismiss context menus and other open menus before selecting the main story.
If enabling Word Count through the status-bar context menu, close that menu
first, then reselect all. Immediately before invoking `FieldsUpdate`, obtain a
fresh accessibility state that verifies menus are dismissed and shows the
selected and total word counts in the status bar; an earlier count is not
sufficient. If selection is absent or uncertain, reselect and verify it before
retrying. Invoke `FieldsUpdate` through its current accessibility node only
after these checks.

In one current CI DOCX copy, Select All showed 42,699 of 42,699 words, but the
status-bar context menu remained open after enabling Word Count. Activating
`FieldsUpdate` closed the menu; selection was no longer present, Word showed
Repeat Update Fields and all three lists remained placeholders. After
reselecting with the menu closed and verifying the same count in the status
bar, invoking `FieldsUpdate` showed Undo Update Fields and eventually populated
the contents, figures and tables lists. Record these observations without
assuming the first activation updated the intended selection. Neither Repeat
Update Fields nor Undo Update Fields proves list correctness or pagination
coverage; inspect the actual results independently.

Handle each resulting dialog separately, selecting Update entire table and
confirming it before reading the next dialog. One observed sequence was Update
Table of Contents followed by two Update Table of Figures dialogs, for the
figures and tables fields. Record the actual sequence; do not assume every
document produces exactly three prompts or that the shared dialog title
identifies which list is being updated. If the accessible radio-button action
fails with `UIA SelectionItem.Select member not found`, capture a fresh dialog
screenshot and click the option at coordinates from that capture through
Computer Use. Reinspect the dialog to confirm the selection before accepting
it; do not repeat the unsupported action or use stale coordinates.

After the last prompt, record the return to Word and any Undo Update Fields
entry as evidence that the selected main-story update was invoked and the
prompts were handled. Reread the contents, figures and tables lists and remaining
field results independently; invocation evidence does not establish their
correctness. Save only the authorized task-owned copy and record its new hash.
Neither Select All word counts nor this update sequence verifies fields in
headers, footers or other stories, or establishes visual pagination coverage.
Keep those checks separate and retain the per-list Captions fallback above.

Read TextPattern-backed values, Document text, Selected text and Caret text
first. Address actions to the app/window and an `element_index` from the latest
`get_window_state`. Use screenshots only for page geometry or artwork that the
accessibility tree cannot establish, or for the unsupported dialog action
described above, with coordinates taken from that capture.
Inspect the agreed pages in Word's Print Layout view; record the page range and
observations separately from text checks. Neither an accessibility text read nor
a PDF export substitutes for that Word visual inspection. Review is read-only;
do not edit the document to make it inspectable. Check page-edge placement and
cell-level legibility separately; a zoom label alone does not establish that
the visible content enlarged. Match printed page labels to Word's page
identities rather than inferring physical numbers from a multipage grid.

After navigation, compare the page or scroll position in the accessibility
tree with the prior state. A completed background action can become visible
after its first response, so let the view settle and reread it before issuing
another navigation. Record only the pages and regions actually visible; an
unchanged or truncated tree does not establish visual coverage.

If a figure appears blank in a capture, treat that capture as inconclusive.
Refresh the view without editing the document: let Word finish rendering, reread
the current page state, then use a non-editing click in the page or move to
another page and return before capturing it again. Confirm the capture still
shows the intended page and region. Where package inspection is available,
check whether the DOCX contains the referenced media and whether image parts
have non-empty content; both SVG and raster representations may be present.
These checks do not prove that Word rendered the figure. One empty capture does
not prove that the publication omits artwork. Report a missing-figure defect
only when the blank result is reproducible in a refreshed view and the artifact
evidence supports the omission. Otherwise record the capture as transient or
unresolved, with the page, artifact hash and checks performed. If a figure
becomes visible after a non-editing click, the initial blank capture is not a
missing-figure finding. The cause remains unknown, and the click does not
establish full pagination coverage.

If an action returns `interrupted`, reread that app with `get_window_state` and
retry the same action; yield to active user input. When permission, foreground
delivery or document access still prevents inspection, report the exact tool
result, affected artifact hash, attempted action and pages left unreviewed.
State the action needed to resume, such as granting the app permission or opening
the verified DOCX. Do not bypass the host's UI controls with COM activation or
shell focus commands; content-only COM inspection remains a separate evidence
route and cannot close the visual coverage gap.

An installed Word application, a COM automation failure and a blocked UI action
are different observations. Record a genuine UI blocker as a review limitation,
not a publication defect. Continue the accessible content checks and leave the
affected visual cells blocked; use assessment incomplete when the missing
evidence prevents the agreed verdict. Report a publication defect only when
current artifact evidence demonstrates it.

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
