import test from "node:test";
import assert from "node:assert/strict";
import { mkdtemp, mkdir, writeFile, readFile, rm, symlink } from "node:fs/promises";
import path from "node:path";
import os from "node:os";
import { ReviewWorkspace, digest, sourceRange, applyReplacement, addedLines, contained, parseTarget } from "./workspace.mjs";
import { startServer } from "./server.mjs";

async function fixture(t) {
    const root = await mkdtemp(path.join(os.tmpdir(), "opc-review-test-"));
    t.after(() => rm(root, { recursive: true, force: true }));
    const file = "source/Demo/spec.md";
    await mkdir(path.join(root, "source", "Demo"), { recursive: true });
    await mkdir(path.join(root, "_work", "docs", "Demo"), { recursive: true });
    const content = "## Scope {#sec-scope}\r\n\r\nA **bold** requirement.\r\nAnother line.\r\n";
    await writeFile(path.join(root, file), content);
    await writeFile(path.join(root, "source", "Demo", "manifest.json"), "{}");
    await writeFile(path.join(root, "_work", "docs", "Demo", "index.html"), '<html><body><section id="sec_1"><p>A <strong>bold</strong> requirement.</p></section></body></html>');
    const sends = [];
    const workspace = new ReviewWorkspace(root, "feature", async input => { sends.push(input); return "message-1"; }, [{ name: "Demo", main: file }], path.join(root, "state.json"), { version: 1, requests: [], accepted: [] });
    workspace.command = async (program, args) => {
        if (program === "git" && args.join(" ") === "branch --show-current") return "feature\n";
        throw new Error(`Unexpected command ${program} ${args.join(" ")}`);
    };
    const refreshPreview = async () => workspace.previews.set("Demo", { map: { sec_1: { file, line: 1, endLine: 4, generated: false }, sec_2: { file: "source/Demo/manifest.json", line: 1, generated: true } }, files: { [file]: digest(await workspace.source(file)), "source/Demo/manifest.json": digest("{}") }, fingerprint: await workspace.fingerprint("Demo") });
    await refreshPreview();
    const input = { spec: "Demo", anchor: "sec_1", quote: "requirement", sourceHash: digest(content), instruction: "Clarify" };
    return { workspace, root, file, content, sends, refreshPreview, input };
}

