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

# ── Colors ──
BG = (6, 6, 8)
RED = (220, 38, 38)
RED_DARK = (130, 20, 20)

# ─────────────────────────────────────
# HEADER — Name only, clean gradient
# ─────────────────────────────────────
def create_header():
    W, H = 1200, 300
    img = Image.new("RGBA", (W, H), (*BG, 255))
    draw = ImageDraw.Draw(img)

    # Simple smooth red glow in center — no grid, no particles
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    od.ellipse([300, 20, 900, 320], fill=(*RED_DARK, 40))
    orb = orb.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    # Top & bottom thin red line
    draw.line([(0, 0), (W, 0)], fill=(*RED, 255), width=3)
    draw.line([(0, H-3), (W, H-3)], fill=(*RED, 255), width=3)

    # ── Name only ──
    font_name = get_font(90, bold=True)
    name = "DHRUV MAVANI"
    bbox = draw.textbbox((0, 0), name, font=font_name)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = (H - th) // 2

    # Soft glow behind
    glow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    gd = ImageDraw.Draw(glow)
    gd.text((tx, ty), name, font=font_name, fill=(*RED, 50))
    glow = glow.filter(ImageFilter.GaussianBlur(20))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Name text — simple gradient red
    cx = tx
    for i, ch in enumerate(name):
        t = i / max(1, len(name) - 1)
        c = lerp(RED, (248, 113, 113), t)
        draw.text((cx, ty), ch, font=font_name, fill=(*c, 255))
        cx += draw.textlength(ch, font=font_name)

    img = img.convert("RGB")
    img.save("assets/header_banner.png", "PNG", quality=95)
    print("Created header_banner.png")

# ─────────────────────────────────────
# ANIMATED WAVE DIVIDER (SVG)
# ─────────────────────────────────────
def create_wave_divider():
    svg = '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1000 40" width="100%">
  <defs>
    <linearGradient id="rg" x1="0%" x2="100%">
      <stop offset="0%" stop-color="#060608"/>
      <stop offset="30%" stop-color="#DC2626"/>
      <stop offset="50%" stop-color="#F87171"/>
      <stop offset="70%" stop-color="#DC2626"/>
      <stop offset="100%" stop-color="#060608"/>
    </linearGradient>
  </defs>
  <rect width="1000" height="40" fill="#060608"/>
  <line x1="0" y1="20" x2="1000" y2="20" stroke="url(#rg)" stroke-width="1.5" stroke-opacity="0.5"/>
  <circle r="4" fill="#DC2626" opacity="0.9">
    <animateMotion dur="3s" repeatCount="indefinite" path="M0,20 Q250,5 500,20 Q750,35 1000,20"/>
  </circle>
  <circle r="2" fill="#F87171" opacity="0.6">
    <animateMotion dur="3s" repeatCount="indefinite" path="M1000,20 Q750,5 500,20 Q250,35 0,20"/>
  </circle>
  <circle r="6" fill="#DC2626" opacity="0.15">
    <animateMotion dur="3s" repeatCount="indefinite" path="M0,20 Q250,5 500,20 Q750,35 1000,20"/>
  </circle>
