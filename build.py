#!/usr/bin/env python3
"""Builds the artifact page and the GitHub Pages bundle from src/game.html."""
import json, os, re
from PIL import Image, ImageDraw

ROOT = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(ROOT, 'src/game.html'), encoding='utf-8').read()
VERSION = re.search(r"VERSION='(v[0-9.]+)'", src).group(1)  # single source: the game's VERSION constant
NAME = 'Maskiner'
SLUG = 'maskiner'

# --- artifact version: page body only (the artifact host adds the skeleton)
os.makedirs(os.path.join(ROOT, 'artifact'), exist_ok=True)
open(os.path.join(ROOT, f'artifact/{SLUG}.html'), 'w', encoding='utf-8').write(src)
open(os.path.join(ROOT, f'artifact/{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(src)

# --- GitHub Pages version
head = f'''<!doctype html>
<html lang="da">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,maximum-scale=1,user-scalable=no,viewport-fit=cover">
<meta name="theme-color" content="#2f5f28">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="apple-mobile-web-app-title" content="{NAME}">
<meta name="description" content="{NAME} – kør mejetærsker, traktor og gummiged på gården: høst kornet, pløj marken og grav jord. Til mobil og browser ({VERSION})">
<link rel="manifest" href="manifest.webmanifest">
<link rel="icon" type="image/png" sizes="192x192" href="icon-192.png">
<link rel="apple-touch-icon" href="apple-touch-icon.png">
<style>:root{{padding:0}}body{{margin:0}}[hidden]{{display:none!important}}</style>
'''
body = src.replace(f'<title>{NAME}</title>', f'<title>{NAME} {VERSION}</title>', 1)
i = body.index('</style>') + len('</style>')
page = head + body[:i] + '\n</head>\n<body>\n' + body[i:] + '\n</body>\n</html>\n'
open(os.path.join(ROOT, 'index.html'), 'w', encoding='utf-8').write(page)
os.makedirs(os.path.join(ROOT, 'versions'), exist_ok=True)
open(os.path.join(ROOT, 'versions', f'{SLUG}-{VERSION}.html'), 'w', encoding='utf-8').write(page)

manifest = {
    "name": NAME, "short_name": NAME, "description": "Landbrugsspil med mejetærsker, traktor og gummiged",
    "start_url": "./", "scope": "./", "display": "fullscreen", "orientation": "any",
    "background_color": "#2f5f28", "theme_color": "#2f5f28", "lang": "da",
    "icons": [
        {"src": "icon-192.png", "sizes": "192x192", "type": "image/png", "purpose": "any maskable"},
        {"src": "icon-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any maskable"}]}
json.dump(manifest, open(os.path.join(ROOT, 'manifest.webmanifest'), 'w'), indent=2)
open(os.path.join(ROOT, '.nojekyll'), 'w').write('')

def icon(n):
    s = 4 * n
    im = Image.new('RGB', (s, s), '#d4a838')
    d = ImageDraw.Draw(im)
    for k in range(0, s, s // 16):
        d.rectangle([0, k, s, k + s // 64], fill='#b88a26')
    d.rectangle([0, s * .62, s, s], fill='#cbb575')
    u = s / 100
    cx, cy = s / 2, s * .55
    def R(x0, y0, x1, y1, col, r=3):
        d.rounded_rectangle([cx + x0 * u, cy + y0 * u, cx + x1 * u, cy + y1 * u], radius=r * u, fill=col)
    R(-31, -34, 31, -22, '#9c231d', 2)          # header
    R(-30, -24, 30, -22.5, '#cfd2d6', 0)
    R(-27, -30, -21, -2, '#1d1d1d'); R(21, -30, 27, -2, '#1d1d1d')  # front wheels
    R(-20, -22, 20, 30, '#d3342a', 5)           # body
    R(-13, -18, 13, -4, '#f1efe6', 3)           # cab
    R(-12, -21, 12, -17.5, '#78bee6', 1)
    R(-12, 0, 12, 18, '#2e2015', 2)             # grain tank
    d.ellipse([cx - 9 * u, cy + 2 * u, cx + 9 * u, cy + 16 * u], fill='#e8b73a')
    R(-18, 22, -12, 34, '#1d1d1d'); R(12, 22, 18, 34, '#1d1d1d')
    return im.resize((n, n), Image.LANCZOS)

icon(192).save(os.path.join(ROOT, 'icon-192.png'))
icon(512).save(os.path.join(ROOT, 'icon-512.png'))
icon(180).save(os.path.join(ROOT, 'apple-touch-icon.png'))
print('built', VERSION)
