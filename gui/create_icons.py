#!/usr/bin/env python3
"""
Convert SVG icon to PNG and ICO formats for ASK GUI
"""

import sys
from pathlib import Path

try:
    from PIL import Image, ImageDraw, ImageFont
except ImportError:
    print("PIL not installed. Install with: pip install Pillow")
    sys.exit(1)

def create_ask_icon():
    """Create ASK icon with pure Python (no SVG conversion needed)"""
    
    # Create image with dark background
    size = 256
    img = Image.new('RGBA', (size, size), color=(13, 13, 13, 255))
    draw = ImageDraw.Draw(img)
    
    # Colors
    purple = (124, 58, 237, 255)
    light_purple = (167, 139, 250, 255)
    white = (255, 255, 255, 255)
    
    # Draw rounded background
    padding = 10
    draw.rectangle(
        [(padding, padding), (size - padding, size - padding)],
        fill=purple,
        outline=white,
        width=2
    )
    
    # Head circle
    head_y = 50
    draw.ellipse(
        [(size//2 - 35, head_y), (size//2 + 35, head_y + 70)],
        fill=light_purple,
        outline=white,
        width=2
    )
    
    # Eyes
    eye_y = head_y + 20
    draw.ellipse([(size//2 - 50, eye_y), (size//2 - 40, eye_y + 10)], fill=white)
    draw.ellipse([(size//2 + 40, eye_y), (size//2 + 50, eye_y + 10)], fill=white)
    
    # Mouth arc
    mouth_y = eye_y + 25
    draw.arc(
        [(size//2 - 30, mouth_y), (size//2 + 30, mouth_y + 20)],
        0, 180,
        fill=white,
        width=3
    )
    
    # Body rectangle
    body_top = head_y + 75
    draw.rectangle(
        [(size//2 - 30, body_top), (size//2 + 30, body_top + 60)],
        fill=light_purple,
        outline=white,
        width=2
    )
    
    # Save as PNG
    png_path = Path(__file__).parent / "ask_icon.png"
    img.save(png_path)
    print(f"✓ Created {png_path}")
    
    # Create ICO version (Windows taskbar)
    ico_path = Path(__file__).parent / "ask_icon.ico"
    # ICO requires specific sizes
    img_ico = img.copy()
    img_ico.thumbnail((128, 128), Image.Resampling.LANCZOS)
    img_ico.save(ico_path)
    print(f"✓ Created {ico_path}")
    
    return str(png_path), str(ico_path)

if __name__ == "__main__":
    create_ask_icon()
