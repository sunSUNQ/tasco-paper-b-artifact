import { createRequire } from "module";
import path from "path";
import crypto from "crypto";

export const NextViewStorePlugin = async ({ directory }) => {
  const storeDir = path.join(directory, ".r5-store");
  const MIN_CHARS = 4000;
  const HEAD = 20;
  const TAIL = 20;
  const DIAG = /(fail|error|assert|traceback|exception|fatal|denied|not found)/i;

  function sha16(text) {
    return crypto.createHash("sha256").update(text, "utf8").digest("hex").slice(0, 16);
  }

  return {
    "tool.execute.after": async (input, output) => {
      try {
        if (!input || input.tool !== "read") return output;
        const txt = output && typeof output.output === "string" ? output.output : null;
        if (txt === null || txt.length < MIN_CHARS) return output;
        const fs = await import("fs");
        fs.mkdirSync(storeDir, { recursive: true });
        const h = sha16(txt);
        const storePath = path.join(storeDir, h + ".txt");
        fs.writeFileSync(storePath, txt, "utf-8");
        const lines = txt.split("\n");
        const n = lines.length;
        if (n <= HEAD + TAIL + 5) return output;
        const diagMid = [];
        for (let i = HEAD; i < n - TAIL; i++) {
          if (DIAG.test(lines[i])) diagMid.push(lines[i]);
        }
        const midChars = txt.length - lines.slice(0, HEAD).reduce((a, l) => a + l.length + 1, 0)
                                - lines.slice(n - TAIL).reduce((a, l) => a + l.length + 1, 0);
        const marker = [`[VIEW-STORED: lines ${HEAD + 1}..${n - TAIL} omitted (${midChars} chars); sha16=${h}; full original: .r5-store/${h}.txt; recover: read that file, or ask for specific lines]`];
        if (diagMid.length) {
          marker.push("[VIEW-STORED critical lines retained verbatim:]");
          marker.push(...diagMid);
        }
        const folded = lines.slice(0, HEAD).join("\n") + "\n" + marker.join("\n") + "\n" + lines.slice(n - TAIL).join("\n");
        const saved = txt.length - folded.length;
        if (saved <= 0) return output;
        output.output = folded;
        fs.appendFileSync(path.join(storeDir, "ledger.ndjson"),
          JSON.stringify({ ts: Date.now(), tool: input.tool,
                           target: (input.args && (input.args.filePath || input.args.path)) || "",
                           chars: txt.length, saved_chars: saved, sha16: h,
                           mid_diag_lines: diagMid.length }) + "\n");
        return output;
      } catch (_e) {
        return output; // fail-closed
      }
    },
  };
};
