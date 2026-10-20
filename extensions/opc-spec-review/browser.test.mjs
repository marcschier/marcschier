import test from "node:test";
import assert from "node:assert/strict";
import { spawn } from "node:child_process";
import { mkdtemp, mkdir, readFile, writeFile, rm } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import { ReviewWorkspace } from "./workspace.mjs";
import { startServer } from "./server.mjs";

const sleep = ms => new Promise(resolve => setTimeout(resolve, ms));
async function until(fn, timeout = 15000) {
    const end = Date.now() + timeout;
    while (Date.now() < end) { const result = await fn(); if (result) return result; await sleep(40); }
    throw new Error("Browser condition timed out.");
}
test("reader position, manual drafts, and question-to-edit flow work through the canvas UI", async t => {
    const root = await mkdtemp(path.join(os.tmpdir(), "opc-review-browser-"));
    const profile = path.join(root, "browser");
    await mkdir(path.join(root, "source", "Demo"), { recursive: true });
    await mkdir(path.join(root, "_work", "docs", "Demo"), { recursive: true });
    const source = Array.from({ length: 60 }, (_, i) => `## Section ${i} {#section-${i}}\n\nParagraph ${i} explains a requirement.\n`).join("\n");
    await writeFile(path.join(root, "source", "Demo", "spec.md"), source);
    await writeFile(path.join(root, "source", "Demo", "manifest.json"), "{}");
    const workspace = new ReviewWorkspace(root, "feature", async () => "test-message", [{ name: "Demo", number: "OPC TEST" }], path.join(root, "state.json"), { version: 1, requests: [], accepted: [] });
    let renders = 0, failBuild = false;
    workspace.command = async (program, args) => {
        if (program === "git" && args[0] === "branch") return "feature\n";
        assert.equal(program, "dotnet");
        if (failBuild) throw new Error("Deliberate publisher failure");
        const map = {};
        const text = await workspace.source("source/Demo/spec.md");
        const sections = text.split(/(?=^## )/m).filter(Boolean);
        let line = 1;
        const html = sections.map((value, i) => {
            map[`sec_${i}`] = { file: "source/Demo/spec.md", line, endLine: line + value.trimEnd().split("\n").length - 1, generated: false };
            line += value.split("\n").length - 1;
            const title = value.split("\n")[0].replace(/^## /, "").replace(/ \{#.*$/, "");
            return `<section id="sec_${i}"><h2>${title}<a class="src" data-src="source/Demo/spec.md" data-line="${map[`sec_${i}`].line}" href="#">Edit</a></h2><p>${value.split("\n")[2]}</p></section>`;
        }).join("");
        await writeFile(path.join(root, "_work", "docs", "Demo", "index.html"), `<!doctype html><html><head><style>
        :root{color-scheme:light dark;--text:#17191c;--muted:#5c636b;--surface:#f6f7f9;--surface-strong:#eceff2;--accent:#0b5fa5}
        @media(prefers-color-scheme:dark){:root{--text:#e6e8eb;--muted:#a0a7af;--surface:#1c1f23;--surface-strong:#24282d;--accent:#6cb2f0}}
        body{margin:0;background:Canvas;color:var(--text)}section{height:320px;padding:12px;box-sizing:border-box}h2{margin:0}
        a{color:var(--accent)}pre{background:var(--surface)}th{background:var(--surface-strong)}.muted{color:var(--muted)}
        </style></head><body data-render="${++renders}">${html}<pre id="code">code</pre><table><tr><th>Heading</th></tr></table><p class="muted">Note</p><input aria-label="Native control"></body></html>`);
        await writeFile(path.join(root, "_work", "docs", "Demo", "test.stsmap.json"), JSON.stringify({ schema: 1, map }));
        return "Rendered fixture.";
    };
    workspace.comments = async () => ({ pr: null, threads: [], conversation: [], reviews: [] });
    const server = await startServer(workspace, "Demo", "browser-test");
    const browser = spawn(process.env.REVIEW_TEST_BROWSER ?? "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe", [
        "--headless=new", "--disable-gpu", "--no-first-run", "--no-default-browser-check", "--remote-debugging-port=0", `--user-data-dir=${profile}`, "about:blank",
    ], { stdio: "ignore" });
    let ws, nextId = 0;
    const pending = new Map(), exceptions = [];
    const rpc = (method, params = {}) => new Promise((resolve, reject) => {
        const id = ++nextId; pending.set(id, { resolve, reject }); ws.send(JSON.stringify({ id, method, params }));
    });
    t.after(async () => {
        if (ws?.readyState === WebSocket.OPEN) { await rpc("Browser.close").catch(() => {}); ws.close(); }
        if (browser.exitCode === null) browser.kill();
        await server.close();
        await sleep(700);
        await rm(root, { recursive: true, force: true, maxRetries: 8, retryDelay: 300 });
    });
    const port = await until(async () => {
        try { return (await readFile(path.join(profile, "DevToolsActivePort"), "utf8")).split("\n")[0]; }
        catch (error) { if (["ENOENT", "EBUSY"].includes(error.code)) return null; throw error; }
    });
    const targets = await (await fetch(`http://127.0.0.1:${port}/json/list`)).json();
    ws = new WebSocket(targets.find(item => item.type === "page").webSocketDebuggerUrl);
    ws.addEventListener("message", event => {
        const value = JSON.parse(event.data);
        if (value.id) {
            const callback = pending.get(value.id); pending.delete(value.id);
            if (value.error) callback.reject(new Error(JSON.stringify(value.error))); else callback.resolve(value.result);
        } else if (value.method === "Runtime.exceptionThrown") exceptions.push(value.params);
    });
    await new Promise((resolve, reject) => { ws.addEventListener("open", resolve); ws.addEventListener("error", reject); });
    const evaluate = async expression => {
        const value = await rpc("Runtime.evaluate", { expression, returnByValue: true, awaitPromise: true });
        assert.equal(value.exceptionDetails, undefined, JSON.stringify(value.exceptionDetails));
        return value.result.value;
    };
    await rpc("Runtime.enable");
    await rpc("Emulation.setEmulatedMedia", { features: [{ name: "prefers-color-scheme", value: "dark" }] });
    await rpc("Emulation.setDeviceMetricsOverride", { width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false });
    await rpc("Page.navigate", { url: server.url });
    const doc = "document.getElementById('document').contentDocument";
    const win = "document.getElementById('document').contentWindow";
    const loaded = async count => until(() => evaluate(`${doc}?.body?.dataset.render === '${count}' && !document.getElementById('build').disabled`));
    await loaded(1);
    const panelSize = () => evaluate("document.getElementById('review-panel').getBoundingClientRect().width");
    const readerSize = () => evaluate("document.querySelector('.reader').getBoundingClientRect().width");
    const dragDivider = async delta => {
        const start = await evaluate("(() => { const r=document.getElementById('panel-divider').getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+100}; })()");
        await rpc("Input.dispatchMouseEvent", { type: "mouseMoved", ...start });
        await rpc("Input.dispatchMouseEvent", { type: "mousePressed", ...start, button: "left", buttons: 1, clickCount: 1 });
        await rpc("Input.dispatchMouseEvent", { type: "mouseMoved", x: start.x + delta, y: start.y, buttons: 1 });
        await rpc("Input.dispatchMouseEvent", { type: "mouseReleased", x: start.x + delta, y: start.y, button: "left", buttons: 0, clickCount: 1 });
        await until(() => evaluate("!document.body.classList.contains('resizing-panel')"));
        assert.equal(await evaluate("getComputedStyle(document.getElementById('document')).pointerEvents"), "auto");
    };
    const dividerKey = async (key, modifiers = 0) => {
        await evaluate("document.getElementById('panel-divider').focus()");
        await rpc("Input.dispatchKeyEvent", { type: "keyDown", key, modifiers });
        await rpc("Input.dispatchKeyEvent", { type: "keyUp", key, modifiers });
    };
    assert.equal(await panelSize(), 390);
    const initialReader = await readerSize();
    await evaluate("document.getElementById('instruction').value='Keep this unsent question'");
    await dragDivider(-300);
    assert.equal(await panelSize(), 690, "Dragging left should widen the editor even when the pointer crosses the preview iframe");
    assert.equal(await readerSize(), initialReader - 300, "The preview must shrink by the same amount");
    assert.equal(await evaluate("document.getElementById('instruction').value"), "Keep this unsent question");
    assert.equal(await evaluate(`${doc}.body.dataset.render`), "1", "Resizing must not reload the preview");
    await dragDivider(100);
    assert.equal(await panelSize(), 590);
    await dividerKey("ArrowLeft");
    assert.equal(await panelSize(), 600);
    await dividerKey("ArrowRight", 8);
    assert.equal(await panelSize(), 550);
    await dividerKey("End");
    assert.equal(await readerSize(), 350, "Maximum editing width must preserve the preview minimum");
    await dividerKey("Home");
    assert.equal(await panelSize(), 320);
    await dragDivider(100);
    assert.equal(await panelSize(), 320, "Dragging must respect the editor minimum");
    await dragDivider(-270);
    assert.equal(await panelSize(), 590);
    assert.equal(await evaluate("document.getElementById('panel-divider').getAttribute('aria-valuenow')"), "590");
    await rpc("Emulation.setDeviceMetricsOverride", { width: 900, height: 1000, deviceScaleFactor: 1, mobile: false });
    await until(async () => (await panelSize()) === await evaluate("document.querySelector('main').clientWidth - 358"));
    assert.equal(await readerSize(), 350);
    await rpc("Emulation.setDeviceMetricsOverride", { width: 800, height: 1000, deviceScaleFactor: 1, mobile: false });
    await until(() => evaluate("getComputedStyle(document.getElementById('panel-divider')).display === 'none'"));
    assert.equal(await panelSize(), await evaluate("document.querySelector('main').clientWidth"), "Narrow windows must retain the stacked layout");
    await rpc("Emulation.setDeviceMetricsOverride", { width: 1440, height: 1000, deviceScaleFactor: 1, mobile: false });
    await until(async () => (await panelSize()) === 590);
    // Simulate host theme mirroring as well as an OS/browser dark preference.
    await evaluate("document.documentElement.dataset.colorMode='dark'; document.documentElement.style.setProperty('--background-color-default','#101010'); document.documentElement.style.setProperty('--text-color-default','#ffffff')");
    const checkLight = async () => {
        const colors = await evaluate(`(() => { const d=${doc}, w=${win}; const css=s=>w.getComputedStyle(d.querySelector(s)); return { scheme:css('html').colorScheme, background:css('body').backgroundColor, text:css('body').color, code:css('pre').backgroundColor, table:css('th').backgroundColor, link:css('a').color, muted:css('.muted').color }; })()`);
        assert.deepEqual(colors, { scheme: "light only", background: "rgb(255, 255, 255)", text: "rgb(23, 25, 28)", code: "rgb(246, 247, 249)", table: "rgb(236, 239, 242)", link: "rgb(11, 95, 165)", muted: "rgb(92, 99, 107)" });
        assert.equal(await evaluate("getComputedStyle(document.body).backgroundColor"), "rgb(16, 16, 16)", "Host controls should retain their own theme");
    };
    await checkLight();
    await rpc("Emulation.setEmulatedMedia", { features: [{ name: "prefers-color-scheme", value: "light" }] });
    await checkLight();
    await rpc("Emulation.setEmulatedMedia", { features: [{ name: "prefers-color-scheme", value: "dark" }] });
    await evaluate("document.querySelector('[data-tab=help]').click()");
    assert.equal(await evaluate("document.getElementById('tab-help').hidden"), false);
    assert.equal(await evaluate("document.querySelectorAll('#tab-help details').length"), 7);
    await evaluate("document.querySelectorAll('#tab-help details').forEach(d=>d.open=true)");
    for (const name of ["Stage manual draft", "Ask follow-up", "Request change from answer", "Post to GitHub...", "Publish to PR...", "Open in separate session", "Publisher diagnostics"]) {
        assert(await evaluate(`document.getElementById('tab-help').innerText.includes(${JSON.stringify(name)})`), `Missing help for ${name}`);
    }
    await evaluate("document.querySelector('[data-tab=edit]').click()");
    await evaluate(`${win}.scrollTo(0, 6500)`);
    await sleep(80);
    const before = await evaluate(`${win}.scrollY`);
    assert(before > 6000);
    await evaluate("document.getElementById('build').click()");
    await loaded(2);
    assert.equal(await panelSize(), 590, "Tab switches and rebuilds must retain the chosen split");
    await checkLight();
    await sleep(100);
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - before) <= 2, `Build preview reset scroll: before=${before}, after=${await evaluate(`${win}.scrollY`)}`);
    await evaluate(`${doc}.querySelector('#sec_20 a.src').click()`);
    await until(() => evaluate("!document.getElementById('manual').disabled"));
    await evaluate("document.getElementById('source').value = document.getElementById('source').value.replace('explains', 'clarifies'); document.getElementById('manual').click()");
    await until(() => evaluate("document.getElementById('drafts').textContent.includes('Accept locally')"));
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - before) <= 2, "Staging reset the reader position");
    await evaluate("[...document.querySelectorAll('#drafts button')].find(b => b.textContent === 'Accept locally').click()");
    await loaded(3);
    await sleep(100);
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - before) <= 2, "Accepting the draft reset the reader position");
    assert.match(await workspace.source("source/Demo/spec.md"), /Paragraph 20 clarifies/);
    const beforeInsert = await evaluate(`${doc}.getElementById('sec_20').getBoundingClientRect().top`);
    await writeFile(path.join(root, "source", "Demo", "spec.md"), `## Inserted section {#new-section}\n\nNew prose above the current reading position.\n\n${await workspace.source("source/Demo/spec.md")}`);
    await evaluate("document.getElementById('build').click()");
    await loaded(4); await sleep(80);
    assert(Math.abs((await evaluate(`${doc}.getElementById('sec_21').getBoundingClientRect().top`)) - beforeInsert) <= 2, "Renumbering or inserted content moved the current section");
    const retained = await evaluate(`${win}.scrollY`);
    failBuild = true;
    await evaluate("document.getElementById('build').click()");
    await until(() => evaluate("document.getElementById('notice').textContent.includes('Deliberate publisher failure')"));
    assert.equal(await evaluate(`${win}.scrollY`), retained, "Failed build moved the reader");
    await evaluate("document.querySelector('[data-tab=help]').click()");
    assert.equal(await evaluate("document.getElementById('tab-help').hidden"), false, "Help should remain available after build failure");
    await evaluate("document.querySelector('[data-tab=drafts]').click()");
    failBuild = false;
    await evaluate("document.getElementById('build').click()");
    await loaded(5);
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - retained) <= 2);
    await evaluate(`${doc}.querySelector('#sec_21 a.src').click()`);
    await until(() => evaluate("!document.getElementById('ask').disabled"));
    await evaluate("document.getElementById('instruction').value='What is this?'; document.getElementById('ask').click()");
    await until(() => workspace.state.requests.some(item => item.kind === "question"));
    const question = workspace.state.requests.find(item => item.kind === "question");
    assert.equal(question.kind, "question");
    const beforeQuestion = await workspace.source("source/Demo/spec.md");
    await workspace.report({ requestId: question.id, message: "This section explains a requirement." });
    await until(() => evaluate("document.getElementById('drafts').textContent.includes('This section explains a requirement.')"));
    assert.equal(await workspace.source("source/Demo/spec.md"), beforeQuestion);
    await evaluate("document.querySelector('[data-question-input]').value='Explain why.'; [...document.querySelectorAll('#drafts button')].find(b=>b.textContent==='Ask follow-up').click()");
    await until(() => workspace.state.requests.some(item => item.parentId === question.id));
    const followup = workspace.state.requests.find(item => item.parentId === question.id);
    assert.equal(followup.discussion[0].answer, "This section explains a requirement.");
    await workspace.report({ requestId: followup.id, message: "It supports interoperability." });
    await until(() => evaluate("document.getElementById('drafts').textContent.includes('It supports interoperability.')"));
    await evaluate("document.querySelector('[data-question-input]').value='Make the wording clearer based on this answer.'; [...document.querySelectorAll('#drafts button')].find(b=>b.textContent==='Request change from answer').click()");
    await until(() => workspace.state.requests.some(item => item.questionId === followup.id));
    const edit = workspace.state.requests.find(item => item.questionId === followup.id);
    assert.equal(edit.discussion.length, 2);
    assert.equal(edit.file, question.file);
    assert.equal(await workspace.source("source/Demo/spec.md"), beforeQuestion, "Requesting a change must not write before acceptance");
    await workspace.propose({ requestId: edit.id, replacement: edit.original.replace("clarifies", "states"), explanation: "Clearer wording." });
    await until(() => evaluate("document.getElementById('drafts').textContent.includes('Clearer wording.')"));
    await evaluate("[...document.querySelectorAll('#drafts button')].find(b=>b.textContent==='Accept locally').click()");
    await loaded(6);
    assert.match(await workspace.source("source/Demo/spec.md"), /Paragraph 20 states/);
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - retained) <= 2, "Question-driven edit reset reading position");
    await evaluate("document.getElementById('undo').click()");
    await until(() => evaluate("document.getElementById('confirm-dialog').open"));
    await evaluate("document.getElementById('confirm-yes').click()");
    await loaded(7);
    await checkLight();
    assert.equal(await workspace.source("source/Demo/spec.md"), beforeQuestion);
    assert(Math.abs((await evaluate(`${win}.scrollY`)) - retained) <= 2, "Undo reset reading position");
    assert.deepEqual(exceptions, []);
});
