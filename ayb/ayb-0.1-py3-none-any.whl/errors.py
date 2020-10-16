class APIError(Exception):
    pass

class InvalidBot(APIError):
    def __init__(self, id_):
        self.id = id_

class InvalidCategory(APIError):
    def __init__(self, id_):
        self.id = id_