from .functions import *
import requests 

__version__ = "0.0.6"

__url__ = "https://api.adviceslip.com/advice"

def advice(name):
    json_result = requests.get(__url__).json()
    advice_result = json_result["slip"]["advice"]
    return f"{name}, {advice_result}"