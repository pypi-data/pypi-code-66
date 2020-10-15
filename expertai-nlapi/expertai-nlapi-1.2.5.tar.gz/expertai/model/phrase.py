# Copyright (c) 2020 original authors
#
# Licensed under the Apache License, Version 2.0 (the License);
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from expertai.errors import ETypeError, EValueError, MissingArgumentError
from expertai.model.phrase_type import PhraseType
from expertai.model.position import Position
from expertai.model.token import Token


class Phrase(Position):
    def __init__(self, tokens, start, end, type=None, type_=None):
        """Initialise the Phrase object

        To minimise the `abuse` of the Python `type` keyword, the
        initialisation method also accepts `type_`. The former argument
        is used when the initialisation is nested inside other
        data-model classes. In these cases the __init__ receives a
        dictionary containing `type` not `type_`, because that how the
        response the server sends is defined. Otherwise when the object
        can be directly initialised using the second alternative.
        Again, to mitigate this name clash with the keyword the
        property was suffixed with the underscore.

        In the remote case a token dictionary is empty, the Token is not
        initialised to prevent an error to be raised.
        """
        super().__init__(start=start, end=end)
        if not (type or type_):
            raise MissingArgumentError("Missing required argument type")

        self._type = PhraseType(key=type_ or type)
        self._tokens = []

        if not isinstance(tokens, list):
            raise ETypeError(tokens, list)

        for token in tokens:
            if not isinstance(token, dict):
                raise ETypeError(expected=list, current=token)
            if not token:
                raise EValueError(token, "Phrase.tokens")

            self._tokens.append(Token(**token))

    @property
    def tokens(self):
        return self._tokens

    @property
    def type_(self):
        return self._type
