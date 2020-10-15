import re
import json
import requests
from clearmacro.errors import ResponseError
from clearmacro.configuration import Configuration
from clearmacro.events import Events
from clearmacro.operations import Operations
from clearmacro.version import VERSION


class Client(Events, Operations):
    configuration = None

    user_agent = 'ClearMacro/python@{}'.format(VERSION)

    def __init__(self, **configuration_overrides):
        super().__init__()
        self.configuration = Configuration(**configuration_overrides)
        self.on("request", lambda req: self.configuration.logger.debug('Request: %s', req))
        self.on("response", lambda res: self.configuration.logger.debug('Request: %s', res))
        self.on("error", lambda err: self.configuration.logger.error(err))
        self.configuration.credentials = self.login(self.configuration.username, self.configuration.password)

    def request(self, path, method, **params):
        url = self.build_request_url(path)
        request_params = {**params, **self.configuration.request_params()}
        self.emit('request', {'url': url, **request_params})
        response = self.call_request(url, method, request_params)
        data = response.json()
        self.emit('response', data)
        return data

    def call_request(self, url, method, params={}):
        try:
            request = getattr(requests, method)
            response = request(url, **params)
            if response.status_code == requests.codes.ok:
                return response
            try:
                raise ResponseError(**response.json())
            except json.decoder.JSONDecodeError:
                raise ResponseError(response, type='network-error')
        except requests.exceptions.Timeout:
            raise ResponseError('Connection timed out', type='timeout')
        except requests.exceptions.RequestException as e:
            raise ResponseError(str(e), type='liberror')

    def build_request_url(self, path):
        request_url = self.configuration.url + path
        safe_request_url = re.sub(r"(?<!:)\/\/", '/', request_url)
        return safe_request_url
