from dataclasses import dataclass
import json

from hop.models import MessageModel
from hop import plugins


@dataclass
class SNEWSBase(MessageModel):
    """
    Defines a base SNEWS message type.

    """
    message_id: str

    @classmethod
    def load(cls, input_):
        """
        :param input: A serialized json string converted by asdict().
        :return:
        """
        if hasattr(input_, 'read'):
            payload = json.load(input_)
        else:
            payload = json.loads(input_)
        return cls(**payload)


@dataclass
class SNEWSAlert(SNEWSBase):
    """
    Defines a SNEWS alert message.

    """
    sent_time: str
    machine_time: str
    content: str


@dataclass
class SNEWSHeartbeat(SNEWSBase):
    """
    Defines a heartbeat published by a detector.

    """
    detector_id: str
    sent_time: str
    machine_time: str
    location: str
    status: str
    content: str


@dataclass
class SNEWSObservation(SNEWSBase):
    """
    Defines an observation published by a detector.

    """
    detector_id: str
    sent_time: str
    neutrino_time: str
    machine_time: str
    location: str
    p_value: float
    status: str
    content: str


@plugins.register
def get_models():
    return {
        "snewsobservation": SNEWSObservation,
        "snewsheartbeat": SNEWSHeartbeat,
        "snewsalert": SNEWSAlert
    }
