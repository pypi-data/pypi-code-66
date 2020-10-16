import requests
from . import _config as _cfg
from . import bot, category, stats

class Client():
    def __init__(self):
        pass
    
    def fetch_stats(self):
        payload = requests.get(_cfg.get_url("stats")).json()
        _stats = stats.Stats(payload)
        return _stats

    def fetch_bot(self, id_):
        payload = requests.get(_cfg.get_url("bot"), params={"id": id_}).json()
        _bot = bot.Bot(self, payload, id_)
        return _bot

    def fetch_category(self, id_):
        payload = requests.get(_cfg.get_url("category"), params={"id": id_}).json()
        _category = category.Category(payload, id_)
        return _category
