#!/usr/bin/env node
/**
 * generate-sitemap.js
 * Reads all .html files in this directory, skips noindex pages and templates,
 * then writes sitemap.xml.
 *
 * Usage: node generate-sitemap.js
 */

const fs   = require('fs');
const path = require('path');

const BASE_URL  = 'https://www.sidehustleguard.com';
const DIR       = __dirname;
const OUT_FILE  = path.join(DIR, 'sitemap.xml');
const TODAY     = new Date().toISOString().slice(0, 10);

// Pages that should never appear in the sitemap regardless of noindex tag
const SKIP_FILES = new Set([
  '_template-article.html',
  '_template-article-card.html',
  'guide-section-options.html',
  'tax-affiliate-options.html',
  'og-image.html',
]);

// Override changefreq per URL slug
const CHANGEFREQ_OVERRIDES = {
  '':      'weekly',   // home
  'guides': 'weekly',
};

// Override priority per URL slug (default: 0.85 for articles)
const PRIORITY_OVERRIDES = {
  '':                           '1.0',
  'tool':                       '0.9',
  'guides':                     '0.9',
  'dashboard':                  '0.92',
  'self-employment-tax-calculator': '0.9',
  'audit-risk-estimator':       '0.9',
  'tax-guard-calculator':       '0.9',
  'scorp-savings-calculator':   '0.88',
  'quarterly-tax-calculator':   '0.9',
  'state-tax-rates':            '0.9',
  'tax-checklist':              '0.9',
  'short-term-rentals':         '0.9',
  'privacy':                    '0.3',
  'terms':                      '0.3',
};

// Yearly changefreq for certain slugs
const YEARLY_SLUGS = new Set(['privacy', 'terms']);

function getSlug(filename) {
  const base = path.basename(filename, '.html');
  return base === 'index' ? '' : base;
}

function isNoindex(content) {
  // Match: <meta name="robots" content="noindex  (any variant)
  return /\<meta\s+name=["']robots["']\s+content=["'][^"']*noindex/i.test(content);
}

function buildEntry(slug, lastmod) {
  const loc        = slug ? `${BASE_URL}/${slug}` : BASE_URL + '/';
  const priority   = PRIORITY_OVERRIDES[slug] ?? '0.85';
  const changefreq = YEARLY_SLUGS.has(slug) ? 'yearly'
                   : (CHANGEFREQ_OVERRIDES[slug] ?? 'monthly');

  return [
    '  <url>',
    `    <loc>${loc}</loc>`,
    `    <lastmod>${lastmod}</lastmod>`,
    `    <changefreq>${changefreq}</changefreq>`,
    `    <priority>${priority}</priority>`,
    '  </url>',
  ].join('\n');
}

// ── main ────────────────────────────────────────────────────────────────────

const htmlFiles = fs
  .readdirSync(DIR)
  .filter(f => f.endsWith('.html') && !SKIP_FILES.has(f) && !f.startsWith('_'));

const entries = [];

for (const file of htmlFiles) {
  const fullPath = path.join(DIR, file);
  const content  = fs.readFileSync(fullPath, 'utf8');

  if (isNoindex(content)) continue;

  const slug    = getSlug(file);
  const statObj = fs.statSync(fullPath);
  const lastmod = statObj.mtime.toISOString().slice(0, 10);

  entries.push({ slug, lastmod });
}

// Sort: home first, then guides, then alphabetical by slug
entries.sort((a, b) => {
  if (a.slug === '')        return -1;
  if (b.slug === '')        return  1;
  if (a.slug === 'guides')  return -1;
  if (b.slug === 'guides')  return  1;
  return a.slug.localeCompare(b.slug);
});

const xml = [
  '<?xml version="1.0" encoding="UTF-8"?>',
  '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
  ...entries.map(e => buildEntry(e.slug, e.lastmod)),
  '</urlset>',
  '',
].join('\n');

fs.writeFileSync(OUT_FILE, xml, 'utf8');
console.log(`✓ sitemap.xml written — ${entries.length} URLs`);
entries.forEach(e => console.log(`  ${e.slug || '(home)'}`));
