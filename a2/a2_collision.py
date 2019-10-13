import hashlib
import random
import string


# create string of length N
def ranstring(len):
    str = string.ascii_lowercase
    finalstr= ''.join(random.choice(str) for num in range(len))
    return finalstr


# create hash of string
def ranhash(str):
    thisStr = str.encode(encoding='ascii')
    hash = hashlib.sha256(thisStr).digest()
    return hash

# searches for two strings where n first bits match
def find_collision(n):
    count = 0
    dict = {}

    while True:
        str2 = ranstring(32)
        hash = ranhash(str2)
        match = str(hash[:n])
        count += 1
        if match in dict:
            return str2, dict[match]
        dict[match] = str2


