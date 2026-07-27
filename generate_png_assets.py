import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import math

def create_directory():
    if not os.path.exists('assets'):
        os.makedirs('assets')

def get_font(size, bold=False):
    font_names = []
    if bold:
        font_names = ["arialbd.ttf", "segoeuib.ttf", "calibrib.ttf"]
    else:
        font_names = ["arial.ttf", "segoeui.ttf", "calibri.ttf"]
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()

def lerp_color(c1, c2, t):
    return tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))

def draw_gradient_rect(draw, box, color1, color2, direction="horizontal"):
    x1, y1, x2, y2 = box
    if direction == "horizontal":
        for i in range(x2 - x1):
            t = i / max(1, x2 - x1)
            c = lerp_color(color1, color2, t)
            draw.line([(x1 + i, y1), (x1 + i, y2)], fill=c)
    else:
        for i in range(y2 - y1):
            t = i / max(1, y2 - y1)
            c = lerp_color(color1, color2, t)
            draw.line([(x1, y1 + i), (x2, y1 + i)], fill=c)

def draw_multi_gradient(img, colors):
    """Draw a multi-stop gradient across the full image width."""
    W, H = img.size
    draw = ImageDraw.Draw(img)
    segments = len(colors) - 1
    seg_width = W / segments
    for s in range(segments):
        x_start = int(s * seg_width)
        x_end = int((s + 1) * seg_width)
        for x in range(x_start, x_end):
            t = (x - x_start) / max(1, x_end - x_start)
            c = lerp_color(colors[s], colors[s + 1], t)
            draw.line([(x, 0), (x, H)], fill=c)

