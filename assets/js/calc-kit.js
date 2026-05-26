/*!
 * SideHustleGuard — Calculator Tool Kit
 *
 * Shared utilities extracted from the /crypto-tax-calculator engine.
 * Pages opt in by loading this file before their inline <script>:
 *
 *   <script src="/assets/js/calc-kit.js"></script>
 *
 * Then in your inline script:
 *
 *   var $ = function(id){ return document.getElementById(id); };
 *   var state = { payment: 0, annual: 0, ... };
 *
 *   CalcKit.bindMoneyInput($('payment'), function(v){
 *     state.payment = v; recalc();
 *   });
 *
 *   CalcKit.bindSegControl($('seg-status'), function(v){
 *     state.status = v; recalc();
 *   });
 *
 *   CalcKit.animateNumber($('r-guard'), prevGuard, newGuard, 600);
 *
 * Behavior:
 *   - Money inputs auto-format with thousand separators on every
 *     keystroke. Caret is restored to the end after re-render.
 *   - State is held in the caller's JS object — the input's .value
 *     stores the formatted string; calculations use the raw number
 *     passed to the onChange callback.
 *   - animateNumber respects `prefers-reduced-motion: reduce` — when
 *     the user requests reduced motion, it snaps to the final value
 *     instead of tweening.
 *   - bindSegControl handles aria-checked toggling automatically.
 */
(function (root) {
  'use strict';

  function reducedMotion() {
    return window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  }

  /* ─── Formatters ──────────────────────────────────────────── */
  function fmt(n) {
    if (!isFinite(n)) n = 0;
    return Math.round(Math.max(0, n)).toLocaleString('en-US');
  }
  function fmtMoney(n) {
    if (!isFinite(n)) n = 0;
    var s = Math.round(Math.abs(n)).toLocaleString('en-US');
    return (n < 0 ? '-' : '') + '$' + s;
  }
  /** HTML format with <em>$</em> for the italic-apricot prefix */
  function fmtRich(n) {
    if (!isFinite(n)) n = 0;
    var s = Math.round(Math.abs(n)).toLocaleString('en-US');
    return (n < 0 ? '-' : '') + '<em>$</em>' + s;
  }
  function fmtPct(r, decimals) {
    var d = (decimals == null) ? 1 : decimals;
    if (!isFinite(r)) r = 0;
    return (r * 100).toFixed(d) + '%';
  }
  function parseMoney(v) {
    var n = parseFloat(String(v).replace(/[^0-9.\-]/g, ''));
    return isFinite(n) ? Math.max(0, n) : 0;
  }

  /* ─── Count-up animation ──────────────────────────────────── */
  /**
   * Tween a number from → to inside `el`, ease-out-cubic over `ms`.
   *
   * opts.isHTML    — render via innerHTML (preserves <em>$</em>) if true.
   *                  defaults to false (textContent).
   * opts.fmt       — custom format fn (default fmtRich if isHTML, else fmtMoney)
   * opts.suffix    — string appended after the number each frame
   *                  (e.g. '%' for percent values without leading $)
   * opts.decimals  — round to N decimals during tween (default 0)
   *
   * Snaps to final value if `prefers-reduced-motion: reduce`.
   */
  function animateNumber(el, from, to, ms, opts) {
    if (!el) return;
    opts = opts || {};
    var isHTML = !!opts.isHTML;
    var defaultFmt = isHTML ? fmtRich : fmtMoney;
    var formatter = opts.fmt || defaultFmt;
    var prop = isHTML ? 'innerHTML' : 'textContent';

    if (reducedMotion() || !ms || ms <= 0) {
      el[prop] = formatter(to);
      return;
    }

    var start = performance.now();
    function ease(t) { return 1 - Math.pow(1 - t, 3); }
    function tick(now) {
      var t = Math.min(1, (now - start) / ms);
      var v = from + (to - from) * ease(t);
      el[prop] = formatter(v);
      if (t < 1) requestAnimationFrame(tick);
    }
    requestAnimationFrame(tick);
  }

  /* ─── Live thousand-separator money input ─────────────────── */
  /**
   * Bind an <input> for live thousand-separator formatting.
   * Calls `onChange(num)` with the parsed numeric value on every keystroke.
   *
   * Caller is responsible for storing num in their state object and
   * triggering a recalc.
   *
   *   CalcKit.bindMoneyInput($('payment'), function(n){
   *     state.payment = n; recalc();
   *   });
   *
   * The input element should be type="text" inputmode="decimal" so the
   * browser shows the numeric keypad on mobile without rejecting commas.
   */
  function bindMoneyInput(el, onChange) {
    if (!el) return;
    // Initial format pass — if the input ships with a value, normalize it
    var initialRaw = el.value.replace(/[^0-9.\-]/g, '');
    var initialNum = parseFloat(initialRaw);
    if (isFinite(initialNum) && initialRaw !== '') {
      el.value = Math.round(initialNum).toLocaleString('en-US');
    }

    el.addEventListener('input', function () {
      var raw = el.value.replace(/[^0-9.\-]/g, '');
      var num = parseFloat(raw);
      if (isFinite(num) && raw !== '') {
        var formatted = Math.round(num).toLocaleString('en-US');
        if (formatted !== el.value) {
          el.value = formatted;
          // Restore caret to the end after re-render
          try { el.setSelectionRange(formatted.length, formatted.length); }
          catch (e) { /* some browsers throw on type=text — ignore */ }
        }
        onChange(num);
      } else {
        onChange(0);
      }
    });
  }

  /* ─── Segmented radio control ─────────────────────────────── */
  /**
   * Bind a `.tool-seg` container of `.tool-seg-opt` buttons.
   * Calls `onChange(value)` with the clicked button's `data-val`.
   * Toggles `.is-active` + `aria-checked` automatically.
   */
  function bindSegControl(container, onChange) {
    if (!container) return;
    container.addEventListener('click', function (e) {
      var btn = e.target.closest('.tool-seg-opt');
      if (!btn || !container.contains(btn)) return;
      var kids = container.children;
      for (var i = 0; i < kids.length; i++) {
        kids[i].classList.remove('is-active');
        kids[i].setAttribute('aria-checked', 'false');
      }
      btn.classList.add('is-active');
      btn.setAttribute('aria-checked', 'true');
      onChange(btn.dataset.val);
    });
  }

  /* ─── Export ──────────────────────────────────────────────── */
  root.CalcKit = {
    fmt:            fmt,
    fmtMoney:       fmtMoney,
    fmtRich:        fmtRich,
    fmtPct:         fmtPct,
    parseMoney:     parseMoney,
    animateNumber:  animateNumber,
    bindMoneyInput: bindMoneyInput,
    bindSegControl: bindSegControl,
    reducedMotion:  reducedMotion
  };
})(window);
