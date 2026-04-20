# Gymcraft Academy — Contexto del Proyecto

## ¿Qué es este proyecto?
Gymcraft Academy es un negocio de productos digitales. Se vende una colección de **+350 planos técnicos de máquinas de gimnasio** (PDFs) orientada a fabricantes, emprendedores metalúrgicos y entusiastas del fitness en LATAM. El tráfico principal viene de TikTok (videos orgánicos y/o pagados).

## Productos
| Producto | Archivo | Precio | Rol |
|---|---|---|---|
| Colección de planos | `Planos Maquinas Gym/` (+350 PDFs) | $10 USD | Producto principal |
| Guía de muebles | `Guía Muebles Metal y Madera.pdf` | $7 USD | Upsell post-compra (OTO) |

## Pipeline de ventas
```
TikTok → Landing Page → Hotmart Checkout ($10) → OTO ($7) → Entrega por email
```

## Decisiones de arquitectura tomadas
- **Landing page:** HTML + CSS + Vanilla JS (sin frameworks). Mobile-first (tráfico TikTok).
- **Hosting:** GitHub Pages (gratis). Dominio propio opcional (~$10/año Namecheap).
- **Pagos + entrega:** Hotmart en **modo privado** (solo procesador, sin aparecer en marketplace público para evitar reseñas en etapa inicial).
- **Upsell/OTO:** Nativo de Hotmart — aparece automáticamente después del pago principal.
- **Entrega:** Hotmart envía email con link de descarga automáticamente al confirmar el pago.
- **No usar:** Gumroad (sin métodos LATAM), Stripe (requiere entidad legal LATAM), Whop (para cursos en video, no PDFs).

## Estructura de archivos del proyecto
```
Gymcraft Academy/
├── CLAUDE.md              ← Este archivo
├── PLAN.md                ← Plan de implementación detallado
├── index.html             ← Landing page principal
├── thank-you.html         ← Página post-compra ("revisa tu email")
├── css/
│   └── style.css          ← Estilos (tema oscuro, acentos naranja/amarillo)
├── js/
│   ├── timer.js           ← Countdown rolling 3 horas (localStorage)
│   └── main.js            ← Interacciones CTA, scroll suave
└── img/
    ├── hero-mockup.png    ← Mockup del producto (crear en Canva)
    └── samples/           ← 3-5 previews de planos con marca de agua
```

## Landing page — secciones (en orden)
1. Barra de anuncio con timer
2. Hero + CTA principal
3. Bloque de dolor (4 problemas del buyer)
4. Solución (presentación del producto)
5. Qué incluye (369 categorías)
6. Previews de muestra (con marca de agua)
7. Anclaje de precio ($97 valor real → $10 lanzamiento)
8. Contador de urgencia (fondo rojo/naranja)
9. CTA repetido + logos de métodos de pago
10. FAQ (5 preguntas)
11. CTA final con timer

## Timer de urgencia — comportamiento
- Countdown de 3 horas que se renueva en ciclos (nunca llega a cero de forma definitiva)
- Persiste entre recargas de página usando `localStorage`
- Clave: `gymcraft_timer_epoch` — guarda el timestamp inicial
- Lógica: `remaining = CYCLE_MS - (elapsed % CYCLE_MS)` donde `CYCLE_MS = 10,800,000 ms`
- Consistente en múltiples pestañas del mismo navegador

## Reglas para este proyecto
- Todo el copy (textos) va en **español** orientado a LATAM
- Diseño **mobile-first** — el 90% del tráfico viene de móvil (TikTok)
- No crear área de miembros ni login — el producto se entrega por email
- No usar frameworks JS (React, Vue, etc.) — vanilla JS es suficiente
- No agregar funcionalidades no planificadas — MVP primero, optimizar después
- Los botones CTA deben tener un placeholder `HOTMART_CHECKOUT_URL` hasta que se configure Hotmart

## Estado actual del proyecto
- [ ] Fase 1: Configurar cuenta y productos en Hotmart
- [ ] Fase 2: Crear landing page (index.html + css + js)
- [ ] Fase 3: Crear thank-you.html
- [ ] Fase 4: Subir a GitHub Pages
- [ ] Fase 5: Prueba de compra completa + lanzamiento TikTok

## Próximo paso inmediato
Crear la landing page (`index.html`, `css/style.css`, `js/timer.js`, `js/main.js`). La URL de Hotmart se agrega después — se usa el placeholder `HOTMART_CHECKOUT_URL` en todos los botones CTA.
