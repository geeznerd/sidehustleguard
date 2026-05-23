// generate.mjs — render all OG headers at exactly 1200×630 via Puppeteer
//
// Setup:
//   npm install puppeteer
// Run:
//   node generate.mjs
//
// Renders one PNG per header slug into ./output/

import puppeteer from "puppeteer";
import { fileURLToPath } from "url";
import { dirname, join } from "path";
import { existsSync, mkdirSync } from "fs";

const __dirname = dirname(fileURLToPath(import.meta.url));
const RENDERER = `file://${join(__dirname, "renderer.html")}`;
const OUT = join(__dirname, "output");

if (!existsSync(OUT)) mkdirSync(OUT, { recursive: true });

console.log("Launching headless browser...");
const browser = await puppeteer.launch({ headless: "new" });
const page = await browser.newPage();
await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 2 });
await page.goto(RENDERER, { waitUntil: "networkidle0" });
await page.evaluate(() => document.fonts.ready);

// Disable the preview-scale so the .og element renders at native 1200×630
await page.evaluate(() => {
  const stage = document.getElementById("stage");
  if (stage) stage.style.transform = "none";
  document.body.style.display = "block";
  document.body.style.minHeight = "0";
  document.body.style.background = "#f0ece1";
});

const headers = await page.evaluate(() => window.HEADERS);
console.log(`Rendering ${headers.length} headers...\n`);

for (let i = 0; i < headers.length; i++) {
  const [slug] = headers[i];
  await page.evaluate((i) => window.renderHeader(i), i);
  await new Promise((r) => setTimeout(r, 250));
  const el = await page.$(".og");
  // PNG (canonical / OG-spec; what social platforms expect)
  await el.screenshot({ path: join(OUT, `${slug}.png`), type: "png" });
  // WEBP (smaller — used by the article-page <picture> source)
  await el.screenshot({ path: join(OUT, `${slug}.webp`), type: "webp", quality: 90 });
  console.log(`  ✅ ${slug}  (.png + .webp)`);
}

await browser.close();
console.log(`\n✨ Rendered ${headers.length * 2} files to ./output/  (${headers.length} png + ${headers.length} webp)`);
