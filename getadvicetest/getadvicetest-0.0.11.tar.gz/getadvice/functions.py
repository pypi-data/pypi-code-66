import requests

class MyClass:

    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"

    def getURL(self):
        return self.url

class Mykonos:

    def __init__(self):
        self.name = "RichismakingpartyinMikonos"
        self.url = "https://api.adviceslip.com/advice"

    def advice(self, name):
        json_result = requests.get(self.url).json()
        advice_result = json_result["slip"]["advice"]
        return f"{name}, {advice_result}"

    def getName(self):
        return self.name