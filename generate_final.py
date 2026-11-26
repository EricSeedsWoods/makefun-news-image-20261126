import math
from PIL import Image, ImageDraw, ImageFont

# Canvas dimensions (2x supersampling for clean antialiasing)
SCALE = 2
WIDTH, HEIGHT = 1024 * SCALE, 1024 * SCALE

# Typography fonts
FONT_BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_REGULAR = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

def f_bold(size):
    return ImageFont.truetype(FONT_BOLD, int(size * SCALE))

def f_reg(size):
    return ImageFont.truetype(FONT_REGULAR, int(size * SCALE))

# Cohesive Executive Color Palette
BG_DARK = (10, 14, 23)           # Ultra-deep slate
CARD_BG = (17, 24, 39)           # Rich dark card surface
CARD_BORDER = (35, 48, 71)       # Crisp border outline
HEADER_BG = (15, 21, 35)

TEXT_HEAD = (255, 255, 255)      # Pure white
TEXT_BODY = (203, 213, 225)      # Slate 300
TEXT_MUTED = (148, 163, 184)     # Slate 400
TEXT_DIM = (100, 116, 139)       # Slate 500

# Region Badges & Accent colors
THEMES = {
    "red":     {"main": (248, 113, 113), "bg": (69, 10, 10),  "border": (185, 28, 28)},
    "amber":   {"main": (251, 191, 36),  "bg": (69, 26, 3),   "border": (217, 119, 6)},
    "blue":    {"main": (96, 165, 250),  "bg": (23, 37, 84),  "border": (37, 99, 235)},
    "rose":    {"main": (251, 113, 133), "bg": (76, 5, 25),   "border": (225, 29, 72)},
    "purple":  {"main": (192, 132, 252), "bg": (59, 7, 100),  "border": (147, 51, 234)},
    "emerald": {"main": (52, 211, 153),  "bg": (2, 44, 34),   "border": (5, 150, 105)},
    "orange":  {"main": (251, 146, 60),  "bg": (67, 20, 7),   "border": (234, 88, 12)},
    "cyan":    {"main": (34, 211, 238),  "bg": (8, 51, 68),   "border": (8, 145, 178)},
}

im = Image.new("RGBA", (WIDTH, HEIGHT), BG_DARK)
draw = ImageDraw.Draw(im)

# Subtle background tech grid lines
for gx in range(0, WIDTH, 48 * SCALE):
    draw.line([gx, 0, gx, HEIGHT], fill=(14, 20, 31), width=1)
for gy in range(0, HEIGHT, 48 * SCALE):
    draw.line([0, gy, WIDTH, gy], fill=(14, 20, 31), width=1)

# Rounded rectangle drawer
def draw_card(x, y, w, h, radius=12*SCALE, fill=CARD_BG, outline=CARD_BORDER, width=2*SCALE):
    draw.rounded_rectangle([x, y, x + w, y + h], radius=radius, fill=fill, outline=outline, width=width)

# ==================== MASTHEAD ====================
m_x, m_y = 18 * SCALE, 16 * SCALE
m_w = (1024 - 36) * SCALE
m_h = 100 * SCALE

draw_card(m_x, m_y, m_w, m_h, radius=12*SCALE, fill=HEADER_BG, outline=(42, 57, 84), width=2*SCALE)

# Cyan/blue top glow line
draw.rounded_rectangle([m_x + 12*SCALE, m_y + 2*SCALE, m_x + m_w - 12*SCALE, m_y + 4*SCALE], radius=1*SCALE, fill=(56, 189, 248))

# Sub-header tracker
draw.text((m_x + 20 * SCALE, m_y + 14 * SCALE), "GLOBAL INTELLIGENCE SUMMARY • VERIFIED 24-HOUR WORLD DISPATCH", fill=(56, 189, 248), font=f_bold(9))

# Date of Record: Bold, prominent, unmissable
draw.text((m_x + 20 * SCALE, m_y + 29 * SCALE), "THURSDAY, 26 NOVEMBER 2026", fill=TEXT_HEAD, font=f_bold(25))

# Masthead subtitle
draw.text((m_x + 20 * SCALE, m_y + 69 * SCALE), "Essential Geopolitical, Military, Nuclear, Trade & Energy Developments Across 8 Global Fronts", fill=TEXT_MUTED, font=f_reg(10.5))

# Right Status Box
sb_w = 208 * SCALE
sb_h = 72 * SCALE
sb_x = m_x + m_w - sb_w - 14 * SCALE
sb_y = m_y + 14 * SCALE
draw.rounded_rectangle([sb_x, sb_y, sb_x + sb_w, sb_y + sb_h], radius=8*SCALE, fill=(10, 14, 23), outline=(42, 57, 84), width=1*SCALE)

