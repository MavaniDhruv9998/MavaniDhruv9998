import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

def create_directory():
    if not os.path.exists('assets'):
        os.makedirs('assets')

def get_font(size, bold=False):
    names = ["arialbd.ttf", "segoeuib.ttf", "calibrib.ttf"] if bold else ["arial.ttf", "segoeui.ttf", "calibri.ttf"]
    for n in names:
        try:
            return ImageFont.truetype(n, size)
        except OSError:
            continue
    return ImageFont.load_default()

def lerp(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def grad_h(draw, box, c1, c2):
    x1, y1, x2, y2 = box
    for i in range(x2 - x1):
        c = lerp(c1, c2, i / max(1, x2 - x1))
        draw.line([(x1+i, y1), (x1+i, y2)], fill=c)

def grad_v(draw, box, c1, c2):
    x1, y1, x2, y2 = box
    for i in range(y2 - y1):
        c = lerp(c1, c2, i / max(1, y2 - y1))
        draw.line([(x1, y1+i), (x2, y1+i)], fill=c)

# ── Color Palette ──
BG_DEEP   = (8, 8, 12)
BG_CARD   = (14, 14, 20)
RED_BRIGHT = (220, 38, 38)
RED_DARK   = (153, 27, 27)
RED_GLOW   = (255, 60, 60)
RED_SOFT   = (248, 113, 113)
WHITE      = (245, 245, 245)
GRAY       = (160, 160, 170)
GRAY_DIM   = (80, 80, 90)

# ─────────────────────────────────────
# 1. HEADER — "DHRUV MAVANI" only
# ─────────────────────────────────────
def create_header():
    W, H = 1200, 350
    img = Image.new("RGBA", (W, H), (*BG_DEEP, 255))
    draw = ImageDraw.Draw(img)
    grad_v(draw, (0, 0, W, H), BG_DEEP, (5, 5, 8))

    # Red orb glow
    orb = Image.new("RGBA", (W, H), (0,0,0,0))
    od = ImageDraw.Draw(orb)
    od.ellipse([300, -50, 900, 400], fill=(*RED_BRIGHT, 35))
    od.ellipse([-100, 100, 400, 450], fill=(*RED_DARK, 25))
    od.ellipse([800, 50, 1300, 400], fill=(*RED_DARK, 20))
    orb = orb.filter(ImageFilter.GaussianBlur(70))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    # Subtle grid
    for x in range(0, W, 60):
        draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 6), width=1)
    for y in range(0, H, 60):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 6), width=1)

    # Particles
    random.seed(77)
    for _ in range(40):
        px, py = random.randint(0, W), random.randint(0, H)
        pr = random.randint(1, 3)
        pa = random.randint(30, 100)
        draw.ellipse([px-pr, py-pr, px+pr, py+pr], fill=(*RED_BRIGHT, pa))

    # Top red accent bar
    bar = Image.new("RGBA", (W, 4), (0,0,0,0))
    bd = ImageDraw.Draw(bar)
    grad_h(bd, (0, 0, W, 4), RED_DARK, RED_BRIGHT)
    img.paste(bar, (0, 0), bar)

    # Bottom red accent bar
    bar2 = Image.new("RGBA", (W, 4), (0,0,0,0))
    bd2 = ImageDraw.Draw(bar2)
    grad_h(bd2, (0, 0, W, 4), RED_BRIGHT, RED_DARK)
    img.paste(bar2, (0, H-4), bar2)

    # ── Name ──
    font_name = get_font(85, bold=True)
    name = "DHRUV MAVANI"
    bbox = draw.textbbox((0, 0), name, font=font_name)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = (H - th) // 2 - 30

    # Glow behind name
    glow = Image.new("RGBA", (W, H), (0,0,0,0))
    gd = ImageDraw.Draw(glow)
    gd.text((tx, ty), name, font=font_name, fill=(*RED_GLOW, 70))
    glow = glow.filter(ImageFilter.GaussianBlur(18))
    img = Image.alpha_composite(img, glow)
    draw = ImageDraw.Draw(img)

    # Name text — gradient red to white
    cx = tx
    for i, ch in enumerate(name):
        t = i / max(1, len(name) - 1)
        c = lerp(RED_BRIGHT, RED_SOFT, t)
        draw.text((cx, ty), ch, font=font_name, fill=(*c, 255))
        cx += draw.textlength(ch, font=font_name)

    # Subtle subtitle
    font_sub = get_font(18, bold=True)
    sub = "AI  DEVELOPER   ·   LLM  ENGINEER   ·   VOICE  AI   ·   RAG  ARCHITECT"
    sbbox = draw.textbbox((0, 0), sub, font=font_sub)
    stw = sbbox[2] - sbbox[0]
    draw.text(((W - stw) // 2, ty + th + 25), sub, font=font_sub, fill=(*GRAY, 200))

    img = img.convert("RGB")
    img.save("assets/header_banner.png", "PNG", quality=95)
    print("Created header_banner.png")

# ─────────────────────────────────────
# 2. SKAIS PROJECT CARD
# ─────────────────────────────────────
def create_skais():
    W, H = 1000, 250
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=16, fill=(*BG_CARD, 250), outline=(*RED_DARK, 180), width=2)

    # Top accent
    for x in range(3, W-3):
        t = (x - 3) / (W - 6)
        c = lerp(RED_DARK, RED_BRIGHT, t)
        draw.line([(x, 2), (x, 5)], fill=(*c, 255))

    f_badge = get_font(11, bold=True)
    f_title = get_font(24, bold=True)
    f_bullet = get_font(13)
    f_stack = get_font(10, bold=True)

    # Badge
    draw.rounded_rectangle([30, 18, 180, 40], radius=11, fill=(30, 10, 10, 230), outline=(*RED_BRIGHT, 200), width=1)
    draw.text((44, 22), "VOICE AI PROJECT", font=f_badge, fill=(*RED_BRIGHT, 255))

    # Title
    draw.text((30, 50), "SKAIS  —  Restaurant AI Agent", font=f_title, fill=(*WHITE, 255))

    # Soundwave visual (right)
    random.seed(7)
    bx = 800
    bars = [30, 60, 85, 45, 100, 70, 35, 75, 50, 25]
    for bh in bars:
        by1, by2 = 120 - bh//2, 120 + bh//2
        draw.rounded_rectangle([bx, by1, bx+8, by2], radius=4, fill=(*RED_BRIGHT, 180))
        bx += 16

    # Metric pill
    draw.rounded_rectangle([790, 180, 960, 205], radius=12, fill=(30, 10, 10, 230), outline=(*RED_BRIGHT, 180), width=1)
    draw.text((808, 186), "103+ Live Calls", font=f_badge, fill=(*RED_SOFT, 255))

    # Bullets
    bullets = [
        "Voice AI agent answering live phone orders & reservations",
        "RAG knowledge base for menu, hours & policies",
        "Auto SMS confirmations via Twilio SDK",
        "50%+ cost savings vs human operators",
    ]
    by = 88
    for b in bullets:
        draw.text((40, by), "▸", font=f_bullet, fill=(*RED_BRIGHT, 255))
        draw.text((58, by), b, font=f_bullet, fill=(*GRAY, 255))
        by += 24

    # Stack
    draw.text((30, 215), "STACK:", font=f_stack, fill=(*GRAY_DIM, 255))
    sx = 80
    for s in ["Python", "FastAPI", "Retell AI", "LangChain", "Supabase", "Twilio", "Next.js"]:
        sw = int(draw.textlength(s, font=f_stack)) + 14
        draw.rounded_rectangle([sx, 212, sx+sw, 230], radius=5, fill=(30, 10, 10, 220))
        draw.text((sx+7, 215), s, font=f_stack, fill=(*RED_SOFT, 255))
        sx += sw + 5

    img = img.convert("RGB")
    img.save("assets/skais_card.png", "PNG", quality=95)
    print("Created skais_card.png")

# ─────────────────────────────────────
# 3. EXAMBRO PROJECT CARD
# ─────────────────────────────────────
def create_exambro():
    W, H = 1000, 250
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=16, fill=(*BG_CARD, 250), outline=(*RED_DARK, 180), width=2)

    # Top accent
    for x in range(3, W-3):
        t = (x - 3) / (W - 6)
        c = lerp(RED_BRIGHT, RED_DARK, t)
        draw.line([(x, 2), (x, 5)], fill=(*c, 255))

    f_badge = get_font(11, bold=True)
    f_title = get_font(24, bold=True)
    f_bullet = get_font(13)
    f_stack = get_font(10, bold=True)

    # Badge
    draw.rounded_rectangle([30, 18, 165, 40], radius=11, fill=(30, 10, 10, 230), outline=(*RED_BRIGHT, 200), width=1)
    draw.text((44, 22), "OCR AI PROJECT", font=f_badge, fill=(*RED_BRIGHT, 255))

    # Title
    draw.text((30, 50), "ExamBro  —  OCR Exam Extraction", font=f_title, fill=(*WHITE, 255))

    # Document visual (right)
    draw.rounded_rectangle([820, 40, 950, 185], radius=10, fill=(20, 10, 14, 230), outline=(*RED_DARK, 200), width=2)
    draw.line([(840, 65), (930, 65)], fill=(*WHITE, 180), width=3)
    draw.line([(840, 82), (910, 82)], fill=(*GRAY, 120), width=2)
    draw.line([(840, 95), (895, 95)], fill=(*GRAY, 120), width=2)
    draw.rounded_rectangle([840, 110, 930, 150], radius=5, fill=(25, 12, 15, 200), outline=(*RED_SOFT, 150), width=1)
    draw.polygon([(855, 142), (875, 120), (895, 142)], fill=None, outline=(*RED_SOFT, 180))
    draw.ellipse([905, 118, 920, 133], fill=(*RED_BRIGHT, 180))
    # Scan line
    draw.line([(815, 125), (955, 125)], fill=(*RED_BRIGHT, 200), width=2)
    draw.line([(840, 165), (930, 165)], fill=(*GRAY, 100), width=2)

    # Bullets
    bullets = [
        "Extracts questions, options & diagrams from PDFs",
        "Fixed critical diagram alignment displacement bug",
        "Gemini AI auto-generates structured JSON answers",
        "Docker deployed with multilingual support",
    ]
    by = 88
    for b in bullets:
        draw.text((40, by), "▸", font=f_bullet, fill=(*RED_BRIGHT, 255))
        draw.text((58, by), b, font=f_bullet, fill=(*GRAY, 255))
        by += 24

    # Stack
    draw.text((30, 215), "STACK:", font=f_stack, fill=(*GRAY_DIM, 255))
    sx = 80
    for s in ["Python", "Django", "FastAPI", "Mistral OCR", "Gemini AI", "PyMuPDF", "Docker"]:
        sw = int(draw.textlength(s, font=f_stack)) + 14
        draw.rounded_rectangle([sx, 212, sx+sw, 230], radius=5, fill=(30, 10, 10, 220))
        draw.text((sx+7, 215), s, font=f_stack, fill=(*RED_SOFT, 255))
        sx += sw + 5

    img = img.convert("RGB")
    img.save("assets/exambro_card.png", "PNG", quality=95)
    print("Created exambro_card.png")

