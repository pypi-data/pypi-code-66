import json

class Sum:
    def __init__(self, num, num1):
        self.num1 = num1
        self.num = num
    def work(self):
        print("Value : "+ str(self.num1 + self.num))
class tr:
    def __init__(self, num, num1):
        self.num1 = num1
        self.num = num
    def work(self):
        print("Value : "+ str(self.num1 - self.num)) 

class multiple:
    def __init__(self, num, num1):
        self.num1 = num1
        self.num = num
    def work(self):
        print("Value : "+ str(self.num1 * self.num)) 

class gsmh:
    def __init__(self, num, num1):
        self.num1 = num1
        self.num = num
    def work(self):
        print("Value : "+ str(self.num1 / self.num)) 