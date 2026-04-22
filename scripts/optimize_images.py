"""
Optimiza las imágenes del proyecto:
- Convierte los planos (JPG) de img/trabajo/ a WebP optimizado en img/samples/
- Convierte logo_redes.jpg en favicon circular (PNG con transparencia)
- Convierte Logo_sin_fondo.png (watermark) a WebP
"""

from PIL import Image, ImageDraw, ImageOps
from pathlib import Path

ROOT = Path(__file__).parent.parent
TRABAJO = ROOT / "img" / "trabajo"
SAMPLES = ROOT / "img" / "samples"
SAMPLES.mkdir(parents=True, exist_ok=True)

# ── 1. Planos: JPG -> WebP con calidad alta (los planos necesitan líneas nítidas)
PLANS = [
    "01-banca-plana-1.jpg",
    "02-banca-regulable-01.jpg",
    "03-power-rack-01.jpg",
    "04-sentadilla-hack-01.jpg",
    "05-polea-01.jpg",
]

MAX_WIDTH = 1600  # suficiente para retina mobile y desktop

for filename in PLANS:
    src = TRABAJO / filename
    if not src.exists():
        print(f"[SKIP] {src} no existe")
        continue

    img = Image.open(src).convert("RGB")
    if img.width > MAX_WIDTH:
        ratio = MAX_WIDTH / img.width
        new_size = (MAX_WIDTH, int(img.height * ratio))
        img = img.resize(new_size, Image.LANCZOS)

    stem = Path(filename).stem
    out_webp = SAMPLES / f"{stem}.webp"
    out_jpg  = SAMPLES / f"{stem}.jpg"

    img.save(out_webp, "WEBP", quality=88, method=6)
    img.save(out_jpg, "JPEG", quality=88, optimize=True, progressive=True)
    print(f"[OK] {filename} -> {out_webp.name} ({out_webp.stat().st_size // 1024}KB) / {out_jpg.name} ({out_jpg.stat().st_size // 1024}KB)")

# ── 2. Favicon circular desde logo_redes.jpg
fav_src = ROOT / "logo_redes.jpg"
if fav_src.exists():
    logo = Image.open(fav_src).convert("RGBA")
    size = min(logo.size)
    logo = ImageOps.fit(logo, (size, size), Image.LANCZOS)

    mask = Image.new("L", (size, size), 0)
    draw = ImageDraw.Draw(mask)
    draw.ellipse((0, 0, size, size), fill=255)

    circ = Image.new("RGBA", (size, size), (0, 0, 0, 0))
    circ.paste(logo, (0, 0), mask)

    for target, px in [("favicon-512.png", 512), ("favicon-192.png", 192), ("favicon-32.png", 32), ("favicon-16.png", 16)]:
        resized = circ.resize((px, px), Image.LANCZOS)
        resized.save(ROOT / target, "PNG", optimize=True)
        print(f"[OK] {target} ({(ROOT / target).stat().st_size // 1024}KB)")

    circ.save(ROOT / "favicon.ico", format="ICO", sizes=[(16,16),(32,32),(48,48),(64,64)])
    print(f"[OK] favicon.ico ({(ROOT / 'favicon.ico').stat().st_size // 1024}KB)")

# ── 3. Watermark: Logo_sin_fondo.png -> WebP (respetando alpha)
wm_src = ROOT / "Logo_sin_fondo.png"
if wm_src.exists():
    wm = Image.open(wm_src).convert("RGBA")
    if wm.width > 800:
        ratio = 800 / wm.width
        wm = wm.resize((800, int(wm.height * ratio)), Image.LANCZOS)
    wm_out = ROOT / "img" / "logo-watermark.webp"
    wm.save(wm_out, "WEBP", quality=90, method=6, lossless=False)
    print(f"[OK] {wm_out.name} ({wm_out.stat().st_size // 1024}KB, antes 813KB)")

print("\nListo.")
