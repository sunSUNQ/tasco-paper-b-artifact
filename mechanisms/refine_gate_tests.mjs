/** Deterministic gate tests (instrumented). */
import { writeFileSync, mkdirSync, rmSync, readFileSync } from "fs";
import path from "path";

const REFINEMENT = process.argv[2];
const tpl = readFileSync(path.join(REFINEMENT, "rds-v2-plugin-template.js"), "utf-8")
  .replace("__RDS_ABS_PATH__", path.join(REFINEMENT, "rds-impl", "post_tool", "repeated_delivery_suppression.js").replace(/\\/g, "\\\\"))
  .replace("__RP_ABS_PATH__", path.join(REFINEMENT, "rds-impl", "guard_core", "runtime_paths.js").replace(/\\/g, "\\\\"));

const tmp = path.join(REFINEMENT, "gate-test-tmp");
rmSync(tmp, { recursive: true, force: true });
mkdirSync(path.join(tmp, ".opencode", "plugins"), { recursive: true });
writeFileSync(path.join(tmp, ".opencode", "plugins", "rds-plugin.mjs"), tpl);
writeFileSync(path.join(tmp, "package.json"), JSON.stringify({ type: "module" }));

const { RdsV2Plugin } = await import("file:///" + path.join(tmp, ".opencode", "plugins", "rds-plugin.mjs").replace(/\\/g, "/"));
const hooks = await RdsV2Plugin({ directory: tmp });
const after = hooks["tool.execute.after"];
if (typeof after !== "function") { console.log("FAIL plugin init"); process.exit(1); }

const results = [];
async function call(name, tool, args, text, sid = "s1") {
  const output = { output: text };
  await after({ tool, sessionID: sid, args }, output);
  const t = typeof output.output;
  const folded = t === "string" && output.output.includes("TASCO-RDS omitted");
  console.log(`[${name}] type=${t} folded=${folded} len=${t === "string" ? output.output.length : "-"}`);
  return { folded, output_type: t };
}

const fileContent = Array.from({ length: 50 }, (_, i) => `source line ${i}: value_${i}`).join("\n");
results.push(["read 1st native", !(await call("read 1st", "read", { filePath: "src/a.js" }, fileContent)).folded]);
results.push(["read 2nd native", !(await call("read 2nd", "read", { filePath: "src/a.js" }, fileContent)).folded]);
results.push(["read 3rd folded", (await call("read 3rd", "read", { filePath: "src/a.js" }, fileContent)).folded]);
results.push(["bash small native", !(await call("bash small", "bash", { command: "ls" }, "ok\n done")).folded]);

const noisy = Array.from({ length: 80 }, (_, i) => `PASS tests/unit/x ${i % 5}`).join("\n") + "\nsummary line\n";
results.push(["bash noisy 1st native", !(await call("noisy 1st", "bash", { command: "npm test" }, noisy)).folded]);
results.push(["bash noisy 2nd folded", (await call("noisy 2nd", "bash", { command: "npm test" }, noisy)).folded]);

const content = Array.from({ length: 80 }, (_, i) => `unique code line ${i} ${"x".repeat(20)}`).join("\n");
results.push(["content-like native", !(await call("content 1st", "bash", { command: "cat" }, content)).folded]);
results.push(["content-like repeat native", !(await call("content 2nd", "bash", { command: "cat" }, content)).folded]);
results.push(["malformed untouched", (await call("malformed", "bash", {}, 12345)).output_type === "number"]);

let pass = true;
for (const [name, ok] of results) {
  if (!ok) { console.log(`FAIL  ${name}`); pass = false; }
}
console.log(JSON.stringify({ gate_test_verdict: pass ? "PASS" : "FAIL", n: results.length }));
process.exit(pass ? 0 : 1);

