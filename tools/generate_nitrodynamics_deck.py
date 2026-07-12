from pathlib import Path

from PIL import Image
from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LABEL_POSITION, XL_LEGEND_POSITION
from pptx.enum.shapes import MSO_CONNECTOR, MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR, PP_ALIGN
from pptx.util import Inches, Pt


ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "_bmad-output"
ASSET_DIR = OUT_DIR / "deck_assets"
PPTX_PATH = OUT_DIR / "Nitrodynamics_Investor_Presentation_V1.pptx"
OUTLINE_PATH = OUT_DIR / "Nitrodynamics_Investor_Presentation_V1_outline.md"

OUT_DIR.mkdir(exist_ok=True)
ASSET_DIR.mkdir(exist_ok=True)

IMG = {
    "flywheel": ASSET_DIR / "image1.png",
    "roadmap": ASSET_DIR / "image2.png",
    "scorecard": ASSET_DIR / "image3.png",
    "arc": ASSET_DIR / "image4.png",
    "revenue_stack": ASSET_DIR / "image5.png",
    "working_capital": ASSET_DIR / "image6.png",
    "fcf_waterfall": ASSET_DIR / "image7.png",
    "funding_cash": ASSET_DIR / "image8.png",
    "tornado": ASSET_DIR / "image9.png",
    "org": ASSET_DIR / "image10.png",
}

# Theme
NAVY = RGBColor(6, 20, 35)
INK = RGBColor(13, 23, 35)
WHITE = RGBColor(255, 255, 255)
MUTED = RGBColor(122, 139, 154)
SLATE = RGBColor(61, 76, 92)
GREEN = RGBColor(0, 194, 144)
GREEN_DARK = RGBColor(0, 139, 111)
CYAN = RGBColor(0, 168, 232)
BLUE = RGBColor(37, 99, 235)
ORANGE = RGBColor(245, 158, 11)
RED = RGBColor(220, 38, 38)
BG = RGBColor(247, 249, 252)
PALE = RGBColor(232, 241, 247)
GRID = RGBColor(209, 218, 229)

SLIDE_W = Inches(13.333333)
SLIDE_H = Inches(7.5)

prs = Presentation()
prs.slide_width = SLIDE_W
prs.slide_height = SLIDE_H
blank = prs.slide_layouts[6]
slide_records = []


def set_fill(shape, color, transparency=0):
    shape.fill.solid()
    shape.fill.fore_color.rgb = color
    if transparency:
        shape.fill.transparency = transparency
    shape.line.fill.background()


def set_line(shape, color, width=1.0, transparency=0):
    shape.line.color.rgb = color
    shape.line.width = Pt(width)
    if transparency:
        shape.line.transparency = transparency


def add_bg(slide, dark=False):
    rect = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, SLIDE_W, SLIDE_H)
    set_fill(rect, NAVY if dark else BG)
    strip = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, 0, 0, Inches(0.16), SLIDE_H)
    set_fill(strip, GREEN if dark else CYAN)
    return rect


def add_text(
    slide,
    text,
    x,
    y,
    w,
    h,
    font_size=24,
    color=INK,
    bold=False,
    align="left",
    font="Aptos",
    valign="top",
    italic=False,
):
    box = slide.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
    tf = box.text_frame
    tf.clear()
    tf.margin_left = Pt(0)
    tf.margin_right = Pt(0)
    tf.margin_top = Pt(0)
    tf.margin_bottom = Pt(0)
    tf.word_wrap = True
    tf.vertical_anchor = {
        "top": MSO_ANCHOR.TOP,
        "middle": MSO_ANCHOR.MIDDLE,
        "bottom": MSO_ANCHOR.BOTTOM,
    }.get(valign, MSO_ANCHOR.TOP)
    p = tf.paragraphs[0]
    p.alignment = {
        "left": PP_ALIGN.LEFT,
        "center": PP_ALIGN.CENTER,
        "right": PP_ALIGN.RIGHT,
    }.get(align, PP_ALIGN.LEFT)
    run = p.add_run()
    run.text = text
    run.font.name = font
    run.font.size = Pt(font_size)
    run.font.bold = bold
    run.font.italic = italic
    run.font.color.rgb = color
    return box


def add_title(slide, title, subtitle=None, dark=False, kicker=None):
    if kicker:
        add_text(
            slide,
            kicker.upper(),
            0.55,
            0.32,
            4.5,
            0.25,
            8.5,
            GREEN if dark else BLUE,
            bold=True,
        )
    add_text(
        slide,
        title,
        0.55,
        0.54 if kicker else 0.38,
        9.4,
        0.55,
        25,
        WHITE if dark else NAVY,
        bold=True,
    )
    if subtitle:
        add_text(
            slide,
            subtitle,
            0.56,
            1.06 if kicker else 0.95,
            9.2,
            0.34,
            10.5,
            RGBColor(199, 213, 225) if dark else SLATE,
        )
    add_text(
        slide,
        "NITRODYNAMICS",
        10.8,
        0.38,
        1.95,
        0.22,
        8.5,
        RGBColor(156, 172, 190) if dark else MUTED,
        bold=True,
        align="right",
    )


def add_footer(slide, n, dark=False):
    add_text(
        slide,
        f"{n:02d}",
        12.55,
        7.08,
        0.32,
        0.18,
        7.5,
        RGBColor(141, 158, 176) if dark else MUTED,
        align="right",
    )
    add_text(
        slide,
        "Confidential | Investor presentation | Figures in INR Crore unless noted",
        0.55,
        7.08,
        7.2,
        0.18,
        7.5,
        RGBColor(141, 158, 176) if dark else MUTED,
    )


def add_pill(
    slide,
    text,
    x,
    y,
    w,
    h=0.34,
    fill=PALE,
    color=NAVY,
    font_size=9.5,
    bold=True,
):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    set_fill(shp, fill)
    shp.line.color.rgb = RGBColor(196, 206, 218)
    shp.line.width = Pt(0.6)
    add_text(
        slide,
        text,
        x + 0.08,
        y + 0.08,
        w - 0.16,
        h - 0.12,
        font_size,
        color,
        bold=bold,
        align="center",
    )
    return shp


