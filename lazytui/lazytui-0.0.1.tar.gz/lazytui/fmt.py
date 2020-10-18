
from .color import color

class FmtString:
    def __init__(self, text, fg, bg, style):
        self.__text = text
        self.__fg = fg
        self.__bg = bg
        self.__style = style
        self.strings = [
            {
                'text': self.__text,
                'fg': self.__fg,
                'bg': self.__bg,
                'style': self.__style
            }
        ]

    def __add__(self, other):
        if isinstance(other, FmtString):
            self.strings.append(other.strings[0])
        elif isinstance(other, str):
            self.strings.append(
                {
                    'text': other,
                    'fg': -1,
                    'bg': -1,
                    'style': 0
                }
            )
        return self

    def __radd__(self, other):
        if isinstance(other, str):
            self.strings.insert(
                0,
                {
                    'text': other,
                    'fg': -1,
                    'bg': -1,
                    'style': 0
                }
            )
        elif isinstance(other, FmtString):
            self.strings.insert(0, other.strings[0])
        return self

    def __iter__(self):
        for string in self.strings:
            yield string['text'], color(string['fg'], string['bg'], string['style'])


def fmt(text, fg=-1, bg=-1, style=0):
    return FmtString(text, fg, bg, style)
