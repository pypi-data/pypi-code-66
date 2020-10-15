"""
Module for event-based api.

Events could be generated by any source,
usually by the implementation backend (i.e., chat messages).

Then bot invokes all its registered event processors,
which is usually the `EventAggregator`.

The `EventAggregator` has the number of registered `EventHandler` classes.
It asks them if they can handle specific event,
and tells the first answered to process the event.
"""

from .command_handler import *
from .event_aggregator import *
from .event_handler import *
from .message_handler import *
from .start_handler import *

__all__ = [ ]
__pdoc__ = { }
__pdoc_extras__ = [ ]

submodules = \
[
    command_handler,
    event_aggregator,
    event_handler,
    message_handler,
    start_handler,
]

for _m in submodules: __all__.extend(_m.__all__)
from botter.util import create_documentation_index
create_documentation_index(submodules, __name__, __pdoc__, __pdoc_extras__)
del create_documentation_index, submodules