# ─────────────────────────────────────────────
# 1. HEADER BANNER — Name Only, Ultra Premium
# ─────────────────────────────────────────────
def create_header_banner():
    W, H = 1200, 400
    img = Image.new("RGBA", (W, H), (0, 0, 0, 255))
    draw = ImageDraw.Draw(img)

    # Deep dark gradient background
    draw_gradient_rect(draw, (0, 0, W, H), (5, 5, 20), (12, 8, 35), "vertical")

    # Ambient Glow Orbs
    orb = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    od = ImageDraw.Draw(orb)
    # Cyan-blue orb top-left
    od.ellipse([-100, -100, 500, 350], fill=(0, 180, 255, 45))
    # Violet orb center-right
    od.ellipse([600, 50, 1300, 500], fill=(120, 60, 220, 50))
    # Pink orb bottom-left
    od.ellipse([200, 200, 800, 550], fill=(255, 50, 130, 30))
    # Emerald accent top-right
    od.ellipse([900, -80, 1250, 200], fill=(0, 220, 160, 30))
    orb = orb.filter(ImageFilter.GaussianBlur(80))
    img = Image.alpha_composite(img, orb)
    draw = ImageDraw.Draw(img)

    # Floating particle dots
    import random
    random.seed(42)
    for _ in range(60):
        px = random.randint(0, W)
        py = random.randint(0, H)
        pr = random.randint(1, 3)
        pa = random.randint(40, 120)
        colors_choice = [(56, 189, 248), (167, 139, 250), (244, 114, 182), (52, 211, 153)]
        pc = random.choice(colors_choice)
        draw.ellipse([px-pr, py-pr, px+pr, py+pr], fill=(*pc, pa))

    # Grid pattern (subtle)
    for x in range(0, W, 50):
        draw.line([(x, 0), (x, H)], fill=(255, 255, 255, 8), width=1)
    for y in range(0, H, 50):
        draw.line([(0, y), (W, y)], fill=(255, 255, 255, 8), width=1)

    # Top accent gradient bar
    bar = Image.new("RGBA", (W, 5), (0, 0, 0, 0))
    draw_multi_gradient(bar, [(0, 180, 255), (120, 80, 255), (255, 50, 150), (0, 220, 160)])
    img.paste(bar, (0, 0), bar)

    # Bottom accent gradient bar
    bar2 = Image.new("RGBA", (W, 5), (0, 0, 0, 0))
    draw_multi_gradient(bar2, [(0, 220, 160), (255, 50, 150), (120, 80, 255), (0, 180, 255)])
    img.paste(bar2, (0, H - 5), bar2)

    # ─── Center Name Typography ───
    font_name = get_font(80, bold=True)
    name_text = "DHRUV MAVANI"
    bbox = draw.textbbox((0, 0), name_text, font=font_name)
    tw = bbox[2] - bbox[0]
    th = bbox[3] - bbox[1]
    tx = (W - tw) // 2
    ty = (H - th) // 2 - 40

    # Draw soft glow behind text
    glow_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    glow_draw = ImageDraw.Draw(glow_layer)
    glow_draw.text((tx, ty), name_text, font=font_name, fill=(100, 140, 255, 80))
    glow_layer = glow_layer.filter(ImageFilter.GaussianBlur(15))
    img = Image.alpha_composite(img, glow_layer)
    draw = ImageDraw.Draw(img)

    # Draw the name with gradient color effect (character by character)
    gradient_colors = [
        (56, 189, 248),   # cyan
        (100, 140, 255),  # blue
        (167, 139, 250),  # violet
        (220, 100, 220),  # magenta
        (244, 114, 182),  # pink
    ]
    char_x = tx
    total_chars = len(name_text)
    for i, ch in enumerate(name_text):
        t = i / max(1, total_chars - 1)
        seg = t * (len(gradient_colors) - 1)
        seg_idx = min(int(seg), len(gradient_colors) - 2)
        local_t = seg - seg_idx
        color = lerp_color(gradient_colors[seg_idx], gradient_colors[seg_idx + 1], local_t)
        draw.text((char_x, ty), ch, font=font_name, fill=(*color, 255))
        char_w = draw.textlength(ch, font=font_name)
        char_x += char_w

    # Subtitle tagline below name
    font_sub = get_font(20, bold=True)
    sub_text = "AI  DEVELOPER   •   LLM  ENGINEER   •   VOICE  AI   •   RAG  ARCHITECT"
    sbbox = draw.textbbox((0, 0), sub_text, font=font_sub)
    stw = sbbox[2] - sbbox[0]
    draw.text(((W - stw) // 2, ty + th + 30), sub_text, font=font_sub, fill=(180, 190, 210, 220))

    # Decorative diamond shapes around name
    diamond_y = ty + th // 2
    # Left diamond
    draw.polygon([(tx - 50, diamond_y), (tx - 35, diamond_y - 12), (tx - 20, diamond_y), (tx - 35, diamond_y + 12)], fill=(56, 189, 248, 120))
    # Right diamond
    rx = tx + tw
    draw.polygon([(rx + 20, diamond_y), (rx + 35, diamond_y - 12), (rx + 50, diamond_y), (rx + 35, diamond_y + 12)], fill=(244, 114, 182, 120))

    img = img.convert("RGB")
    img.save("assets/header_banner.png", "PNG", quality=95)
    print("Created assets/header_banner.png")

# ─────────────────────────────────────────────
# 2. SKILLS SECTION BANNER
# ─────────────────────────────────────────────
def create_skills_banner():
    W, H = 1000, 200
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Dark card background
    draw.rounded_rectangle([0, 0, W-1, H-1], radius=20, fill=(10, 12, 28, 240), outline=(40, 50, 80, 200), width=2)

    # Title
    font_title = get_font(28, bold=True)
    draw.text((40, 25), "⚡  TECH  STACK  &  ARSENAL", font=font_title, fill=(56, 189, 248, 255))

    # Horizontal divider line with gradient
    line = Image.new("RGBA", (920, 3), (0, 0, 0, 0))
    draw_multi_gradient(line, [(56, 189, 248), (167, 139, 250), (244, 114, 182)])
    img.paste(line, (40, 65), line)

    # Category icons and names in a clean grid
    font_cat = get_font(15, bold=True)
    categories = [
        ("🤖", "AI & LLMs", (167, 139, 250)),
        ("⚡", "RAG & Vectors", (56, 189, 248)),
        ("👁️", "Vision & OCR", (52, 211, 153)),
        ("🎙️", "Voice Agents", (244, 114, 182)),
        ("💻", "Backend", (251, 191, 36)),
        ("☁️", "Cloud & DevOps", (96, 165, 250)),
    ]
    cx = 50
    cy = 85
    for icon, name, color in categories:
        # Pill background
        pill_w = 150
        draw.rounded_rectangle([cx, cy, cx + pill_w, cy + 42], radius=12, fill=(20, 25, 50, 220), outline=(*color, 150), width=1)
        draw.text((cx + 12, cy + 10), f"{icon}  {name}", font=font_cat, fill=(*color, 255))
        cx += pill_w + 10
        if cx + pill_w > W - 20:
            cx = 50
            cy += 52

    img = img.convert("RGB")
    img.save("assets/skills_banner.png", "PNG", quality=95)
    print("Created assets/skills_banner.png")

# ─────────────────────────────────────────────
# 3. PROJECT CARD — SKAIS
# ─────────────────────────────────────────────
def create_skais_card():
    W, H = 1000, 280
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=20, fill=(8, 12, 28, 245), outline=(40, 50, 80, 200), width=2)

    # Top accent bar
    bar = Image.new("RGBA", (W-4, 4), (0,0,0,0))
    draw_multi_gradient(bar, [(56, 189, 248), (100, 140, 255), (167, 139, 250)])
    img.paste(bar, (2, 2), bar)

    font_badge = get_font(11, bold=True)
    font_title = get_font(26, bold=True)
    font_bullet = get_font(14)
    font_stack = get_font(11, bold=True)

    # Badge
    draw.rounded_rectangle([35, 22, 175, 45], radius=12, fill=(20, 30, 60, 230), outline=(56, 189, 248, 200), width=1)
    draw.text((47, 26), "🎙️  VOICE AI PROJECT", font=font_badge, fill=(56, 189, 248, 255))

    # Title
    draw.text((35, 55), "SKAIS — Restaurant AI Agent", font=font_title, fill=(255, 255, 255, 255))

    # Right side: visual soundwave bars
    import random
    random.seed(7)
    bx = 780
    bars_h = [35, 70, 100, 55, 120, 80, 45, 90, 60, 30]
    bar_colors = [(56, 189, 248), (100, 140, 255), (167, 139, 250), (56, 189, 248), (120, 80, 255),
                  (167, 139, 250), (56, 189, 248), (100, 140, 255), (120, 80, 255), (56, 189, 248)]
    for i, bh in enumerate(bars_h):
        by1 = 140 - bh // 2
        by2 = 140 + bh // 2
        draw.rounded_rectangle([bx, by1, bx + 10, by2], radius=5, fill=(*bar_colors[i], 200))
        bx += 18

    # Metric pill
    draw.rounded_rectangle([770, 210, 960, 240], radius=15, fill=(20, 30, 60, 230), outline=(56, 189, 248, 200), width=1)
    draw.text((790, 216), "📞 103+ Live Calls", font=font_badge, fill=(56, 189, 248, 255))

    # Bullet points — concise
    bullets = [
        ("🎙️", "Voice AI agent answering live phone orders & reservations"),
        ("🧠", "RAG knowledge base for menu, hours & policies"),
        ("📲", "Auto SMS confirmations via Twilio SDK"),
        ("💰", "50%+ cost savings vs human operators"),
    ]
    by = 95
    for icon, text in bullets:
        draw.text((45, by), f"{icon}  {text}", font=font_bullet, fill=(210, 218, 235, 255))
        by += 26

    # Tech stack row
    draw.text((35, 242), "STACK:", font=font_stack, fill=(100, 116, 139, 255))
    stacks = ["Python", "FastAPI", "Retell AI", "LangChain", "Supabase", "Twilio", "Next.js"]
    sx = 95
    for s in stacks:
        sw = int(draw.textlength(s, font=font_stack)) + 16
        draw.rounded_rectangle([sx, 238, sx + sw, 258], radius=6, fill=(20, 30, 55, 230))
        draw.text((sx + 8, 242), s, font=font_stack, fill=(56, 189, 248, 255))
        sx += sw + 6

    img = img.convert("RGB")
    img.save("assets/skais_card.png", "PNG", quality=95)
    print("Created assets/skais_card.png")

# ─────────────────────────────────────────────
# 4. PROJECT CARD — ExamBro
# ─────────────────────────────────────────────
def create_exambro_card():
    W, H = 1000, 280
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=20, fill=(10, 8, 28, 245), outline=(40, 50, 80, 200), width=2)

    # Top accent bar (purple-pink gradient)
    bar = Image.new("RGBA", (W-4, 4), (0,0,0,0))
    draw_multi_gradient(bar, [(167, 139, 250), (220, 100, 220), (244, 114, 182)])
    img.paste(bar, (2, 2), bar)

    font_badge = get_font(11, bold=True)
    font_title = get_font(26, bold=True)
    font_bullet = get_font(14)
    font_stack = get_font(11, bold=True)

    # Badge
    draw.rounded_rectangle([35, 22, 175, 45], radius=12, fill=(25, 20, 50, 230), outline=(167, 139, 250, 200), width=1)
    draw.text((47, 26), "📄  OCR AI PROJECT", font=font_badge, fill=(167, 139, 250, 255))

    # Title
    draw.text((35, 55), "ExamBro — OCR Exam Extraction", font=font_title, fill=(255, 255, 255, 255))

    # Right side: document icon visual
    draw.rounded_rectangle([800, 40, 940, 200], radius=12, fill=(15, 18, 40, 230), outline=(167, 139, 250, 200), width=2)
    # Text lines inside doc
    draw.line([(820, 70), (920, 70)], fill=(200, 210, 230, 200), width=3)
    draw.line([(820, 88), (900, 88)], fill=(148, 163, 184, 160), width=2)
    draw.line([(820, 102), (880, 102)], fill=(148, 163, 184, 160), width=2)
    # Diagram box
    draw.rounded_rectangle([820, 118, 920, 165], radius=6, fill=(25, 30, 55, 200), outline=(52, 211, 153, 200), width=1)
    draw.polygon([(840, 155), (860, 130), (880, 155)], fill=None, outline=(52, 211, 153, 200))
    draw.ellipse([890, 128, 908, 146], fill=(244, 114, 182, 200))
    # OCR scan line
    draw.line([(795, 130), (945, 130)], fill=(244, 114, 182, 200), width=3)
    # More text lines
    draw.line([(820, 178), (920, 178)], fill=(148, 163, 184, 120), width=2)

    # Bullet points — concise
    bullets = [
        ("📄", "Extracts questions, options & diagrams from PDFs"),
        ("🎯", "Fixed critical diagram alignment displacement bug"),
        ("🤖", "Gemini AI auto-generates structured JSON answers"),
        ("🐳", "Docker deployed with multilingual support"),
    ]
    by = 95
    for icon, text in bullets:
        draw.text((45, by), f"{icon}  {text}", font=font_bullet, fill=(210, 218, 235, 255))
        by += 26

    # Tech stack row
    draw.text((35, 242), "STACK:", font=font_stack, fill=(100, 116, 139, 255))
    stacks = ["Python", "Django", "FastAPI", "Mistral OCR", "Gemini AI", "PyMuPDF", "Docker"]
    sx = 95
    for s in stacks:
        sw = int(draw.textlength(s, font=font_stack)) + 16
        draw.rounded_rectangle([sx, 238, sx + sw, 258], radius=6, fill=(25, 20, 50, 230))
        draw.text((sx + 8, 242), s, font=font_stack, fill=(167, 139, 250, 255))
        sx += sw + 6

    img = img.convert("RGB")
    img.save("assets/exambro_card.png", "PNG", quality=95)
    print("Created assets/exambro_card.png")

