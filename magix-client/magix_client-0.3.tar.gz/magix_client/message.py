import json


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

    @classmethod
    def from_json(cls, data, payload_cls=None):
        result = json.loads(data)
        payload = result.get('payload')
        if payload and payload_cls:
            result['payload'] = payload_cls(**payload)
        return Message(**result)