def add_card(
    slide,
    x,
    y,
    w,
    h,
    title,
    value=None,
    note=None,
    fill=WHITE,
    accent=GREEN,
    dark=False,
    value_size=28,
    title_size=9.5,
):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    set_fill(shp, fill)
    set_line(shp, RGBColor(216, 224, 235), 0.8)
    bar = slide.shapes.add_shape(
        MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.06), Inches(h)
    )
    set_fill(bar, accent)
    add_text(
        slide,
        title.upper(),
        x + 0.18,
        y + 0.16,
        w - 0.32,
        0.2,
        title_size,
        MUTED if not dark else RGBColor(201, 213, 225),
        bold=True,
    )
    if value is not None:
        add_text(
            slide,
            value,
            x + 0.18,
            y + 0.42,
            w - 0.32,
            0.46,
            value_size,
            NAVY if not dark else WHITE,
            bold=True,
        )
    if note:
        add_text(
            slide,
            note,
            x + 0.18,
            y + h - 0.42,
            w - 0.32,
            0.28,
            8.5,
            SLATE if not dark else RGBColor(203, 213, 225),
        )
    return shp


def add_bullet_list(
    slide, bullets, x, y, w, h, font_size=13, color=INK, bullet_color=GREEN, gap=0.34
):
    cy = y
    for b in bullets:
        circ = slide.shapes.add_shape(
            MSO_SHAPE.OVAL, Inches(x), Inches(cy + 0.05), Inches(0.09), Inches(0.09)
        )
        set_fill(circ, bullet_color)
        add_text(slide, b, x + 0.18, cy, w - 0.18, 0.34, font_size, color)
        cy += gap


def add_quote(slide, text, x, y, w, h, dark=False):
    shp = slide.shapes.add_shape(
        MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
    )
    set_fill(shp, RGBColor(15, 40, 63) if dark else WHITE)
    set_line(shp, RGBColor(33, 75, 102) if dark else RGBColor(209, 218, 229), 0.8)
    add_text(slide, '"', x + 0.25, y + 0.05, 0.35, 0.5, 30, GREEN, bold=True)
    add_text(
        slide,
        text,
        x + 0.62,
        y + 0.26,
        w - 0.85,
        h - 0.45,
        15,
        WHITE if dark else NAVY,
        bold=True,
    )
    return shp


def add_full_bleed_image(slide, path, x, y, w, h, border=True):
    path = Path(path)
    if not path.exists():
        return None
    with Image.open(path) as im:
        iw, ih = im.size
    box_w, box_h = Inches(w), Inches(h)
    ratio = min(box_w / iw, box_h / ih)
    pw, ph = int(iw * ratio), int(ih * ratio)
    px = Inches(x) + int((box_w - pw) / 2)
    py = Inches(y) + int((box_h - ph) / 2)
    pic = slide.shapes.add_picture(str(path), px, py, width=pw, height=ph)
    if border:
        rect = slide.shapes.add_shape(
            MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(w), Inches(h)
        )
        rect.fill.background()
        set_line(rect, RGBColor(190, 202, 216), 0.8)
    return pic


def add_simple_table(slide, data, x, y, w, h, col_widths=None, header_fill=NAVY, font_size=8.6):
    rows, cols = len(data), len(data[0])
    tbl_shape = slide.shapes.add_table(rows, cols, Inches(x), Inches(y), Inches(w), Inches(h))
    table = tbl_shape.table
    if col_widths:
        for i, cw in enumerate(col_widths):
            table.columns[i].width = Inches(cw)
    for r in range(rows):
        for c in range(cols):
            cell = table.cell(r, c)
            cell.text = str(data[r][c])
            cell.margin_left = Pt(5)
            cell.margin_right = Pt(5)
            cell.margin_top = Pt(3)
            cell.margin_bottom = Pt(3)
            fill = cell.fill
            fill.solid()
            fill.fore_color.rgb = header_fill if r == 0 else (RGBColor(247, 249, 252) if r % 2 == 1 else WHITE)
            for p in cell.text_frame.paragraphs:
                p.alignment = PP_ALIGN.CENTER if c > 0 else PP_ALIGN.LEFT
                for run in p.runs:
                    run.font.name = "Aptos"
                    run.font.size = Pt(font_size if r else font_size + 0.2)
                    run.font.bold = r == 0
                    run.font.color.rgb = WHITE if r == 0 else INK
    return tbl_shape


def add_chart_bar(slide, categories, values, x, y, w, h, title=None, color=BLUE):
    chart_data = CategoryChartData()
    chart_data.categories = categories
    chart_data.add_series(title or "Series", values)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.COLUMN_CLUSTERED, Inches(x), Inches(y), Inches(w), Inches(h), chart_data
    ).chart
    chart.has_legend = False
    chart.has_title = False
    chart.value_axis.has_major_gridlines = True
    chart.value_axis.tick_labels.font.size = Pt(8)
    chart.category_axis.tick_labels.font.size = Pt(8)
    chart.value_axis.major_gridlines.format.line.color.rgb = GRID
    series = chart.series[0]
    series.format.fill.solid()
    series.format.fill.fore_color.rgb = color
    series.has_data_labels = True
    series.data_labels.font.size = Pt(7)
    series.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
    return chart


def add_chart_line(slide, categories, series_dict, x, y, w, h, colors):
    data = CategoryChartData()
    data.categories = categories
    for name, vals in series_dict.items():
        data.add_series(name, vals)
    chart = slide.shapes.add_chart(
        XL_CHART_TYPE.LINE_MARKERS, Inches(x), Inches(y), Inches(w), Inches(h), data
    ).chart
    chart.has_legend = True
    chart.legend.position = XL_LEGEND_POSITION.BOTTOM
    chart.legend.font.size = Pt(8)
    chart.value_axis.has_major_gridlines = True
    chart.value_axis.major_gridlines.format.line.color.rgb = GRID
    chart.value_axis.tick_labels.font.size = Pt(8)
    chart.category_axis.tick_labels.font.size = Pt(8)
    chart.has_title = False
    for i, s in enumerate(chart.series):
        s.format.line.color.rgb = colors[i % len(colors)]
        s.format.line.width = Pt(2.2)
        s.marker.format.fill.solid()
        s.marker.format.fill.fore_color.rgb = colors[i % len(colors)]
        s.marker.size = 5
    return chart


