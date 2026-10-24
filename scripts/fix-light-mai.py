from PIL import Image
from pathlib import Path

path = Path("assets/mai-light-new.png")
image = Image.open(path).convert("RGBA")
pixels = image.load()
for y in range(image.height):
    for x in range(image.width):
        r, g, b, alpha = pixels[x, y]
        # Preserve image geometry, do not resize or resample.
        # Increase opacity of faint pencil strokes to make them visible on white.
        if alpha <= 12:
            pixels[x, y] = (0, 0, 0, 0)
        else:
            stronger_alpha = min(255, round((alpha / 255) ** 0.48 * 255))
            pixels[x, y] = (0, 0, 0, stronger_alpha)
image.save(path, optimize=True)

# Trigger GitHub Actions after workflow registration.
