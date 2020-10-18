'''
Style, sheet, theme - simple coloring for python standard `logging` module

*Currently works only for '{'-style formatting*
'''


import logging
import sys
import string
import enum

import colorama


colorama.init(wrap=False)
ANSI_STREAM_HANDLER = colorama.AnsiToWin32(sys.stderr).stream


CRITICAL = logging.CRITICAL
ERROR    = logging.ERROR
WARNING  = logging.WARNING
INFO     = logging.INFO
DEBUG    = logging.DEBUG


class FG(enum.Enum):
    BLACK   = 30
    RED     = 31
    GREEN   = 32
    YELLOW  = 33
    BLUE    = 34
    MAGENTA = 35
    CYAN    = 36
    WHITE   = 37
    BRIGHT_BLACK   = 90
    BRIGHT_RED     = 91
    BRIGHT_GREEN   = 92
    BRIGHT_YELLOW  = 93
    BRIGHT_BLUE    = 94
    BRIGHT_MAGENTA = 95
    BRIGHT_CYAN    = 96
    BRIGHT_WHITE   = 97

class BG(enum.Enum):
    BLACK   = 40
    RED     = 41
    GREEN   = 42
    YELLOW  = 43
    BLUE    = 44
    MAGENTA = 45
    CYAN    = 46
    WHITE   = 47
    BRIGHT_BLACK   = 100
    BRIGHT_RED     = 101
    BRIGHT_GREEN   = 102
    BRIGHT_YELLOW  = 103
    BRIGHT_BLUE    = 104
    BRIGHT_MAGENTA = 105
    BRIGHT_CYAN    = 106
    BRIGHT_WHITE   = 107



class Style():

    def __init__(self, fg: FG = FG.BRIGHT_BLACK, bg: BG = BG.BLACK, bold: bool = False, pattern: str = '{}'):
        self._pattern = f"\033[{';'.join(map(str, [fg.value, bg.value, 1 if bold else 22]))}m{pattern}"

    @property
    def pattern(self) -> str:
        return self._pattern


class Sheet():
    
    def __init__(self, fmt: str = '', datefmt: str = '%H:%M:%S', msecs: int = 3, indent: int = 13, default: Style = None):
        self._attrs = {}
        self.datefmt = datefmt
        self.msecs = msecs
        self.indent = indent
        self._default = default or Style()
        self.setFormat(fmt)

    

    def getAttr(self, attrname: str) -> Style:
        style = self._attrs.get(attrname)
        if not style:
            style = self._default
            self.setAttr(attrname, style)
        return style

    def setAttr(self, attrname: str, style: Style):
        self._attrs[attrname] = style
        self._format = None

    def getFormat(self, ansi=True) -> str:
        if not ansi:
            return self._raw
        if not self._format:
            self._format = self._formatRaw()
        return self._format

    def setFormat(self, fmt: str):
        self._raw = fmt
        self._format = None

    def _formatRaw(self) -> str:
        formatter = string.Formatter()
        arr = formatter.parse(self._raw)
        result = []
        for txt, field, spec, conv in arr:
            if txt:
                result.append(self._default.pattern.format(txt))
            if field:
                fmt_field = f"{{{field}{'!'+conv if conv else ''}{':'+spec if spec else ''}}}"
                result.append( self.getAttr(field).pattern.format(fmt_field))
        return ''.join(result)+'\033[0m'



class Theme():

    def __init__(self, default: Sheet = None):
        self._default = default or Sheet()
        self._levels = {}

    def setSheet(self, levelname, sheet: Sheet):
        self._levels[levelname] = sheet

    def getSheet(self, levelname) -> Sheet:
        sheet = self._levels.get(levelname)
        if not sheet:
            self.setSheet(levelname, self._default)
            return self._default
        return sheet

    def setFormat(self, fmt: str):
        for sheet in self._levels.values():
            sheet.setFormat(fmt)

    def setDatefmt(self, datefmt: str):
        for sheet in self._levels.values():
            sheet.datefmt = datefmt

    def setMsecs(self, msecs: int):
        for sheet in self._levels.values():
            sheet.msecs = msecs

    def setIndent(self, indent: int):
        for sheet in self._levels.values():
            sheet.indent = indent



