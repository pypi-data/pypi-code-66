from PyQt5 import QtGui  # type: ignore
import pyqtgraph as pg  # type: ignore
from typing import cast, Callable


pg.setConfigOptions(antialias=True)


class GraphicsError(Exception):
    pass


class Graphics:

    def __init__(self):
        self.app = QtGui.QApplication([])
        self.windows = {}
        self.close_timer = pg.QtCore.QTimer()
        self.update_timer = pg.QtCore.QTimer()
        self.close_timer.timeout.connect(lambda: self.close())
        self.to_close: bool = False

        def check_close(instance):
            if instance.to_close:
                instance.app.closeAllWindows()
        self.add_update(lambda: check_close(self))

    def add_window(self, name: str, width: int = 500, height: int = 500) -> None:
        if name in self.windows:
            raise GraphicsError("Window '%s' already exists" % name)
        else:
            w = pg.GraphicsLayoutWidget(show=True, title=name)
            w.resize(width, height)
            self.windows[name] = w

    def add_update(self, p: Callable):
        self.update_timer.timeout.connect(p)

    def display(self, update_interval: int = 50, ttl=None) -> None:
        """
        :param update_interval:
        :param ttl: time before closing windows, in millis
        """
        if ttl is not None:
            self.close_timer.start(ttl)
        self.update_timer.start(update_interval)
        self.app.exec()

    def get_window(self, window_name: str) -> pg.GraphicsLayoutWidget:
        if window_name not in self.windows:
            raise GraphicsError("Window '%s' does not exist" % window_name)
        else:
            return cast(pg.GraphicsLayoutWidget, self.windows[window_name])

    def close(self):
        self.to_close = True
