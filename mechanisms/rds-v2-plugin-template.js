/**
 * TASCO-R4 REFINEMENT-R1 — RDS v2 eligibility-gated plugin (research workspace only).
 *
 * Wraps the FROZEN v0.11-D3-E5 primitive (verbatim vendored) with deployment-form gates
 * derived from the 100-case root-cause audit (refinement-root-cause.json):
 *   G1 tool gate   : `read` outputs fold only from the 3rd delivery of the same path
 *                    onward (1st/2nd stay native — the model may need to re-see content).
 *   G2 noise gate  : non-read outputs fold only if >=1000 chars AND duplicate-line char
 *                    share >= 0.30 (noise-type repeated delivery: test runs/build logs).
 *   G3 primitive   : exact-only contiguous folding, anchor-first, fail-closed, markers,
 *                    per-session ledger — UNCHANGED frozen semantics.
 * No benchmark/task-family labels; only runtime-observable facts (tool name, path,
 * per-session delivery counters, content statistics).
 * Traceability: every call appends an eligibility row to the session ledger.
 */
import { createRequire } from "module";
import path from "path";

const RDS_PATH = "__RDS_ABS_PATH__";
const RP_PATH = "__RP_ABS_PATH__";

const DUP_THRESHOLD = 0.30;
const MIN_CHARS = 1000;

function dupLineCharShare(text) {
  const lines = text.split("\n");
  const counts = new Map();
  let dup = 0;
  let total = 0;
  for (const l of lines) {
    total += l.length + 1;
    counts.set(l, (counts.get(l) || 0) + 1);
  }
  for (const [l, k] of counts) if (k > 1) dup += (l.length + 1) * (k - 1);
  return total > 0 ? dup / total : 0;
}

export const RdsV2Plugin = async ({ directory }) => {
  try {
    process.env.CODE_GUARD_BASE_DIR = path.join(directory, ".rds-state");
    const require = createRequire(import.meta.url);
    const rds = require(RDS_PATH);
    const rp = require(RP_PATH);
    const sessions = new Map(); // sessionID -> {seq, readDeliveries: Map(path->count)}

    return {
      "tool.execute.after": async (input, output) => {
        try {
          const txt = output && typeof output.output === "string" ? output.output : null;
          if (txt === null || txt.length === 0) return output;
          const sid = (input && input.sessionID) || "s";
          if (!sessions.has(sid)) sessions.set(sid, { readDeliveries: new Map() });
          const S = sessions.get(sid);
          const tool = (input && input.tool) || "unknown";
          const p = (input && input.args && (input.args.filePath || input.args.path)) || "";

          let decision = "native";
          let reason = "";
          if (tool === "read") {
            const n = (S.readDeliveries.get(p) || 0) + 1;
            S.readDeliveries.set(p, n);
            if (n >= 3) {
              decision = "fold_eligible";
              reason = `read_delivery_${n}`;
            } else {
              reason = `read_delivery_${n}_kept_native`;
            }
          } else {
            const share = dupLineCharShare(txt);
            if (txt.length >= MIN_CHARS && share >= DUP_THRESHOLD) {
              decision = "fold_eligible";
              reason = `noise_type_share_${share.toFixed(2)}`;
            } else {
              reason = `content_or_small_chars_${txt.length}_share_${share.toFixed(2)}`;
            }
          }

          let compressed = false;
          let matched = 0;
          // Always run the frozen primitive (it registers anchors even when native);
          // the gate decides whether to ADOPT the compressed text.
          try { rp.setActiveSessionId(sid); } catch (_e) { /* fail-closed */ }
          const res = rds.process(txt);
          if (decision === "fold_eligible" && res && res.compressed && typeof res.text === "string") {
            output.output = res.text;
            compressed = true;
            matched = res.matched_chars || 0;
          } else if (decision === "fold_eligible") {
            decision = "gate_fold_but_primitive_native";
            reason += "|primitive_native";
          } else if (res && res.compressed) {
            reason += "|gate_overrode_primitive_compression";
          }
          try {
            const fs = await import("fs");
            const dir = path.join(directory, ".rds-state", "eligibility");
            fs.mkdirSync(dir, { recursive: true });
            fs.appendFileSync(path.join(dir, "eligibility.ndjson"), JSON.stringify({
              ts: Date.now(), tool, path: p, chars: txt.length,
              decision, reason, compressed, matched_chars: matched,
            }) + "\n");
          } catch (_e) { /* traceability is best-effort; folding already fail-closed */ }
          return output;
        } catch (_e) {
          return output; // fail-closed: native passthrough
        }
      },
    };
  } catch (_e) {
    console.error(String(_e && _e.message)); return {};
  }
};
