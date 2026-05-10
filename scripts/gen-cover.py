#!/usr/bin/env python3
"""Generate Dev.to cover images with consistent branding."""
import argparse
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 640

def hex_to_rgb(h): return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def gradient(draw, w, h, top, bottom):
    tr, tg, tb = hex_to_rgb(top)
    br, bg, bb = hex_to_rgb(bottom)
    for y in range(h):
        r = int(tr + (br - tr) * y / h)
        g = int(tg + (bg - tg) * y / h)
        b = int(tb + (bb - tb) * y / h)
        draw.line([(0, y), (w, y)], fill=(r, g, b))

def gen(title, subtitle, output):
    img = Image.new("RGB", (W, H))
    draw = ImageDraw.Draw(img)
    
    # Background gradient
    gradient(draw, W, H, "1a0a2e", "0d1b3e")
    
    # Accent line
    draw.line([(40, H-80), (W-40, H-80)], fill=hex_to_rgb("00d4ff"), width=1)
    
    # Try system fonts
    try:
        title_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 52)
        sub_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
        small_font = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 16)
    except:
        title_font = ImageFont.load_default()
        sub_font = title_font
        small_font = title_font
    
    # Title (left side, white)
    draw.text((40, 180), title, fill="white", font=title_font)
    
    # Subtitle
    if subtitle:
        draw.text((40, 260), subtitle, fill=(255,255,255,160), font=sub_font)
    
    # Bottom bar text
    draw.text((40, H-55), "@nerudek", fill=(180,180,180), font=small_font)
    draw.text((W-220, H-55), "github.com/nerudek", fill=(180,180,180), font=small_font)
    
    img.save(output, "PNG", optimize=True)
    print(f"✅ {output} ({os.path.getsize(output)//1024}KB)")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--title", required=True)
    parser.add_argument("--subtitle", default="")
    parser.add_argument("--output", default="cover.png")
    args = parser.parse_args()
    gen(args.title, args.subtitle, args.output)
