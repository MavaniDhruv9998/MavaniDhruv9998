import os
from PIL import Image, ImageDraw, ImageFont, ImageFilter

def create_directory():
    if not os.path.exists('assets'):
        os.makedirs('assets')

def get_font(size, bold=False, italic=False):
    # Try system fonts on Windows
    font_names = []
    if bold and italic:
        font_names = ["arialbi.ttf", "segoeuiib.ttf", "calibrii.ttf"]
    elif bold:
        font_names = ["arialbd.ttf", "segoeuib.ttf", "calibrib.ttf", "verdana.ttf"]
    elif italic:
        font_names = ["ariali.ttf", "segoeuii.ttf", "calibrii.ttf"]
    else:
        font_names = ["arial.ttf", "segoeui.ttf", "calibri.ttf"]
        
    for font_name in font_names:
        try:
            return ImageFont.truetype(font_name, size)
        except OSError:
            continue
    return ImageFont.load_default()

def draw_gradient_rect(draw, box, color1, color2, direction="horizontal"):
    x1, y1, x2, y2 = box
    width = x2 - x1
    height = y2 - y1
    
    if direction == "horizontal":
        for i in range(width):
            r = int(color1[0] + (color2[0] - color1[0]) * (i / max(1, width)))
            g = int(color1[1] + (color2[1] - color1[1]) * (i / max(1, width)))
            b = int(color1[2] + (color2[2] - color1[2]) * (i / max(1, width)))
            draw.line([(x1 + i, y1), (x1 + i, y2)], fill=(r, g, b))
    else:
        for i in range(height):
            r = int(color1[0] + (color2[0] - color1[0]) * (i / max(1, height)))
            g = int(color1[1] + (color2[1] - color1[1]) * (i / max(1, height)))
            b = int(color1[2] + (color2[2] - color1[2]) * (i / max(1, height)))
            draw.line([(x1, y1 + i), (x2, y1 + i)], fill=(r, g, b))

