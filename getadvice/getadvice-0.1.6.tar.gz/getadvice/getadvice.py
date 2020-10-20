import requests


class MagicEightBall:
    def __init__(self):
        self.name = "RichismakingpartyinMykonos"
        self.url = "https://api.adviceslip.com/advice"

    def advice(self, name):
        json_result = requests.get(self.url).json()
        advice_result = json_result["slip"]["advice"]
        return f"{name}, {advice_result}"

    def getName(self):
        return self.name
