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

from expertai.errors import ETypeError, EValueError
from expertai.model.position import Position


class MainSyncon:
    def __init__(self, syncon, score, positions):
        self._syncon = syncon
        self._score = score
        self._positions = []
        if not isinstance(positions, list):
            raise ETypeError(positions, list)

        for position in positions:
            if not isinstance(position, dict):
                raise ETypeError(expected=dict, current=position)
            if not position:
                raise EValueError(position, "MainSyncon.positions")

            self._positions.append(Position(**position))

    @property
    def syncon(self):
        return self._syncon

    @property
    def score(self):
        return self._score

    @property
    def positions(self):
        return self._positions
