import json

from .SpSearch import sp_strategy
from .SpSearch.SpSettings import SpSettings
from .YtSearch import YtSearch


class SpYt:
    def __init__(self):
        self.uri = ''
        self.sp_instance = None

    def set_credentials(self, sp_client_id, sp_client_secret):
        SpSettings().SPOTIPY_CLIENT_ID = sp_client_id
        SpSettings().SPOTIPY_CLIENT_SECRET = sp_client_secret

    def sp_search(self, uri):
        self.uri = uri
        self.sp_instance = sp_strategy(uri)
        return self.get_data()

    def yt_search(self):
        for ite, track in enumerate(self.sp_instance.parsed['tracks']):
            self.sp_instance.parsed['tracks'][ite]['yt'] = YtSearch(track).to_dict()

    def get_data(self):
        return json.dumps(self.sp_instance.parsed)
