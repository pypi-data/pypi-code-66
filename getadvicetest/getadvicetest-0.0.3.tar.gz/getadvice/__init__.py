import requests 

__version__ = "0.0.3"

__url__ = "https://api.adviceslip.com/advice"

def advice(self, name):
    json_result = requests.get(self.url).json()
    advice_result = json_result["slip"]["advice"]
    return f"{name}, {advice_result}"