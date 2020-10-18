from email.message import Message
from typing import (
    Text
)

from sifter.grammar.string import expand_variables
from sifter.grammar.command import Command
from sifter.validators.stringlist import StringList
from sifter.grammar.state import EvaluationState


class CommandRewrite(Command):

    HANDLER_ID: Text = 'REWRITE'
    EXTENSION_NAME = 'rewrite'
    POSITIONAL_ARGS = [
        StringList(length=1),
        StringList(length=1),
    ]

    def evaluate(self, message: Message, state: EvaluationState) -> None:
        state.check_required_extension('rewrite', 'REWRITE')
        search = self.positional_args[0][0]  # type: ignore
        replace = self.positional_args[1][0]  # type: ignore
        search = expand_variables(search, state)
        replace = expand_variables(replace, state)
        state.actions.append('rewrite', (search, replace))  # type: ignore
