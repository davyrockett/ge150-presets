"""Draws the app icons into ../icons. Run: python3 tools/make-icons.py (needs Pillow)."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parent.parent / "icons"
BG = (20, 20, 19)          # dark page background
BODY = (44, 43, 40)        # pedal housing
SCREEN = (251, 146, 60)    # orange display
INK = (20, 20, 19)
METAL = (200, 196, 188)


def draw(size: int) -> Image.Image:
    s = 1024  # draw large, then shrink for smooth edges
    img = Image.new("RGB", (s, s), BG)
    d = ImageDraw.Draw(img)
    # Pedal body, kept inside the safe zone iOS/Android won't crop
    d.rounded_rectangle([196, 176, 828, 848], radius=70, fill=BODY)
    # Display showing a preset slot
    d.rounded_rectangle([270, 250, 754, 520], radius=28, fill=SCREEN)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Menlo.ttc", 190)
    except OSError:
        font = ImageFont.load_default()
    d.text((512, 388), "2A", font=font, fill=INK, anchor="mm")
    # Two footswitches
    for x in (370, 654):
        d.ellipse([x - 64, 640, x + 64, 768], fill=METAL)
        d.ellipse([x - 40, 664, x + 40, 744], fill=BODY)
    return img.resize((size, size), Image.LANCZOS)


OUT.mkdir(exist_ok=True)
for name, size in [("icon-192.png", 192), ("icon-512.png", 512), ("apple-touch-icon.png", 180)]:
    draw(size).save(OUT / name, optimize=True)
    print("wrote", OUT / name)
