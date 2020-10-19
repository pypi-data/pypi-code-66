import random
from base64 import b64encode

def getSalt(max=10, rplc="-"):
    loop = random.randint(1, max)
    words = list("abcdefghijklmnopqrstuvwxyz1234567890")
    word = ""
    for _ in range(loop):
        get = random.choice(words)
        word += "".join([get.upper() if random.randint(0,1) == 1 else get.lower()])
    encrypted = reverseString(b64(word.encode()).decode()).replace("=", rplc)
    return encrypted

def getType(type):
    return "".join([reverseString(type).lower() if random.randint(0,1) == 0 else reverseString(type).upper()])

def b64(s):
    return b64encode(s)

def reverseString(string=""):
    return "".join(reversed(string))