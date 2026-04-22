(function () {
  // FAQ accordion
  var faqItems = document.querySelectorAll('.faq-item');
  faqItems.forEach(function (item) {
    var btn = item.querySelector('.faq-q');
    if (!btn) return;
    btn.addEventListener('click', function () {
      item.classList.toggle('open');
    });
  });

  // Sticky CTA visible después de pasar el hero
  var sticky = document.getElementById('sticky-cta');
  var hero = document.querySelector('.hero');
  if (sticky && hero) {
    var heroBottom = hero.getBoundingClientRect().bottom + window.scrollY;
    var check = function () {
      if (window.scrollY > heroBottom - 80) {
        sticky.classList.add('visible');
        document.body.classList.add('has-sticky-cta');
      } else {
        sticky.classList.remove('visible');
        document.body.classList.remove('has-sticky-cta');
      }
    };
    window.addEventListener('scroll', check, { passive: true });
    check();
  }

  // Visitantes viendo (oscilación sutil, poco frecuente)
  var liveEl = document.getElementById('live-viewers');
  if (liveEl) {
    var current = 22 + Math.floor(Math.random() * 6);
    liveEl.textContent = String(current);
    setInterval(function () {
      var delta = Math.random() < 0.5 ? -1 : 1;
      current = Math.max(18, Math.min(34, current + delta));
      liveEl.textContent = String(current);
    }, 18000);
  }
})();
