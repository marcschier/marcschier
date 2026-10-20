# OPC specification review canvas

A user-scoped Copilot canvas for repositories using the OPC Foundation
`Opc.Ua.SpecificationPublisher` Markdown authoring pipeline. Open canvas type
`opc-spec-review` in the repository's **isolated project session**, with optional
input `{ "spec": "WoT-Binding" }`.

## In-canvas help and appearance

Open **Help** in the review sidebar for the workflow guide. Its expandable
sections cover selecting content, questions and follow-ups, manual and assisted
edits, draft acceptance and undo, PR comments, publishing, other repositories,
troubleshooting and privacy. The guide is available even if the publisher fails.

Drag the divider between the rendered document and the review sidebar **left**
to widen the editing panel, or right to give the preview more space. The divider
also supports keyboard focus: Left/Right resize by 10 pixels (50 with Shift),
and Home/End select the minimum/maximum editing width. Both panes keep usable
minimum widths. The chosen split remains while switching tabs and rebuilding
previews; narrow windows use the stacked layout instead. Reopening the canvas
starts with the default split.

The rendered specification always uses the publisher's **light** palette,
regardless of the operating system or Copilot theme. This includes text, links,
tables, code blocks and browser-native controls. The surrounding canvas controls
still follow the app theme. The override is applied to the served preview before
first paint; it does not modify generated files, source documents, figure artwork
or the deployed GitHub Pages theme.

## Install from this repository

Ask Copilot to install this extension in **User** scope so it is available
across your specification repositories:

> Install the extension from this repository folder in user scope:
> https://github.com/marcschier/marcschier/tree/main/extensions/opc-spec-review

Open an isolated project session for a supported specification repository, then ask:

> Open the OPC specification review canvas.

Use a Copilot host with extension canvas support; this is not a standalone web
application or a VS Code extension. The host supplies `@github/copilot-sdk`.
The repository also needs its .NET SDK and restored pinned publisher, plus Git
and an authenticated GitHub CLI (`gh`). Each user supplies their own credentials.

This distribution contains only extension code, documentation and synthetic
tests, not review history, undo snapshots, credentials or specification files.
Review history and undo snapshots are local-only; keep the generated
`artifacts/` directory out of any shared copy.

## Review and edit

1. Opening the canvas builds the initial preview and loads PR comments. Choose
   another specification and **Build preview** to switch. The repository's pinned publisher
   runs `dotnet Opc.Ua.SpecificationPublisher html --spec <name>` and supplies both
   the HTML and `.stsmap.json` source map under `_work/docs/`. This uses the same
   rendering pipeline as publication, including generated clauses, numbering,
   node tables and inline draw.io SVG figures.
2. Select rendered prose, or click its source pencil. Plain selections that match
   uniquely map exactly; selections spanning Markdown formatting use the containing
   mapped block, with the selected quote retained for the agent. Cross-block
   selections are rejected rather than guessed.
3. Edit the mapped Markdown and **Stage manual draft**, or enter an instruction and
   **Request rewrite**. Copilot receives a request in the existing session and
   responds through the canvas `read_request` / `propose_edit` actions.
4. Review the before/after changes in **Drafts**. **Accept locally** writes the
   source range and rebuilds. **Reject** never writes. **Undo accepted edit**
   restores the last canvas edit only if no intervening edit would be overwritten.
   Staging and accepting drafts, rebuilding the preview, and undoing an edit keep
   the reader at the current content rather than jumping to the top. Restoration
   follows the nearby clause and text across renumbering or insertions above it;
   if that content disappears, it falls back to the previous pixel position.
5. **Publish to PR** explicitly authorizes the session agent to validate, commit
   and push the accepted source changes, and create a PR if this branch has none.
   PR creation follows the repository template and the app's PR-creation tool.
   No push happens on open, selection, save, proposal, or acceptance.

Generated content and publisher-managed agreement text are read-only. Their mapped
owner is shown rather than pretending generated HTML is authored Markdown.
The cross-reference picker offers source anchors, not renumbered publication IDs.
Publisher output, including failures, is visible under **Tools**.

## Ask about selected content

Highlight text or select a section with its source pencil, enter a question, and
choose **Ask about selection**. **Explain** and **What is this?** fill in common
questions. Copilot explains the selection without modifying files or creating a
rewrite proposal. Questions also work on read-only generated content.

