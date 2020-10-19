import requests
import logging
LOG = logging.getLogger(__name__)
class Base(object):
    def __init__(self, url):

        self.BASEURL = url

    def get(self, url, params=""):

        response = requests.get("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), params=params)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()

    def post(self, url, data):

        response = requests.post("{BASEURL}{url}".format(BASEURL=self.BASEURL, url=url), json=data)
        if response.status_code >= 400:
            LOG.warning('create charging_rule error: %s:%s', response.status_code, response.text)
            return None
        return response.json()