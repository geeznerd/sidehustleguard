/* ═══════════════════════════════════════════════════════════════════════
 * W-4 PDF Generator — shared module
 *
 * Generates a pre-filled IRS Form W-4 PDF, fully client-side via pdf-lib.
 * All processing happens in the browser; no PII ever leaves the user's
 * device.
 *
 * Public API:
 *   W4PdfGenerator.generate(values)  → Promise<Blob>
 *   W4PdfGenerator.download(values)  → Promise<void>  (triggers browser DL)
 *
 * Values shape (every field optional; only provided values get filled):
 *   {
 *     taxYear:        2025 | 2026,
 *     filing:         'single' | 'mfs' | 'mfj' | 'qss' | 'hoh',
 *     step2c:         boolean,    // ☑ Multiple jobs (Step 2(c))
 *     step3Kids:      number,     // dollar amount for kids × $2,000 line
 *     step3OtherDeps: number,     // dollar amount for other deps × $500 line
 *     step3Total:     number,     // Step 3 total (the line that flows down)
 *     step4a:         number,     // Step 4(a) other income
 *     step4b:         number,     // Step 4(b) deductions above standard
 *     step4c:         number      // Step 4(c) extra withholding per paycheck
 *   }
 *
 * Field discovery (IRS Form W-4, via pypdf inspection):
 *   c1_1[0]  Step 1(c) filing-status radio: Single / MFS
 *   c1_1[1]  Step 1(c) filing-status radio: MFJ / QSS
 *   c1_1[2]  Step 1(c) filing-status radio: HoH
 *   c1_2[0]  Step 2(c) multiple-jobs checkbox
 *   f1_06    Step 3 qualifying children × $2,000
 *   f1_07    Step 3 other dependents × $500
 *   f1_08    Step 3 total
 *   f1_09    Step 4(a) other income
 *   f1_10    Step 4(b) deductions above standard
 *   f1_11    Step 4(c) extra withholding per paycheck
 *
 * NOTE: IRS sometimes renumbers internal field names between form years.
 * If the 2026 W-4 ships with different identifiers, the per-field try/catch
 * keeps the rest of the fill working — failed fields log to console only.
 * ═══════════════════════════════════════════════════════════════════════ */
(function () {
  'use strict';

  // ───── pdf-lib loader (lazy, idempotent) ─────
  var pdfLibPromise = null;
  function loadPdfLib() {
    if (pdfLibPromise) return pdfLibPromise;
    pdfLibPromise = new Promise(function (resolve, reject) {
      if (window.PDFLib) return resolve(window.PDFLib);
      var s = document.createElement('script');
      s.src = '/assets/js/vendor/pdf-lib.min.js';
      s.onload = function () { resolve(window.PDFLib); };
      s.onerror = function () {
        pdfLibPromise = null;
        reject(new Error('Failed to load pdf-lib'));
      };
      document.head.appendChild(s);
    });
    return pdfLibPromise;
  }

  // ───── Filing status → IRS Step 1(c) radio index ─────
  // The W-4 collapses 5 filing statuses to 3 radios.
  var FILING_TO_RADIO = {
    single: 0, mfs: 0,
    mfj:    1, qss: 1,
    hoh:    2
  };

  // ───── Text-field map (key → IRS field name) ─────
  // Only provided values get filled; zeros/empty skipped (the IRS form's
  // default rendering shows nothing rather than "0", which looks cleaner).
  var TEXT_FIELDS = {
    step3Kids:      'topmostSubform[0].Page1[0].Step3_ReadOrder[0].f1_06[0]',
    step3OtherDeps: 'topmostSubform[0].Page1[0].Step3_ReadOrder[0].f1_07[0]',
    step3Total:     'topmostSubform[0].Page1[0].f1_08[0]',
    step4a:         'topmostSubform[0].Page1[0].f1_09[0]',
    step4b:         'topmostSubform[0].Page1[0].f1_10[0]',
    step4c:         'topmostSubform[0].Page1[0].f1_11[0]'
  };

  // ───── Core generator ─────
  async function generate(values) {
    if (!values || typeof values !== 'object') {
      throw new Error('W4PdfGenerator: values object required');
    }
    var PDFLib = await loadPdfLib();
    var taxYear = values.taxYear || 2025;

    var formUrl = '/assets/forms/fw4-' + taxYear + '.pdf';
    var resp = await fetch(formUrl);
    if (!resp.ok) {
      throw new Error('Form fetch failed (' + resp.status + '): ' + formUrl);
    }
    var bytes = await resp.arrayBuffer();
    var pdfDoc = await PDFLib.PDFDocument.load(bytes);
    var form = pdfDoc.getForm();

    // Text fields (Step 3 + Step 4 lines)
    Object.keys(TEXT_FIELDS).forEach(function (key) {
      var v = values[key];
      // Skip undefined, null, empty, and explicit zero — zero renders nicer as blank
      if (v === undefined || v === null || v === '' || v === 0) return;
      try {
        form.getTextField(TEXT_FIELDS[key]).setText(String(v));
      } catch (e) {
        console.warn('W4PdfGenerator: text fill failed for ' + key, e);
      }
    });

    // Step 1(c) filing-status radio
    var radioIdx = FILING_TO_RADIO[values.filing];
    if (radioIdx !== undefined) {
      try {
        form.getCheckBox('topmostSubform[0].Page1[0].c1_1[' + radioIdx + ']').check();
      } catch (e) {
        console.warn('W4PdfGenerator: filing status check failed', e);
      }
    }

    // Step 2(c) multiple-jobs checkbox
    if (values.step2c === true) {
      try {
        form.getCheckBox('topmostSubform[0].Page1[0].c1_2[0]').check();
      } catch (e) {
        console.warn('W4PdfGenerator: step 2(c) check failed', e);
      }
    }

    // Footer credit on page 1 — Helvetica 7pt in the bottom margin
    try {
      var page1 = pdfDoc.getPages()[0];
      var font = await pdfDoc.embedFont(PDFLib.StandardFonts.Helvetica);
      page1.drawText(
        'Generated by SideHustleGuard.com  ·  Sign + add your name, address, and SSN before submitting to HR.',
        {
          x: 36,
          y: 18,
          size: 7,
          font: font,
          color: PDFLib.rgb(0.45, 0.45, 0.50)
        }
      );
    } catch (e) {
      console.warn('W4PdfGenerator: footer stamp failed', e);
    }

    // Leave form unflattened so HR can still edit if their workflow needs that
    var outBytes = await pdfDoc.save();
    return new Blob([outBytes], { type: 'application/pdf' });
  }

  // ───── Download trigger ─────
  async function download(values) {
    var blob = await generate(values);
    var url = URL.createObjectURL(blob);
    var a = document.createElement('a');
    a.href = url;
    a.download = 'W-4-prefilled-' + (values.taxYear || 2025) + '.pdf';
    document.body.appendChild(a);
    a.click();
    // Defer cleanup so iOS Safari has time to honor the click
    setTimeout(function () {
      URL.revokeObjectURL(url);
      if (a.parentNode) a.parentNode.removeChild(a);
    }, 120);
  }

  window.W4PdfGenerator = {
    generate: generate,
    download: download,
    // Exposed for testing / extension. Don't mutate from page code.
    _FILING_TO_RADIO: FILING_TO_RADIO,
    _TEXT_FIELDS: TEXT_FIELDS
  };
})();
