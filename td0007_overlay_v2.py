"""
TD0007 v2: Correct implementation matching reference exactly
Structure:
1. White canvas background
2. Emerald triangle (solid) in upper-left corner
3. Photo diagonally cropped - right side of diagonal line
4. Diagonal line goes from (crop_x, 0) at top to (0, h-bar_h) at bottom
   → photo's diagonal cut MEETS the bottom teal bar at the left edge
5. Teal bar at bottom (full width)
"""
from PIL import Image, ImageDraw
import requests
from io import BytesIO
import os

ASSETS_DIR = os.path.join(os.path.dirname(__file__), 'ualr_email_automation', 'assets')
TARGET_WIDTH = 600

MINT = (145, 217, 198)        # #91d9c6 from website SVG
WHITE_BG = (255, 255, 255)    # white background
TEAL_BAR = (36, 93, 122)      # #245D7A

hero_images = {
    'hero_accounting.jpg': 'https://ualr.edu/accounting/wp-content/uploads/sites/76/2024/11/business-student-portrait-2-2023.jpg',
    'hero_business_analytics.jpg': 'https://ualr.edu/bis/wp-content/uploads/sites/131/2024/11/biz-portrait-2022_03.jpg',
    'hero_bis.jpg': 'https://ualr.edu/bis/wp-content/uploads/sites/131/2024/11/biz-portrait-2022_03.jpg',
    'hero_economics.jpg': 'https://ualr.edu/economics/wp-content/uploads/sites/93/2024/11/ASBTDC-setups-2021_12.jpg',
    'hero_finance.jpg': 'https://ualr.edu/economics/wp-content/uploads/sites/93/2024/11/business-team-winners1.jpg',
    'hero_intl_business.jpg': 'https://ualr.edu/accounting/wp-content/uploads/sites/76/2024/11/business-student-portrait-2-2023.jpg',
    'hero_management.jpg': 'https://ualr.edu/management/wp-content/uploads/sites/108/2024/11/business-student-portrait-2023.jpg',
    'hero_marketing.jpg': 'https://ualr.edu/business/wp-content/uploads/sites/163/2024/12/BIZ-MBA-portrait-2024_BG_200.jpg',
}


def apply_overlay(photo):
    w, h = photo.size
    bar_h = int(h * 0.08)
    crop_bottom_y = h - bar_h

    # 1. White canvas
    canvas = Image.new('RGB', (w, h), WHITE_BG)
    draw = ImageDraw.Draw(canvas)

    # 2. Mint SVG background (exact website values)
    # SVG polygon: points="40 0 1000 0 1000 1000 240 1000" in 1000x1000 viewBox
    # = (4%, 0) (100%, 0) (100%, 100%) (24%, 100%)
    mint_poly = [
        (int(w * 0.04), 0),
        (w, 0),
        (w, crop_bottom_y),
        (int(w * 0.24), crop_bottom_y),
    ]
    draw.polygon(mint_poly, fill=MINT)

    # 3. Photo with clip-path mask (exact website CSS)
    # clip-path: polygon(20% 0px, 100% 0px, 100% 100%, 0px 100%)
    mask = Image.new('L', (w, h), 0)
    mask_draw = ImageDraw.Draw(mask)
    photo_area = [
        (int(w * 0.20), 0),
        (w, 0),
        (w, crop_bottom_y),
        (0, crop_bottom_y),
    ]
    mask_draw.polygon(photo_area, fill=255)
    canvas.paste(photo, mask=mask)

    # 4. Teal bar at bottom (full width, on top of everything)
    draw = ImageDraw.Draw(canvas)
    draw.rectangle([(0, h - bar_h), (w, h)], fill=TEAL_BAR)

    return canvas


for name, url in hero_images.items():
    print(f"  Processing {name}...")
    resp = requests.get(url, timeout=30)
    resp.raise_for_status()
    img = Image.open(BytesIO(resp.content))

    ratio = TARGET_WIDTH / img.width
    new_h = int(img.height * ratio)
    img = img.resize((TARGET_WIDTH, new_h), Image.LANCZOS)

    result = apply_overlay(img)
    out_path = os.path.join(ASSETS_DIR, name)
    result.save(out_path, 'JPEG', quality=85, optimize=True)

    fsize = os.path.getsize(out_path) / 1024
    print(f"  Saved: {name} ({fsize:.0f}KB)")

print("\nDone!")