def create_header_banner_png():
    W, H = 1200, 420
    img = Image.new("RGBA", (W, H), (8, 12, 20, 255))
    draw = ImageDraw.Draw(img)

    # Background gradient
    draw_gradient_rect(draw, (0, 0, W, H), (8, 12, 20), (15, 23, 42), "vertical")

    # Ambient Orbs (Draw blurred circles on overlay)
    orb_layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    orb_draw = ImageDraw.Draw(orb_layer)
    
    # Cyan orb top left
    orb_draw.ellipse([50, -50, 450, 350], fill=(14, 165, 233, 60))
    # Purple orb bottom right
    orb_draw.ellipse([800, 100, 1250, 450], fill=(139, 92, 246, 60))
    # Emerald orb bottom center
    orb_draw.ellipse([450, 200, 850, 480], fill=(16, 185, 129, 40))

    orb_layer = orb_layer.filter(ImageFilter.GaussianBlur(50))
    img = Image.alpha_composite(img, orb_layer)
    draw = ImageDraw.Draw(img)

    # Outer border and top highlight bar
    draw.rectangle([0, 0, W-1, H-1], outline=(30, 41, 59, 255), width=2)
    
    # Top gradient bar
    top_bar = Image.new("RGBA", (W, 6), (0, 0, 0, 0))
    tb_draw = ImageDraw.Draw(top_bar)
    draw_gradient_rect(tb_draw, (0, 0, W, 6), (56, 189, 248), (192, 132, 252), "horizontal")
    img.paste(top_bar, (0, 0), top_bar)

    # Bottom gradient bar
    bot_bar = Image.new("RGBA", (W, 6), (0, 0, 0, 0))
    bb_draw = ImageDraw.Draw(bot_bar)
    draw_gradient_rect(bb_draw, (0, 0, W, 6), (56, 189, 248), (244, 114, 182), "horizontal")
    img.paste(bot_bar, (0, H-6), bot_bar)

    # Fonts
    font_badge = get_font(13, bold=True)
    font_name = get_font(52, bold=True)
    font_sub = get_font(22, bold=True)
    font_desc = get_font(15)
    font_pill = get_font(13, bold=True)
    font_edu = get_font(13)
    font_code = get_font(12, bold=True)

    # Right side graphic - Tech Node Grid
    # Draw glowing connecting lines
    nodes = [(820, 120), (950, 80), (1060, 140), (1120, 260), (990, 310), (860, 270), (940, 200)]
    lines = [(0,6), (1,6), (2,6), (3,6), (4,6), (5,6), (0,1), (1,2), (2,3), (3,4), (4,5), (5,0)]
    for n1, n2 in lines:
        draw.line([nodes[n1], nodes[n2]], fill=(56, 189, 248, 80), width=2)

    for nx, ny in nodes:
        draw.ellipse([nx-12, ny-12, nx+12, ny+12], fill=(15, 23, 42, 200), outline=(56, 189, 248, 255), width=2)
        draw.ellipse([nx-4, ny-4, nx+4, ny+4], fill=(56, 189, 248, 255))

    # Node labels
    draw.text((800, 95), "<RAG_Engine/>", font=font_code, fill=(56, 189, 248, 220))
    draw.text((930, 55), "LLM.Orchestrate()", font=font_code, fill=(192, 132, 252, 220))
    draw.text((1040, 115), "Voice_AI.agent()", font=font_code, fill=(244, 114, 182, 220))
    draw.text((820, 295), "OCR.pipeline()", font=font_code, fill=(52, 211, 153, 220))

    # Left Content
    # Status Badge
    draw.rounded_rectangle([60, 45, 330, 80], radius=17, fill=(15, 23, 42, 230), outline=(51, 65, 85, 255), width=1)
    draw.ellipse([75, 58, 85, 68], fill=(16, 185, 129, 255))
    draw.text((95, 52), "BUILDING PRODUCTION AI", font=font_badge, fill=(226, 232, 240, 255))

    # Title Name
    draw.text((60, 105), "DHRUV MAVANI", font=font_name, fill=(56, 189, 248, 255))

    # Professional Subtitle
    draw.text((60, 175), "AI DEVELOPER & LLM SYSTEMS ENGINEER", font=font_sub, fill=(241, 245, 249, 255))

    # Description
    draw.text((60, 212), "Specializing in Conversational Voice AI, RAG Pipelines, Multi-Agent Workflows & OCR Systems", font=font_desc, fill=(148, 163, 184, 255))

    # Tech Pills
    pills = [
        ("⚡ RAG & Vector AI", (56, 189, 248)),
        ("🎙️ Voice AI (Retell)", (129, 140, 248)),
        ("🤖 LangChain / Agents", (192, 132, 252)),
        ("🔍 OCR Pipelines", (52, 211, 153))
    ]
    px = 60
    py = 250
    for text, col in pills:
        tw = int(draw.textlength(text, font=font_pill)) + 24
        draw.rounded_rectangle([px, py, px + tw, py + 36], radius=10, fill=(30, 41, 59, 230), outline=col, width=1)
        draw.text((px + 12, py + 9), text, font=font_pill, fill=col)
        px += tw + 15

    # Academic & Location Bar
    draw.rounded_rectangle([60, 335, 720, 375], radius=10, fill=(15, 23, 42, 230), outline=(51, 65, 85, 255), width=1)
    draw.text((80, 345), "🎓 M.Sc. Artificial Intelligence (MKBU) | BCA Graduate   📍 Gujarat, India", font=font_edu, fill=(203, 213, 225, 255))

    img.save("assets/header_banner.png", "PNG")
    print("Created assets/header_banner.png")

