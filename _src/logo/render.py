# -*- coding: utf-8 -*-
"""Logo işaretini (isaret.svg) 512px şeffaf PNG'ye çevirir → media.py favicon'ları bundan üretir.
Çalıştır: python3 _src/logo/render.py  (yalnız logo değişince)"""
import asyncio, os
from playwright.async_api import async_playwright
K = os.path.dirname(os.path.abspath(__file__))
async def m():
    svg = open(os.path.join(K, "isaret.svg"), encoding="utf-8").read().replace("<svg ", '<svg width="512" height="512" ', 1)
    async with async_playwright() as p:
        b = await p.chromium.launch(); pg = await b.new_page(viewport={"width": 512, "height": 512})
        await pg.set_content(f'<body style="margin:0;background:transparent">{svg}</body>')
        await pg.locator("svg").screenshot(path=os.path.join(K, "isaret-512.png"), omit_background=True)
        await b.close()
asyncio.run(m())