test("source ranges preserve CRLF and reject invalid lines", () => {
    assert.deepEqual(sourceRange("one\r\nsecond\nthird", 2, 2), { start: 5, end: 12 });
    assert.throws(() => sourceRange("one", 0, 1), /Invalid/);
    assert.throws(() => sourceRange("one", 1, 2), /Invalid/);
});
test("replacement is hash-guarded and preserves source newline convention", () => {
    const text = "one\r\ntwo\r\n";
    const request = { start: 5, end: 10, original: "two\r\n", replacement: "new\nline\n", sourceHash: digest(text) };
    assert.equal(applyReplacement(text, request), "one\r\nnew\r\nline\r\n");
    assert.throws(() => applyReplacement(text + "external", request), /Source changed/);
});
test("only added PR lines may receive new inline comments", () => {
    assert.deepEqual([...addedLines("@@ -1,3 +1,4 @@\n context\n-old\n+new\n+extra\n tail\n@@ -20 +21 @@\n-x\n+y")], [2, 3, 21]);
    assert.equal(addedLines().size, 0);
});
test("cross-repository targets are structured, not shell commands", () => {
    assert.deepEqual(parseTarget("https://github.com/OPCF-Members/Demo/pull/42"), { repo: "OPCF-Members/Demo", pr: 42 });
    assert.throws(() => parseTarget("https://evil.example/OPCF-Members/Demo/pull/42"), /Enter/);
    assert.throws(() => parseTarget("owner/repo; rm stuff"), /Enter/);
});
test("contained paths reject traversal and junction escape", async t => {
    const { root } = await fixture(t);
    const source = path.join(root, "source");
    await assert.rejects(contained(source, "../_work/docs/Demo/index.html"), /escapes/);
    await symlink(path.join(root, "_work"), path.join(source, "escape"), "junction");
    await assert.rejects(contained(source, "escape/docs/Demo/index.html"), /escapes/);
});
test("exact and formatted selections use reliable source ranges", async t => {
    const { workspace, input } = await fixture(t);
    const exact = await workspace.selection(input);
    assert.equal(exact.original, "requirement"); assert.equal(exact.exact, true); assert.equal(exact.line, 3);
    const formatted = await workspace.selection({ ...input, quote: "A bold requirement." });
    assert.equal(formatted.exact, false); assert.match(formatted.original, /\*\*bold\*\*/);
    assert.equal((await workspace.selection({ spec: "Demo", anchor: "sec_2" })).generated, true);
    await assert.rejects(workspace.createEdit({ ...input, anchor: "sec_2" }, "panel"), /read-only/);
});
test("agent proposals are durable and cannot mutate until accepted; undo restores bytes", async t => {
    const { workspace, input, content, file, root, sends } = await fixture(t);
    const request = await workspace.createEdit(input, "panel-one");
    assert.equal(sends.length, 1);
    assert.match(sends[0].prompt, /panel-one/);
    await workspace.propose({ requestId: request.id, replacement: "rule", explanation: "Clearer" });
    assert.equal(await workspace.source(file), content);
    const persisted = JSON.parse(await readFile(workspace.stateFile, "utf8"));
    const rehydrated = new ReviewWorkspace(root, "feature", workspace.send, workspace.specs, workspace.stateFile, persisted);
    assert.equal(rehydrated.readRequest(request.id).replacement, "rule");
    await workspace.decide(request.id, true);
    assert.equal(await workspace.source(file), content.replace("requirement", "rule"));
    assert.equal(workspace.previews.size, 0);
    await workspace.undo();
    assert.equal(await workspace.source(file), content);
    assert.equal(workspace.readRequest(request.id).status, "undone");
});
test("stale selection, stale proposal and stale undo never overwrite external edits", async t => {
    const { workspace, root, file, input, content, refreshPreview } = await fixture(t);
    const request = await workspace.createEdit({ ...input, replacement: "rule" }, "panel");
    await writeFile(path.join(root, file), content + "external\r\n");
    await assert.rejects(workspace.decide(request.id, true), /Source changed/);
    await refreshPreview();
    await assert.rejects(workspace.createEdit(input, "panel"), /source changed/i);
    await workspace.decide(request.id, false);
    const updated = await workspace.selection(input);
    const second = await workspace.createEdit({ ...input, sourceHash: updated.sourceHash, replacement: "rule" }, "panel");
    await workspace.decide(second.id, true);
    await writeFile(path.join(root, file), "independent change");
    await assert.rejects(workspace.undo(), /Undo refused/);
    assert.equal(await workspace.source(file), "independent change");
});
test("rejected requests cannot be revived by a late agent response", async t => {
    const { workspace, input } = await fixture(t);
    const request = await workspace.createEdit(input, "panel");
    await workspace.decide(request.id, false);
    await assert.rejects(workspace.propose({ requestId: request.id, replacement: "late", explanation: "Late" }), /no longer/);
});
test("failed session dispatch is persisted explicitly and does not leave a phantom queue", async t => {
    const { workspace, input } = await fixture(t);
    workspace.send = async () => { throw new Error("Disconnected"); };
    await assert.rejects(workspace.createEdit(input, "panel"), /Disconnected/);
    const saved = JSON.parse(await readFile(workspace.stateFile, "utf8"));
    assert.equal(saved.requests[0].status, "failed");
    assert.match(saved.requests[0].message, /Could not send/);
});
test("manual invalid input cannot persist a queued rewrite", async t => {
    const { workspace, input } = await fixture(t);
    await assert.rejects(workspace.createEdit({ ...input, replacement: 123 }, "panel"), /Invalid replacement/);
    assert.equal(workspace.state.requests.length, 0);
});
test("questions persist context and answers without changing source, then explicitly become edit proposals", async t => {
    const { workspace, input, file, content, sends } = await fixture(t);
    const question = await workspace.createQuestion({ ...input, instruction: "What is this?", renderedText: "A bold requirement." }, "panel");
    assert.equal(question.kind, "question");
    assert.equal(question.quote, "requirement");
    assert.match(question.context, /\*\*bold\*\*/);
    assert.match(sends[0].prompt, /not for a rewrite/);
    assert.match(sends[0].prompt, /report_request/);
    await assert.rejects(workspace.propose({ requestId: question.id, replacement: "rule", explanation: "No" }), /no longer/);
    await assert.rejects(workspace.decide(question.id, true), /Questions cannot/);
    await workspace.report({ requestId: question.id, message: "This is a normative requirement." });
    assert.equal(await workspace.source(file), content);
    const followup = await workspace.createQuestion({ parentId: question.id, instruction: "Why is it needed?" }, "panel");
    assert.deepEqual(followup.discussion, [{ question: "What is this?", answer: "This is a normative requirement." }]);
    assert.equal(followup.original, question.original);
    await workspace.report({ requestId: followup.id, message: "It defines interoperable behaviour." });
    const draft = await workspace.createEdit({ questionId: followup.id, instruction: "Clarify it using that explanation." }, "panel");
    assert.equal(draft.kind, "edit");
    assert.equal(draft.discussion.length, 2);
    assert.equal(draft.questionId, followup.id);
    assert.equal(draft.start, question.start);
    await workspace.propose({ requestId: draft.id, replacement: "interoperability requirement", explanation: "Clarified intent." });
    assert.equal(await workspace.source(file), content);
    await workspace.decide(draft.id, true);
    assert.equal(await workspace.source(file), content.replace("requirement", "interoperability requirement"));
    const persisted = JSON.parse(await readFile(workspace.stateFile, "utf8"));
    assert.equal(persisted.requests[0].message, "This is a normative requirement.");
});
test("questions allow read-only generated content but cannot convert it to a Markdown edit", async t => {
    const { workspace } = await fixture(t);
    const question = await workspace.createQuestion({ spec: "Demo", anchor: "sec_2", quote: "Overview", renderedText: "Generated overview", sourceHash: digest("{}"), instruction: "Explain this." }, "panel");
    assert.equal(question.generated, true);
    await workspace.report({ requestId: question.id, message: "The manifest supplies this." });
    await assert.rejects(workspace.createEdit({ questionId: question.id, instruction: "Rewrite" }, "panel"), /read-only/);
});
test("old question answers cannot silently target changed source, and cancellation rejects late answers", async t => {
    const { workspace, input, root, file, content, refreshPreview } = await fixture(t);
    const question = await workspace.createQuestion({ ...input, renderedText: "requirement" }, "panel");
    await workspace.decide(question.id, false);
    await assert.rejects(workspace.report({ requestId: question.id, message: "Late" }), /not queued/);
    const second = await workspace.createQuestion({ ...input, renderedText: "requirement" }, "panel");
    await workspace.report({ requestId: second.id, message: "Answer" });
    await writeFile(path.join(root, file), content + "New text.\r\n");
    await refreshPreview();
    await assert.rejects(workspace.createQuestion({ parentId: second.id, instruction: "Explain more." }, "panel"), /source changed since/);
    await assert.rejects(workspace.createEdit({ questionId: second.id, instruction: "Make clearer." }, "panel"), /source changed since/);
});
test("source-map fingerprint detects model and figure changes", async t => {
    const { workspace, root, input } = await fixture(t);
    await writeFile(path.join(root, "source", "Demo", "figure.drawio"), "<mxfile/>");
    await assert.rejects(workspace.selection(input), /stale/);
});
test("explicit publication consent and successful current render are required", async t => {
    const { workspace, input } = await fixture(t);
    await assert.rejects(workspace.agentOperation({ kind: "publish" }, "panel"), /consent/);
    const request = await workspace.createEdit({ ...input, replacement: "rule" }, "panel");
    await assert.rejects(workspace.agentOperation({ kind: "publish", confirm: true }, "panel"), /pending drafts/);
    await workspace.decide(request.id, true);
    await assert.rejects(workspace.agentOperation({ kind: "publish", confirm: true }, "panel"), /Build the preview/);
});
test("GitHub inline comments are rejected on context lines and accepted on added lines", async t => {
    const { workspace, input, file, content } = await fixture(t);
    workspace.prInfo = async () => ({ repo: "owner/repo", pr: { number: 9, head: "abc" } });
    workspace.command = async (_, args) => args[0] === "rev-parse" ? "abc\n" : content;
    workspace.pages = async () => [{ filename: file, patch: "@@ -1,4 +1,4 @@\n heading\n blank\n+changed\n end" }];
    let posted;
    workspace.api = async (endpoint, body) => { posted = { endpoint, body }; return { id: 11 }; };
    await workspace.postComment({ ...input, kind: "inline", body: "Comment", prNumber: 9 });
    assert.equal(posted.body.line, 3); assert.equal(posted.body.commit_id, "abc");
    await assert.rejects(workspace.postComment({ ...input, quote: "", kind: "inline", body: "Comment", prNumber: 9 }), /not an added/);
});
test("reply uses the PR review thread endpoint and general comment uses the conversation endpoint", async t => {
    const { workspace } = await fixture(t);
    workspace.prInfo = async () => ({ repo: "owner/repo", pr: { number: 9, head: "abc" } });
    workspace.pages = async () => [{ id: 101 }, { id: 102, in_reply_to_id: 101 }];
    const calls = [];
    workspace.api = async (endpoint, body) => { calls.push({ endpoint, body }); return { id: 103 }; };
    await workspace.postComment({ kind: "reply", body: "Reply", prNumber: 9, rootId: 101 });
    assert.equal(calls[0].endpoint, "repos/owner/repo/pulls/9/comments/101/replies");
    await assert.rejects(workspace.postComment({ kind: "reply", body: "Reply", prNumber: 9, rootId: 102 }), /Thread root/);
    await workspace.postComment({ kind: "general", body: "General", prNumber: 9 });
    assert.equal(calls[1].endpoint, "repos/owner/repo/issues/9/comments");
});
test("loopback HTTP requires origin/token, serves actual publication assets with script sandbox", async t => {
    const { workspace } = await fixture(t);
    const server = await startServer(workspace, "Demo", "panel");
    t.after(() => server.close());
    const url = new URL(server.url), token = url.pathname.split("/")[1];
    const app = await fetch(server.url);
    assert.equal(app.status, 200); assert.match(await app.text(), /Specification review/);
    const invalid = await fetch(new URL("api/status", server.url), { method: "POST", headers: { "Content-Type": "application/json" }, body: "{}" });
    assert.equal(invalid.status, 400);
    const status = await fetch(new URL("api/status", server.url), { method: "POST", headers: { "Content-Type": "application/json", "Origin": url.origin, "X-Review-Key": token }, body: "{}" });
    assert.equal(status.status, 200); assert.equal((await status.json()).branch, "feature");
    const html = await fetch(new URL("render/Demo/index.html", server.url));
    assert.equal(html.status, 200); assert.match(html.headers.get("content-security-policy"), /script-src 'none'/);
    assert.match(html.headers.get("content-security-policy"), /sandbox allow-same-origin/);
    assert.match(await html.text(), /id="review-preview-light"/);
    assert.doesNotMatch(await readFile(path.join(workspace.root, "_work", "docs", "Demo", "index.html"), "utf8"), /review-preview-light/, "Serving light mode must not modify generated HTML");
    assert.equal((await fetch(new URL("workspace.mjs", server.url))).status, 400);
    assert.equal((await fetch(new URL("render/Demo/spec.md", server.url))).status, 400);
});
