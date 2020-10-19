import sys
import random
from .utils import getSalt, reverseString, b64, getType
from .exceptions import *

class Garuda45:
    def __init__(self):
        super().__init__()

        self.salt = getSalt(3)
        self.type = getType("Garuda45")
        self.output = ""

    @property
    def show(self):
        print (self.output)

    @property
    def result(self):
        return self.output

    def encrypt(self, s=""):
        if s == "":
            raise G30SValueError("Unknown error, please read a document")
        reverse = reverseString(s)
        encToB64 = b64(reverse.encode()).decode()
        results = self.salt + encToB64 + self.type + str(len(self.salt))
        self.output = results

class Garuda1945:
    def __init__(self):
        super().__init__()

        self.string = ""
        self.output = ""
        self.type = getType("Garuda1945")
        self.salt = getSalt(10, "=")
        self.rand = random.randint(1, len(self.string) + 10)

    @property
    def show(self):
        print (self.output)
    
    @property
    def result(self):
        return self.output

    def encrypt(self, s=""):
        self.string = s
        if s == "":
            raise G30SValueError("Unknown error, please read a document")
        num = [x for x in range(self.rand)]
        enc = b64(s.encode()).decode()
        word = ""
        for x in enc:
            word += b64(x.encode()).decode()[0]
        results = self.salt + word + self.type + str(len(self.salt))
        self.output = results
