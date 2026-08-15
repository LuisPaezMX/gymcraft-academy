(function () {
  // Propaga los parámetros de la URL de la landing (Meta Ads, TikTok, etc.)
  // a los enlaces de Hotmart, sin sobrescribir los que el enlace ya lleva.
  var incoming = new URLSearchParams(window.location.search);
  if (!incoming.toString()) return;

  var isHotmart = /(^|\.)hotmart\.com$/i;

  var apply = function () {
    var links = document.querySelectorAll('a[href*="hotmart.com"]');
    Array.prototype.forEach.call(links, function (link) {
      var url;
      try {
        url = new URL(link.href, window.location.href);
      } catch (e) {
        return;
      }
      if (!isHotmart.test(url.hostname)) return;
      incoming.forEach(function (value, key) {
        if (!url.searchParams.has(key)) url.searchParams.append(key, value);
      });
      link.href = url.href;
    });
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', apply);
  } else {
    apply();
  }
})();
