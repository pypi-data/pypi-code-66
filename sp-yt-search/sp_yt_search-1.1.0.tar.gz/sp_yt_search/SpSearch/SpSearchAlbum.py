import copy

from .Sp import Sp
from .SpObjects import GenericObj, GenericTrackObj


class SpSearchAlbum(Sp):
    def __init__(self, album_id):
        self.album_id = album_id
        super(SpSearchAlbum, self).__init__()

    def search(self):
        album = self.client.album(self.album_id)
        album_tracks = self.client.album_tracks(self.album_id)
        album['tracks'] = list()

        while True:
            album['tracks'].extend(album_tracks['items'])
            if album_tracks['next'] is None:
                break
            album_tracks = self.client.next(album_tracks)

        if len(album['tracks']) != album['total_tracks']:
            raise Exception('To Do')

        return album

    def parse(self):
        generic = copy.deepcopy(self.data)

        for ite, track in enumerate(generic['tracks']):
            track['album'] = {}
            track['album']['id'] = generic['id']
            track['album']['uri'] = generic['uri']
            track['album']['name'] = generic['name']
            track['album']['release_date'] = generic['release_date']
            generic['tracks'][ite] = GenericTrackObj(track).__dict__

        return GenericObj(generic).__dict__
