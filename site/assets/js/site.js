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

  /* Valuation step 1: address -> lead, Zillow tab, Street View, reveal.
   *
   * Order matters and it is not the obvious one. The address is POSTed as a
   * lead BEFORE the Zillow tab opens, because a good share of people will
   * look at their Zestimate and never come back to this page. Firing the lead
   * first means an abandoned session still reaches an agent with the one
   * piece of information that matters.
   *
   * window.open is called synchronously inside the submit handler — inside
   * the user gesture — or popup blockers eat it. So the POST is fire-and-
   * forget (keepalive) rather than awaited.
   *
   * Progressive enhancement: with JS off, step 1 does nothing and the full
   * form below it still posts normally. Nobody is stranded. */
  var step1 = document.querySelector("[data-address-step]");
  if (step1) {
    step1.addEventListener("submit", function (e) {
      e.preventDefault();
      var input = step1.querySelector("[name=address]");
      var address = input ? input.value.trim() : "";
      if (!address) return;

      var endpoint = step1.getAttribute("data-endpoint");
      var zillow = step1.getAttribute("data-zillow");
      var key = step1.getAttribute("data-streetview-key");
      var enc = encodeURIComponent(address);

      /* 1. The lead, first and unconditionally. */
      if (endpoint && endpoint.indexOf("REPLACE") === -1) {
        try {
          fetch(endpoint, {
            method: "POST",
            keepalive: true,
            headers: { "Content-Type": "application/json", Accept: "application/json" },
            body: JSON.stringify({
              address: address,
              _subject: "Address lookup — " + address,
              kind: "address-lookup",
              note: "Submitted the address step and was sent to Zillow. May not have completed the full form."
            })
          });
        } catch (err) { /* never block the flow on this */ }
      }

      /* 2. Zillow, in a new tab, inside the gesture. */
      if (zillow) {
        window.open(zillow.replace("{address}", enc), "_blank", "noopener");
      }

      /* 3. The house, if a Street View key is configured. */
      var result = document.querySelector("[data-address-result]");
      var shot = document.querySelector("[data-streetview]");
      var echo = document.querySelector("[data-address-echo]");
      if (echo) echo.textContent = address;
      if (shot && key) {
        /* return_error_code makes Google 404 rather than serve a grey "no
         * imagery" tile, so onerror can hide the figure instead of showing a
         * blank box where someone's house should be. */
        shot.onload = function () { shot.hidden = false; };
        shot.onerror = function () { shot.hidden = true; };
        shot.alt = "Street view of " + address;
        shot.src =
          "https://maps.googleapis.com/maps/api/streetview?size=800x500&fov=80" +
          "&return_error_code=true&location=" + enc + "&key=" + encodeURIComponent(key);
      }

      /* 4. Reveal, and carry the address into the full form so they do not
       *    type it twice. */
      if (result) {
        result.hidden = false;
        result.scrollIntoView({ behavior: "smooth", block: "start" });
      }
      var full = document.querySelector("#full-valuation [name=address]");
      if (full && !full.value) full.value = address;
    });
  }

  /* Copyright year — one less thing to go stale, since the old site shipped
   * "Copyright © 2022" for four years. */
  var year = document.querySelector("[data-year]");
  if (year) year.textContent = String(new Date().getFullYear());
})();