def add_notes(slide, notes):
    # PowerPoint speaker notes are not exposed by python-pptx. This hidden off-slide
    # textbox preserves notes in the file for future extraction/editing.
    box = slide.shapes.add_textbox(Inches(14.0), Inches(0.2), Inches(4.5), Inches(5.0))
    box.text = "SPEAKER NOTES:\n" + notes
    return box


headline_metrics = [
    ("10-yr cumulative revenue", "Rs.21,200 Cr", "Six product lines"),
    ("Y10 revenue", "Rs.5,055 Cr", "Mature run-rate"),
    ("Y10 EBITDA / margin", "Rs.2,347 Cr / 46.4%", "vs 10-15% legacy-prime norm"),
    ("10-yr cumulative FCF", "Rs.4,803 Cr", "After tax, capex, WC"),
    ("Project IRR / NPV", "31.9% / Rs.747 Cr", "At 18% WACC"),
    ("Total equity raised", "Rs.1,100 Cr", "450 / 400 / 250"),
]
product_lines = [
    ["V2", "EW / SIGINT", "Y1", "Day-1 cash engine"],
    ["V6", "Military AI", "Y1", "93-94% GM software attach"],
    ["V1", "AESA Radar", "Y2", "RF/DSP hardware flagship"],
    ["V3", "Counter-UAS", "Y2", "Highest unit volume"],
    ["V5", "AUV / USV", "Y3", "Maritime autonomy"],
    ["V4", "MALE UAS", "Y4", "Highest unit price"],
]
rev_years = ["Y1", "Y2", "Y3", "Y4", "Y5", "Y6", "Y7", "Y8", "Y9", "Y10"]
rev_vals = [53, 203, 491, 855, 1448, 2180, 2884, 3659, 4381, 5055]
gm_vals = [51, 56, 62, 64, 65, 66, 66, 67, 67, 67]
fcf_vals = [-181, -232, -196, 65, 238, 519, 773, 1061, 1328, 1549]
prod_mix_y10 = [
    ("V1 AESA", 1080),
    ("V2 EW", 850),
    ("V3 C-UAS", 1150),
    ("V4 MALE", 900),
    ("V5 AUV/USV", 575),
    ("V6 AI", 500),
]


# 1 Cover
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_text(slide, "NITRODYNAMICS", 0.68, 0.58, 4.2, 0.35, 15, GREEN, bold=True)
add_text(slide, "A platform-native\ndefense prime", 0.65, 1.26, 8.2, 1.55, 42, WHITE, bold=True)
add_text(
    slide,
    "Engineer once, deploy everywhere.\nOne platform, six product lines, four domains.",
    0.70,
    3.02,
    6.8,
    0.72,
    19,
    RGBColor(218, 229, 238),
)
add_pill(slide, "Investor Presentation | Confidential", 0.70, 4.03, 2.85, fill=RGBColor(16, 52, 76), color=WHITE)
add_pill(slide, "Seed Ask: Rs.450 Cr", 3.75, 4.03, 2.05, fill=RGBColor(16, 52, 76), color=WHITE)
for i, (title, value, note) in enumerate(
    [
        ("Opening order book", "Rs.105 Cr", "Phase 1 of firm Rs.210 Cr MoQ"),
        ("10-yr revenue", "Rs.21,200 Cr", "six product lines"),
        ("Y10 EBITDA margin", "46.4%", "platform reuse economics"),
    ]
):
    add_card(slide, 8.15, 1.05 + i * 1.25, 3.7, 0.98, title, value, note, fill=RGBColor(11, 38, 60), accent=GREEN, dark=True, value_size=26)
add_footer(slide, 1, dark=True)
add_notes(slide, "Open with the one-line thesis: Nitrodynamics is not six startups; it is one reusable defense engineering platform industrialised into six product lines.")
slide_records.append(("Cover", "Platform-native defense prime; investor presentation."))

# 2 Investment case
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "The one-slide investment case", "Six product lines ride one reusable engineering platform.", kicker="Investment thesis")
cols = [
    ("01", "Start with revenue", "Rs.105 Cr opening ESM order book: Phase 1 of firm Rs.210 Cr iDEX ESM MoQ."),
    ("02", "Engineer once", "M1-M5 building blocks reused across radar, EW, C-UAS, UAS, maritime autonomy and AI."),
    ("03", "Margins compound", "Gross margin rises from ~51% to ~67%; Y10 EBITDA margin reaches 46.4%."),
]
for i, (num, head, body) in enumerate(cols):
    x = 0.72 + i * 4.08
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(1.55), Inches(3.65), Inches(2.25))
    set_fill(shp, WHITE)
    set_line(shp, RGBColor(215, 224, 235), 0.8)
    add_text(slide, num, x + 0.22, 1.78, 0.5, 0.35, 13, GREEN, bold=True)
    add_text(slide, head, x + 0.22, 2.17, 2.8, 0.28, 17, NAVY, bold=True)
    add_text(slide, body, x + 0.22, 2.62, 3.05, 0.72, 11.5, SLATE)
for i, (title, value, note) in enumerate(headline_metrics[:4]):
    add_card(slide, 0.72 + i * 3.05, 4.55, 2.78, 1.17, title, value, note, fill=WHITE, accent=[GREEN, CYAN, ORANGE, BLUE][i], value_size=20)
add_quote(slide, "The equity funds a platform flywheel - not six disconnected R&D bets.", 0.72, 6.08, 11.85, 0.56)
add_footer(slide, 2)
add_notes(slide, "3-second rule: If the investor remembers one thing, it is reusable platform plus Day-1 order book.")
slide_records.append(("Investment case", "Revenue traction, platform reuse, margin compounding."))

