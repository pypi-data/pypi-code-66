from .Sp import Sp
from .SpObjects import GenericObj, GenericTrackObj


class SpSearchTrack(Sp):
    def __init__(self, track_id):
        self.track_id = track_id
        super(SpSearchTrack, self).__init__()

    def search(self):
        return self.client.track(self.track_id)

    def parse(self):
        return GenericObj({
            'type': self.data['type'],
            'id': self.data['id'],
            'uri': self.data['uri'],
            'tracks': [GenericTrackObj(self.data).__dict__],
        }).__dict__
