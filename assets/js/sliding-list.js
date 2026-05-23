/*!
 * SideHustleGuard — Sliding List
 *
 * The signature Direction E interaction: a vertical stack of items where
 * hovering or focusing any item slides an apricot-bordered cream pill to
 * that row over 350ms with cubic-bezier(0.4, 0, 0.2, 1).
 *
 * Markup contract:
 *   <div class="sliding-list" data-sliding-list>
 *     <div class="sliding-list-indicator" aria-hidden="true"></div>
 *     <button class="sliding-list-row" aria-current="true" data-value="...">
 *       <span class="sliding-list-num">01</span>
 *       <span class="sliding-list-title">…</span>
 *       <span class="sliding-list-meta">…</span>
 *     </button>
 *     <button class="sliding-list-row" data-value="...">…</button>
 *     …
 *   </div>
 *
 * The active row is identified by aria-current="true". Defaults to the
 * first row if none is marked.
 *
 * The component dispatches a `sliding-list:change` CustomEvent on the
 * list element whenever the active row changes, with detail:
 *   { index: <number>, row: <HTMLElement>, value: <string|null> }
 *
 * Listen for this to update a paired preview card, etc.
 *
 * Vanilla JS. No dependencies. Auto-bootstraps on DOMContentLoaded.
 * Respects prefers-reduced-motion (indicator snaps instead of slides).
 */
(function () {
  'use strict';

  var reduced = window.matchMedia &&
                window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  function init(list) {
    var indicator = list.querySelector('.sliding-list-indicator');
    var rows = Array.prototype.slice.call(
      list.querySelectorAll('.sliding-list-row')
    );
    if (!indicator || rows.length === 0) return;

    // If reduced motion is preferred, turn off the slide transition
    if (reduced) {
      indicator.style.transition = 'none';
    }

    function moveTo(row, options) {
      options = options || {};
      var top = row.offsetTop - list.offsetTop;
      indicator.style.top = top + 'px';

      rows.forEach(function (r) {
        if (r === row) {
          r.setAttribute('aria-current', 'true');
        } else {
          r.removeAttribute('aria-current');
        }
      });

      if (!options.silent) {
        var changeEvt;
        try {
          changeEvt = new CustomEvent('sliding-list:change', {
            bubbles: true,
            detail: {
              index: rows.indexOf(row),
              row: row,
              value: row.getAttribute('data-value')
            }
          });
        } catch (e) {
          // IE11 fallback
          changeEvt = document.createEvent('CustomEvent');
          changeEvt.initCustomEvent('sliding-list:change', true, false, {
            index: rows.indexOf(row),
            row: row,
            value: row.getAttribute('data-value')
          });
        }
        list.dispatchEvent(changeEvt);
      }
    }

    rows.forEach(function (row) {
      row.addEventListener('mouseenter', function () { moveTo(row); });
      row.addEventListener('focus', function () { moveTo(row); });
      row.addEventListener('click', function () { moveTo(row); });
    });

    // Set initial position. Find first row with aria-current="true",
    // else default to row 0.
    var initialIndex = -1;
    rows.forEach(function (r, i) {
      if (r.getAttribute('aria-current') === 'true' && initialIndex === -1) {
        initialIndex = i;
      }
    });
    if (initialIndex === -1) initialIndex = 0;

    // Use rAF so layout is measured after the element is in the DOM
    // and any sibling content has settled.
    requestAnimationFrame(function () {
      moveTo(rows[initialIndex], { silent: true });
    });

    // Reposition on viewport resize (the list may reflow).
    var resizeTimer = null;
    window.addEventListener('resize', function () {
      if (resizeTimer) clearTimeout(resizeTimer);
      resizeTimer = setTimeout(function () {
        var active = list.querySelector('.sliding-list-row[aria-current="true"]')
                     || rows[0];
        moveTo(active, { silent: true });
      }, 100);
    });
  }

  function bootstrap() {
    var lists = document.querySelectorAll('[data-sliding-list]');
    for (var i = 0; i < lists.length; i++) {
      init(lists[i]);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }
})();
