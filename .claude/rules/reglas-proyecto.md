---
description: Reglas generales de desarrollo para Gymcraft Academy
---

- Todo el copy (textos) va en español orientado a LATAM
- Diseño mobile-first — el 90% del tráfico viene de móvil (TikTok)
- No crear área de miembros ni login — la entrega del producto la gestiona Hotmart automáticamente: al confirmar el pago envía el email con el link de descarga sin intervención manual
- Preferir vanilla JS sobre frameworks (React, Vue, etc.) para mantener el proyecto ligero; si en algún momento la complejidad lo justifica, evaluar antes de agregar dependencias
- No agregar funcionalidades no planificadas — MVP primero, optimizar después
- Los botones CTA deben usar el placeholder `HOTMART_CHECKOUT_URL` hasta que se configure Hotmart