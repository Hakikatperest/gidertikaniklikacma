# -*- coding: utf-8 -*-
"""Görsel türevleri + favicon. Kaynak: _src/kaynak/ (kullanıcının yüklediği orijinaller). Çıktı: images/, kökte favicon.
Çalıştır: python3 _src/media.py   (build.py'den önce, yalnızca görsel değişince)

⚠️ banner-orijinal.webp: yapay zekâ üretimi banner. Sol yarısında "İstanbul Avrupa Yakası" yazıyor (YANLIŞ bölge —
   site Anadolu Yakası) → yalnız sağ yarısı (usta + makaralı kamera, yazısız) KIRP ile alınır. Sol yarı ASLA yayınlanmaz."""
import os
from PIL import Image, ImageDraw

KOK = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KAYNAK = os.path.join(KOK, "_src", "kaynak")
CIKTI = os.path.join(KOK, "images")

# kaynak dosya → (yayın tabanı, kırpma kutusu (x0,y0,x1,y1) ya da None, genişlikler)
GORSELLER = {
 "banner-orijinal.webp": ("gider-tikaniklik-acma-kamerali-tespit", (890, 0, 1639, 960), (480, 749)),
}
# saha fotoğrafları gelince: "dosya.webp": ("anahtar-kelimeli-taban", None, (480, 960))

def kaydet(k, taban, g):
    k.save(os.path.join(CIKTI, f"{taban}-{g}.webp"), "WEBP", quality=78 if g < 1000 else 74, method=6)
    k.save(os.path.join(CIKTI, f"{taban}-{g}.avif"), "AVIF", quality=55 if g < 1000 else 50, speed=4)

def turev():
    os.makedirs(CIKTI, exist_ok=True)
    for ad, (taban, kutu, genler) in GORSELLER.items():
        im = Image.open(os.path.join(KAYNAK, ad)).convert("RGB")
        if kutu: im = im.crop(kutu)
        for g in genler:
            k = im.copy()
            if k.width > g: k = k.resize((g, round(k.height * g / k.width)), Image.LANCZOS)
            kaydet(k, taban, k.width)
        print(taban, im.size, genler)
    # og:image 1200×800 JPEG — kırpılmış bölgenin ortasından (yalnız sağ yarı; yanlış bölge yazısı yok)
    im = Image.open(os.path.join(KAYNAK, "banner-orijinal.webp")).convert("RGB").crop((890, 140, 1639, 640))
    im.resize((1200, 801), Image.LANCZOS).save(os.path.join(CIKTI, "og-gider-tikaniklik-acma.jpg"), quality=82, optimize=True)

def favicon():
    # Lacivert yuvarlak kare + mavi damla (banner logosunun damlası). ⚠️ WebP favicon Google'da görünmez → ico + png.
    S = 512
    im = Image.new("RGBA", (S, S), (0, 0, 0, 0)); d = ImageDraw.Draw(im)
    d.rounded_rectangle((0, 0, S - 1, S - 1), radius=112, fill=(10, 32, 72, 255))
    d.ellipse((136, 196, 376, 436), fill=(30, 136, 229, 255))
    d.polygon([(256, 64), (148, 270), (364, 270)], fill=(30, 136, 229, 255))
    d.ellipse((196, 290, 252, 346), fill=(255, 255, 255, 210))
    im.resize((48, 48), Image.LANCZOS).save(os.path.join(KOK, "favicon.ico"), sizes=[(48, 48), (32, 32), (16, 16)])
    for b in (48, 96, 180, 192, 512):
        im.resize((b, b), Image.LANCZOS).save(os.path.join(CIKTI, f"favicon-{b}.png"), optimize=True)
    print("favicon tamam")

if __name__ == "__main__":
    turev(); favicon()
