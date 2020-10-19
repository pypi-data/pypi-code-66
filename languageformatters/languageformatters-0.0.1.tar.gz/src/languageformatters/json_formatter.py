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

from languageformatters.format_tools import depopulate, add_indents, repopulate


def format_json(json_str: str,
                spaces: int = 4,
                use_tabs: bool = False,
                newline_for_bracket: bool = False) -> str:
    """Get a nicely formatted JSON string.

    :param json_str: Unformatted JSON string.
    :param spaces: Number of spaces to indent by, default is 4.
    :param use_tabs: Will indent with tabs if True, default is False.
    :param newline_for_bracket: Add a newline for every open bracket.
    :return: Formatted version of the given JSON string.
    """
    # Depopulate all JSON values.
    num_reg = re.compile(r'(\d+\.?\d*)')
    numbers, num_mark, json_str = depopulate(num_reg, json_str)
    quote_reg = re.compile(r'".*?(?<!\\)"')
    quotes, quotes_mark, json_str = depopulate(quote_reg, json_str)
    kw_reg = re.compile(r'(null|true|false)')
    key_words, kw_mark, json_str = depopulate(kw_reg, json_str)
    # Remove all white space.
    json_str = re.sub(r'\s', '', json_str)
    # Add a newline after open brackets that are not immediately
    # followed by a closing bracket.
    json_str = re.sub(r'{(?!})', '{\n', json_str)
    json_str = re.sub(r'\[(?!])', '[\n', json_str)
    # Add a newline after opening brackets that are preceded by an
    # open and close brackets.
    json_str = re.sub(r'{},{', '{},\n{', json_str)
    json_str = re.sub(r'\[],\[', '[],\n[', json_str)
    # Add a newline after the end of any JSON values (All values have
    # already been depopulated so they will end with a ">").
    json_str = re.sub(r'(>,)', r'\1\n', json_str)
    # Add a space after colons.
    json_str = re.sub(r':', ': ', json_str)
    # Add a newline before any closing brackets that are not immediately
    # preceded by an open bracket.
    json_str = re.sub(r'(?<!{)}', '\n}', json_str)
    json_str = re.sub(r'(?<!\[)]', '\n]', json_str)
    # This determines if close and open "}, {" on the same line should
    # be allowed.
    if newline_for_bracket:
        json_str = re.sub(r'(?<!{)},(?!\n)', '},\n', json_str)
    else:
        json_str = re.sub(r'(?<!{)},(?!\n)(?!{)', '},\n', json_str)
    # Add a newline after any occurrence of "]," that is not preceded by
    # an open bracket.
    json_str = re.sub(r'(?<!\[)],(?!\n)', '],\n', json_str)
    # Add a space after any comma that is followed by non-whitespace.
    json_str = re.sub(r',(?=\S)', ', ', json_str)
    json_str = add_indents(json_str, spaces, use_tabs)
    # Repopulate all depopulated JSON values.
    json_str = repopulate(quotes, quotes_mark, json_str)
    json_str = repopulate(key_words, kw_mark, json_str)
    json_str = repopulate(numbers, num_mark, json_str)
    return json_str
