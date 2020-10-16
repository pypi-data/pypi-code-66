def not_allowed():
    return "", 405

def preflight():
    return "", 204, {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "GET",
        "Access-Control-Allow-Headers": "Content-Type",
        "Access-Control-Max-Age": "3600"
    }

class Endpoint:
    http_verbs = ["get", "head", "post", "put", "delete", "connect", "options",
                  "trace", "patch"]

    def __init__(self, request):
        self.headers = request.headers
        self.args = request.args
        self.body = request.get_json(silent=True)
        self.parameters = {}

    @classmethod
    def handle(cls, method):
        method = method.lower()

        if method == "options":
            return preflight

        methods = ([f for f in dir(cls) if f in cls.http_verbs])
        if method not in methods:
            return not_allowed

        return getattr(cls, method)
