import { joinSession, createCanvas, CanvasError } from "@github/copilot-sdk/extension";
import { ReviewWorkspace } from "./workspace.mjs";
import { startServer } from "./server.mjs";

const panels = new Map();
let workspace;
let session;
const object = (properties, required = []) => ({ type: "object", properties, required, additionalProperties: false });
const string = { type: "string", minLength: 1 };
const actions = [
    ["status", "Read current specification, draft requests, preview and runtime status.", object({}), () => workspace.status()],
    ["rebuild", "Rebuild the actual publisher HTML and source maps from local files.", object({ spec: string }, ["spec"]), async input => {
        const result = await workspace.build(input.spec);
        return { spec: result.name, built: result.built, locations: Object.keys(result.map).length, output: result.output };
    }],
    ["read_request", "Read a persisted selection, question or edit instruction, source range and discussion context.", object({ requestId: string }, ["requestId"]), input => workspace.readRequest(input.requestId)],
    ["propose_edit", "Return replacement Markdown for the complete original range in read_request. This only stages a proposal; the user accepts it.", object({ requestId: string, replacement: { type: "string" }, explanation: string }, ["requestId", "replacement", "explanation"]), input => workspace.propose(input)],
    ["report_request", "Answer a selection question, report a failed rewrite, or report a requested GitHub operation's result.", object({ requestId: string, message: string, failed: { type: "boolean" } }, ["requestId", "message"]), input => workspace.report(input)],
];

session = await joinSession({
    canvases: [createCanvas({
        id: "opc-spec-review",
        displayName: "OPC specification review",
        description: "Review publisher-rendered specifications and figures, propose source edits, and work with GitHub PR comments.",
        inputSchema: object({ spec: string }),
        actions: actions.map(([name, description, inputSchema, handler]) => ({
            name, description, inputSchema,
            handler: async ctx => {
                if (!workspace) throw new CanvasError("not_ready", "Open the review canvas first.");
                try { return await handler(ctx.input ?? {}); }
                catch (error) { throw new CanvasError("review_error", error.message); }
            },
        })),
        open: async ctx => {
            workspace ??= await ReviewWorkspace.open(process.cwd(), options => session.send(options));
            const spec = ctx.input?.spec ?? workspace.specs[0]?.name;
            if (!spec) throw new CanvasError("no_specifications", "No source/*/manifest.json specifications found in this session's checkout.");
            workspace.spec(spec);
            let panel = panels.get(ctx.instanceId);
            if (!panel) {
                panel = await startServer(workspace, spec, ctx.instanceId);
                panels.set(ctx.instanceId, panel);
            }
            return { title: "OPC specification review", url: panel.url, status: "Local drafts; GitHub writes require explicit actions" };
        },
        onClose: async ctx => {
            const panel = panels.get(ctx.instanceId);
            if (panel) { panels.delete(ctx.instanceId); await panel.close(); }
        },
    })],
});
