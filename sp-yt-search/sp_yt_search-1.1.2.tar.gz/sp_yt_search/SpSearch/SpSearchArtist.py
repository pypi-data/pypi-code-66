import copy

from .Sp import Sp
from .SpSearchAlbum import SpSearchAlbum
from .SpObjects import GenericObj


class SpSearchArtist(Sp):
    def __init__(self, artist_id):
        self.artist_id = artist_id
        super(SpSearchArtist, self).__init__()

    def search(self):
        artist = self.client.artist(self.artist_id)
        artist_albums = self.client.artist_albums(self.artist_id)
        artist['albums'] = list()

        while True:
            for item in artist_albums['items']:
                artist['albums'].append(SpSearchAlbum(item['id']))

            if artist_albums['next'] is None:
                break
            artist_albums = self.client.next(artist_albums)

        return artist

    def parse(self):
        generic = copy.deepcopy(self.data)
        generic['tracks'] = []

        for album in generic['albums']:
            generic['tracks'].extend(album.parse()['tracks'])

        return GenericObj(generic).__dict__
