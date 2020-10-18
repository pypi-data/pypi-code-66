
import curses
from curses.textpad import rectangle
from .color import color

def draw_hline(stdscr, y, x, width, ch='─', fg=-1, bg=-1, style=0, colors=None):
    """
    Draw horizontal line to stdscr
    """

    if not stdscr.enclose(y, x) or not stdscr.enclose(y, x + width - 1):
        return

    h, w = stdscr.getmaxyx()
    if h == 1:
        stdscr.resize(h+1, width)

    if colors:
        _color = colors
    else:
        _color = color(fg, bg, style)

    for x in range(x, width):
        stdscr.addstr(y, x, ch, _color)

def validyx(stdscr, y, x):
    height, width = stdscr.getmaxyx()
    if y < 0 or y >= height:
        return False
    if x < 0 or x >= width:
        return False
    return True

def write(stdscr, y=None, x=None, text='', fg=-1, bg=-1, style=0, colors=None, wrap=False):
    """
    Write text to stdscr
    """
    # TODO proll need to rewrite
    text = str(text)

    if colors:
        _color = colors
    else:
        _color = color(fg, bg, style)

    if y is None and x is None:
        stdscr.addstr(text, _color)
    else:
        if not validyx(stdscr, y, x):
            return
        elif not wrap and not validyx(stdscr, y, x + len(text) - 1):
            return
        stdscr.addstr(y, x, text, _color)


def border(stdscr, colors):
    stdscr.attron(colors)
    stdscr.border()
    stdscr.attroff(colors)

# def draw_box(stdscr, y, x, height, width, fg=-1, bg=-1, style=0, attr=None, fill=False):
#     """
#     Draws a box on stdscr
#     """
#     height -= 1
#     width -= 1
#     if not validyx(stdscr, y, x) or not validyx(stdscr, y + height, x + width - 1):
#         return
#     if attr:
#         _color = attr
#     else:
#         _color = color(fg, bg, style)
#     stdscr.attron(_color)
#     try:
#         rectangle(stdscr, y, x, y + height, x + width)
#     except Exception:
#         pass
#     stdscr.attroff(_color | style)
