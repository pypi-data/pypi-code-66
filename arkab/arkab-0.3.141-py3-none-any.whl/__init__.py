import arkab.nlp as nlp
from arkab.nlp.knowledge import KnowledgeKit
from arkab.delegates import FileDelegate

from arkab.trainer import Trainable
from typing import Literal

__all__ = ['nlp', 'Trainable', '__version__', 'version', 'KnowledgeKit', 'MODE', 'FileDelegate']

__version__ = '0.3.141'

MODE = Literal['train', 'valid', 'test']


def version():
    return __version__
