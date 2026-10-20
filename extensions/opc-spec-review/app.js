const $ = id => document.getElementById(id);
const token = location.pathname.split("/")[1];
const base = `/${token}/`;
let state, preview, selected, discussion, threadRoot, draftsSignature = "", currentSpec, busy = false;
let renderedPreview, renderedSpec, restorePosition;
const readerPositions = new Map();
const frame = $("document");
const pending = new Set(["queued", "proposed", "applying"]);
const layout = document.querySelector("main");
const divider = $("panel-divider");
let panelWidth = 390, panelDrag;
function panelLimits() {
    return { min: 320, max: Math.max(320, layout.clientWidth - 350 - divider.offsetWidth) };
}
function sizePanel(width = panelWidth) {
    const { min, max } = panelLimits();
    const clamped = Math.round(Math.max(min, Math.min(max, width)));
    layout.style.setProperty("--review-panel-width", `${clamped}px`);
    divider.setAttribute("aria-valuemax", String(max));
    divider.setAttribute("aria-valuenow", String(clamped));
    divider.setAttribute("aria-valuetext", `Editing panel ${clamped} pixels wide`);
    return clamped;
}
function finishPanelDrag() {
    if (!panelDrag) return;
    const { pointerId } = panelDrag;
    panelDrag = null;
    document.body.classList.remove("resizing-panel");
    if (divider.hasPointerCapture(pointerId)) divider.releasePointerCapture(pointerId);
}
divider.addEventListener("pointerdown", event => {
    if (event.button !== 0 || panelDrag) return;
    event.preventDefault();
    divider.focus({ preventScroll: true });
    panelDrag = { pointerId: event.pointerId, x: event.clientX, width: $("review-panel").getBoundingClientRect().width };
    divider.setPointerCapture(event.pointerId);
    document.body.classList.add("resizing-panel");
});
window.addEventListener("pointermove", event => {
    if (panelDrag?.pointerId === event.pointerId) panelWidth = sizePanel(panelDrag.width + panelDrag.x - event.clientX);
});
for (const type of ["pointerup", "pointercancel", "lostpointercapture"]) {
    window.addEventListener(type, event => { if (panelDrag?.pointerId === event.pointerId) finishPanelDrag(); });
}
window.addEventListener("blur", finishPanelDrag);
divider.addEventListener("keydown", event => {
    const { min, max } = panelLimits();
    const width = $("review-panel").getBoundingClientRect().width;
    const step = event.shiftKey ? 50 : 10;
    const sizes = { ArrowLeft: width + step, ArrowRight: width - step, Home: min, End: max };
    if (!(event.key in sizes)) return;
    event.preventDefault();
    panelWidth = sizePanel(sizes[event.key]);
});
new ResizeObserver(() => {
    if (!divider.offsetWidth) finishPanelDrag();
    sizePanel();
}).observe(layout);
function ownerOf(node, map) {
    for (let value = node; value; value = value.parentElement) if (value.id && map[value.id]) return value;
    return null;
}
function headingText(owner) {
    const heading = owner.querySelector("h2,h3,h4,h5,h6,figcaption,caption")?.cloneNode(true);
    heading?.querySelectorAll(".label,.src,[data-thread-id]").forEach(node => node.remove());
    return heading?.textContent.trim() ?? "";
}
function readerBlocks(owner, map) {
    return [...owner.querySelectorAll("h2,h3,h4,h5,h6,p,li,pre,table,figure")]
        .filter(node => !node.closest("nav,header") && ownerOf(node, map) === owner);
}
function captureReader() {
    const doc = frame.contentDocument, win = frame.contentWindow;
    if (frame.hidden || !renderedPreview || !doc?.body) return null;
    const map = renderedPreview.map;
    const blocks = [...doc.querySelectorAll("h2,h3,h4,h5,h6,p,li,pre,table,figure")]
        .filter(node => !node.closest("nav,header") && ownerOf(node, map) && node.getBoundingClientRect().bottom > 0);
    blocks.sort((a, b) => Math.abs(a.getBoundingClientRect().top) - Math.abs(b.getBoundingClientRect().top));
    const block = blocks[0], owner = block && ownerOf(block, map);
    return {
        x: win.scrollX, y: win.scrollY, outerX: window.scrollX, outerY: window.scrollY,
        file: owner && map[owner.id].file, heading: owner && headingText(owner),
        text: block?.textContent.trim(), tag: block?.tagName,
        index: owner ? readerBlocks(owner, map).indexOf(block) : -1,
        offset: block?.getBoundingClientRect().top,
        toc: doc.querySelector(".toc")?.scrollTop ?? 0,
    };
}
function restoreReader(position) {
    if (!position || !renderedPreview) return;
    const doc = frame.contentDocument, win = frame.contentWindow;
    let y = position.y;
    const owners = Object.entries(renderedPreview.map)
        .filter(([, location]) => location.file === position.file)
        .map(([id]) => doc.getElementById(id))
        .filter(owner => owner && headingText(owner) === position.heading);
    if (owners.length === 1) {
        const blocks = readerBlocks(owners[0], renderedPreview.map);
        const matches = blocks.filter(node => node.tagName === position.tag && node.textContent.trim() === position.text);
        const block = matches.length === 1 ? matches[0] : blocks[position.index];
        if (block) y = win.scrollY + block.getBoundingClientRect().top - position.offset;
    }
    win.scrollTo({ left: position.x, top: y, behavior: "instant" });
    const toc = doc.querySelector(".toc");
    if (toc) toc.scrollTop = position.toc;
    window.scrollTo({ left: position.outerX, top: position.outerY, behavior: "instant" });
}
function notice(message, error = false) { $("notice").textContent = message; $("notice").classList.toggle("error", error); }
function tab(name) {
    document.querySelectorAll(".tab").forEach(item => { item.hidden = item.id !== `tab-${name}`; });
    document.querySelectorAll("[data-tab]").forEach(item => item.classList.toggle("active", item.dataset.tab === name));
}
async function api(action, input = {}) {
    const response = await fetch(`${base}api/${action}`, { method: "POST", headers: { "Content-Type": "application/json", "X-Review-Key": token }, body: JSON.stringify(input) });
    const result = await response.json();
    if (!response.ok) throw new Error(result.error ?? `HTTP ${response.status}`);
    return result;
}
function run(action) { return async event => { try { await action(event); } catch (error) { notice(error.message, true); } }; }
function element(tag, text, className) {
    const node = document.createElement(tag);
    if (text !== undefined) node.textContent = text;
    if (className) node.className = className;
    return node;
}
function button(text, action) { const node = element("button", text); node.addEventListener("click", run(action)); return node; }
function link(text, url) {
    const node = element("a", text);
    if (typeof url === "string" && url.startsWith("https://github.com/")) { node.href = url; node.target = "_blank"; node.rel = "noopener noreferrer"; }
    return node;
}
function confirmAction(title, text) {
    $("confirm-title").textContent = title; $("confirm-text").textContent = text;
    const dialog = $("confirm-dialog");
    dialog.showModal();
    return new Promise(resolve => {
        const done = value => { dialog.close(); $("confirm-yes").onclick = null; $("confirm-cancel").onclick = null; dialog.oncancel = null; resolve(value); };
        $("confirm-yes").onclick = () => done(true); $("confirm-cancel").onclick = () => done(false);
        dialog.oncancel = event => { event.preventDefault(); done(false); };
    });
}
async function refresh() {
    state = await api("status");
    $("repository").textContent = `${state.root} | ${state.branch}`;
    $("undo").disabled = !state.undoAvailable;
    $("diagnostics").textContent = state.lastBuild?.output ?? "No build run yet.";
    $("draft-count").textContent = state.requests.filter(item => pending.has(item.status)).length || "";
    if (preview && !state.previews.includes(currentSpec)) {
        preview = null;
        $("preview-status").textContent = "Stale - rebuild before editing";
        $("ask").disabled = $("rewrite").disabled = $("manual").disabled = true;
    }
    const signature = JSON.stringify(state.requests);
    if (signature !== draftsSignature) { draftsSignature = signature; await renderDrafts(); }
}
async function build() {
    if (busy) return;
    busy = true; $("build").disabled = true;
    $("spec").disabled = true;
    for (const thread of discussion?.threads ?? []) thread.canPin = false;
    notice("Rendering with the repository's pinned specification publisher...");
    try {
        preview = await api("build", { spec: currentSpec });
        selected = null; $("source").value = ""; $("source").disabled = true;
        $("ask").disabled = $("rewrite").disabled = $("manual").disabled = true;
        $("selection-meta").textContent = "Highlight rendered text or click a source pencil.";
        $("quote").hidden = true;
        if (renderedSpec && !frame.hidden) readerPositions.set(renderedSpec, captureReader());
        $("welcome").hidden = true; frame.hidden = false;
        restorePosition = readerPositions.get(currentSpec);
        await new Promise((resolve, reject) => {
            const loaded = () => { clearTimeout(timer); resolve(); };
            const timer = setTimeout(() => { frame.removeEventListener("load", loaded); reject(new Error("Preview page did not finish loading.")); }, 60000);
            frame.addEventListener("load", loaded, { once: true });
            frame.src = `${base}render/${encodeURIComponent(currentSpec)}/index.html?v=${Date.now()}`;
        });
        $("preview-status").textContent = `Built ${new Date(preview.built).toLocaleTimeString()}`;
        notice("Preview ready. Select text to propose a rewrite; click a source pencil to edit its Markdown block.");
    } catch (error) {
        preview = null; $("preview-status").textContent = "Build failed - preview not editable";
        $("ask").disabled = $("rewrite").disabled = $("manual").disabled = true;
        throw error;
    } finally { busy = false; $("build").disabled = false; $("spec").disabled = false; await refresh(); }
}
function mapped(node) {
    if (!preview) return null;
    let value = node?.nodeType === Node.ELEMENT_NODE ? node : node?.parentElement;
    while (value) { if (value.id && preview.map[value.id]) return value.id; value = value.parentElement; }
    return null;
}
async function select(anchor, quote = "") {
    if (!preview) throw new Error("Rebuild the preview before editing.");
    selected = await api("selection", { spec: currentSpec, anchor, quote });
    $("source").value = selected.original;
    $("source").disabled = selected.generated;
    $("selection-meta").textContent = `${selected.file}:${selected.line}${selected.endLine ? `-${selected.endLine}` : ""}${selected.generated ? " | GENERATED: edit its owning source, not rendered text." : ""}`;
    $("selection-kind").textContent = selected.generated ? "(read-only owner)" : selected.exact ? "(exact selection)" : "(mapped block)";
    $("quote").textContent = quote; $("quote").hidden = !quote;
    $("rewrite").disabled = $("manual").disabled = selected.generated;
    $("ask").disabled = false;
    tab("edit");
    const anchorSelect = $("anchors");
    anchorSelect.replaceChildren(new Option("Insert cross-reference...", ""));
    // Only source anchors are offered; publication IDs are renumbered and must not be authored.
    for (const anchor of preview.anchors ?? []) anchorSelect.add(new Option(anchor, anchor));
    if (!selected.generated && !selected.exact && quote) notice("Formatted selection could not be mapped exactly. The complete mapped block is shown; Copilot will target the highlighted quote within it.");
}
frame.addEventListener("load", run(async () => {
    const doc = frame.contentDocument;
    if (!doc || !preview) return;
    renderedPreview = preview; renderedSpec = currentSpec;
    doc.addEventListener("mouseup", run(async () => {
        const selection = frame.contentWindow.getSelection();
        if (!selection || selection.isCollapsed || !selection.toString().trim()) return;
        const anchor = mapped(selection.anchorNode);
        if (!anchor || anchor !== mapped(selection.focusNode)) { notice("Select text within one mapped clause, table or figure.", true); return; }
        await select(anchor, selection.toString());
    }));
    doc.addEventListener("click", run(async event => {
        const source = event.target.closest("a.src");
        const badge = event.target.closest("[data-thread-id]");
        if (badge) { event.preventDefault(); tab("comments"); document.getElementById(`thread-${badge.dataset.threadId}`)?.scrollIntoView({ block: "center" }); return; }
        if (source) {
            event.preventDefault();
            const anchor = mapped(source);
            if (anchor) await select(anchor);
            else notice("No source mapping for this content.", true);
            return;
        }
        const anchor = event.target.closest("a[href]");
        if (anchor && !anchor.getAttribute("href").startsWith("#")) {
            event.preventDefault();
            const href = anchor.getAttribute("href");
            if (/^https?:\/\//i.test(href)) window.open(href, "_blank", "noopener,noreferrer");
            else notice("This link leaves the specification. Open the corresponding specification using the selector.");
        }
    }));
    decorateComments();
    restoreReader(restorePosition);
    restorePosition = null;
}));
function decorateComments() {
    const doc = frame.contentDocument;
    if (!doc || !preview) return;
    const position = captureReader();
    doc.querySelectorAll("[data-thread-id]").forEach(node => node.remove());
    for (const thread of discussion?.threads ?? []) {
        if (thread.outdated || !thread.canPin || thread.side === "LEFT" || !thread.line) continue;
        const candidates = Object.entries(preview.map).filter(([, value]) => value.file === thread.path && value.line <= thread.line && (value.endLine ?? value.line) >= thread.line);
        candidates.sort((a, b) => ((a[1].endLine ?? a[1].line) - a[1].line) - ((b[1].endLine ?? b[1].line) - b[1].line));
        const owner = doc.getElementById(candidates[0]?.[0]);
        if (!owner) continue;
        const badge = doc.createElement("button");
        badge.textContent = `PR comment: ${thread.author}`;
        badge.dataset.threadId = String(thread.id);
        badge.title = thread.body.slice(0, 300);
        (owner.querySelector("h2,h3,h4,h5,h6,figcaption,caption") ?? owner).append(badge);
    }
    restoreReader(position);
}
async function requestEdit(manual) {
    if (!selected || selected.generated) throw new Error("Select authored Markdown first.");
    const instruction = manual ? "Manual source edit" : $("instruction").value.trim();
    if (!instruction) throw new Error("Describe the requested rewrite.");
    await api("edit", {
        spec: currentSpec, anchor: selected.anchor, quote: selected.quote, sourceHash: selected.sourceHash, instruction,
        ...(manual ? { replacement: $("source").value } : {}),
    });
    notice(manual ? "Manual draft staged. Review and accept it in Drafts." : "Rewrite queued in your Copilot session. Its proposal will appear in Drafts.");
    tab("drafts"); await refresh();
}
async function askSelection() {
    if (!selected) throw new Error("Select specification text first.");
    const instruction = $("instruction").value.trim();
    if (!instruction) throw new Error("Enter a question about the selection.");
    const renderedText = frame.contentDocument.getElementById(selected.anchor)?.innerText ?? selected.quote;
    await api("question", { spec: currentSpec, anchor: selected.anchor, quote: selected.quote, sourceHash: selected.sourceHash, instruction, renderedText });
    notice("Question queued. Its answer will appear in Drafts; no source changes will be made.");
    tab("drafts"); await refresh();
}
function diff(before, after) {
    const old = before.split("\n"), next = after.split("\n");
    let start = 0, end = 0;
    while (start < old.length && start < next.length && old[start] === next[start]) start++;
    while (end < old.length - start && end < next.length - start && old[old.length - 1 - end] === next[next.length - 1 - end]) end++;
    const block = element("div", undefined, "diff");
    block.append(element("p", `Changed range (${start} unchanged leading, ${end} trailing lines omitted)`, "hint"));
    block.append(element("pre", old.slice(start, old.length - end).map(line => `- ${line}`).join("\n") || "(no removed lines)", "before"));
    block.append(element("pre", next.slice(start, next.length - end).map(line => `+ ${line}`).join("\n") || "(no added lines)", "after"));
    return block;
}
async function renderDrafts() {
    const container = $("drafts");
    const inputs = new Map([...container.querySelectorAll("[data-question-input]")].map(node => [node.dataset.questionInput, node.value]));
    const focusedId = document.activeElement?.dataset.questionInput;
    const caret = focusedId ? [document.activeElement.selectionStart, document.activeElement.selectionEnd] : null;
    container.replaceChildren();
    if (!state.requests.length) container.append(element("p", "No drafts yet.", "muted"));
    for (const item of [...state.requests].reverse()) {
        const card = element("article", undefined, "card");
        card.append(element("div", `${item.status.toUpperCase()} | ${item.kind}`, "meta"));
        card.append(element("p", item.instruction));
        if (item.file) card.append(element("p", `${item.file}:${item.line}`, "meta"));
        if (item.message) card.append(element("p", item.message, "body"));
        if (item.explanation) card.append(element("p", item.explanation));
        if (item.kind === "question" && item.status === "completed") {
            const request = await api("request", { id: item.id });
            const followup = element("textarea");
            followup.dataset.questionInput = item.id; followup.rows = 3;
            followup.setAttribute("aria-label", "Follow-up question or requested change");
            followup.placeholder = "Ask another question, or describe the change you want based on this answer.";
            followup.value = inputs.get(item.id) ?? "";
            card.append(followup);
            card.append(button("Ask follow-up", async () => {
                if (!followup.value.trim()) throw new Error("Enter a follow-up question.");
                await api("question", { parentId: item.id, instruction: followup.value.trim() });
                followup.value = ""; await refresh(); notice("Follow-up queued with this selection and its discussion history.");
            }));
            if (!request.generated) card.append(button("Request change from answer", async () => {
                if (!followup.value.trim()) throw new Error("Describe the change you want based on the answer.");
                await api("edit", { questionId: item.id, instruction: followup.value.trim() });
                followup.value = ""; await refresh(); notice("Change requested with the explanation as context. Review its proposal before accepting.");
            }));
            else card.append(element("p", "You can ask follow-ups about generated content. To change it, edit its owning manifest or model through the source workflow.", "hint"));
        }
        if (item.status === "proposed") {
            const request = await api("request", { id: item.id });
            card.append(diff(request.original, request.replacement));
            const detail = element("details"); detail.append(element("summary", "Full replacement Markdown"), element("pre", request.replacement)); card.append(detail);
            card.append(button("Accept locally", async () => {
                await api("decide", { id: item.id, accept: true });
                notice("Accepted locally. Rebuilding the published preview...");
                currentSpec = item.spec; $("spec").value = currentSpec;
                await build(); if (discussion) await loadComments(); await refresh();
            }));
        }
        if (item.kind === "edit" && ["queued", "proposed"].includes(item.status)) card.append(button("Reject", async () => { await api("decide", { id: item.id, accept: false }); await refresh(); }));
        if (item.kind === "question" && item.status === "queued") card.append(button("Cancel question", async () => { await api("decide", { id: item.id, accept: false }); await refresh(); }));
        if (item.status === "applying") card.append(element("p", "An interrupted save may have occurred. Undo accepted edit can recover it if no external edit intervened."));
        container.append(card);
    }
    if (focusedId) {
        const input = [...container.querySelectorAll("[data-question-input]")].find(node => node.dataset.questionInput === focusedId);
        input?.focus({ preventScroll: true });
        input?.setSelectionRange(...caret);
    }
}
async function loadComments() {
    notice("Loading GitHub PR comments...");
    discussion = await api("comments");
    const info = $("pr-info");
    info.replaceChildren();
    if (discussion.pr) info.append(link(`#${discussion.pr.number}: ${discussion.pr.title}`, discussion.pr.url), element("p", discussion.note, "hint"));
    else info.textContent = "No open PR for this branch. Accept an edit, rebuild, then Publish to PR to create one.";
    const container = $("comments"); container.replaceChildren();
    for (const thread of discussion.threads) {
        const card = element("article", undefined, "card"); card.id = `thread-${thread.id}`;
        card.append(link(`${thread.author} | ${thread.path}:${thread.line ?? thread.originalLine ?? "file"}`, thread.url));
        if (thread.outdated || thread.side === "LEFT") card.append(element("p", "Outdated or deletion-side: not pinned to current prose.", "hint"));
        else if (!thread.canPin) card.append(element("p", "Local source differs from the PR: not pinned until published or synced.", "hint"));
        card.append(element("p", thread.body, "body"));
        for (const reply of thread.replies) { const node = element("div", undefined, "reply"); node.append(element("p", reply.author, "meta"), element("p", reply.body, "body")); card.append(node); }
        card.append(button("Reply", () => { threadRoot = thread.id; $("comment-kind").value = "reply"; $("reply-target").textContent = `Replying to ${thread.author} on ${thread.path}`; $("comment-body").focus(); }));
        card.append(button("Go to source", async () => {
            if (!preview) throw new Error("Build a preview first.");
            if (thread.outdated || !thread.canPin || thread.side === "LEFT") throw new Error("This thread is not anchored to the current source. Its original discussion is available on GitHub.");
            const candidates = Object.entries(preview.map).filter(([, value]) => value.file === thread.path && value.line <= thread.line && (value.endLine ?? value.line) >= thread.line);
            candidates.sort((a, b) => ((a[1].endLine ?? a[1].line) - a[1].line) - ((b[1].endLine ?? b[1].line) - b[1].line));
            if (!candidates.length) throw new Error("Comment is outside this specification's source map.");
            frame.contentDocument.getElementById(candidates[0][0])?.scrollIntoView({ block: "center" });
            await select(candidates[0][0]);
            $("instruction").value = `Address this review comment. Explain the proposed change:\n\n${thread.body}`;
        }));
        container.append(card);
    }
    for (const item of [...discussion.conversation, ...discussion.reviews]) {
        const card = element("article", undefined, "card"); card.append(link(`${item.author}${item.state ? ` | ${item.state}` : ""}`, item.url), element("p", item.body, "body")); container.append(card);
    }
    decorateComments(); notice("PR comments refreshed.");
}
document.querySelectorAll("[data-tab]").forEach(node => node.addEventListener("click", () => tab(node.dataset.tab)));
document.querySelectorAll("[data-instruction]").forEach(node => node.addEventListener("click", () => { $("instruction").value = node.dataset.instruction; }));
$("build").addEventListener("click", run(async () => { await build(); if (discussion) await loadComments(); }));
$("spec").addEventListener("change", run(async () => {
    if (renderedSpec) readerPositions.set(renderedSpec, captureReader());
    currentSpec = $("spec").value; preview = null; selected = null;
    frame.hidden = true; $("welcome").hidden = false;
    $("source").value = ""; $("source").disabled = true; $("ask").disabled = $("rewrite").disabled = $("manual").disabled = true;
    $("preview-status").textContent = "Build this specification to edit";
}));
$("rewrite").addEventListener("click", run(() => requestEdit(false)));
$("ask").addEventListener("click", run(askSelection));
$("manual").addEventListener("click", run(() => requestEdit(true)));
$("undo").addEventListener("click", run(async () => {
    if (!await confirmAction("Undo last canvas edit?", "Restore the previous source only if the file has not changed since that edit. This does not rewrite Git history.")) return;
    await api("undo"); await build(); notice("Last accepted canvas edit undone locally.");
}));
$("publish").addEventListener("click", run(async () => {
    if (!await confirmAction("Publish accepted edits to GitHub?", "Authorize Copilot to validate, commit and push accepted source edits on this feature branch, then update its existing PR or create one using the repository template. Unrelated changes require separate approval.")) return;
    await api("operation", { kind: "publish", confirm: true }); tab("drafts"); await refresh(); notice("Publishing queued in Copilot. The result or any approval/blocker will appear in the session and Drafts.");
}));
$("open-target").addEventListener("click", run(async () => {
    await api("operation", { kind: "open-target", target: $("target").value }); tab("drafts"); await refresh(); notice("Opening request queued in Copilot. This checkout stays unchanged.");
}));
$("refresh-comments").addEventListener("click", run(loadComments));
$("post-comment").addEventListener("click", run(async () => {
    if (!discussion?.pr) throw new Error("Refresh PR comments first; an open PR is required.");
    const kind = $("comment-kind").value;
    if (kind === "reply" && !threadRoot) throw new Error("Choose Reply on a thread first.");
    if (kind === "inline" && !selected) throw new Error("Select the changed source text first.");
    if (!$("comment-body").value.trim()) throw new Error("Write a comment first.");
    if (!await confirmAction("Post this comment to GitHub?", `Post as your authenticated GitHub account to PR #${discussion.pr.number}. This is not a local draft.`)) return;
    await api("comment", { kind, body: $("comment-body").value, prNumber: discussion.pr.number, rootId: threadRoot, ...(kind === "inline" ? { spec: currentSpec, anchor: selected.anchor, quote: selected.quote, sourceHash: selected.sourceHash } : {}) });
    $("comment-body").value = ""; await loadComments(); notice("Comment posted to GitHub.");
}));
$("insert-anchor").addEventListener("click", () => {
    if (!selected || selected.generated || !$("anchors").value) return;
    const source = $("source");
    source.setRangeText(`[](#${$("anchors").value})`, source.selectionStart, source.selectionEnd, "end"); source.focus();
});
$("find-next").addEventListener("click", () => {
    const query = $("find").value.trim(), doc = frame.contentDocument;
    if (!query || !doc || !preview) return;
    const nodes = [...doc.querySelectorAll("main p,main li,main h2,main h3,main h4,main td,article p,section p,section li")].filter(node => node.textContent.toLowerCase().includes(query.toLowerCase()));
    const index = Number($("find").dataset.index ?? -1) + 1;
    $("find").dataset.index = String(nodes.length ? index % nodes.length : -1);
    const node = nodes.length ? nodes[index % nodes.length] : undefined;
    if (node) { node.scrollIntoView({ block: "center" }); notice(`Match ${index % nodes.length + 1} of ${nodes.length}`); }
    else notice("No matches.");
});
$("find").addEventListener("input", () => { $("find").dataset.index = "-1"; });
run(async () => {
    await refresh();
    currentSpec = new URLSearchParams(location.search).get("spec") ?? state.specs[0].name;
    for (const spec of state.specs) $("spec").add(new Option(`${spec.number} - ${spec.name}`, spec.name));
    $("spec").value = currentSpec;
    setInterval(() => { if (!busy && !document.hidden) refresh().catch(error => notice(error.message, true)); }, 2500);
    await build();
    await loadComments();
})();
