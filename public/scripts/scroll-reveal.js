(function () {
  function initReveal() {
    var els = document.querySelectorAll(".reveal");
    var prefersReduced = window.matchMedia("(prefers-reduced-motion: reduce)").matches;
    if (!("IntersectionObserver" in window) || prefersReduced) {
      els.forEach(function (el) {
        el.classList.add("revealed");
      });
      return;
    }
    var observer = new IntersectionObserver(
      function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("revealed");
            observer.unobserve(entry.target);
          }
        });
      },
      { threshold: 0.15 }
    );
    els.forEach(function (el) {
      observer.observe(el);
    });
  }

  if (document.readyState === "complete") {
    initReveal();
  } else {
    window.addEventListener("load", initReveal);
  }
})();
