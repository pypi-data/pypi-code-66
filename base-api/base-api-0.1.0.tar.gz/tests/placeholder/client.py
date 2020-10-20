from baseapi import Client


class PlaceholderClient(Client):
    DEFAULT_URL = 'https://jsonplaceholder.typicode.com'
    DEFAULT_APIS = ('tests.placeholder.todos',)
