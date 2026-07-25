/* Team Azizi — progressive enhancement only.
 *
 * Every page renders complete without this file: schema is server-rendered,
 * navigation is real links, and the nav is opaque by default (the transparent
 * hero treatment is the enhancement, not the baseline). Nothing here is
 * load-bearing for content or for crawlers.
 */

(function () {
  "use strict";

  /* Nav: solid once the hero is behind us. */
  var nav = document.querySelector("[data-nav]");
  if (nav && document.body.classList.contains("has-hero")) {
    var threshold = window.innerHeight * 0.6;
    var ticking = false;

    var sync = function () {
      nav.classList.toggle("is-scrolled", window.scrollY > threshold);
      ticking = false;
    };

    window.addEventListener(
      "scroll",
      function () {
        if (!ticking) {
          window.requestAnimationFrame(sync);
          ticking = true;
        }
      },
      { passive: true }
    );

    window.addEventListener(
      "resize",
      function () {
        threshold = window.innerHeight * 0.6;
        sync();
      },
      { passive: true }
    );

    sync();
  }

  /* Drawer. */
  var drawer = document.querySelector("[data-drawer]");
  var openBtn = document.querySelector("[data-drawer-open]");
  var closeBtn = document.querySelector("[data-drawer-close]");

  if (drawer && openBtn) {
    var lastFocus = null;

    var open = function () {
      lastFocus = document.activeElement;
      drawer.hidden = false;
      openBtn.setAttribute("aria-expanded", "true");
      document.body.style.overflow = "hidden";
      if (closeBtn) closeBtn.focus();
    };

    var close = function () {
      drawer.hidden = true;
      openBtn.setAttribute("aria-expanded", "false");
      document.body.style.overflow = "";
      if (lastFocus) lastFocus.focus();
    };

    openBtn.addEventListener("click", open);
    if (closeBtn) closeBtn.addEventListener("click", close);

    drawer.addEventListener("click", function (event) {
      if (event.target === drawer) close();
    });

    document.addEventListener("keydown", function (event) {
      if (event.key === "Escape" && !drawer.hidden) close();
    });
  }


  /* Lead forms: put the property address in the notification subject line.
   * The address IS the lead on the valuation form — an email titled
   * "Home valuation request" is a chore to triage, one titled
   * "Valuation request — 12860 El Camino Real, 92130" is actionable from the
   * phone. Progressive enhancement: without JS the form still posts and still
   * emails, just with the generic subject. */
  var leadForms = document.querySelectorAll("[data-lead-form]");
  Array.prototype.forEach.call(leadForms, function (form) {
    form.addEventListener("submit", function () {
      var subject = form.querySelector("[data-subject-prefix]");
      if (!subject) return;
      var address = form.querySelector("[name=address]");
      var hood = form.querySelector("[name=neighborhood]");
      var parts = [subject.getAttribute("data-subject-prefix")];
      if (address && address.value) parts.push(address.value.trim());
      if (hood && hood.value) parts.push(hood.value);
      subject.value = parts.join(" \u2014 ");
    });
  });

  /* Copyright year — one less thing to go stale, since the old site shipped
   * "Copyright © 2022" for four years. */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
