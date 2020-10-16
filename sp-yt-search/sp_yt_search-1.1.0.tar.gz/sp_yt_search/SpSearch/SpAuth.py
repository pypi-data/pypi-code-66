import spotipy
import spotipy.oauth2 as oauth2

from .SpSettings import SpSettings


class SpAuth:
    def __init__(self):
        self.client = self.auth()

    def check_credentials(self):
        return (
                SpSettings().SPOTIPY_CLIENT_ID is None
                and
                SpSettings().SPOTIPY_CLIENT_SECRET is None
        )

    def auth(self):
        if self.check_credentials():
            raise Exception('You need to set your Spotify credentials.')

        auth = oauth2.SpotifyClientCredentials(
            client_id=SpSettings().SPOTIPY_CLIENT_ID,
            client_secret=SpSettings().SPOTIPY_CLIENT_SECRET
        )

        token = auth.get_access_token()
        return spotipy.Spotify(auth=token)
