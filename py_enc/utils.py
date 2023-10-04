def get_pixels(width, height):
    for n in range(width):
        for m in range(height):
            yield (n, m)