# ─────────────────────────────────────
# 4. QUOTE CARD
# ─────────────────────────────────────
def create_quote():
    W, H = 1000, 120
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=16, fill=(*BG_CARD, 250), outline=(*RED_DARK, 150), width=2)

    # Left accent bar (vertical red gradient)
    for y in range(20, H-20):
        t = (y - 20) / (H - 40)
        c = lerp(RED_BRIGHT, RED_DARK, t)
        draw.line([(12, y), (16, y)], fill=(*c, 255))

    f_q = get_font(17, bold=True)
    f_a = get_font(12, bold=True)

    draw.text((35, 30), '"Ever tried. Ever failed. No matter. Try again. Fail again. Fail better"', font=f_q, fill=(*WHITE, 240))

    draw.rounded_rectangle([35, 70, 180, 94], radius=12, fill=(30, 10, 10, 220), outline=(*RED_DARK, 180), width=1)
    draw.text((50, 75), "— Samuel Beckett", font=f_a, fill=(*RED_SOFT, 255))

    img = img.convert("RGB")
    img.save("assets/quote_card.png", "PNG", quality=95)
    print("Created quote_card.png")

# ─────────────────────────────────────
# 5. DIVIDER
# ─────────────────────────────────────
def create_divider():
    W, H = 1000, 16
    img = Image.new("RGBA", (W, H), (0,0,0,0))
    draw = ImageDraw.Draw(img)

    for x in range(100, 900):
        t = (x - 100) / 800
        edge = min(1.0, (x - 100) / 80, (900 - x) / 80)
        if t < 0.5:
            c = lerp(RED_DARK, RED_BRIGHT, t * 2)
        else:
            c = lerp(RED_BRIGHT, RED_DARK, (t - 0.5) * 2)
        a = int(180 * edge)
        draw.line([(x, 7), (x, 9)], fill=(*c, a))

    # Center diamond
    draw.polygon([(500, 2), (506, 8), (500, 14), (494, 8)], fill=(*RED_BRIGHT, 220))
    draw.ellipse([498, 6, 502, 10], fill=(*WHITE, 255))

    img.save("assets/divider.png", "PNG")
    print("Created divider.png")


if __name__ == '__main__':
    create_directory()
    create_header()
    create_skais()
    create_exambro()
    create_quote()
    create_divider()
    print("Done!")
