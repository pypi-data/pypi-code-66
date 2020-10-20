
import curses
from curses.textpad import rectangle
from .color import color

def draw_hline(screen, y, x, width, ch='─', fg=-1, bg=-1, style=0, colors=None):
    """
    Draw horizontal line to screen
    """

    if not screen.enclose(y, x) or not screen.enclose(y, x + width - 1):
        return

    h, w = screen.getmaxyx()
    if h == 1:
        screen.resize(h+1, width)

    if colors:
        _color = colors
    else:
        _color = color(fg, bg, style)

    for x in range(x, width):
        screen.addstr(y, x, ch, _color)

def validyx(screen, y, x):
    height, width = screen.getmaxyx()
    if y < 0 or y >= height:
        return False
    if x < 0 or x >= width:
        return False
    return True

def write(screen, y=None, x=None, text='', fg=-1, bg=-1, style=0, colors=None, wrap=False):
    """
    Write text to screen
    """
    # TODO proll need to rewrite
    text = str(text)

    if colors:
        _color = colors
    else:
        _color = color(fg, bg, style)

    if y is None and x is None:
        screen.addstr(text, _color)
    else:
        if not validyx(screen, y, x):
            return
        elif not wrap and not validyx(screen, y, x + len(text) - 1):
            return
        screen.addstr(y, x, text, _color)


def border(screen, colors):
    screen.attron(colors)
    screen.border()
    screen.attroff(colors)

# def draw_box(screen, y, x, height, width, fg=-1, bg=-1, style=0, attr=None, fill=False):
#     """
#     Draws a box on screen
#     """
#     height -= 1
#     width -= 1
#     if not validyx(screen, y, x) or not validyx(screen, y + height, x + width - 1):
#         return
#     if attr:
#         _color = attr
#     else:
#         _color = color(fg, bg, style)
#     screen.attron(_color)
#     try:
#         rectangle(screen, y, x, y + height, x + width)
#     except Exception:
#         pass
#     screen.attroff(_color | style)
