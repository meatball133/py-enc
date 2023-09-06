def get_pixels(image, width, height):
    for n in range(width):
        for m in range(height):
            yield image.getpixel((n, m))
