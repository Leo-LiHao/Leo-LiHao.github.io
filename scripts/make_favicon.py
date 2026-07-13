#!/usr/bin/env python3
"""Generate the "HL" monogram favicon set (white on Queen's red).

Produces, in images/:
  - favicon.svg              (vector, rounded square + "HL")
  - favicon-32x32.png
  - favicon-192x192.png
  - favicon-512x512.png
  - favicon.ico              (16, 32, 48 multi-size)
  - apple-touch-icon-180x180.png  (opaque, square; iOS applies its own mask)

Re-run after editing BG/TEXT/LETTERS below. Requires Pillow.
"""
import os
from PIL import Image, ImageDraw, ImageFont

BG = (157, 25, 57, 255)      # Queen's crimson #9d1939
TEXT = (255, 255, 255, 255)  # white
LETTERS = "HL"
FONT_PATH = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
SS = 4  # supersampling factor for smooth edges

HERE = os.path.dirname(os.path.abspath(__file__))
IMAGES = os.path.join(HERE, "..", "images")


def _fit_font(draw, text, box, path):
    """Largest font size whose text fits within box (a square side length)."""
    size = box
    while size > 4:
        font = ImageFont.truetype(path, size)
        l, t, r, b = draw.textbbox((0, 0), text, font=font)
        if (r - l) <= box and (b - t) <= box:
            return font
        size -= 2
    return ImageFont.truetype(path, 4)


def render(size, rounded=True, transparent=True):
    S = size * SS
    img = Image.new("RGBA", (S, S), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    if rounded:
        radius = int(S * 0.22)
        draw.rounded_rectangle([0, 0, S - 1, S - 1], radius=radius, fill=BG)
    else:
        draw.rectangle([0, 0, S - 1, S - 1], fill=BG)

    # Text target box: ~76% of the tile so the two letters sit with even padding.
    box = int(S * 0.76)
    font = _fit_font(draw, LETTERS, box, FONT_PATH)
    l, t, r, b = draw.textbbox((0, 0), LETTERS, font=font)
    w, h = r - l, b - t
    x = (S - w) / 2 - l
    y = (S - h) / 2 - t
    draw.text((x, y), LETTERS, font=font, fill=TEXT)

    img = img.resize((size, size), Image.LANCZOS)
    if not transparent:
        flat = Image.new("RGBA", (size, size), BG)
        flat.alpha_composite(img)
        img = flat
    return img


def main():
    out = lambda n: os.path.join(IMAGES, n)

    render(32).save(out("favicon-32x32.png"))
    render(192).save(out("favicon-192x192.png"))
    render(512).save(out("favicon-512x512.png"))

    # apple-touch: opaque, square (iOS masks corners itself)
    render(180, rounded=False, transparent=False).convert("RGB").save(
        out("apple-touch-icon-180x180.png")
    )

    # multi-size .ico
    ico = render(64)
    ico.save(out("favicon.ico"), sizes=[(16, 16), (32, 32), (48, 48)])

    # SVG (portable sans-serif stack; two letters tolerate minor font variance)
    r, g, b = BG[0], BG[1], BG[2]
    svg = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" role="img" aria-label="HL">
  <rect width="512" height="512" rx="113" ry="113" fill="#{r:02x}{g:02x}{b:02x}"/>
  <text x="256" y="256" fill="#ffffff"
        font-family="Arial, Helvetica, 'Helvetica Neue', sans-serif"
        font-weight="700" font-size="300"
        text-anchor="middle" dominant-baseline="central">HL</text>
</svg>
'''
    with open(out("favicon.svg"), "w") as f:
        f.write(svg)

    print("Wrote favicon set to images/")


if __name__ == "__main__":
    main()
