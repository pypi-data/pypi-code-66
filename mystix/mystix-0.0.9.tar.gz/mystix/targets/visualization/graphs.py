from mystix.ui.graphics import Graphics
from typing import Callable, List
from os import path, listdir, remove, mkdir
import pickle
import re
from pyqtgraph import PlotItem  # type: ignore

from mystix.language.evaluation.errors import LanguageError


class GraphManagerError(LanguageError):
    pass


CONST_FRAGMENT_CACHE = "/tmp/mystix_vis_cache"
CONST_DEBUG_OUTPUT = "/tmp/mystix_vis_trace"


class Plot:

    CONST_DATA_LIMIT = 10000

    def __init__(self, name: str, plot: PlotItem, line: bool):
        self.name = name
        self.fr_fmt = re.compile("%s_([0-9]+)" % self.name)
        self.graphics: PlotItem = plot
        self.plot_data \
            = self.graphics.plot() if line \
            else self.graphics.plot(pen=None, symbol='x', symbolPen=None,
                                    symbolSize=10)
        self.data_frag = 0

        self.x_data: List = []
        self.y_data: List = []

    def update(self):
        fragments = sorted([
            int(self.fr_fmt.match(fn).group(1)) for fn in listdir(
                CONST_FRAGMENT_CACHE)
            if path.isfile(path.join(CONST_FRAGMENT_CACHE, fn))
            and self.name in fn])
        for fr in fragments:
            fn = self.num_fragment(fr)
            with open(fn, "rb") as f:
                try:
                    x_data, y_data = pickle.loads(f.read())
                    self.x_data = (self.x_data + x_data)
                    self.y_data = (self.y_data + y_data)
                    # data limiting
                    if len(self.x_data) > Plot.CONST_DATA_LIMIT:
                        self.x_data = (self.x_data + x_data)[-Plot.CONST_DATA_LIMIT:]
                    if len(self.y_data) > Plot.CONST_DATA_LIMIT:
                        self.y_data = (self.y_data + y_data)[-Plot.CONST_DATA_LIMIT:]
                    read = True
                except EOFError:
                    continue
            if read:
                remove(fn)
        self.plot_data.setData(self.x_data, self.y_data)

    def num_fragment(self, i: int):
        return path.join(CONST_FRAGMENT_CACHE, self.name + "_%d" % i)

    def log(self, msg: str):
        with open(path.join(CONST_DEBUG_OUTPUT, self.name + ".log"), "a") as trace:
            trace.write("[]: %s\n" % msg)

    def name_fragment(self):
        return self.num_fragment(self.data_frag)

    def add_data(self, x_data: List, y_data: List):
        if len(x_data) != len(y_data):
            raise GraphManagerError("New data arrays are not the same length")
        with open(self.name_fragment(), "wb") as frag:
            frag.write(pickle.dumps((x_data,y_data)))
        self.data_frag = self.data_frag + 1

    def clear_cache(self):
        self.log("Clearing cache")
        files = [path.join(CONST_FRAGMENT_CACHE, f) for f in listdir(
            CONST_FRAGMENT_CACHE) if
                 self.fr_fmt.match(f)]
        for f in files:
            remove(f)


class GraphManager:

    def __init__(self):
        self.closed = False
        self.graphics = Graphics()
        self.plots = {}
        self.graphics.add_window("410 DSL", 600, 600)
        self.graphics.add_window("410 DSL 2", 600, 600)
        self.graphics.add_update(lambda: self.update_plots())
        for d in [CONST_DEBUG_OUTPUT, CONST_FRAGMENT_CACHE]:
            if path.isfile(d):
                raise GraphManagerError("%s is already a file" % d)
            if not path.isdir(d):
                mkdir(d)

    def add_plot(self, plot_name: str, line_plot: bool = False):
        if ' ' in plot_name:
            raise GraphManagerError("Plot name cannot contain spaces")
        if plot_name in self.plots:
            raise GraphManagerError("Plot '%s' already exists" % plot_name)
        else:
            p: Plot = Plot(plot_name, self.graphics
                           .get_window("410 DSL 2")
                           .addPlot(title=plot_name), line_plot)
            self.plots[plot_name] = p

    def update_plots(self):
        if not self.graphics.to_close and not self.closed:
            try:
                for p in self.plots:
                    self.plots[p].update()
            except RuntimeError:
                print("Warning: plots attempted to update after close")

    def _confirm_plot_(self,  plot_name: str, p: Callable):
        if plot_name not in self.plots:
            raise GraphManagerError("Plot '%s' does not exist" % plot_name)
        else:
            return p(self.plots[plot_name])

    def add_plot_data(self, plot_name: str, x_data: List, y_data: List):
        def add(p: Plot):
            p.add_data(x_data, y_data)
        return self._confirm_plot_(plot_name, add)

    def clean(self):
        for p in self.plots.values():
            p.clear_cache()

    def close(self):
        print("Closing graph manager")
        self.closed = True
        self.graphics.close()
