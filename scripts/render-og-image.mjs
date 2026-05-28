// scripts/render-og-image.mjs
//
// Renders /og-image.html to /og-image.png at exactly 1200×630 (2x device
// scale for sharp social-card display). Reuses the puppeteer install
// from /headers/node_modules.
//
// Run:
//   node scripts/render-og-image.mjs
//
// This is the file social platforms fetch when the URL is shared, so
// rerun after changes to og-image.html.

import puppeteer from "puppeteer";
import { fileURLToPath } from "url";
import { dirname, join, resolve } from "path";

const __dirname = dirname(fileURLToPath(import.meta.url));
const ROOT = resolve(__dirname, "..");
const SRC = `file://${join(ROOT, "og-image.html")}`;
const OUT = join(ROOT, "og-image.png");

console.log("Launching headless browser...");
const browser = await puppeteer.launch({ headless: "new" });
const page = await browser.newPage();

// Important: 1200×630 at deviceScaleFactor: 2 yields a sharp 2400×1260
// rendering downsampled to 1200×630, which is what social platforms
// expect for OG images (high DPI).
await page.setViewport({
  width: 1200,
  height: 630,
  deviceScaleFactor: 2,
});

await page.goto(SRC, { waitUntil: "networkidle0" });

// Wait for fonts (Fraunces is heavy — make sure it's loaded before screenshot)
await page.evaluate(() => document.fonts.ready);

// Extra 300ms in case anything else needs to settle
await new Promise((r) => setTimeout(r, 300));

const el = await page.$(".og");
if (!el) {
  console.error("Could not find .og element. Aborting.");
  await browser.close();
  process.exit(1);
}

await el.screenshot({ path: OUT, type: "png" });
console.log(`  ✅ Wrote ${OUT}`);

await browser.close();
console.log("Done.");
