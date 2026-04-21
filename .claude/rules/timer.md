---
description: Lógica del countdown de urgencia rolling de 3 horas
paths:
  - js/timer.js
---

- Countdown de 3 horas que se renueva en ciclos (nunca llega a cero de forma definitiva)
- Persiste entre recargas de página usando `localStorage`
- Clave: `gymcraft_timer_epoch` — guarda el timestamp inicial
- Lógica: `remaining = CYCLE_MS - (elapsed % CYCLE_MS)` donde `CYCLE_MS = 10_800_000` ms
- Debe ser consistente en múltiples pestañas del mismo navegador