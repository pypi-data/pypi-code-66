#
# Mystix: A domain-specific language intended for event-driven acquisition,
# analysis, and visualization of data.
#
# Copyright (C) 2020  Adrian Pang, Brandon Chung, Jack Griffiths, Rowan
# Lindsay, Sofia Chang
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#

import sys


from .language.evaluation.main import run_program


if len(sys.argv) >= 2:
    if sys.argv[1] == "-v":
        print("Mystix v0.1.2")
    else:
        run_program(sys.argv[1])
