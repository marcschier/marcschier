import { createServer } from "node:http";
import { randomBytes } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import { check, contained, home } from "./workspace.mjs";

const previewLightCss = await readFile(path.join(home, "preview-light.css"), "utf8");
const mime = { ".html": "text/html; charset=utf-8", ".js": "text/javascript; charset=utf-8", ".css": "text/css; charset=utf-8", ".svg": "image/svg+xml", ".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".gif": "image/gif", ".webp": "image/webp", ".woff2": "font/woff2" };
async function body(req) {
    check(req.headers["content-type"]?.startsWith("application/json"), "JSON content type required.");
    let size = 0;
    const chunks = [];
    for await (const chunk of req) {
        size += chunk.length;
        check(size <= 2_100_000, "Request exceeds 2 MB.");
        chunks.push(chunk);
    }
    const value = JSON.parse(Buffer.concat(chunks).toString("utf8"));
    check(value && typeof value === "object" && !Array.isArray(value), "Expected a JSON object.");
    return value;
}
export async function startServer(workspace, spec, instanceId) {
    const token = randomBytes(32).toString("hex");
    const prefix = `/${token}/`;
    let origin;
    const server = createServer(async (req, res) => {
        res.setHeader("Cache-Control", "no-store");
        res.setHeader("X-Content-Type-Options", "nosniff");
        res.setHeader("Referrer-Policy", "no-referrer");
        try {
            check(req.headers.host === new URL(origin).host, "Invalid Host.");
            const url = new URL(req.url, origin);
            check(url.pathname.startsWith(prefix), "Not found.");
            const route = decodeURIComponent(url.pathname.slice(prefix.length));
            if (route.startsWith("api/")) {
                check(req.method === "POST", "API requires POST.");
                check(req.headers.origin === origin && req.headers["x-review-key"] === token, "Untrusted request origin.");
                const input = await body(req);
                let result;
                switch (route) {
                    case "api/status": result = await workspace.status(); break;
                    case "api/build": result = await workspace.build(input.spec); break;
                    case "api/preview": result = await workspace.preview(input.spec); break;
                    case "api/selection": result = await workspace.selection(input); break;
                    case "api/edit": result = await workspace.createEdit(input, instanceId); break;
                    case "api/question": result = await workspace.createQuestion(input, instanceId); break;
                    case "api/request": result = workspace.readRequest(input.id); break;
                    case "api/decide": check(typeof input.accept === "boolean", "Expected accept flag."); result = await workspace.decide(input.id, input.accept); break;
                    case "api/undo": result = await workspace.undo(); break;
                    case "api/comments": result = await workspace.comments(); break;
                    case "api/comment": result = await workspace.postComment(input); break;
                    case "api/operation": result = await workspace.agentOperation(input, instanceId); break;
                    default: throw new Error("Unknown API endpoint.");
                }
                res.setHeader("Content-Type", "application/json");
                res.end(JSON.stringify(result));
                return;
            }
            check(req.method === "GET", "Method not allowed.");
            let file;
            if (route.startsWith("render/")) {
                const relative = route.slice("render/".length);
                check(mime[path.extname(relative).toLowerCase()], "Unsupported preview resource.");
                file = await contained(path.join(workspace.root, "_work", "docs"), relative);
                res.setHeader("Content-Security-Policy", "default-src 'none'; img-src 'self' data:; style-src 'self' 'unsafe-inline'; font-src 'self'; script-src 'none'; connect-src 'none'; frame-src 'none'; object-src 'none'; base-uri 'none'; form-action 'none'; sandbox allow-same-origin");
            } else {
                check(["", "index.html", "app.js", "style.css"].includes(route), "Not found.");
                file = path.join(home, route || "index.html");
                res.setHeader("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self'; connect-src 'self'; frame-src 'self'; img-src 'self' data:; base-uri 'none'; form-action 'none'");
            }
            res.setHeader("Content-Type", mime[path.extname(file)]);
            if (route.startsWith("render/") && path.extname(file).toLowerCase() === ".html") {
                const html = await readFile(file, "utf8");
                const style = `<style id="review-preview-light">${previewLightCss}</style>`;
                // Apply before first paint, without changing generated files or enabling scripts.
                res.end(/<\/head\s*>/i.test(html) ? html.replace(/<\/head\s*>/i, `${style}</head>`) : style + html);
            } else res.end(await readFile(file));
        } catch (error) {
            res.statusCode = 400;
            res.setHeader("Content-Type", "application/json");
            res.end(JSON.stringify({ error: error.message }));
        }
    });
    await new Promise((resolve, reject) => {
        server.once("error", reject);
        server.listen(0, "127.0.0.1", () => { server.off("error", reject); resolve(); });
    });
    origin = `http://127.0.0.1:${server.address().port}`;
    return {
        url: `${origin}${prefix}?spec=${encodeURIComponent(spec)}`,
        close: () => new Promise(resolve => { server.closeAllConnections(); server.close(resolve); }),
    };
}
