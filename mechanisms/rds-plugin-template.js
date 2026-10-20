import { createRequire } from "module";
import path from "path";

export const RdsPlugin = async ({ directory }) => {
  try {
    process.env.CODE_GUARD_BASE_DIR = path.join(directory, ".rds-state");
    const require = createRequire(import.meta.url);
    const rds = require("RDS_ABS_PATH");
    const rp = require("RP_ABS_PATH");
    const seen = new Set();
    return {
      "tool.execute.after": async (input, output) => {
        try {
          const txt = output && typeof output.output === "string" ? output.output : null;
          if (txt === null || txt.length === 0) return output;
          const sid = (input && input.sessionID) || "s";
          if (!seen.has(sid)) {
            try { rp.setActiveSessionId(sid); } catch (_e) { /* fail-closed */ }
            seen.add(sid);
          }
          const res = rds.process(txt);
          if (res && res.compressed && typeof res.text === "string") {
            output.output = res.text;
          }
          return output;
        } catch (_e) {
          return output; // fail-closed: native passthrough
        }
      },
    };
  } catch (_e) {
    return {}; // fail-closed: no hooks if RDS cannot load
  }
};
