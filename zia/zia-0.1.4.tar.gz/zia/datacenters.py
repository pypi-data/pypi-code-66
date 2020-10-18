import logging
from .defaults import ZiaApiBase


class Datacenters(ZiaApiBase):
    def get_all_vips(self):
        path = 'vips?include=all'
        return self._session.get(path)

    def get_all_public_vips(self):
        path = 'vips?include=public'
        return self._session.get(path)

    def get_all_private_vips(self):
        path = 'vips?include=private'
        return self._session.get(path)


LOGGER = logging.getLogger(__name__)