# 3 Market timing
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Why now: India needs indigenous multi-domain capability", "The demand window is open across EW, radar, drones, autonomous maritime and AI.", kicker="Market")
markets = [
    ("EW / SIGINT", "USD 22-25bn/yr", "6-8% CAGR"),
    ("Counter-UAS", "USD 6-7bn by 2030", "25-30% CAGR"),
    ("Defense AI", "USD 8-12bn today", "20%+ CAGR"),
    ("AESA radar", "USD 5-7bn/yr", "7-9% CAGR"),
    ("MALE UAS", "USD 4-5bn/yr", "8-10% CAGR"),
    ("AUV / USV", "USD 2.5-3.5bn/yr", "12-15% CAGR"),
]
for i, (seg, size, cagr) in enumerate(markets):
    x = 0.72 + (i % 3) * 4.05
    y = 1.45 + (i // 3) * 1.18
    add_card(slide, x, y, 3.55, 0.92, seg, size, cagr, fill=WHITE, accent=[GREEN, CYAN, ORANGE, BLUE, GREEN_DARK, CYAN][i], value_size=20)
add_text(slide, "India-specific demand drivers", 0.82, 4.30, 4.6, 0.25, 17, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Atmanirbhar Bharat biases procurement toward domestic capability.",
        "Positive indigenisation lists ringfence equipment families for domestic sourcing.",
        "Rs.50,000 Cr annual defense export target by 2028-29 supports allied-government channels.",
        "MoD anchor buyer on Day 1; allied exports begin layering from Year 2.",
    ],
    0.88,
    4.78,
    5.65,
    1.35,
    font_size=11.5,
    gap=0.34,
)
add_text(slide, "Structural gap", 7.15, 4.30, 4.2, 0.25, 17, NAVY, bold=True)
add_quote(slide, "Mid-tier defense programs are too slow for legacy primes, too integrated for point-product startups - exactly where a platform-native company wins.", 7.10, 4.75, 5.0, 1.16)
add_footer(slide, 3)
add_notes(slide, "Keep market talk short: this is not a TAM lecture. The point is that multiple market waves converge on a platform reuse strategy.")
slide_records.append(("Market timing", "Segment TAMs and India-specific demand drivers."))

# 4 Platform flywheel
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_title(slide, "The platform flywheel: five modules feed six verticals", "The moat is reusable qualified engineering, not a single SKU.", dark=True, kicker="Platform")
add_full_bleed_image(slide, IMG["flywheel"], 0.68, 1.35, 7.55, 4.25, border=False)
add_text(slide, "What compounds", 8.55, 1.50, 3.5, 0.3, 17, WHITE, bold=True)
add_bullet_list(
    slide,
    [
        "M1 radio / microwave and M2 signal processing de-risk AESA, EW and C-UAS together.",
        "M4 embedded mission software and M5 AI/ML attach to every hardware line.",
        "Module reuse rises toward 97-99% by Year 10.",
        "Blended gross margin climbs to ~67% by Year 10.",
    ],
    8.58,
    1.98,
    3.65,
    1.65,
    font_size=11.3,
    color=RGBColor(221, 232, 240),
    gap=0.38,
)
add_card(slide, 8.55, 4.25, 3.55, 0.95, "10-year platform investment", "~Rs.575 Cr", "M1-M5 combined", fill=RGBColor(11, 38, 60), accent=GREEN, dark=True, value_size=23)
add_card(slide, 8.55, 5.42, 3.55, 0.95, "NRE avoided by reuse", "~Rs.994 Cr", "Counterfactual savings", fill=RGBColor(11, 38, 60), accent=CYAN, dark=True, value_size=23)
add_footer(slide, 4, dark=True)
add_notes(slide, "Use the flywheel diagram. Say: every qualified block becomes an asset multiple product lines can draw from.")
slide_records.append(("Platform flywheel", "M1-M5 modules reused across V1-V6 product lines."))

# 5 Day-1 traction
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Day-1 traction: a funded cash engine, not a promise", "The ESM/SIGINT line starts with production-order revenue.", kicker="Traction")
add_card(slide, 0.75, 1.45, 3.3, 1.35, "Opening order book", "Rs.105 Cr", "Phase 1: 5 systems x Rs.21 Cr", fill=WHITE, accent=GREEN, value_size=30)
add_card(slide, 4.35, 1.45, 3.3, 1.35, "Firm ESM MoQ", "Rs.210 Cr", "10 systems in two 12-month phases", fill=WHITE, accent=CYAN, value_size=30)
add_card(slide, 7.95, 1.45, 3.3, 1.35, "Technical status", "4 milestones", "Development signed off; FOPM in build", fill=WHITE, accent=ORANGE, value_size=30)
add_text(slide, "Commitment ladder", 0.82, 3.37, 3.2, 0.25, 16, NAVY, bold=True)
steps = [("Forecast", 0.85), ("LOI", 2.55), ("iDEX MoQ\nproduction order", 4.05), ("Series\ncontract", 7.1)]
y = 4.05
for i, (label, x) in enumerate(steps):
    fill = GREEN if i == 2 else WHITE
    col = WHITE if i == 2 else NAVY
    width = 1.35 if i != 2 else 2.1
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(width), Inches(0.7))
    set_fill(shp, fill)
    set_line(shp, RGBColor(190, 202, 216), 0.8)
    add_text(slide, label, x + 0.07, y + 0.17, width - 0.15, 0.33, 10.5, col, bold=True, align="center")
    if i < len(steps) - 1:
        x1 = x + width + 0.05
        line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(x1), Inches(y + 0.35), Inches(steps[i + 1][1] - 0.08), Inches(y + 0.35))
        line.line.color.rgb = MUTED
        line.line.width = Pt(1.5)
add_text(slide, "We are here", 4.48, 4.85, 1.25, 0.22, 10, GREEN_DARK, bold=True, align="center")
add_text(slide, "Why it matters", 8.55, 3.37, 2.2, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Turns Year 1 into a revenue + gross-profit year.",
        "Funds M1-M5 industrialisation in parallel.",
        "Explains why equity rounds step down, not up.",
    ],
    8.60,
    3.86,
    3.55,
    1.1,
    font_size=11.8,
    gap=0.39,
)
add_quote(slide, "Live risk: Phase-1 to Phase-2 / series conversion timing; tracked against Series B sizing.", 0.82, 5.95, 11.45, 0.55)
add_footer(slide, 5)
add_notes(slide, "Do not oversell. This is above forecast/LOI and is production-order revenue, but conversion timing remains a named risk.")
slide_records.append(("Day-1 traction", "Rs.105 Cr opening order book, firm Rs.210 Cr ESM MoQ."))

