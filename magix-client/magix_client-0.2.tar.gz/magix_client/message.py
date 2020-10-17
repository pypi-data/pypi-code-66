import json


def toMessage(dict):
    return Message(id=dict["id"], origin=dict["origin"], parentId=dict["parentId"], target=dict["target"],
                   user=dict["user"], action=dict["action"], payload=dict["payload"])


def fromJson(jsonStr):
    return json.loads(jsonStr, object_hook=toMessage)


class Message:
    """Waltz-Controls Message as defined in RFC-1
    """

    # TODO payload hook
    def __init__(self, id, origin, parentId=None, target=None, user=None, action=None, payload=None):
        self.id = id
        self.origin = origin
        self.parentId = parentId
        self.target = target
        self.user = user
        self.action = action
        self.payload = payload
