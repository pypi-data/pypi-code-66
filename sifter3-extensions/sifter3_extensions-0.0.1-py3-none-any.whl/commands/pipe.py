from email.message import Message
from typing import (
    Text
)

from sifter.grammar.command import Command
from sifter.grammar.string import expand_variables
from sifter.validators.stringlist import StringList
from sifter.grammar.state import EvaluationState


class CommandPipe(Command):

    HANDLER_ID: Text = 'PIPE'
    EXTENSION_NAME = 'pipe'
    POSITIONAL_ARGS = [StringList(length=1)]

    def evaluate(self, message: Message, state: EvaluationState) -> None:
        state.check_required_extension('pipe', 'PIPE')
        pipe_dest = self.positional_args[0]
        pipe_dest = map(lambda s: expand_variables(s, state), pipe_dest)  # type: ignore
        state.actions.append('pipe', pipe_dest)  # type: ignore
        state.actions.cancel_implicit_keep()
