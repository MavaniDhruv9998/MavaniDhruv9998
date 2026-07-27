import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_directory():
    if not os.path.exists('assets'):
        os.makedirs('assets')

def get_font(size, bold=False):
    names = ["arialbd.ttf", "segoeuib.ttf"] if bold else ["arial.ttf", "segoeui.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

BG = (6, 6, 8)
RED = (220, 38, 38)
RED_DARK = (130, 20, 20)
RED_SOFT = (248, 113, 113)


def make_banner(name, icon_func, filename, W=1000, H=200):
    """Shared banner style — same as header: name + one icon, clean gradient."""
    img = Image.new("RGBA", (W, H), (*BG, 255))
    draw = ImageDraw.Draw(img)

    # Smooth red glow center
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    od.ellipse([W//4, 10, W*3//4, H-10], fill=(*RED_DARK, 35))
    orb = orb.filter(ImageFilter.GaussianBlur(60))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    # Top & bottom red lines
    draw.line([(0, 0), (W, 0)], fill=(*RED, 255), width=3)
    draw.line([(0, H-3), (W, H-3)], fill=(*RED, 255), width=3)

    # Name centered
    font_name = get_font(50, bold=True)
    bbox = draw.textbbox((0, 0), name, font=font_name)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = (H - th) // 2

    # Glow behind name
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text((tx, ty), name, font=font_name, fill=(*RED, 45))
    glow = glow.filter(ImageFilter.GaussianBlur(16))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Name gradient text
    cx = tx
    for i, ch in enumerate(name):
        t = i / max(1, len(name) - 1)
        c = lerp(RED, RED_SOFT, t)
        draw.text((cx, ty), ch, font=font_name, fill=(*c, 255))
        cx += draw.textlength(ch, font=font_name)

    # Draw icon on the right side
    icon_func(draw, W, H)

    img = img.convert("RGB")
    img.save(f"assets/{filename}", "PNG", quality=95)
    print(f"Created {filename}")


# ─── HEADER ───
def create_header():
    def no_icon(draw, W, H):
        pass
    make_banner("DHRUV MAVANI", no_icon, "header_banner.png", W=1200, H=300)
    # Re-make with bigger font
    W, H = 1200, 300
    img = Image.new("RGBA", (W, H), (*BG, 255))
    draw = ImageDraw.Draw(img)

    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    od.ellipse([300, 20, 900, 320], fill=(*RED_DARK, 40))
    orb = orb.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    draw.line([(0, 0), (W, 0)], fill=(*RED, 255), width=3)
    draw.line([(0, H-3), (W, H-3)], fill=(*RED, 255), width=3)

    font_name = get_font(90, bold=True)
    name = "DHRUV MAVANI"
    bbox = draw.textbbox((0, 0), name, font=font_name)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = (H - th) // 2

    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text((tx, ty), name, font=font_name, fill=(*RED, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(20))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    cx = tx
    for i, ch in enumerate(name):
        t = i / max(1, len(name) - 1)
        c = lerp(RED, RED_SOFT, t)
        draw.text((cx, ty), ch, font=font_name, fill=(*c, 255))
        cx += draw.textlength(ch, font=font_name)

    img = img.convert("RGB")
    img.save("assets/header_banner.png", "PNG", quality=95)
    print("Created header_banner.png")


# ─── SKAIS — phone icon ───
def create_skais():
    def phone_icon(draw, W, H):
        # Simple phone/handset icon on the right
        ix, iy = W - 120, H // 2
        # Phone body
        draw.rounded_rectangle([ix-20, iy-40, ix+20, iy+40], radius=8, fill=(*RED, 200))
        # Screen area
        draw.rounded_rectangle([ix-14, iy-32, ix+14, iy+20], radius=4, fill=(*BG, 240))
        # Earpiece
        draw.rounded_rectangle([ix-8, iy-28, ix+8, iy-22], radius=2, fill=(*RED_SOFT, 180))
        # Home button
        draw.ellipse([ix-5, iy+24, ix+5, iy+34], fill=(*RED_SOFT, 150))
        # Sound waves from phone
        for r in range(1, 4):
            draw.arc([ix+20, iy-10*r, ix+20+15*r, iy+10*r], start=-60, end=60, fill=(*RED, 60 + r*30), width=2)

    make_banner("SKAIS", phone_icon, "skais_card.png")
    print("Created skais_card.png")


# ─── EXAMBRO — document/PDF icon ───
def create_exambro():
    def doc_icon(draw, W, H):
        # Simple document/page icon
        ix, iy = W - 110, H // 2
        # Page
        draw.rounded_rectangle([ix-22, iy-38, ix+22, iy+38], radius=4, fill=(*RED, 200))
        # Inner white area
        draw.rounded_rectangle([ix-16, iy-32, ix+16, iy+32], radius=2, fill=(*BG, 240))
        # Text lines
        draw.line([(ix-10, iy-22), (ix+10, iy-22)], fill=(*RED_SOFT, 200), width=2)
        draw.line([(ix-10, iy-14), (ix+6, iy-14)], fill=(*RED_SOFT, 150), width=2)
        draw.line([(ix-10, iy-6), (ix+10, iy-6)], fill=(*RED_SOFT, 150), width=2)
        # Magnifying glass over doc
        draw.ellipse([ix+2, iy+4, ix+22, iy+24], outline=(*RED, 220), width=2)
        draw.line([(ix+18, iy+22), (ix+28, iy+32)], fill=(*RED, 220), width=3)

    make_banner("EXAMBRO", doc_icon, "exambro_card.png")
    print("Created exambro_card.png")


# ─── WAVE DIVIDER (animated SVG) ───
def create_wave_divider():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 30" width="100%">
  <defs>
    <linearGradient id="rg" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#991B1B" stop-opacity="0.3"/>
      <stop offset="20%" stop-color="#DC2626"/>
      <stop offset="50%" stop-color="#F87171"/>
      <stop offset="80%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#991B1B" stop-opacity="0.3"/>
    </linearGradient>
    <filter id="glow">
      <feGaussianBlur stdDeviation="3" result="blur"/>
      <feMerge><feMergeNode in="blur"/><feMergeNode in="SourceGraphic"/></feMerge>
    </filter>
  </defs>
  <!-- Main visible straight red line -->
  <line x1="0" y1="15" x2="1000" y2="15" stroke="url(#rg)" stroke-width="2"/>
  <!-- Animated glowing dot traveling in wave motion -->
  <circle r="5" fill="#F87171" filter="url(#glow)">
    <animateMotion dur="2.5s" repeatCount="indefinite" path="M0,15 Q250,4 500,15 Q750,26 1000,15"/>
  </circle>
  <!-- Second dot going opposite direction -->
  <circle r="3" fill="#DC2626" opacity="0.8" filter="url(#glow)">
    <animateMotion dur="2.5s" repeatCount="indefinite" path="M1000,15 Q750,4 500,15 Q250,26 0,15"/>
  </circle>
  <!-- Trailing glow for first dot -->
  <circle r="10" fill="#DC2626" opacity="0.2">
    <animateMotion dur="2.5s" repeatCount="indefinite" path="M0,15 Q250,4 500,15 Q750,26 1000,15"/>
  </circle>
</svg>'''
    with open('assets/wave_divider.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created wave_divider.svg")


# ─── QUOTE CARD ───
def create_quote():
    W, H = 1000, 100
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=14, fill=(10, 10, 14, 250), outline=(*RED_DARK, 160), width=2)

    # Left red accent bar
    for y in range(15, H-15):
        t = (y - 15) / (H - 30)
        c = lerp(RED, RED_DARK, t)
        draw.line([(10, y), (14, y)], fill=(*c, 255))

    f_q = get_font(16, bold=True)
    f_a = get_font(11, bold=True)

    draw.text((30, 25), '"Ever tried. Ever failed. No matter. Try again. Fail again. Fail better"', font=f_q, fill=(245, 245, 245, 240))
    draw.rounded_rectangle([30, 60, 170, 82], radius=11, fill=(25, 10, 10, 220), outline=(*RED_DARK, 180), width=1)
    draw.text((44, 64), "-- Samuel Beckett", font=f_a, fill=(*RED_SOFT, 255))

    img = img.convert("RGB")
    img.save("assets/quote_card.png", "PNG", quality=95)
    print("Created quote_card.png")


if __name__ == '__main__':
    create_directory()
    create_header()
    create_skais()
    create_exambro()
    create_wave_divider()
    create_quote()
    print("Done")