</svg>'''
    with open('assets/wave_divider.svg', 'w', encoding='utf-8') as f:
        f.write(svg)
    print("Created wave_divider.svg")

# ─────────────────────────────────────
# QUOTE CARD — simple
# ─────────────────────────────────────
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
    draw.text((44, 64), "— Samuel Beckett", font=f_a, fill=(248, 113, 113, 255))

    img = img.convert("RGB")
    img.save("assets/quote_card.png", "PNG", quality=95)
    print("Created quote_card.png")

# ─────────────────────────────────────
# SKAIS CARD — clean
# ─────────────────────────────────────
def create_skais():
    W, H = 1000, 220
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=14, fill=(10, 10, 14, 250), outline=(*RED_DARK, 160), width=2)

    # Top accent line
    for x in range(3, W-3):
        t = (x - 3) / (W - 6)
        c = lerp(RED_DARK, RED, t)
        draw.line([(x, 2), (x, 4)], fill=(*c, 255))

    f_badge = get_font(10, bold=True)
    f_title = get_font(22, bold=True)
    f_bullet = get_font(13)
    f_stack = get_font(10, bold=True)

    draw.rounded_rectangle([25, 15, 155, 34], radius=10, fill=(25, 10, 10, 230), outline=(*RED, 180), width=1)
    draw.text((37, 18), "VOICE AI PROJECT", font=f_badge, fill=(*RED, 255))

    draw.text((25, 42), "SKAIS  —  Restaurant AI Agent", font=f_title, fill=(245, 245, 245, 255))

    bullets = [
        "Voice AI agent answering live phone orders & reservations",
        "RAG knowledge base for menu, hours & policies",
        "Auto SMS confirmations via Twilio SDK",
        "50%+ cost savings vs human operators",
    ]
    by = 76
    for b in bullets:
        draw.text((35, by), "▸", font=f_bullet, fill=(*RED, 255))
        draw.text((52, by), b, font=f_bullet, fill=(180, 180, 185, 255))
        by += 22

    draw.text((25, 185), "STACK:", font=f_stack, fill=(80, 80, 90, 255))
    sx = 72
    for s in ["Python", "FastAPI", "Retell AI", "LangChain", "Supabase", "Twilio", "Next.js"]:
        sw = int(draw.textlength(s, font=f_stack)) + 12
        draw.rounded_rectangle([sx, 182, sx+sw, 198], radius=4, fill=(25, 10, 10, 220))
        draw.text((sx+6, 184), s, font=f_stack, fill=(248, 113, 113, 255))
        sx += sw + 4

    img = img.convert("RGB")
    img.save("assets/skais_card.png", "PNG", quality=95)
    print("Created skais_card.png")

# ─────────────────────────────────────
# EXAMBRO CARD — clean
# ─────────────────────────────────────
def create_exambro():
    W, H = 1000, 220
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=14, fill=(10, 10, 14, 250), outline=(*RED_DARK, 160), width=2)

    for x in range(3, W-3):
        t = (x - 3) / (W - 6)
        c = lerp(RED, RED_DARK, t)
        draw.line([(x, 2), (x, 4)], fill=(*c, 255))

    f_badge = get_font(10, bold=True)
    f_title = get_font(22, bold=True)
    f_bullet = get_font(13)
    f_stack = get_font(10, bold=True)

    draw.rounded_rectangle([25, 15, 145, 34], radius=10, fill=(25, 10, 10, 230), outline=(*RED, 180), width=1)
    draw.text((37, 18), "OCR AI PROJECT", font=f_badge, fill=(*RED, 255))

    draw.text((25, 42), "ExamBro  —  OCR Exam Extraction", font=f_title, fill=(245, 245, 245, 255))

    bullets = [
        "Extracts questions, options & diagrams from PDFs",
        "Fixed critical diagram alignment displacement bug",
        "Gemini AI auto-generates structured JSON answers",
        "Docker deployed with multilingual support",
    ]
    by = 76
    for b in bullets:
        draw.text((35, by), "▸", font=f_bullet, fill=(*RED, 255))
        draw.text((52, by), b, font=f_bullet, fill=(180, 180, 185, 255))
        by += 22

    draw.text((25, 185), "STACK:", font=f_stack, fill=(80, 80, 90, 255))
    sx = 72
    for s in ["Python", "Django", "FastAPI", "Mistral OCR", "Gemini AI", "PyMuPDF", "Docker"]:
        sw = int(draw.textlength(s, font=f_stack)) + 12
        draw.rounded_rectangle([sx, 182, sx+sw, 198], radius=4, fill=(25, 10, 10, 220))
        draw.text((sx+6, 184), s, font=f_stack, fill=(248, 113, 113, 255))
        sx += sw + 4

    img = img.convert("RGB")
    img.save("assets/exambro_card.png", "PNG", quality=95)
    print("Created exambro_card.png")


if __name__ == '__main__':
    create_directory()
    create_header()
    create_wave_divider()
    create_quote()
    create_skais()
    create_exambro()
    print("Done")
