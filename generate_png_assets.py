
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


# ─── WAVE DIVIDER (PNG — GitHub strips SVG animations) ───
def create_wave_divider():
    import math
    W, H = 1200, 40
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Draw a sine wave red line across full width
    points = []
    for x in range(W):
        y = int(H // 2 + 8 * math.sin(x * 2 * math.pi / 150))
        points.append((x, y))

    # Draw the wave line thick with glow effect
    # Outer glow
    for x in range(len(points) - 1):
        draw.line([points[x], points[x+1]], fill=(220, 38, 38, 40), width=8)
    # Mid glow
    for x in range(len(points) - 1):
        draw.line([points[x], points[x+1]], fill=(220, 38, 38, 80), width=4)
    # Core line
    for x in range(len(points) - 1):
        t = x / W
        r = int(180 + 68 * t)  # 180 -> 248
        g = int(20 + 93 * t)   # 20 -> 113
        b = int(20 + 93 * t)   # 20 -> 113
        draw.line([points[x], points[x+1]], fill=(r, g, b, 255), width=2)

    img.save("assets/wave_divider.png", "PNG")
    print("Created wave_divider.png")


# ─── FOOTER BANNER — same style as project banners ───
def create_footer_banner():
    """Same style as SKAIS/EXAMBRO banners: text + icon, clean gradient."""
    W, H = 1000, 200
    img = Image.new("RGBA", (W, H), (*BG, 255))
    draw = ImageDraw.Draw(img)

    # Smooth red glow center — same as make_banner
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    od.ellipse([W//4, 10, W*3//4, H-10], fill=(*RED_DARK, 35))
    orb = orb.filter(ImageFilter.GaussianBlur(60))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    # Top & bottom red lines
    draw.line([(0, 0), (W, 0)], fill=(*RED, 255), width=3)
    draw.line([(0, H-3), (W, H-3)], fill=(*RED, 255), width=3)

    # Quote text — centered, two lines
    font_quote = get_font(28, bold=True)
    font_author = get_font(13, bold=True)

    line1 = '"Ever tried. Ever failed. No matter.'
    line2 = 'Try again. Fail again. Fail better"'

    # Glow behind text
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    b1 = gd.textbbox((0, 0), line1, font=font_quote)
    b2 = gd.textbbox((0, 0), line2, font=font_quote)
    x1 = (W - 80 - (b1[2] - b1[0])) // 2
    x2 = (W - 80 - (b2[2] - b2[0])) // 2
    y1, y2 = 50, 90
    gd.text((x1, y1), line1, font=font_quote, fill=(*RED, 45))
    gd.text((x2, y2), line2, font=font_quote, fill=(*RED, 45))
    glow = glow.filter(ImageFilter.GaussianBlur(14))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Quote text gradient
    for line, lx, ly in [(line1, x1, y1), (line2, x2, y2)]:
        cx = lx
        for i, ch in enumerate(line):
            t = i / max(1, len(line) - 1)
            c = lerp(RED, RED_SOFT, t)
            draw.text((cx, ly), ch, font=font_quote, fill=(*c, 255))
            cx += draw.textlength(ch, font=font_quote)

    # Author pill badge
    author = "— Samuel Beckett"
    ab = draw.textbbox((0, 0), author, font=font_author)
    atw = ab[2] - ab[0]
    ax = (W - 80 - atw) // 2
    draw.rounded_rectangle([ax - 12, 135, ax + atw + 12, 157], radius=11, fill=(25, 10, 10, 220), outline=(*RED_DARK, 180), width=1)
    draw.text((ax, 138), author, font=font_author, fill=(*RED_SOFT, 255))

    # Pen/quill icon on the right — matching project banner style
    ix, iy = W - 100, H // 2
    # Pen body (angled)
    draw.line([(ix-15, iy+25), (ix+15, iy-25)], fill=(*RED, 200), width=4)
    draw.line([(ix-12, iy+22), (ix+12, iy-22)], fill=(*RED_SOFT, 150), width=2)
    # Pen tip
    draw.polygon([(ix-18, iy+30), (ix-15, iy+25), (ix-12, iy+28)], fill=(*RED, 220))
    # Pen cap
    draw.rounded_rectangle([ix+10, iy-30, ix+20, iy-20], radius=2, fill=(*RED, 200))
    # Writing lines coming from pen
    draw.line([(ix-30, iy+35), (ix-10, iy+35)], fill=(*RED_DARK, 120), width=1)
    draw.line([(ix-35, iy+40), (ix-15, iy+40)], fill=(*RED_DARK, 80), width=1)
    draw.line([(ix-28, iy+45), (ix-12, iy+45)], fill=(*RED_DARK, 50), width=1)

    img = img.convert("RGB")
    img.save("assets/footer_banner.png", "PNG", quality=95)
    print("Created footer_banner.png")


if __name__ == '__main__':
    create_directory()
    create_header()
    create_skais()
    create_exambro()
    create_wave_divider()
    create_footer_banner()
    print("Done")
