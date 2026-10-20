const rds = require(process.argv[2]);
const rp = require(process.argv[3]);
rp.setActiveSessionId("smoke");
const r1 = rds.process("line-a\nline-b\nline-c");
const r2 = rds.process("line-a\nline-b\nline-c\nline-d");
console.log(JSON.stringify({
  r1_compressed: r1.compressed,
  r2_compressed: r2.compressed,
  matched: r2.matched_chars,
  has_marker: (r2.text || "").includes("TASCO-RDS")
}));