# 6 Product portfolio
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Six product lines, one platform", "A staged portfolio across air, land, sea and cyber/AI.", kicker="Portfolio")
add_simple_table(slide, [["Code", "Product", "First ship", "Strategic role"]] + product_lines, 0.65, 1.35, 6.35, 4.6, col_widths=[0.7, 2.2, 1.0, 2.45], font_size=9.4)
add_text(slide, "Launch wave", 7.45, 1.38, 2.0, 0.25, 16, NAVY, bold=True)
wave_data = [
    ("Year 1", "V2 ESM + V6 AI", GREEN),
    ("Year 2", "V1 AESA + V3 C-UAS", CYAN),
    ("Year 3", "V5 AUV / USV", ORANGE),
    ("Year 4+", "V4 MALE UAS + exports", BLUE),
]
for i, (yr, txt, col) in enumerate(wave_data):
    y = 1.85 + i * 0.82
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(7.45), Inches(y), Inches(4.45), Inches(0.58))
    set_fill(shp, WHITE)
    set_line(shp, RGBColor(216, 224, 235), 0.8)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(7.45), Inches(y), Inches(0.08), Inches(0.58))
    set_fill(bar, col)
    add_text(slide, yr, 7.65, y + 0.11, 0.9, 0.22, 11, col, bold=True)
    add_text(slide, txt, 8.55, y + 0.11, 2.9, 0.22, 11.3, NAVY, bold=True)
add_quote(slide, "The portfolio is sequenced so early ESM + AI cash de-risks longer-cycle AESA, maritime autonomy and MALE UAS.", 7.45, 5.35, 4.45, 0.85)
add_footer(slide, 6)
add_notes(slide, "Avoid reading every row. The story is sequencing: short-cycle ESM/AI first, heavy programs later.")
slide_records.append(("Portfolio", "V1-V6 product lines and first ship timing."))

# 7 Roadmap
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_title(slide, "10-year roadmap: staged risk, staged capital", "Qualification and production gates are intentionally sequenced.", dark=True, kicker="Roadmap")
add_full_bleed_image(slide, IMG["roadmap"], 0.70, 1.35, 7.2, 4.15, border=False)
add_text(slide, "Funding gates are dual-gated", 8.35, 1.45, 3.5, 0.3, 17, WHITE, bold=True)
add_bullet_list(
    slide,
    [
        "Every round requires both platform maturity and contracted backlog.",
        "Seed unlocks M1/M2/M4, ESM MVP and V6 first ship.",
        "Series A unlocks productised platform + Wave 2 contracts.",
        "Series B bridges to FCF-positive in Year 4.",
    ],
    8.38,
    1.95,
    3.65,
    1.55,
    font_size=11.2,
    color=RGBColor(221, 232, 240),
    gap=0.36,
)
add_card(slide, 8.35, 4.25, 3.48, 0.86, "First positive EBITDA / FCF", "Year 4", "Post Wave-4 ramp", fill=RGBColor(11, 38, 60), accent=GREEN, dark=True, value_size=24)
add_card(slide, 8.35, 5.30, 3.48, 0.86, "Peak debt", "Rs.200 Cr", "Repaid by Year 9", fill=RGBColor(11, 38, 60), accent=CYAN, dark=True, value_size=24)
add_footer(slide, 7, dark=True)
add_notes(slide, "Emphasize disciplined sequencing, not 'we will build everything at once.'")
slide_records.append(("Roadmap", "10-year roadmap and dual funding gates."))

# 8 Competitive positioning
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Competitive position: faster than primes, deeper than specialists", "The wedge is the mispriced mid-tier programme segment.", kicker="Moat")
add_full_bleed_image(slide, IMG["scorecard"], 0.65, 1.35, 7.2, 3.75, border=True)
add_text(slide, "What the heatmap is saying", 8.25, 1.42, 3.8, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Tier-1 primes have breadth but slower fielding cycles.",
        "Pure-plays have speed but weaker cross-domain integration.",
        "Nitrodynamics aims to combine breadth, IP ownership and platform reuse.",
        "Cross-domain coverage increases customer expansion paths.",
    ],
    8.30,
    1.86,
    3.65,
    1.4,
    font_size=11.3,
    gap=0.36,
)
add_quote(slide, "Legacy primes sell programs. Point startups sell products. Nitrodynamics sells a reusable platform that keeps spawning programs.", 0.75, 5.65, 11.55, 0.75)
add_footer(slide, 8)
add_notes(slide, "Use this slide to position against categories, not to attack named competitors.")
slide_records.append(("Competitive position", "Heatmap and wedge against primes vs pure-plays."))

# 9 Revenue build
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Revenue build: from Rs.53 Cr to Rs.5,055 Cr", "All six product lines ship concurrently by Year 5.", kicker="Financials")
add_chart_bar(slide, rev_years, rev_vals, 0.70, 1.35, 7.35, 3.65, title="Revenue", color=BLUE)
add_text(slide, "Revenue (Rs.Cr)", 0.72, 1.13, 2.2, 0.25, 11, MUTED, bold=True)
add_text(slide, "Y10 product mix", 8.45, 1.30, 2.7, 0.25, 16, NAVY, bold=True)
colors = [BLUE, GREEN, CYAN, ORANGE, GREEN_DARK, RGBColor(120, 90, 240)]
for i, (name, val) in enumerate(prod_mix_y10):
    y = 1.78 + i * 0.55
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(8.45), Inches(y + 0.08), Inches(val / 1150 * 2.0), Inches(0.18))
    set_fill(bar, colors[i])
    add_text(slide, name, 10.65, y, 1.3, 0.22, 9.8, NAVY, bold=True)
    add_text(slide, f"{val:,}", 11.70, y, 0.6, 0.22, 9.8, MUTED, align="right")
add_text(slide, "Rs.Cr", 11.75, 1.52, 0.55, 0.18, 7.5, MUTED, align="right")
add_quote(slide, "Closing backlog reaches Rs.16,680 Cr by Year 10 - more than 3.3x forward revenue cover.", 0.75, 5.75, 11.55, 0.65)
add_footer(slide, 9)
add_notes(slide, "This is the growth slide. Anchor the scale: Y10 Rs.5,055 Cr with backlog cover.")
slide_records.append(("Revenue build", "Y1-Y10 revenue and Y10 product mix."))

