(function () {
  var EPOCH_KEY = 'gymcraft_timer_epoch';
  var CYCLE_MS = 3 * 60 * 60 * 1000; // 3 horas rodantes

  function getEpoch() {
    var stored = localStorage.getItem(EPOCH_KEY);
    if (stored) {
      var e = parseInt(stored, 10);
      if (!isNaN(e) && e > 0) return e;
    }
    var fresh = Date.now();
    localStorage.setItem(EPOCH_KEY, String(fresh));
    return fresh;
  }

  function format(ms) {
    if (ms < 0) ms = 0;
    var total = Math.floor(ms / 1000);
    var h = String(Math.floor(total / 3600)).padStart(2, '0');
    var m = String(Math.floor((total % 3600) / 60)).padStart(2, '0');
    var s = String(total % 60).padStart(2, '0');
    return h + ':' + m + ':' + s;
  }

  var epoch = getEpoch();
  var targets = document.querySelectorAll('[data-timer]');

  function tick() {
    var elapsed = Date.now() - epoch;
    var remaining = CYCLE_MS - (elapsed % CYCLE_MS);
    var text = format(remaining);
    for (var i = 0; i < targets.length; i++) {
      targets[i].textContent = text;
    }
  }

  tick();
  setInterval(tick, 1000);
})();
