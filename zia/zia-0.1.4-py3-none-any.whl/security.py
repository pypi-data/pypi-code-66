import logging

from zia import ZiaApiBase


class WhiteList(ZiaApiBase):
    def get(self):
        """
        Gets a list of white-listed URLs
        """
        path = 'security'
        return self._output(self._session.get(path))

    def update(self, urls):
        """
        Updates the list of white-listed URLs
        """
        path = 'security'
        return self._output(self._session.put(path, urls))


class BlackList(ZiaApiBase):
    def get(self):
        """
        Gets a list of black-listed URLs
        """
        path = 'security/advanced'
        return self._output(self._session.get(path))

    def update(self, urls):
        """
        Updates the list of black-listed URLs
        """
        path = 'security/advanced'
        return self._output(self._session.put(path, urls))

    def add(self, urls):
        """
        Adds URLs to the black list
        """
        path = 'security/advanced/blacklistUrls?action=ADD_TO_LIST'
        return self._output(self._session.post(path, urls))

    def remove(self, urls):
        """
        Removes URLs from the black list
        """
        path = 'security/advanced/blacklistUrls?action=REMOVE_FROM_LIST'
        return self._output(self._session.post(path, urls))


class Security(ZiaApiBase):
    def __init__(self, _session, _output_type):
        super().__init__(_session, _output_type)
        self.whitelist = WhiteList(self._session, _output_type)
        self.blacklist = BlackList(self._session, _output_type)


LOGGER = logging.getLogger(__name__)
