from __future__ import unicode_literals

import logging
import re

from mopidy import backend
from mopidy.models import Album, Artist, Ref, SearchResult, Track, Image

logger = logging.getLogger(__name__)


class RadioNetLibraryProvider(backend.LibraryProvider):
    root_directory = Ref.directory(uri='radionet:root', name='Radio.net')

    def lookup(self, uri):

        if not uri.startswith('radionet:'):
            return None

        variant, identifier = self.parse_uri(uri)

        if variant == 'station':
            identifier = int(identifier)
            radio_data = self.backend.radionet.get_station_by_id(identifier)

            artist = Artist(name=radio_data.name)

            album = Album(
                artists=[artist],
                name=radio_data.description + ' / ' + radio_data.continent +
                     ' / ' + radio_data.country + ' - ' + radio_data.city,
                uri='radionet:station:%s' % (identifier))

            track = Track(
                artists=[artist],
                album=album,
                name=radio_data.name,
                genre=radio_data.genres,
                comment=radio_data.description,
                uri=radio_data.stream_url)
            return [track]

        return []

    def browse(self, uri):
        self.backend.refresh()

        directories = []
        tracks = []
        variant, identifier = self.parse_uri(uri)
        if variant == 'root':
            if self.backend.radionet.local_stations:
                directories.append(
                    self.ref_directory(
                        "radionet:category:localstations", "Local stations")
                )
            if self.backend.radionet.top_stations:
                directories.append(
                    self.ref_directory(
                        "radionet:category:top100", "Top 100")
                )
            return directories
        elif variant == 'category' and identifier:
            if identifier == "localstations":
                for station in self.backend.radionet.local_stations:
                    tracks.append(self.station_to_ref(station))
            if identifier == "top100":
                for station in self.backend.radionet.top_stations:
                    tracks.append(self.station_to_ref(station))
            tracks.sort(key=lambda ref: ref.name)
            return tracks
        else:
            logger.debug('Unknown URI: %s', uri)
            return []

    def search(self, query=None, uris=None, exact=False):

        result = []

        self.backend.radionet.do_search(' '.join(query['any']))

        for station in self.backend.radionet.search_results:
            result.append(self.station_to_track(station))

        return SearchResult(
            tracks=result
        )

    def get_images(self, uris):
        print("Get images: ")
        print(uris)
        results = {}
        for uri in uris:
            variant, identifier = self.parse_uri(uri)
            if variant != "station":
                continue
            station = self.backend.radionet.get_station_by_id(identifier)
            image = self.station_to_image(station)
            results[uri] = [image]
        return results

    def station_to_ref(self, station):
        return Ref.track(
            uri='radionet:station:%s' % (station.id),
            name=station.name,
        )

    def station_to_track(self, station):
        ref = self.station_to_ref(station)
        return Track(uri=ref.uri, name=ref.name, album=Album(uri=ref.uri, name=ref.name),
                     artists=[Artist(uri=ref.uri, name=ref.name)])

    def station_to_image(self, station):
        if station is not None and "image" in station:
            return Image(uri=station["image"])

    def ref_directory(self, uri, name):
        return Ref.directory(uri=uri, name=name)

    def parse_uri(self, uri):
        result = re.findall(r'^radionet:([a-z]+):?([a-z0-9]+|\d+)?$', uri)
        if result:
            return result[0]
        return None, None
