
def encode_rail_fence_cipher(message, rails):
    fence = {}
    for rail in range(rails):
        fence[rail] = ""
    rail = 0
    down = True
    for item in message:
        fence[rail] += item
        if down:
            rail += 1
        else:
            rail -= 1
        if rail % (rails - 1) == 0 :
            down = not down
    result = ""
    for value in fence.values():
        result += value
    return result

def decode_rail_fence_cipher(message, rails):
    fence = { rails: 0 for rails in range(rails) }
    for n in range(rails):
        k = (2 * (rails - 1)) - (n * 2)
        m = n * 2
        message_length = len(message) - n
        i = 0
        Up = True
        if n == 0:
            fence[n] = message_length // k
            continue
        if n == rails - 1:
            fence[n] = message_length // m
            continue
        while i < message_length:
            if (Up and i % k == 0) or (not Up and i % m == 0):
                fence[n] += 1
                Up = not Up
            i += 1
    print(fence)

decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 4)
                

            
            
        
        
