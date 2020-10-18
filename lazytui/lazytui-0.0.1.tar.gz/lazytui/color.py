
import curses

COLOR_MAP = {
    "BLACK": curses.COLOR_BLACK,
    "BLUE": curses.COLOR_BLUE,
    "CYAN": curses.COLOR_CYAN,
    "GREEN": curses.COLOR_GREEN,
    "MAGENTA": curses.COLOR_MAGENTA,
    "RED": curses.COLOR_RED,
    "WHITE": curses.COLOR_WHITE,
    "YELLOW": curses.COLOR_YELLOW,
}

STYLE_MAP = {}

try:
    # Alternate character set mode
    STYLE_MAP["ALTCHARSET"] = curses.A_ALTCHARSET
except AttributeError:
    pass
try:
    # Blink mode
    STYLE_MAP["BLINK"] = curses.A_BLINK
except AttributeError:
    pass
try:
    # Bold mode
    STYLE_MAP["BOLD"] = curses.A_BOLD
except AttributeError:
    pass
try:
    # Dim mode
    STYLE_MAP["DIM"] = curses.A_DIM
except AttributeError:
    pass
try:
    # Invisible or blank mode
    STYLE_MAP["INVIS"] = curses.A_INVIS
except AttributeError:
    pass
try:
    # Italic mode
    STYLE_MAP["ITALIC"] = curses.A_ITALIC
except AttributeError:
    pass
try:
    # Normal attribute
    STYLE_MAP["NORMAL"] = curses.A_NORMAL
except AttributeError:
    pass
try:
    # Protected mode
    STYLE_MAP["PROTECT"] = curses.A_PROTECT
except AttributeError:
    pass
try:
    # Reverse background and foreground colors
    STYLE_MAP["REVERSE"] = curses.A_REVERSE
except AttributeError:
    pass
try:
    # Standout mode
    STYLE_MAP["STANDOUT"] = curses.A_STANDOUT
except AttributeError:
    pass
try:
    # Underline mode
    STYLE_MAP["UNDERLINE"] = curses.A_UNDERLINE
except AttributeError:
    pass
try:
    # "Horizontal" highlight
    STYLE_MAP["HORIZONTAL"] = curses.A_HORIZONTAL
except AttributeError:
    pass
try:
    # Left highlight
    STYLE_MAP["LEFT"] = curses.A_LEFT
except AttributeError:
    pass
try:
    # Low highlight
    STYLE_MAP["LOW"] = curses.A_LOW
except AttributeError:
    pass
try:
    # Right highlight
    STYLE_MAP["RIGHT"] = curses.A_RIGHT
except AttributeError:
    pass
try:
    # Top highlight
    STYLE_MAP["TOP"] = curses.A_TOP
except AttributeError:
    pass
try:
    # Vertical highlight
    STYLE_MAP["VERTICAL"] = curses.A_VERTICAL
except AttributeError:
    pass
try:
    # Bit-mask to extract a character
    STYLE_MAP["CHARTEXT"] = curses.A_CHARTEXT
except AttributeError:
    pass


color_pairs = {}


def color(fg=-1, bg=-1, style=0):
    if isinstance(fg, str):
        fg = COLOR_MAP[fg.upper()]
    if isinstance(bg, str):
        bg = COLOR_MAP[bg.upper()]
    if isinstance(style, str):
        style = STYLE_MAP[style.upper()]
    elif isinstance(style, list):
        for index, s in enumerate(style):
            if isinstance(s, str):
                style[index] = STYLE_MAP[s.upper()]

    if color_pairs.get((fg, bg)):
        pair_number = color_pairs.get((fg, bg))
        if isinstance(style, list):
            _color = curses.color_pair(pair_number)
            for s in style:
                _color = _color | s
            return _color
        else:
            return curses.color_pair(pair_number) | style
    else:
        pair_number = len(color_pairs) + 1
        curses.init_pair(pair_number, fg, bg)
        color_pairs[(fg, bg)] = pair_number
        if isinstance(style, list):
            _color = curses.color_pair(pair_number)
            for s in style:
                _color = _color | s
            return _color
        else:
            return curses.color_pair(pair_number) | style