# Live status pulse dot
draw.ellipse([sb_x + 12*SCALE, sb_y + 13*SCALE, sb_x + 20*SCALE, sb_y + 21*SCALE], fill=(239, 68, 68))
draw.text((sb_x + 26 * SCALE, sb_y + 11 * SCALE), "AUTHENTICATED RECORD", fill=(241, 245, 249), font=f_bold(8.5))
draw.text((sb_x + 12 * SCALE, sb_y + 31 * SCALE), "RECORD DATE: 2026-11-26 UTC", fill=TEXT_MUTED, font=f_reg(8.5))
draw.text((sb_x + 12 * SCALE, sb_y + 49 * SCALE), "SOURCES: WSJ • REUTERS • AP • CNBC", fill=(56, 189, 248), font=f_bold(8))

# ==================== 8 FACT STORIES ====================
stories = [
    {
        "region": "MIDDLE EAST",
        "theme": "red",
        "topic": "FATAL DRONE STRIKE",
        "headline": "Iranian Drone Kills 2 Italians in Kuwait Base",
        "summary": "Suicide drone struck a Kuwait military base, killing two Italian technicians from Rheinmetall Italia who were servicing a critical air-defense radar system.",
        "sources": "WSJ • Reuters",
        "icon": "drone"
    },
    {
        "region": "UKRAINE",
        "theme": "amber",
        "topic": "POWER GRID ATTACKS",
        "headline": "Zelenskyy Grid Warning; Kyiv Hit by Missiles",
        "summary": "President Zelenskyy alerted that Moscow prepares another massive strike on energy infrastructure as Russian ballistic missiles hit targets in Kyiv.",
        "sources": "PBS News • AP",
        "icon": "grid"
    },
    {
        "region": "US / NATO",
        "theme": "blue",
        "topic": "STRATEGIC ALLIANCE",
        "headline": "Trump & Rutte Warn Russia on Expanding War",
        "summary": "Following high-level talks at Mar-a-Lago, Donald Trump and NATO Chief Mark Rutte issued a joint statement urging Russia not to widen the Ukraine war.",
        "sources": "CNBC • Fox News",
        "icon": "nato"
    },
    {
        "region": "RUSSIA",
        "theme": "rose",
        "topic": "RECORD WAR BUDGET",
        "headline": "Kremlin Escalation Claims & Record Budget",
        "summary": "Moscow claimed Ukraine seeks to widen war to Baltic & Mediterranean; enacted record defense budget as German Chancellor Merz warned Russia wants more.",
        "sources": "The Hindu • 10things",
        "icon": "military"
    },
    {
        "region": "NORTH KOREA",
        "theme": "purple",
        "topic": "NUCLEAR ARSENAL",
        "headline": "Kim Orders Fissile Nuclear Arsenal Expansion",
        "summary": "Inspecting nuclear production sites, Kim Jong Un demanded rapid expansion of weapon-grade materials output to bolster North Korea's atomic arsenal.",
        "sources": "CNBC • Deutsche Welle",
        "icon": "nuclear"
    },
    {
        "region": "GLOBAL TRADE",
        "theme": "emerald",
        "topic": "TARIFF ESCALATION",
        "headline": "US Targets 14 Nations; China Truce at Risk",
        "summary": "US proposed sweeping new tariff rounds on 14 trading partners; new levies on Chinese imports threaten to undermine the fragile bilateral trade truce.",
        "sources": "CNBC • Wall Street Journal",
        "icon": "trade"
    },
    {
        "region": "ENERGY",
        "theme": "orange",
        "topic": "OPEC+ 2027 QUOTAS",
        "headline": "OPEC+ Weighs 2027 Output Amid Oil Surplus",
        "summary": "Energy cartel prepares decisive 2027 production target decisions as forecasts project expanding global crude surplus, balancing prices with quotas.",
        "sources": "Wall Street Journal",
        "icon": "oil"
    },
    {
        "region": "EUROPE",
        "theme": "cyan",
        "topic": "BORDER DEFENSE",
        "headline": "EU Budget Summit; Poland Prepares No-Fly Zone",
        "summary": "EU leaders met in Brussels on joint defense funding while Poland finalized operational plans for a border no-fly defense perimeter near western Ukraine.",
        "sources": "The Guardian • DW",
        "icon": "europe"
    }
]

