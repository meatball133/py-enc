def get_pixels(width, height):
    for n in range(width):
        for m in range(height):
            yield (n, m)

def get_rail_fence_pixels(width, height, rail_fence_height):
    for n in range(width):
        for m in range(height):
            if m % (rail_fence_height * 2 - 2) == n % (rail_fence_height * 2 - 2):
                yield (n, m)

def put_least_significant_bit(pixel, letter):
    numeric = ord(letter)
    if ord > 2 ** 8:
        raise ValueError("The letter is too big")
    binary = reversed(bin(numeric)[2:])
    idx = 0
    for bit in binary:
        
        idx += 1
    