# 10 Margin engine
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Margin engine: reuse converts engineering into economics", "Hardware learning + platform reuse + software mix drive the gross-margin bridge.", kicker="Unit economics")
add_chart_line(slide, rev_years, {"Gross margin %": gm_vals}, 0.72, 1.35, 6.0, 3.4, [GREEN])
add_text(slide, "Blended gross margin trajectory", 0.72, 1.12, 3.0, 0.25, 11, MUTED, bold=True)
add_card(slide, 7.30, 1.45, 2.05, 1.05, "Y1 GM", "~51%", "base year", fill=WHITE, accent=ORANGE, value_size=26)
add_card(slide, 9.65, 1.45, 2.05, 1.05, "Y10 GM", "~67%", "reuse maturity", fill=WHITE, accent=GREEN, value_size=26)
add_card(slide, 7.30, 2.82, 2.05, 1.05, "Y10 EBITDA", "Rs.2,347 Cr", "46.4% margin", fill=WHITE, accent=CYAN, value_size=20)
add_card(slide, 9.65, 2.82, 2.05, 1.05, "V6 AI GM", "93-94%", "software attach", fill=WHITE, accent=BLUE, value_size=23)
add_text(slide, "Three margin levers", 0.82, 5.15, 2.6, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Wright's-law learning lowers hardware BoM as production doubles.",
        "Qualified platform blocks reduce duplicated NRE and integration cost.",
        "Military AI software grows as an attach layer across hardware sales.",
    ],
    0.88,
    5.58,
    6.6,
    1.0,
    font_size=11.6,
    gap=0.34,
)
add_footer(slide, 10)
add_notes(slide, "Use 'engineering into economics' as the soundbite. The 46.4% EBITDA margin is the payoff.")
slide_records.append(("Margin engine", "Gross margin trajectory and EBITDA margin drivers."))

# 11 Cash flow and FCF
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_title(slide, "Cash flow turns in Year 4, then compounds hard", "The trough is funded by staged equity and modest debt.", dark=True, kicker="Cash flow")
add_full_bleed_image(slide, IMG["fcf_waterfall"], 0.72, 1.35, 5.9, 3.5, border=False)
add_text(slide, "Annual FCF (Rs.Cr)", 7.05, 1.36, 2.2, 0.25, 13, RGBColor(218, 229, 238), bold=True)
maxv = 1600
zero = 3.85
for i, (yr, val) in enumerate(zip(rev_years, fcf_vals)):
    x = 7.00 + i * 0.48
    if val >= 0:
        bh = val / maxv * 2.15
        y = zero - bh
        col = GREEN
    else:
        bh = abs(val) / 250 * 0.55
        y = zero
        col = RED
    shp = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.28), Inches(max(0.03, bh)))
    set_fill(shp, col)
    add_text(slide, yr, x - 0.02, 4.08, 0.34, 0.16, 6.8, RGBColor(201, 213, 225), align="center")
line = slide.shapes.add_connector(MSO_CONNECTOR.STRAIGHT, Inches(6.95), Inches(3.85), Inches(11.90), Inches(3.85))
line.line.color.rgb = RGBColor(107, 122, 139)
line.line.width = Pt(1)
add_card(slide, 7.05, 5.02, 2.15, 0.86, "10-year cumulative FCF", "Rs.4,803 Cr", "", fill=RGBColor(11, 38, 60), accent=GREEN, dark=True, value_size=21)
add_card(slide, 9.55, 5.02, 2.15, 0.86, "FCF positive", "Year 4", "", fill=RGBColor(11, 38, 60), accent=CYAN, dark=True, value_size=21)
add_footer(slide, 11, dark=True)
add_notes(slide, "Be crisp: cash is negative through Y3, turns in Y4, then funds scale and debt repayment.")
slide_records.append(("Cash flow", "FCF waterfall and annual FCF turning positive in Y4."))

# 12 Funding ask
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Funding ask: Rs.1,100 Cr staged equity, led by Seed Rs.450 Cr", "Capital is milestone-gated to platform maturity and contracted backlog.", kicker="Capital")
rounds = [
    ("Seed", "Y1", "Rs.450 Cr", "M1-M5 platform; ESM industrialisation; first production line", GREEN),
    ("Series A", "Y2", "Rs.400 Cr", "ESM/C-UAS/AI scale-up; AESA prototype; EMI/anechoic facility", CYAN),
    ("Series B", "Y3", "Rs.250 Cr", "AESA, MALE and autonomy first deliveries; bridge to FCF-positive Y4", ORANGE),
]
for i, (r, yr, amt, use, col) in enumerate(rounds):
    x = 0.76 + i * 4.05
    add_card(slide, x, 1.43, 3.55, 1.38, f"{r} ({yr})", amt, use, fill=WHITE, accent=col, value_size=27)
add_full_bleed_image(slide, IMG["funding_cash"], 0.75, 3.25, 5.95, 2.6, border=True)
add_text(slide, "Use-of-proceeds logic", 7.20, 3.28, 2.6, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Seed is the lead ask: Rs.450 Cr.",
        "Equity rounds step down as ESM and platform reuse de-risk the next wave.",
        "Peak debt Rs.200 Cr; fully repaid by Year 9.",
        "Pre-money valuations are illustrative unless separately confirmed.",
    ],
    7.25,
    3.75,
    4.55,
    1.38,
    font_size=11.5,
    gap=0.36,
)
add_footer(slide, 12)
add_notes(slide, "Important caution: valuations in the business plan are analyst illustrations, not founder-confirmed. Keep ask focused on round sizes and gates.")
slide_records.append(("Funding ask", "Seed 450, Series A 400, Series B 250; staged equity and peak debt."))

