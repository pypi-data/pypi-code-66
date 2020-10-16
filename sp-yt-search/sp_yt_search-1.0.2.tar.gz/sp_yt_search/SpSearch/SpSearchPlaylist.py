import copy

from .Sp import Sp
from .SpObjects import GenericObj, GenericTrackObj


class SpSearchPlaylist(Sp):
    def __init__(self, playlist_id):
        self.playlist_id = playlist_id
        super(SpSearchPlaylist, self).__init__()

    def search(self):
        playlist = self.client.playlist(self.playlist_id)
        playlist['total_tracks'] = playlist['tracks']['total']
        playlist['tracks'] = list()
        response = self.client.playlist_tracks(self.playlist_id)

        while True:
            playlist['tracks'].extend(response['items'])
            if response['next'] is None:
                break
            response = self.client.next(response)

        if len(playlist['tracks']) != playlist['total_tracks']:
            raise Exception('To Do')

        return playlist

    def parse(self):
        generic = copy.deepcopy(self.data)

        for ite, track in enumerate(generic['tracks']):
            generic['tracks'][ite] = GenericTrackObj(track['track']).__dict__

        return GenericObj(generic).__dict__
