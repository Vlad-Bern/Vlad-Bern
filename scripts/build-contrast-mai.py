"""Produce one Mai PNG legible on light and dark GitHub themes.

Uses the exact uploaded PNG as source, without resizing or resampling.
The original black ink is preserved. A soft, narrow off-white
backing sits behind the strokes for contrast on dark backgrounds.
"""
from pathlib import Path
from PIL import Image, ImageFilter

original = Path("assets/Mai-black-lines.png")
destination = Path("assets/mai-visible-both.png")
image = Image.open(original).convert("RGBA")
mask = image.getchannel("A")
backing_mask = mask.filter(ImageFilter.MaxFilter(9))
backing = Image.new("RGBA", image.size, (239, 236, 244, 0))
backing.putalpha(backing_mask)
backing.alpha_composite(image)
backing.save(destination, optimize=True)
print(f"Built {destination}: {image.width}x{image.height}, black original over light outline")
