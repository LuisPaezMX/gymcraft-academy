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
TikTok → Landing Page → Hotmart Checkout ($10) → OTO ($7) → Entrega: Hotmart envía PDF "Guía de descarga Gymcraft" → Usuario abre PDF → Botón lleva a carpeta Google Drive con los planos
```

## Estructura de archivos
```
Gymcraft Academy/
├── index.html                  ← Landing page principal
├── thank-you.html              ← Página post-compra (instrucciones Hotmart → Drive)
├── pending-payment.html        ← Compras con pago pendiente (OXXO, efectivo) [PENDIENTE]
├── pending-credit.html         ← Compras en análisis de crédito [PENDIENTE]
├── legal.html                  ← Términos y política de privacidad
├── guia-descarga.html          ← Guía de descarga para los clientes
├── favicon.ico                 ← Favicon circular generado desde logo_redes.jpg
├── favicon-{16,32,192,512}.png ← Variantes para navegador, Android, splash
├── css/
│   └── style.css               ← Estilos (mobile-first, tema claro, acentos naranja/ámbar)
├── js/
│   ├── timer.js                ← Countdown rolling 3 horas (localStorage, modular)
│   └── main.js                 ← FAQ accordion, sticky CTA, live viewers
├── scripts/
│   └── optimize_images.py      ← Pipeline Pillow: JPG → WebP + fallback + favicon circular
└── img/
    ├── logo-watermark.webp     ← Logo optimizado (54KB vs 813KB del PNG original)
    ├── trabajo/                ← Imágenes fuente editadas manualmente (pre-optimización)
    └── samples/                ← 5 previews de planos en WebP + JPG fallback
        ├── 01-banca-plana-1.{webp,jpg}
        ├── 02-banca-regulable-01.{webp,jpg}
        ├── 03-power-rack-01.{webp,jpg}
        ├── 04-sentadilla-hack-01.{webp,jpg}
        └── 05-polea-01.{webp,jpg}
```

## Hotmart
- Producto ID: `7578464`
- **Checkout URL**: `https://pay.hotmart.com/R105424818K` ← usar en todos los botones CTA
- Página de Ventas: `https://go.hotmart.com/R105424818K`
- Página de Producto: `https://go.hotmart.com/R105424818K?dp=1`

## Estado actual
- [x] Fase 1: Configurar cuenta y productos en Hotmart
- [x] Fase 2: Crear landing page (index.html + css + js + imágenes optimizadas WebP)
- [x] Fase 3: Crear thank-you.html (flujo Hotmart → PDF guía → Drive)
- [ ] Fase 4: Crear pending-payment.html (OXXO/efectivo)
- [ ] Fase 5: Decidir y crear pending-credit.html (análisis de crédito)
- [ ] Fase 6: Subir a GitHub Pages
- [ ] Fase 7: Prueba de compra completa + lanzamiento TikTok

## Próximo paso
Crear `pending-payment.html` para cuando el cliente elige pagar por OXXO o efectivo y el pago aún no se confirma. Debe explicar que el acceso llega cuando Hotmart valide el pago (24-48h típicamente) y reforzar que todavía no cancele ni vuelva a pagar.