# ==================== ICON ARTWORK ====================
def draw_icon_art(cx, cy, icon_name, col_main):
    r = 14 * SCALE
    white = (255, 255, 255)
    
    if icon_name == "drone":
        # Reticle circle
        draw.arc([cx - r, cy - r, cx + r, cy + r], start=0, end=360, fill=(55, 75, 105), width=1*SCALE)
        draw.line([cx - r - 2*SCALE, cy, cx - r + 4*SCALE, cy], fill=col_main, width=2*SCALE)
        draw.line([cx + r - 4*SCALE, cy, cx + r + 2*SCALE, cy], fill=col_main, width=2*SCALE)
        draw.line([cx, cy - r - 2*SCALE, cx, cy - r + 4*SCALE], fill=col_main, width=2*SCALE)
        draw.line([cx, cy + r - 4*SCALE, cx, cy + r + 2*SCALE], fill=col_main, width=2*SCALE)
        # Swept delta-wing combat UAV silhouette
        nose = (cx, cy - r + 4*SCALE)
        tip_r = (cx + r - 3*SCALE, cy + r - 5*SCALE)
        notch = (cx, cy + r * 0.25)
        tip_l = (cx - r + 3*SCALE, cy + r - 5*SCALE)
        draw.polygon([nose, tip_r, notch, tip_l], fill=col_main)
        # Center sensor dot
        draw.ellipse([cx - 2*SCALE, cy - 2*SCALE, cx + 2*SCALE, cy + 2*SCALE], fill=white)

    elif icon_name == "grid":
        # Transmission pylon
        top = (cx, cy - r + 3*SCALE)
        b_r = (cx + r * 0.65, cy + r - 3*SCALE)
        b_l = (cx - r * 0.65, cy + r - 3*SCALE)
        draw.line([top, b_l], fill=col_main, width=2*SCALE)
        draw.line([top, b_r], fill=col_main, width=2*SCALE)
        # Pylon cross arms
        draw.line([cx - r * 0.45, cy - r * 0.2, cx + r * 0.45, cy - r * 0.2], fill=col_main, width=2*SCALE)
        draw.line([cx - r * 0.6, cy + r * 0.25, cx + r * 0.6, cy + r * 0.25], fill=col_main, width=2*SCALE)
        # Sharp high-voltage lightning bolt
        bolt = [
            (cx + 1*SCALE, cy - r + 2*SCALE),
            (cx - 4*SCALE, cy),
            (cx + 2*SCALE, cy),
            (cx - 3*SCALE, cy + r - 2*SCALE)
        ]
        draw.line(bolt, fill=white, width=2*SCALE)

    elif icon_name == "nato":
        # NATO 4-point compass star
        star = [
            (cx, cy - r), (cx + 3*SCALE, cy - 3*SCALE),
            (cx + r, cy), (cx + 3*SCALE, cy + 3*SCALE),
            (cx, cy + r), (cx - 3*SCALE, cy + 3*SCALE),
            (cx - r, cy), (cx - 3*SCALE, cy - 3*SCALE)
        ]
        draw.polygon(star, fill=col_main)
        draw.ellipse([cx - 5*SCALE, cy - 5*SCALE, cx + 5*SCALE, cy + 5*SCALE], fill=(17, 24, 39), outline=white, width=2*SCALE)

    elif icon_name == "military":
        # Shield with budget trend chart
        shield = [
            (cx - r + 3*SCALE, cy - r + 3*SCALE),
            (cx + r - 3*SCALE, cy - r + 3*SCALE),
            (cx + r - 3*SCALE, cy + 2*SCALE),
            (cx, cy + r - 2*SCALE),
            (cx - r + 3*SCALE, cy + 2*SCALE)
        ]
        draw.polygon(shield, fill=(24, 34, 52), outline=col_main, width=2*SCALE)
        # 3 ascending budget bars
        bw = 3 * SCALE
        draw.rectangle([cx - 8*SCALE, cy + 1*SCALE, cx - 8*SCALE + bw, cy + 7*SCALE], fill=col_main)
        draw.rectangle([cx - 2*SCALE, cy - 3*SCALE, cx - 2*SCALE + bw, cy + 7*SCALE], fill=col_main)
        draw.rectangle([cx + 4*SCALE, cy - 7*SCALE, cx + 4*SCALE + bw, cy + 7*SCALE], fill=white)

    elif icon_name == "nuclear":
        # Radiation trefoil emblem
        draw.ellipse([cx - r + 2*SCALE, cy - r + 2*SCALE, cx + r - 2*SCALE, cy + r - 2*SCALE], outline=col_main, width=1*SCALE)
        # Central dot
        draw.ellipse([cx - 3*SCALE, cy - 3*SCALE, cx + 3*SCALE, cy + 3*SCALE], fill=white)
        # Three sectors (top, bottom-left, bottom-right)
        for ang in [-90, 30, 150]:
            rad1 = math.radians(ang - 24)
            rad2 = math.radians(ang + 24)
            rad_m = math.radians(ang)
            p1 = (cx + math.cos(rad1) * (r * 0.85), cy + math.sin(rad1) * (r * 0.85))
            p2 = (cx + math.cos(rad2) * (r * 0.85), cy + math.sin(rad2) * (r * 0.85))
            pm = (cx + math.cos(rad_m) * (r * 0.4), cy + math.sin(rad_m) * (r * 0.4))
            draw.polygon([(cx, cy), p1, p2], fill=col_main)

    elif icon_name == "trade":
        # Container cargo freighter & tariff indicator
        hull = [
            (cx - r + 2*SCALE, cy + 2*SCALE),
            (cx + r - 2*SCALE, cy + 2*SCALE),
            (cx + r * 0.55, cy + r - 3*SCALE),
            (cx - r * 0.55, cy + r - 3*SCALE)
        ]
        draw.polygon(hull, fill=col_main)
        # Cargo crates
        draw.rectangle([cx - 10*SCALE, cy - 6*SCALE, cx - 2*SCALE, cy + 1*SCALE], fill=white)
        draw.rectangle([cx, cy - 8*SCALE, cx + 8*SCALE, cy + 1*SCALE], fill=col_main, outline=white, width=1*SCALE)
        # Tariff percent marker
        draw.text((cx - 8*SCALE, cy - r + 1*SCALE), "%", fill=white, font=f_bold(7))

    elif icon_name == "oil":
        # Industrial oil drum with petroleum droplet
        bw, bh = 18 * SCALE, 22 * SCALE
        draw.rounded_rectangle([cx - bw//2, cy - bh//2, cx + bw//2, cy + bh//2], radius=3*SCALE, fill=(24, 34, 52), outline=col_main, width=2*SCALE)
        draw.line([cx - bw//2, cy - bh//6, cx + bw//2, cy - bh//6], fill=col_main, width=1*SCALE)
        draw.line([cx - bw//2, cy + bh//6, cx + bw//2, cy + bh//6], fill=col_main, width=1*SCALE)
        # Petroleum droplet
        draw.ellipse([cx - 4*SCALE, cy - 1*SCALE, cx + 4*SCALE, cy + 6*SCALE], fill=white)
        draw.polygon([(cx, cy - 6*SCALE), (cx - 4*SCALE, cy), (cx + 4*SCALE, cy)], fill=white)

    elif icon_name == "europe":
        # Defense perimeter radar circle with interceptor
        draw.ellipse([cx - r + 2*SCALE, cy - r + 2*SCALE, cx + r - 2*SCALE, cy + r - 2*SCALE], outline=col_main, width=2*SCALE)
        # Tactical interceptor jet
        nose = (cx + r * 0.6, cy - r * 0.5)
        tail = (cx - r * 0.5, cy + r * 0.5)
        l_wing = (cx - r * 0.1, cy - r * 0.4)
        r_wing = (cx + r * 0.4, cy + r * 0.1)
        draw.line([nose, tail], fill=white, width=3*SCALE)
        draw.line([l_wing, r_wing], fill=white, width=2*SCALE)
        # Diagonal no-fly ban line
        draw.line([cx - r * 0.8, cy + r * 0.8, cx + r * 0.8, cy - r * 0.8], fill=(239, 68, 68), width=2*SCALE)

# ==================== GRID GEOMETRY ====================
COL_W = 476 * SCALE
ROW_H = 198 * SCALE
START_X = 18 * SCALE
START_Y = 132 * SCALE
GAP_X = 36 * SCALE
GAP_Y = 14 * SCALE

for i, story in enumerate(stories):
    col = i % 2
    row = i // 2
    x = START_X + col * (COL_W + GAP_X)
    y = START_Y + row * (ROW_H + GAP_Y)
    
    pal = THEMES[story["theme"]]
    
    # 1. Card Container
    draw_card(x, y, COL_W, ROW_H, radius=12*SCALE, fill=CARD_BG, outline=CARD_BORDER, width=2*SCALE)
    
    # 2. Colored Left Border Ribbon
    draw.rounded_rectangle([x + 3*SCALE, y + 12*SCALE, x + 7*SCALE, y + ROW_H - 12*SCALE], radius=2*SCALE, fill=pal["main"])
    
    # 3. Region Tag & Topic Label
    reg_font = f_bold(8.5)
    reg_text = story["region"]
    r_bbox = draw.textbbox((0, 0), reg_text, font=reg_font)
    r_w = (r_bbox[2] - r_bbox[0]) + 16 * SCALE
    r_h = 20 * SCALE
    rx = x + 16 * SCALE
    ry = y + 13 * SCALE
    draw.rounded_rectangle([rx, ry, rx + r_w, ry + r_h], radius=4*SCALE, fill=pal["bg"], outline=pal["border"], width=1*SCALE)
    draw.text((rx + 8*SCALE, ry + 3*SCALE), reg_text, fill=pal["main"], font=reg_font)
    
    # Topic Tag
    top_font = f_bold(8)
    draw.text((rx + r_w + 10*SCALE, ry + 4*SCALE), f"// {story['topic']}", fill=TEXT_MUTED, font=top_font)
    
    # 4. Icon Container
    icon_w = 34 * SCALE
    icon_x = x + COL_W - icon_w - 14 * SCALE
    icon_y = y + 10 * SCALE
    draw.rounded_rectangle([icon_x, icon_y, icon_x + icon_w, icon_y + icon_w], radius=7*SCALE, fill=(23, 32, 50), outline=(42, 57, 84), width=1*SCALE)
    draw_icon_art(icon_x + icon_w//2, icon_y + icon_w//2, story["icon"], pal["main"])
    
    # 5. Headline
    head_font = f_bold(12.5)
    hx = x + 16 * SCALE
    hy = y + 41 * SCALE
    draw.text((hx, hy), story["headline"], fill=TEXT_HEAD, font=head_font)
    
    # Separator Line
    draw.line([hx, y + 68 * SCALE, x + COL_W - 16 * SCALE, y + 68 * SCALE], fill=(30, 42, 64), width=1*SCALE)
    
    # 6. Summary Body
    body_font = f_reg(10)
    body_y = y + 76 * SCALE
    max_line_w = COL_W - 32 * SCALE
    
    words = story["summary"].split()
    lines = []
    curr = []
    for w in words:
        test = " ".join(curr + [w])
        bb = draw.textbbox((0, 0), test, font=body_font)
        if bb[2] - bb[0] <= max_line_w:
            curr.append(w)
        else:
            lines.append(" ".join(curr))
            curr = [w]
    if curr:
        lines.append(" ".join(curr))
        
    for l_idx, line in enumerate(lines[:3]):
        draw.text((hx, body_y + l_idx * 18 * SCALE), line, fill=TEXT_BODY, font=body_font)
        
    # 7. Source & Verification Footer
    foot_card_y = y + ROW_H - 24 * SCALE
    
    src_label_font = f_bold(8)
    src_val_font = f_bold(8.5)
    draw.text((hx, foot_card_y), "SOURCE:", fill=TEXT_DIM, font=src_label_font)
    draw.text((hx + 52 * SCALE, foot_card_y), story["sources"], fill=pal["main"], font=src_val_font)
    
    # Green check + confirmed tag
    chk_x = x + COL_W - 118 * SCALE
    draw.ellipse([chk_x, foot_card_y + 1*SCALE, chk_x + 9*SCALE, foot_card_y + 10*SCALE], fill=(16, 185, 129))
    draw.text((chk_x + 13 * SCALE, foot_card_y), "26 NOV RECORD", fill=TEXT_DIM, font=f_bold(7.5))

# ==================== BOTTOM FOOTER ====================
foot_y = 986 * SCALE
foot_w = (1024 - 36) * SCALE
foot_h = 24 * SCALE
draw_card(18 * SCALE, foot_y, foot_w, foot_h, radius=6*SCALE, fill=HEADER_BG, outline=(35, 48, 71), width=1*SCALE)

draw.text((32 * SCALE, foot_y + 5 * SCALE), "DATE OF RECORD: THURSDAY 26 NOVEMBER 2026", fill=(56, 189, 248), font=f_bold(8))
draw.text((320 * SCALE, foot_y + 5 * SCALE), "WORLD NEWS SUMMARY BRIEFING • ALL 8 PRIMARY REGIONS CROSS-VERIFIED WITH INTERNATIONAL WIRES", fill=TEXT_MUTED, font=f_reg(8))
draw.text((885 * SCALE, foot_y + 5 * SCALE), "MAKE.FUN BOUNTY", fill=TEXT_DIM, font=f_bold(8))

# Downscale from 2048x2048 to 1024x1024 with Lanczos for ultra-crisp antialiasing
final_im = im.resize((1024, 1024), Image.Resampling.LANCZOS)
final_im.save("entry.png", "PNG", optimize=True)
print("Final entry.png written successfully.")
