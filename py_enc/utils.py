def get_pixels(width, height):
    for n in range(width):
        for m in range(height):
            yield (n, m)


def insert_data(pixel, data):
    new_pixel = [0, 0, 0, 0]

    data = bin(data)

    i = 0
    while i <= 3:
        pixel_channel = pixel[i]

        # Konverterar data till binärt i en sträng med korrekt antal siffror (8) 
        binary_data = f"0b{"0" * (10 - len(data))}{data[2:]}"
        
        # Plockar ut delen av datan att sätta i varje pixel
        subdata = int((binary_data)[2*i+2 : 2*i+4], 2)

        # Sätter in data
        pixel_channel = pixel_channel >> 2 << 2 
        pixel_channel += subdata
        
        new_pixel[i] = pixel_channel

        i += 1

    return tuple(new_pixel)



