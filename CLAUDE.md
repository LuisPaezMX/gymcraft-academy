# Gymcraft Academy — Contexto del Proyecto

## ¿Qué es este proyecto?
Negocio de productos digitales. Se vende una colección de +350 planos técnicos de máquinas de gimnasio (PDFs) orientada a fabricantes, emprendedores metalúrgicos y entusiastas del fitness en LATAM. El tráfico principal viene de TikTok.

## Productos
| Producto | Archivo | Precio | Rol |
|---|---|---|---|
| Colección de planos | `Planos Maquinas Gym/` (+350 PDFs) | $10 USD | Producto principal |
| Guía de muebles | `Guía Muebles Metal y Madera.pdf` | $7 USD | Upsell post-compra (OTO) |

## Pipeline de ventas
```
TikTok → Landing Page → Hotmart Checkout ($10) → OTO ($7) → Entrega por email
```

## Estructura de archivos
```
Gymcraft Academy/
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

## Estado actual
- [ ] Fase 1: Configurar cuenta y productos en Hotmart
- [ ] Fase 2: Crear landing page (index.html + css + js)
- [ ] Fase 3: Crear thank-you.html
- [ ] Fase 4: Subir a GitHub Pages
- [ ] Fase 5: Prueba de compra completa + lanzamiento TikTok

## Próximo paso
Crear la landing page (`index.html`, `css/style.css`, `js/timer.js`, `js/main.js`). Usar el placeholder `HOTMART_CHECKOUT_URL` en todos los botones CTA.
