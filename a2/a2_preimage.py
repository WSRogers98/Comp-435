
import hashlib
import string
import random

# create string of length N
def ranstring(len):
    str = string.ascii_lowercase
    finalstr = ''.join(random.choice(str) for num in range(len))
    return finalstr


# create hash of string
def ranhash(str):
    thisStr = str.encode(encoding='ascii')
    hash = hashlib.sha256(thisStr).digest()
    return hash


# find a string with first n bits matching
def find_preimage(target, n):
    str = ranstring(32)
    hash = ranhash(str)
    count = 0
    # loop until match
    while hash[:n] != target[:n]:
        str = ranstring(32)
        hash = ranhash(str)
        count += 1
    return str

