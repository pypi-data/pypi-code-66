class GenericObj:
    def __init__(self, obj):
        self.type = obj['type']
        self.id = obj['id']
        self.uri = obj['uri']
        self.tracks = obj['tracks']


class GenericAlbumObj:
    def __init__(self, album):
        self.id = album['id']
        self.uri = album['uri']
        self.name = album['name']
        self.release_date = album['release_date']


class GenericArtistsObj:
    def __init__(self, artists):
        self.data = []
        for artist in artists:
            temp = {'id': artist['id'], 'uri': artist['uri'], 'name': artist['name']}
            self.data.append(temp)


class GenericTrackObj:
    def __init__(self, track):
        self.type = track['type']
        self.id = track['id']
        self.uri = track['uri']
        self.name = track['name']
        self.duration_ms = track['duration_ms']
        self.artists = GenericArtistsObj(track['artists']).data
        self.album = GenericAlbumObj(track['album']).__dict__
        self.full_name = ', '.join(
            [str(elem['name']) for elem in track['artists']]) + f" - {track['name']}"
        self.duration = int(track['duration_ms'] / 1000)

        self.is_remix = 'remix' in track['name'].lower()
        self.is_instrumental = 'instrumental' in track['name'].lower()
        self.is_live = 'live' in track['name'].lower()
        self.is_official = not self.is_remix and not self.is_instrumental