# ─────────────────────────────────────────────
# 5. QUOTE CARD — Samuel Beckett
# ─────────────────────────────────────────────
def create_quote_card():
    W, H = 1000, 140
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=20, fill=(8, 10, 25, 245), outline=(40, 50, 80, 200), width=2)

    # Left accent bar
    bar = Image.new("RGBA", (5, H - 40), (0,0,0,0))
    draw_multi_gradient(bar, [(56, 189, 248), (167, 139, 250), (244, 114, 182)])
    # rotate for vertical
    for y in range(H - 40):
        t = y / max(1, H - 41)
        colors = [(56, 189, 248), (167, 139, 250), (244, 114, 182)]
        seg = t * (len(colors) - 1)
        idx = min(int(seg), len(colors) - 2)
        lt = seg - idx
        c = lerp_color(colors[idx], colors[idx + 1], lt)
        draw.line([(15, 20 + y), (20, 20 + y)], fill=(*c, 255))

    # Large quote mark
    font_quote_mark = get_font(70, bold=True)
    draw.text((30, 10), '"', font=font_quote_mark, fill=(56, 189, 248, 60))

    # Quote text
    font_quote = get_font(18, bold=True)
    draw.text((70, 35), '"Ever tried. Ever failed. No matter. Try again. Fail again. Fail better"', font=font_quote, fill=(240, 245, 255, 240))

    # Author badge
    font_author = get_font(13, bold=True)
    draw.rounded_rectangle([70, 78, 230, 105], radius=14, fill=(20, 25, 50, 220), outline=(167, 139, 250, 180), width=1)
    draw.text((86, 84), "— Samuel Beckett", font=font_author, fill=(167, 139, 250, 255))

    img = img.convert("RGB")
    img.save("assets/quote_card.png", "PNG", quality=95)
    print("Created assets/quote_card.png")

