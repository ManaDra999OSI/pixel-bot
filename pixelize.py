from PIL import Image
import io

def pixelate_image(image_bytes, pixel_size=10):
    img = Image.open(io.BytesIO(image_bytes))
    w, h = img.size
    img_small = img.resize((max(1, w // pixel_size), max(1, h // pixel_size)), resample=Image.NEAREST)
    img_pixelated = img_small.resize((w, h), Image.NEAREST)
    output = io.BytesIO()
    img_pixelated.save(output, format='PNG')
    return output.getvalue()