Answers appear in **Drafts and activity**, alongside the original question and
source location. Enter a follow-up and choose **Ask follow-up**, or describe a
desired change and choose **Request change from answer**. A change request carries
the original selection and the question/answer history into a separate proposal,
which still needs explicit acceptance. Generated content remains read-only.
If the source has changed since the question, follow-ups and edits are refused
until you select the current text again. **Cancel question** rejects a queued
answer without changing files.

Questions and answers are persisted with the other review requests. The agent
reads them using `read_request`, answers through `report_request`, and uses
`propose_edit` only for an explicitly requested rewrite.

## GitHub review

**PR comments / Refresh** reads the open PR for this checkout's origin and branch,
including inline threads, replies, general comments and review summaries. All
pages are fetched. Current inline comments appear beside the mapped clause when
the local file matches the PR head. Outdated, deletion-side and locally diverged
comments remain in the sidebar without misleading inline placement.

Post a general comment, reply to a thread, or comment on selected changed text.
Posting requires explicit confirmation. New inline comments require an added PR
line, a local HEAD equal to the remote PR head and no local change in that source
file. The UI does not silently fall back to a general comment if an inline
placement fails. REST does not expose resolved-thread status, so the canvas
neither labels threads unresolved nor offers an unsupported resolve toggle.

**Tools / Repository / PR** accepts `owner/repository` or a GitHub PR URL. It asks
Copilot to open an isolated session there and open this user extension. It never
switches this checkout to another PR. Publishing and cross-repository opening
are agent-assisted operations; their completion or blockers are reported in the
session and Drafts. They are not claimed successful when merely queued.

## Storage and safety

Drafts, proposals and undo snapshots live in this extension's
`artifacts/<SHA256 of real checkout path and branch>/state.json`. They survive
panel/provider/app reloads and use the document file/range identity rather than a
panel ID. Unstaged textarea edits are transient: stage a draft before closing.
The active preview is deliberately rebuilt after provider restart.
Draft/undo artifacts contain private specification text; exclude `artifacts/`
if you distribute a copy of the extension.

File hashes prevent stale proposals or undo from overwriting external changes.
A source/model/figure fingerprint prevents editing against stale publication
maps. An interrupted acceptance retains recovery data; Undo can restore it when
the file still matches the recorded before/after bytes.

The renderer serves only local loopback assets, with a random per-panel URL
capability and same-origin, token-checked POST APIs. Published HTML is in a
script-disabled sandbox; remote images, frames and scripts are blocked. No source
or diagram is uploaded to an external rendering service. Explicit GitHub actions
use the locally authenticated `gh` CLI; credentials never reach the browser.
Copilot assistance uses the already-open session, its model and its permissions.

## Requirements and limitations

- An installed .NET SDK, the repository's restored **pinned** publisher, Git and
  authenticated `gh`. Restore missing tools with `dotnet tool restore` in the
  intended checkout. The extension does not silently install or upgrade them.
- Publisher HTML/source-map schema 1 and `source/<spec>/manifest.json`. Repositories
  without this pipeline fail explicitly rather than showing a generic Markdown
  preview as though it were the publication.
- GitHub.com origin remotes and a named branch. Forks should be opened in the
  appropriate upstream PR session; automatic cross-fork PR discovery is not
  currently implemented.
- The canvas edits authored Markdown blocks beside the real rendering. It does
  not round-trip arbitrary `contenteditable` HTML, edit generated node tables, or
  provide a draw.io diagram editor. Figures are rendered by the publisher.
- Publisher scripts are disabled in the embedded page. Static publication layout,
  figures and native anchor navigation work; script-based publication widgets do
  not run. External assets are intentionally blocked.
- Existing comments render as escaped text, preserving their Markdown source,
  not as executable HTML.
- A failed/blocked agent publication is reported, not retried automatically.
  Queued agent work can be processed after the current turn ends.

## Development

The SDK is provided by Copilot; no npm dependencies or SDK package install are
needed. After editing, call `extensions_reload`, inspect `opc-spec-review`, and
re-open the canvas. Unit/HTTP tests: `node --test workspace.test.mjs`.
Browser regression: `node --test browser.test.mjs` (Node 22+ and Microsoft Edge on
Windows, or set `REVIEW_TEST_BROWSER` to a Chromium executable). It exercises the
real UI and workspace against a temporary specification with a deterministic
publisher fixture, never altering the working specification or contacting GitHub.

Useful next additions: a base-versus-PR rendered comparison; cross-spec reference
and terminology checks; normative-language diagnostics; figure change overlays;
NodeSet-aware completion; and navigation from publisher diagnostics to exact
source lines. These are suggestions, not implemented features.