# ─────────────────────────────────────────────
# 6. DIVIDER — Gradient Line
# ─────────────────────────────────────────────
def create_divider():
    W, H = 1000, 20
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    # Gradient line
    for x in range(80, 920):
        t = (x - 80) / 840
        colors = [(56, 189, 248), (167, 139, 250), (244, 114, 182), (52, 211, 153)]
        seg = t * (len(colors) - 1)
        idx = min(int(seg), len(colors) - 2)
        lt = seg - idx
        c = lerp_color(colors[idx], colors[idx + 1], lt)
        # Fade in/out at edges
        edge_alpha = min(1.0, (x - 80) / 60, (920 - x) / 60)
        alpha = int(200 * edge_alpha)
        draw.line([(x, 9), (x, 11)], fill=(*c, alpha))

    # Center diamond
    cx = 500
    draw.polygon([(cx, 4), (cx + 8, 10), (cx, 16), (cx - 8, 10)], fill=(167, 139, 250, 220))
    draw.ellipse([cx - 2, 8, cx + 2, 12], fill=(255, 255, 255, 255))

    img.save("assets/divider.png", "PNG")
    print("Created assets/divider.png")

# ─────────────────────────────────────────────
# 7. CONNECT BANNER
# ─────────────────────────────────────────────
def create_connect_banner():
    W, H = 1000, 100
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw.rounded_rectangle([0, 0, W-1, H-1], radius=20, fill=(8, 10, 25, 245), outline=(40, 50, 80, 200), width=2)

    font_title = get_font(22, bold=True)
    draw.text((40, 35), "📫  LET'S  CONNECT  &  BUILD  AMAZING  AI  TOGETHER", font=font_title, fill=(56, 189, 248, 240))

    img = img.convert("RGB")
    img.save("assets/connect_banner.png", "PNG", quality=95)
    print("Created assets/connect_banner.png")


if __name__ == '__main__':
    create_directory()
    create_header_banner()
    create_skills_banner()
    create_skais_card()
    create_exambro_card()
    create_quote_card()
    create_divider()
    create_connect_banner()
    print("\n✅ All assets generated successfully!")
