# Copyright © 2020 Matthew Burkard
#
# This file is part of Language Formatters
#
# Language Formatters is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# Language Formatters is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Language Formatters.  If not, see
# <https://www.gnu.org/licenses/>.
import re
from random import choice
from typing import Generator, List, Optional, Dict, Pattern, Tuple


def get_marker(example: str, length: int = 6) -> str:
    """Get a generated substring that doesn't exist in the example.

    :param example: String to check against to ensure marker is unique.
    :param length: Number of digits you want in the new marker.
    :return: A newly generated substring unique to the provided example.
    """
    seq = f"<{''.join(choice('0123456789') for _ in range(length))}>"
    return seq if not re.search(seq, example) else get_marker(example, length)


def depopulate(reg: Pattern, string: str) -> Tuple[List[str], str, str]:
    """Replace all matches of a pattern with marker in a string.

    Get a tuple of all matches of reg, a newly generated marker, and
    the string with all matches of reg replaced by the new marker.

    :param reg: Pattern to match.
    :param string: String to search for matches in.
    :return: Matches, sequence, string.
    """
    # TODO Depopulated elements should be replaced with markers that
    #  include the length of the depopulated element.
    mark = get_marker(string)
    matches = re.findall(reg, string)
    string = re.sub(reg, mark, string)
    return matches, mark, string


def repopulate(items: List[str], marker: str, string: str) -> str:
    """Get a string with markers replaced by the items.

    Get a string where all appearances of marker in the string are
    replaced by the contents of iterable in the order they appear.

    :param items: List of items to replace sequences with.
    :param marker: Sequence to replace.
    :param string: String to repopulate.
    :return: A new string repopulated with items where sequences where.
    """
    items.append('')
    return ''.join(it + items.pop(0) for it in re.split(marker, string))


def add_indents(string: str,
                spaces: int = 4,
                use_tabs: bool = False,
                block_markers: Optional[Dict[str, str]] = None) -> str:
    """Add indents based on the openers and closers.

    :param string: String to add indents to.
    :param spaces: Number of spaces to indent by.
    :param use_tabs: Indents will use tabs instead of spaces if True,
        defaults to False.
    :param block_markers: Dictionary of block openers as keys and
        closers as values, defaults to {'{': '}', '[': ']'}
    :return: The string with indentation added.
    """
    block_markers = block_markers or {'{': '}', '[': ']'}
    indent = 1 if use_tabs else spaces
    indent_char = '\t' if use_tabs else ' '

    def process_lines(lines: List[str],
                      opener: str,
                      closer: str) -> Generator[str, None, None]:
        opener = re.escape(opener)
        closer = re.escape(closer)
        depth = 0
        for line in lines:
            if re.search(opener + closer, line):
                line = f'{indent_char * depth}{line}'
            elif re.search(opener, line):
                if re.search(closer, line):
                    line = f'{indent_char * (depth - indent)}{line}'
                else:
                    line = f'{indent_char * depth}{line}'
                    depth += indent
            elif re.search(closer, line):
                depth -= indent
                line = f'{indent_char * depth}{line}'
            else:
                line = f'{indent_char * depth}{line}'
            yield line + '\n'

    for k, v in block_markers.items():
        string = ''.join(process_lines(string.split('\n'), k, v))
    return string.strip()
