#!/usr/bin/env python3
# termial-random
# Copyright(C) 2020 Fridolin Pokorny
#
# This program is free software: you can redistribute it and / or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.

"""Implementation of random termial."""

__title__ = "termial"
__version__ = "0.0.1"
__author__ = "Fridolin Pokorny <fridolin@redhat.com>"

from .random import random
from .random import seed
from .random import seed_init

__all__ = [
    "random",
    "seed",
    "seed_init",
]
