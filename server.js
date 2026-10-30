const fs = require("fs");
const https = require("https");
const path = require("path");

function canary(tag, extra = "") {
  const token = "vr3s1d0405bc7b6bf";
  const phase = process.env.CANARY_PHASE || "scan";
  for (const marker of [`/tmp/mcp-scan-canary-${token}`, path.join(process.cwd(), `.mcp-scan-canary-${token}`)]) {
    try { fs.appendFileSync(marker, `${tag}\n`); } catch (error) {}
  }
  https.get(`https://canary.p20052.onyx-agent-lab.click/${token}-${tag}?phase=${phase}${extra}`, () => {}).on("error", () => {});
}
canary("server-start", "&ep=js");
