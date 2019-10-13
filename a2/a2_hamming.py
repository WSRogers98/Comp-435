

def hammingdistance(hex1, hex2):
    count = 0
    ham = int(hex1, 16) ^ int(hex2, 16)
    while ham:
        count += (ham % 2)
        # Bitwise shift through bits
        ham = ham >> 1
    return count
