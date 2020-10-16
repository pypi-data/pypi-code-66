from .SpSearchAlbum import SpSearchAlbum
from .SpSearchArtist import SpSearchArtist
from .SpSearchPlaylist import SpSearchPlaylist
from .SpSearchTrack import SpSearchTrack

TRACK_STRATEGY_NAME = 'track'
PLAYLIST_STRATEGY_NAME = 'playlist'
ALBUM_STRATEGY_NAME = 'album'
ARTIST_STRATEGY_NAME = 'artist'


def sp_strategy(uri):
    strategy_name = list(uri.split(":"))[1]
    resource_id = list(uri.split(":"))[2]

    strategy = None
    if strategy_name == TRACK_STRATEGY_NAME:
        strategy = SpSearchTrack(resource_id)
    if strategy_name == PLAYLIST_STRATEGY_NAME:
        strategy = SpSearchPlaylist(resource_id)
    if strategy_name == ALBUM_STRATEGY_NAME:
        strategy = SpSearchAlbum(resource_id)
    if strategy_name == ARTIST_STRATEGY_NAME:
        strategy = SpSearchArtist(resource_id)

    if strategy is None:
        raise Exception('To Do')

    return strategy
