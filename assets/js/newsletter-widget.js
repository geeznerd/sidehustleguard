/* SideHustleGuard — Newsletter signup widget
 *
 * Auto-hydrates into every <footer> on the page. Posts to /api/subscribe
 * (the existing ConvertKit-wired serverless function used by /tool's
 * email gate). Inline success + error states; no page reload.
 *
 * To skip on a specific page, add data-no-newsletter to the <footer>.
 * To customize copy on a specific page, pre-place a <div data-newsletter>
 * with custom inner HTML and the script will leave it alone.
 */
(function () {
  'use strict';

  var EMAIL_RE = /^[^\s@]+@[^\s@]+\.[^\s@]{2,}$/;

  function buildWidget() {
    var wrap = document.createElement('div');
    wrap.className = 'newsletter-widget';
    wrap.setAttribute('data-newsletter', 'auto');
    wrap.innerHTML = [
      '<div class="newsletter-widget-text">',
      '<strong>Get notified when new guides ship.</strong>',
      '<span>Occasional updates on tax changes, deadlines, and new tools. Unsubscribe any time.</span>',
      '</div>',
      '<form class="newsletter-widget-form" novalidate>',
      '<input type="email" name="email" required autocomplete="email"',
      '       placeholder="you@email.com" aria-label="Your email address"',
      '       inputmode="email" maxlength="254"/>',
      '<button type="submit">Notify me &rarr;</button>',
      '</form>',
      '<div class="newsletter-widget-state" role="status" aria-live="polite"></div>'
    ].join('');
    return wrap;
  }

  function attachHandlers(widget) {
    var form = widget.querySelector('form');
    var input = widget.querySelector('input[type="email"]');
    var btn = widget.querySelector('button');
    var state = widget.querySelector('.newsletter-widget-state');
    if (!form || !input || !btn || !state) return;

    function setState(kind, message) {
      state.textContent = message;
      state.setAttribute('data-kind', kind);
    }

    form.addEventListener('submit', function (e) {
      e.preventDefault();
      var email = (input.value || '').trim().toLowerCase();
      if (!email || !EMAIL_RE.test(email) || email.length > 254) {
        setState('error', 'Please enter a valid email address.');
        input.focus();
        return;
      }
      setState('loading', 'Subscribing…');
      btn.disabled = true;

      fetch('/api/subscribe', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email: email })
      })
        .then(function (r) {
          if (!r.ok) throw new Error('subscribe-failed');
          return r.json().catch(function () { return {}; });
        })
        .then(function () {
          widget.classList.add('is-success');
          form.style.display = 'none';
          setState('success', '✓ You’re on the list. Check your inbox to confirm.');
        })
        .catch(function () {
          setState('error', 'Couldn’t subscribe right now. Try again in a moment?');
          btn.disabled = false;
        });
    });
  }

  function hydrate() {
    var footers = document.querySelectorAll('footer:not([data-newsletter-hydrated]):not([data-no-newsletter])');
    Array.prototype.forEach.call(footers, function (footer) {
      footer.setAttribute('data-newsletter-hydrated', '1');
      /* If the page pre-placed a custom [data-newsletter] block, leave it alone */
      var existing = footer.querySelector('[data-newsletter]');
      if (existing) {
        attachHandlers(existing);
        return;
      }
      var widget = buildWidget();
      /* Insert at the top of the footer so it's the first thing visitors see
       * in the footer block, before the legal nav links + disclaimer */
      footer.insertBefore(widget, footer.firstChild);
      attachHandlers(widget);
    });
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', hydrate);
  } else {
    hydrate();
  }
})();
