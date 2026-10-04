#!/usr/bin/env python3
# Renders shared/og.png (1200x630 share image) from the fiscal 2025 shares in the two data files.
# Needs Pillow; uses Halyard Text from ~/Library/Fonts if present, Helvetica Neue otherwise.
import json, os
from PIL import Image, ImageDraw, ImageFont
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..'); F = os.path.expanduser('~/Library/Fonts/')
def font(names, size):
    for n in names:
        if os.path.exists(F + n): return ImageFont.truetype(F + n, size)
    return ImageFont.truetype('/System/Library/Fonts/HelveticaNeue.ttc', size)
black = font(['Halyard-Text-Black.ttf', 'Halyard-Text-Bold.ttf', 'Halyard-Text-SemiBold.ttf'], 84)
light = font(['Halyard-Text-Light.ttf', 'Halyard-Text-Regular.ttf'], 30); cap = font(['Halyard-Text-Bold.ttf', 'Halyard-Text-SemiBold.ttf'], 17)
REV = {'property_tax': '#ff7c53', 'personal_income_tax': '#217ebe', 'sales_tax': '#dde44c', 'business_taxes': '#e7466d', 'other_taxes': '#cea9be', 'state_aid': '#394882', 'federal_aid': '#9b9fbc', 'fees_fines_other': '#707175'}
SPE = {'education': '#217ebe', 'social_services': '#e7466d', 'public_safety': '#394882', 'pensions': '#ff7c53', 'benefits': '#cea9be', 'debt_service': '#050507', 'health': '#dde44c', 'general_government': '#9b9fbc', 'environmental': '#707175', 'everything_else': '#c9c9cb'}
def alloc(items, N=100):
    tot = sum(v for _, v in items); c = [[k, int(v / tot * N), (v / tot * N) % 1] for k, v in items]; used = sum(x[1] for x in c)
    for x in sorted(c, key=lambda x: -x[2])[:N - used]: x[1] += 1
    return c
r = json.load(open(os.path.join(ROOT, 'nyc-who-pays/data/revenue_per_100.json')))['years']['2025']['per_100']
s = json.load(open(os.path.join(ROOT, 'nyc-where-it-goes/data/spending_per_100.json')))['years']['2025']['per_100']
W, H = 1200, 630; im = Image.new('RGB', (W, H), '#ffffff'); d = ImageDraw.Draw(im); d.rectangle([0, 0, W - 1, H - 1], outline='#050507', width=3)
y = 150
for line in ["New York", "City's budget", "in $100"]: d.text((64, y), line, font=black, fill='#050507'); y += 88
d.text((66, y + 22), "Who pays, where it goes, what changed", font=light, fill='#707175'); d.text((66, y + 60), "since 2000 and what the city builds.", font=light, fill='#707175')
def waffle(x0, y0, size, items, colors, label):
    cell = (size - 9 * 4) / 10; i = 0
    for k, n, _ in alloc(items):
        for _ in range(n):
            cx = x0 + (i % 10) * (cell + 4); cy = y0 + (i // 10) * (cell + 4); d.rectangle([cx, cy, cx + cell, cy + cell], fill=colors[k]); i += 1
    d.text((x0, y0 + size + 14), label.upper(), font=cap, fill='#707175')
waffle(640, 170, 240, [(k, r[k]) for k in REV], REV, 'Where it comes from'); waffle(912, 170, 240, [(k, s[k]) for k in SPE], SPE, 'Where it goes')
im.save(os.path.join(HERE, '..', 'shared', 'og.png'), optimize=True)