# 13 Returns
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Returns: venture-scale upside from defense-prime economics", "Base case clears high-growth return thresholds before terminal optionality.", kicker="Investor returns")
add_card(slide, 0.75, 1.45, 2.55, 1.25, "Project IRR", "31.9%", "10-year FCF basis", fill=WHITE, accent=GREEN, value_size=32)
add_card(slide, 3.55, 1.45, 2.55, 1.25, "NPV @ 18% WACC", "Rs.747 Cr", "base FCF NPV", fill=WHITE, accent=CYAN, value_size=27)
add_card(slide, 6.35, 1.45, 2.55, 1.25, "Y10 EV range", "Rs.20k-35k Cr", "triangulated", fill=WHITE, accent=ORANGE, value_size=21)
add_card(slide, 9.15, 1.45, 2.55, 1.25, "Seed Y9 case", "10.6x MoIC", "illustrative exit case", fill=WHITE, accent=BLUE, value_size=24)
exit_data = [
    ["Round", "Post-B stake", "Y7 exit", "Y9 exit", "Y11 exit"],
    ["Seed", "17.8%", "6.2x / 30% IRR", "10.6x / 33%", "15.8x / 30%"],
    ["Series A", "7.9%", "3.1x / 25%", "5.3x / 28%", "7.9x / 25%"],
    ["Series B", "3.0%", "1.9x / 17%", "3.2x / 22%", "4.8x / 22%"],
]
add_simple_table(slide, exit_data, 0.75, 3.25, 6.8, 1.75, col_widths=[1.25, 1.2, 1.45, 1.45, 1.45], font_size=8.8)
add_text(slide, "Y10 terminal framing", 8.10, 3.25, 3.2, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "EV/EBITDA 15x midpoint: Rs.35,205 Cr.",
        "EV/Revenue 4.5x midpoint: Rs.22,748 Cr.",
        "Triangulated range: ~Rs.20,000-35,000 Cr.",
    ],
    8.15,
    3.72,
    4.1,
    1.05,
    font_size=11.2,
    gap=0.36,
)
add_text(slide, "Note: exit cases and pre-money values are scenario illustrations, not confirmed financing terms.", 0.78, 6.12, 10.5, 0.24, 8.3, MUTED, italic=True)
add_footer(slide, 13)
add_notes(slide, "Keep 'illustrative' language. Do not present valuation as a committed round term.")
slide_records.append(("Returns", "IRR, NPV, terminal valuation and round return scenarios."))

# 14 Sensitivity and risk
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_title(slide, "Sensitivity: the risk map is known and manageable", "The biggest variables are working capital, BoM learning and customer advances.", dark=True, kicker="Risk")
add_full_bleed_image(slide, IMG["tornado"], 0.70, 1.30, 6.5, 3.65, border=False)
add_text(slide, "Top named risks", 7.65, 1.38, 3.4, 0.28, 17, WHITE, bold=True)
risks = [
    ("MoD concentration", "Mitigated by six-product diversification + allied export pipeline."),
    ("Long DSO / BG cash trap", "Modelled with customer advances, WC bridge and collateral schedule."),
    ("Hardware qualification slips", "Dedicated certification team, partner labs, MVP-first releases."),
    ("Export-control friction", "Dual ITAR-clean / EAR99 variants from Day 1."),
]
for i, (r, m) in enumerate(risks):
    y = 1.85 + i * 0.78
    add_text(slide, r, 7.70, y, 3.5, 0.20, 11.5, GREEN, bold=True)
    add_text(slide, m, 7.70, y + 0.25, 4.25, 0.30, 9.4, RGBColor(218, 229, 238))
add_quote(slide, "Bad decks hide risk. Good decks price it, gate it and show the owner. This plan does the adult version.", 0.78, 5.55, 11.35, 0.72, dark=True)
add_footer(slide, 14, dark=True)
add_notes(slide, "The sensitivity slide builds trust. Say which risks move valuation and how management controls them.")
slide_records.append(("Risk and sensitivity", "Tornado and top residual risks."))

# 15 Operating model
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Operating model: platform core + product squads", "Centralised reusable modules, decentralised product execution.", kicker="Execution")
add_full_bleed_image(slide, IMG["org"], 0.65, 1.28, 7.4, 3.55, border=True)
add_text(slide, "Execution principles", 8.40, 1.35, 3.1, 0.25, 16, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Platform engineering owns M1-M5 reusable blocks.",
        "Product squads own V1-V6 delivery and field feedback.",
        "Compliance, finance and export controls scale as shared services.",
        "Headcount grows from 91 in Y1 to ~543 by Y10.",
    ],
    8.45,
    1.80,
    3.55,
    1.35,
    font_size=11.3,
    gap=0.36,
)
facility_data = [
    ("Y1-Y2", "Partner labs + asset-light"),
    ("Y3", "Anechoic / EMI / SMT ramp"),
    ("Y4", "UAS hangar"),
    ("Y5+", "Maritime tank + export scale"),
]
for i, (yr, txt) in enumerate(facility_data):
    add_pill(slide, f"{yr}: {txt}", 0.75 + i * 3.05, 5.45, 2.65, 0.43, fill=PALE, color=NAVY, font_size=8.7)
add_footer(slide, 15)
add_notes(slide, "Do not over-explain the org chart. The message is modular execution: platform core and product squads.")
slide_records.append(("Operating model", "Org model and facilities ramp."))

