/* SideHustleGuard — Inline icon expander
 *
 * Lets pages drop a one-liner like:
 *
 *     <span class="icon icon--md" data-icon="warn"></span>
 *
 * and have the SVG markup hydrated at load. The icons themselves live as
 * standalone files under /assets/icons/ for easy editing and direct linking,
 * and this script fetches each one once and caches the markup.
 *
 * Use plain inline <svg>...</svg> when:
 *   - The icon appears in markup that must work without JS (e.g. og-image.html,
 *     print stylesheets, server-rendered nav lockups).
 *   - You're inside dangerously-fast-render territory (mega-card hero).
 *
 * Use this helper when:
 *   - The icon appears many times on a page (article callouts, list bullets).
 *   - You want to swap an emoji for an icon without bloating the page source.
 */
(function () {
  'use strict';

  var ICON_PATH = '/assets/icons/';
  var cache = Object.create(null);
  var pending = Object.create(null);

  function fetchIcon(name) {
    if (cache[name]) return Promise.resolve(cache[name]);
    if (pending[name]) return pending[name];
    pending[name] = fetch(ICON_PATH + name + '.svg', { credentials: 'omit' })
      .then(function (res) {
        if (!res.ok) throw new Error('icon ' + name + ' missing');
        return res.text();
      })
      .then(function (txt) {
        cache[name] = txt;
        return txt;
      })
      .catch(function () {
        cache[name] = '';
        return '';
      });
    return pending[name];
  }

  function hydrate(root) {
    var scope = root || document;
    var nodes = scope.querySelectorAll('[data-icon]:not([data-icon-hydrated])');
    nodes.forEach(function (el) {
      var name = el.getAttribute('data-icon');
      if (!name) return;
      el.setAttribute('data-icon-hydrated', '1');
      fetchIcon(name).then(function (svg) {
        if (svg) el.innerHTML = svg;
      });
    });
  }

  // Expose so pages can re-hydrate after DOM mutations
  window.SHGIcons = { hydrate: hydrate, fetch: fetchIcon };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', function () { hydrate(); });
  } else {
    hydrate();
  }
})();
