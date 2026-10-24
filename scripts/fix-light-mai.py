from PIL import Image
from pathlib import Path

# Build a fresh, cache-busting black-line image from Mai's current art.
# No scaling, interpolation, blur, or new drawing.
src = Path("assets/mai-light-new.png")
dst = Path("assets/mai-black-opaque.png")
im = Image.open(src).convert("RGBA")
p = im.load()
for y in range(im.height):
    for x in range(im.width):
        a = p[x, y][3]
        # Strong ink while retaining partially transparent edge pixels.
        p[x, y] = (0, 0, 0, 0 if a < 5 else max(160, a))
im.save(dst, "PNG", optimize=True)
print(f"saved {dst}: {im.width}x{im.height}")

# Trigger rebuilt art workflow.