class Formatter(logging.Formatter):

    def __init__(
            self,
            theme: Theme,
            ansi: bool = True):
        
        self.theme = theme
        self.ansi = ansi
        super().__init__(fmt=None, datefmt=None, style='{')

    def format(self, record: logging.LogRecord, *args, **kwargs):
        theme = self.theme.getSheet(record.levelno)
        self.default_time_format = theme.datefmt
        self.default_msec_format = f'%s.%0{theme.msecs}d' if theme.msecs>0 else '%s'
        self._style._fmt = theme.getFormat(self.ansi)
        result = super().format(record, *args, **kwargs)
        if theme.indent:
            return ('\n' + ' '*theme.indent).join(result.splitlines())
        return result



#----------------------------------------------------------------------------------------------#
#
#   helpers
#

def getStreamHandler() -> logging.Handler:
    return logging.StreamHandler(stream=ANSI_STREAM_HANDLER)


def getFormatter(theme: Theme, ansi: bool = True) -> logging.Formatter:
    return Formatter(theme=theme, ansi=ansi)


def getDefaultTheme() -> Theme:
    theme = Theme()
    
    FORMAT_ERR = '{asctime} {levelname:3.3}: {message}\n'
    
    sheet_cri = Sheet(FORMAT_ERR, indent=18, default=Style(fg=FG.RED))
    sheet_cri.setAttr('levelname', Style(fg=FG.WHITE, bg=BG.RED, bold=True))
    sheet_cri.setAttr('message', Style(fg=FG.RED, bold=True))
    theme.setSheet(CRITICAL, sheet_cri)

    sheet_err = Sheet(FORMAT_ERR, indent=18)
    sheet_err.setAttr('levelname', Style(fg=FG.BRIGHT_RED, bold=True))
    sheet_err.setAttr('message', Style(fg=FG.RED, bold=True))
    theme.setSheet(ERROR, sheet_err)

    FORMAT_LOG = '{asctime} {levelname:3.3}: {message}'

    sheet_war = Sheet(FORMAT_LOG, indent=18)
    sheet_war.setAttr('levelname', Style(fg=FG.YELLOW, bold=True))
    sheet_war.setAttr('message', Style(fg=FG.YELLOW))
    theme.setSheet(WARNING, sheet_war)

    sheet_inf = Sheet(FORMAT_LOG, indent=18)
    sheet_inf.setAttr('message', Style(fg=FG.WHITE))
    theme.setSheet(INFO, sheet_inf)

    sheet_deb = Sheet(FORMAT_LOG, indent=18)
    theme.setSheet(DEBUG, sheet_deb)

    return theme


def configHandler(
        theme: Theme = None,
        datefmt: str = None,
        msecs: int = None,
        indent: int = None,
        ansi: bool = True) -> logging.Handler:
    
    theme = theme or getDefaultTheme()
    if datefmt is not None:
        theme.setDatefmt(datefmt)
    if msecs is not None:
        theme.setMsecs(msecs)
    if indent is not None:
        theme.setIndent(indent)
    
    formatter = getFormatter(theme=theme, ansi=ansi)
    handler = getStreamHandler()
    handler.setFormatter(formatter)
    return handler


def configLogger(
        name: str = None,
        level: int = None,
        theme: Theme = None,
        datefmt: str = None,
        msecs: int = None,
        indent: int = None,
        ansi: bool = True) -> logging.Logger:
    
    hdlr = configHandler(
            theme=theme,
            datefmt=datefmt,
            msecs=msecs,
            indent=indent,
            ansi=ansi)

    lg = getLogger(name, level)
    lg.addHandler(hdlr)
    return lg


def getLogger(name: str = None, level: int = None) -> logging.Logger:
    lg = logging.getLogger(name)
    if level:
        lg.setLevel(level)
    return lg



