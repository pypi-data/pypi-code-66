import requests

class GetAdvice:
    def __init__(self):
        self.url = "https://api.adviceslip.com/advice"

    def advice(self, name):
        json_result = requests.get(self.url).json()
        advice_result = json_result["slip"]["advice"]
        return f"{name}, {advice_result}"