# 16 Governance and compliance
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Governance, compliance and IP are designed in early", "Defense buyers underwrite process maturity as much as product performance.", kicker="Trust architecture")
board_data = [
    ["Stage", "Board shape"],
    ["Post-Seed", "5 seats: chair, 2 founders, 1 investor, 1 independent"],
    ["Post-A", "7 seats: 2 investors, 2 independents"],
    ["Post-B", "8 seats: 3 investors, 2 independents"],
]
add_simple_table(slide, board_data, 0.75, 1.45, 5.4, 1.95, col_widths=[1.45, 3.95], font_size=9.2)
comp = [
    ("Quality", "AS9100 + CMMI L3", "Defense-grade delivery discipline"),
    ("Cyber", "CMMC L3", "Secure software and data handling"),
    ("Export", "SCOMET / ITAR / EAR", "Dual exportable variants from Day 1"),
    ("IP", "Platform-owned modules", "Reusable source and data-rights strategy"),
]
for i, (a, b, c) in enumerate(comp):
    x = 6.75 + (i % 2) * 2.75
    y = 1.45 + (i // 2) * 1.18
    add_card(slide, x, y, 2.45, 0.92, a, b, c, fill=WHITE, accent=[GREEN, CYAN, ORANGE, BLUE][i], value_size=13.5, title_size=8.5)
add_quote(slide, "Investor diligence question: can this company sell to MoD and allied governments repeatedly? This is the control system for yes.", 0.78, 4.55, 11.35, 0.75)
add_text(slide, "Core message", 0.82, 5.70, 1.5, 0.22, 13, NAVY, bold=True)
add_bullet_list(
    slide,
    [
        "Compliance is budgeted, governed and assigned - not left as later.",
        "Source-code and platform IP ownership defend both MoD preference and export optionality.",
    ],
    2.10,
    5.70,
    8.6,
    0.65,
    font_size=11.2,
    gap=0.34,
)
add_footer(slide, 16)
add_notes(slide, "Use this to lower perceived institutional risk. Defense investors care deeply about governance and export controls.")
slide_records.append(("Governance and compliance", "Board, compliance architecture and IP ownership."))

# 17 KPI dashboard
slide = prs.slides.add_slide(blank)
add_bg(slide)
add_title(slide, "Investor dashboard: the KPIs that prove the model", "The board should watch growth, profitability, capital efficiency and platform reuse.", kicker="Measurement")
kpi = [
    ("Growth", "Revenue, backlog, book-to-bill, export %", GREEN),
    ("Profitability", "Gross margin, EBITDA, FCF, cumulative FCF", CYAN),
    ("Capital efficiency", "ROIC, NWC/revenue, BG collateral, debt/equity", ORANGE),
    ("Platform execution", "Reuse %, NRE avoided, qualification schedule, RPE", BLUE),
]
for i, (tier, txt, col) in enumerate(kpi):
    x = 0.78 + (i % 2) * 5.9
    y = 1.45 + (i // 2) * 1.62
    shp = slide.shapes.add_shape(MSO_SHAPE.ROUNDED_RECTANGLE, Inches(x), Inches(y), Inches(5.25), Inches(1.18))
    set_fill(shp, WHITE)
    set_line(shp, RGBColor(216, 224, 235), 0.8)
    bar = slide.shapes.add_shape(MSO_SHAPE.RECTANGLE, Inches(x), Inches(y), Inches(0.07), Inches(1.18))
    set_fill(bar, col)
    add_text(slide, tier, x + 0.24, y + 0.20, 2.5, 0.26, 16, NAVY, bold=True)
    add_text(slide, txt, x + 0.24, y + 0.62, 4.6, 0.28, 10.5, SLATE)
for i, (title, value, note) in enumerate(
    [
        ("Y10 revenue", "Rs.5,055 Cr", "monthly"),
        ("Y10 backlog", "Rs.16,680 Cr", "monthly"),
        ("Y10 revenue / employee", "Rs.9.3 Cr", "quarterly"),
        ("Y10 reuse", "97-99%", "quarterly"),
    ]
):
    add_card(slide, 0.78 + i * 3.05, 5.02, 2.55, 0.92, title, value, note, fill=WHITE, accent=[GREEN, CYAN, ORANGE, BLUE][i], value_size=19)
add_footer(slide, 17)
add_notes(slide, "End diligence section by showing how management will report progress and catch slips early.")
slide_records.append(("KPI dashboard", "Four-tier investor reporting dashboard."))

# 18 Close
slide = prs.slides.add_slide(blank)
add_bg(slide, dark=True)
add_text(slide, "The ask", 0.70, 0.74, 2.5, 0.35, 18, GREEN, bold=True)
add_text(slide, "Lead the Seed: Rs.450 Cr", 0.68, 1.32, 7.5, 0.75, 38, WHITE, bold=True)
add_text(
    slide,
    "To industrialise the M1-M5 platform, deliver the ESM cash engine, launch Military AI, and unlock Wave 2 product scale.",
    0.72,
    2.25,
    8.2,
    0.72,
    17,
    RGBColor(218, 229, 238),
)
for i, (title, value, note) in enumerate(
    [
        ("Day-1 traction", "Rs.105 Cr", "opening order book"),
        ("Y10 revenue", "Rs.5,055 Cr", "multi-domain prime"),
        ("Y10 EBITDA", "Rs.2,347 Cr", "46.4% margin"),
        ("IRR", "31.9%", "base case"),
    ]
):
    add_card(slide, 0.78 + i * 3.05, 4.15, 2.65, 1.05, title, value, note, fill=RGBColor(11, 38, 60), accent=[GREEN, CYAN, ORANGE, BLUE][i], dark=True, value_size=22)
add_quote(slide, "Nitrodynamics is built to be India's reusable defense platform - one engineering base, six product lines, four domains.", 1.55, 5.75, 10.0, 0.72, dark=True)
add_footer(slide, 18, dark=True)
add_notes(slide, "Close by repeating the same narrative spine: revenue traction, reusable platform, disciplined capital, venture-scale upside.")
slide_records.append(("Close", "Seed Rs.450 Cr ask and narrative recap."))

prs.core_properties.title = "Nitrodynamics Investor Presentation V1"
prs.core_properties.subject = "Converted from Nitrodynamics Business Plan V4 final"
prs.core_properties.author = "Caravaggio / BMAD Presentation Master"
prs.core_properties.comments = "Generated from investor_plan/Nitrodynamics_Business_Plan_V4_final.docx and project-context.md SOT."
prs.save(PPTX_PATH)

lines = [
    "# Nitrodynamics Investor Presentation V1 - Deck Outline",
    "",
    "Generated from `investor_plan/Nitrodynamics_Business_Plan_V4_final.docx` with `project-context.md` as the single source of truth.",
    "",
    "## Slide list",
]
for i, (title, summary) in enumerate(slide_records, start=1):
    lines.append(f"{i}. **{title}** - {summary}")
lines.extend(
    [
        "",
        "## Source discipline / caveats",
        "- Currency is INR Crore (Rs.Cr) unless otherwise noted.",
        "- The ESM MoQ is treated per SOT D-012: Rs.210 Cr = 10 systems x Rs.21 Cr; Phase 1 = Rs.105 Cr opening order book.",
        "- iDEX/TDF/Make-II grants are excluded from the base case and framed only as upside.",
        "- Pre-money valuations and some exit cases are scenario illustrations; confirm before presenting as financing terms.",
    ]
)
OUTLINE_PATH.write_text("\n".join(lines), encoding="utf-8")

print(PPTX_PATH)
print(OUTLINE_PATH)