def create_skais_banner_png():
    W, H = 1000, 320
    img = Image.new("RGBA", (W, H), (11, 19, 41, 255))
    draw = ImageDraw.Draw(img)

    draw_gradient_rect(draw, (0, 0, W, H), (11, 19, 41), (7, 13, 30), "vertical")

    # Border & top accent
    draw.rectangle([0, 0, W-1, H-1], outline=(30, 41, 59, 255), width=2)
    top_bar = Image.new("RGBA", (W, 4), (0, 0, 0, 0))
    tb_draw = ImageDraw.Draw(top_bar)
    draw_gradient_rect(tb_draw, (0, 0, W, 4), (56, 189, 248), (192, 132, 252), "horizontal")
    img.paste(top_bar, (0, 0), top_bar)

    # Soundwave visual on right
    soundwave_bars = [40, 100, 160, 80, 200, 120, 60, 140, 80, 30]
    bx = 720
    for h_val in soundwave_bars:
        by1 = 160 - (h_val // 2)
        by2 = 160 + (h_val // 2)
        draw.rounded_rectangle([bx, by1, bx + 10, by2], radius=5, fill=(56, 189, 248, 220))
        bx += 20

    # Floating metric pill on right
    draw.rounded_rectangle([680, 230, 930, 274], radius=22, fill=(15, 23, 42, 240), outline=(56, 189, 248, 255), width=2)
    font_metric = get_font(13, bold=True)
    draw.text((705, 243), "📞 103+ Production Calls", font=font_metric, fill=(56, 189, 248, 255))

    # Left content
    font_badge = get_font(12, bold=True)
    font_title = get_font(30, bold=True)
    font_sub = get_font(15, bold=True)
    font_bullet = get_font(14)
    font_stack = get_font(11, bold=True)

    draw.rounded_rectangle([50, 35, 230, 63], radius=14, fill=(15, 23, 42, 230), outline=(56, 189, 248, 255), width=1)
    draw.text((64, 41), "FEATURED PROJECT 01", font=font_badge, fill=(56, 189, 248, 255))

    draw.text((50, 75), "SKAIS — Voice AI Restaurant System", font=font_title, fill=(255, 255, 255, 255))
    draw.text((50, 115), "Autonomous Conversational AI Order & Reservation Platform", font=font_sub, fill=(148, 163, 184, 255))

    bullets = [
        "🔹 Retell AI Voice Agent taking live customer phone orders & reservations autonomously",
        "🔹 RAG Knowledge Base answering restaurant hours, policies, & menu items accurately",
        "🔹 FastAPI + Supabase + Twilio SDK for instant SMS order confirmations & prep-time logic",
        "🔹 50%+ Cost Reduction ($1,000–$1,500/mo software cost vs $2,000–$3,000/mo human operator)"
    ]
    by = 145
    for b in bullets:
        draw.text((50, by), b, font=font_bullet, fill=(226, 232, 240, 255))
        by += 26

    # Tech stack pills
    draw.text((50, 270), "TECH STACK:", font=get_font(12, bold=True), fill=(100, 116, 139, 255))
    stacks = ["Python", "FastAPI", "Retell AI SDK", "LangChain", "Supabase", "Twilio SDK", "Next.js"]
    sx = 145
    for s in stacks:
        sw = int(draw.textlength(s, font=font_stack)) + 16
        draw.rounded_rectangle([sx, 266, sx + sw, 290], radius=6, fill=(30, 41, 59, 230))
        draw.text((sx + 8, 271), s, font=font_stack, fill=(56, 189, 248, 255))
        sx += sw + 10

    img.save("assets/skais_banner.png", "PNG")
    print("Created assets/skais_banner.png")

def create_exambro_banner_png():
    W, H = 1000, 320
    img = Image.new("RGBA", (W, H), (20, 11, 41, 255))
    draw = ImageDraw.Draw(img)

    draw_gradient_rect(draw, (0, 0, W, H), (20, 11, 41), (9, 5, 24), "vertical")

    # Border & top accent
    draw.rectangle([0, 0, W-1, H-1], outline=(30, 41, 59, 255), width=2)
    top_bar = Image.new("RGBA", (W, 4), (0, 0, 0, 0))
    tb_draw = ImageDraw.Draw(top_bar)
    draw_gradient_rect(tb_draw, (0, 0, W, 4), (167, 139, 250), (52, 211, 153), "horizontal")
    img.paste(top_bar, (0, 0), top_bar)

    # Right side graphic - PDF OCR document card
    draw.rounded_rectangle([720, 45, 880, 255], radius=10, fill=(15, 23, 42, 240), outline=(167, 139, 250, 255), width=2)
    draw.line([(745, 75), (855, 75)], fill=(226, 232, 240, 255), width=3)
    draw.line([(745, 95), (835, 95)], fill=(148, 163, 184, 255), width=2)
    draw.line([(745, 110), (820, 110)], fill=(148, 163, 184, 255), width=2)

    # Diagram box inside PDF
    draw.rounded_rectangle([745, 130, 855, 190], radius=6, fill=(30, 41, 59, 230), outline=(52, 211, 153, 255), width=1)
    draw.polygon([(760, 175), (785, 145), (810, 175)], fill=None, outline=(52, 211, 153, 255))
    draw.ellipse([820, 145, 836, 161], fill=(244, 114, 182, 255))

    # OCR Scan Line
    draw.line([(710, 160), (890, 160)], fill=(244, 114, 182, 255), width=3)

    # Left content
    font_badge = get_font(12, bold=True)
    font_title = get_font(30, bold=True)
    font_sub = get_font(15, bold=True)
    font_bullet = get_font(14)
    font_stack = get_font(11, bold=True)

    draw.rounded_rectangle([50, 35, 230, 63], radius=14, fill=(15, 23, 42, 230), outline=(167, 139, 250, 255), width=1)
    draw.text((64, 41), "FEATURED PROJECT 02", font=font_badge, fill=(167, 139, 250, 255))

    draw.text((50, 75), "ExamBro — OCR & Exam Extraction", font=font_title, fill=(255, 255, 255, 255))
    draw.text((50, 115), "Automated Question, Diagram & Solution Extraction Pipeline", font=font_sub, fill=(148, 163, 184, 255))

    bullets = [
        "🔹 Mistral OCR + PyMuPDF pipeline pulling questions, options & diagrams straight from PDFs",
        "🔹 Diagram Alignment Engine resolving recurring spatial displacement bugs in OCR output",
        "🔹 Gemini AI via LangChain converting raw text into structured JSON & auto-filling answers",
        "🔹 Docker Containerized with multilingual translation & bulk admin dashboard"
    ]
    by = 145
    for b in bullets:
        draw.text((50, by), b, font=font_bullet, fill=(226, 232, 240, 255))
        by += 26

    # Tech stack pills
    draw.text((50, 270), "TECH STACK:", font=get_font(12, bold=True), fill=(100, 116, 139, 255))
    stacks = ["Python", "Django", "FastAPI", "Mistral OCR", "Gemini AI", "PyMuPDF", "Docker"]
    sx = 145
    for s in stacks:
        sw = int(draw.textlength(s, font=font_stack)) + 16
        draw.rounded_rectangle([sx, 266, sx + sw, 290], radius=6, fill=(30, 41, 59, 230))
        draw.text((sx + 8, 271), s, font=font_stack, fill=(167, 139, 250, 255))
        sx += sw + 10

    img.save("assets/exambro_banner.png", "PNG")
    print("Created assets/exambro_banner.png")

def create_quote_card_png():
    W, H = 1000, 160
    img = Image.new("RGBA", (W, H), (15, 23, 42, 255))
    draw = ImageDraw.Draw(img)

    draw_gradient_rect(draw, (0, 0, W, H), (15, 23, 42), (9, 13, 22), "vertical")

    draw.rectangle([0, 0, W-1, H-1], outline=(51, 65, 85, 255), width=2)
    
    # Left vertical accent line
    left_bar = Image.new("RGBA", (6, H), (0, 0, 0, 0))
    lb_draw = ImageDraw.Draw(left_bar)
    draw_gradient_rect(lb_draw, (0, 0, 6, H), (56, 189, 248), (244, 114, 182), "vertical")
    img.paste(left_bar, (0, 0), left_bar)

    font_quote = get_font(19, bold=True, italic=True)
    font_author = get_font(13, bold=True)

    draw.text((45, 42), '"Ever tried. Ever failed. No matter. Try again. Fail again. Fail better"', font=font_quote, fill=(248, 250, 252, 255))
    
    draw.rounded_rectangle([45, 92, 215, 122], radius=15, fill=(30, 41, 59, 230), outline=(129, 140, 248, 255), width=1)
    draw.text((62, 99), "— Samuel Beckett", font=font_author, fill=(167, 139, 250, 255))

    img.save("assets/quote_card.png", "PNG")
    print("Created assets/quote_card.png")

def create_divider_png():
    W, H = 1000, 20
    img = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(img)

    draw_gradient_rect(draw, (50, 9, 950, 11), (56, 189, 248), (244, 114, 182), "horizontal")
    draw.ellipse([495, 5, 505, 15], fill=(167, 139, 250, 255))
    draw.ellipse([498, 8, 502, 12], fill=(255, 255, 255, 255))

    img.save("assets/divider.png", "PNG")
    print("Created assets/divider.png")

if __name__ == '__main__':
    create_directory()
    create_header_banner_png()
    create_skais_banner_png()
    create_exambro_banner_png()
    create_quote_card_png()
    create_divider_png()
