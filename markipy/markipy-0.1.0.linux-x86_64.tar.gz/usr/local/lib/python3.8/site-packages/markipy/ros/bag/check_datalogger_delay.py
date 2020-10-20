from matplotlib import pyplot as plt
from pathlib import Path
import pandas as pd

from .io import BagReader
from markipy.basic import Logger, Channel, ThreadConsumer
from markipy.basic import Folder, File, Hdf

_check_datalogger_delay_ = {'class': 'CheckDataloggerDelay', 'version': 3}
_check_datalogger_delay_plotter_ = {'class': 'CheckDataloggerDelayPlotter', 'version': 4}


def produce_delay_analysis(bag_path, stats_path):
    channel = Channel()
    # Create Bag reader
    reader = BagReader(bag_path, channel)
    # Create Bag
    checker = CheckDataloggerDelay(bag_path, channel, hdf_path=stats_path)
    # Start workers
    reader.start()
    checker.start()
    # Wait workers
    reader.join()
    checker.join()
    # Show
    plot_delay_analysis(hdf_path=stats_path)


def plot_delay_analysis(hdf_path):
    plotter = CheckDataloggerDelayPlotter(hdf_path)
    plotter.produce_plots()


class CheckDataloggerDelay(ThreadConsumer):

    def __init__(self, bag_file, channel, hdf_path='bags_statistics.hdf',console=True):
        ThreadConsumer.__init__(self, channel, 'CheckDataloggerDelay', console=console)
        self._init_atom_register_class(_check_datalogger_delay_)
        self.hdf_file = Hdf(hdf_path, console=console)
        self.hdf_key = bag_file.replace('.bag', '').replace('#', '').replace("_", "").replace("-", "")
        self.data = []
        self.dataframe = None

    def task(self, val):
        topic, msg, time = val[0], val[1], val[2]

        if hasattr(msg, 'header'):
            if msg.header.stamp.secs > 0:
                diff = time - msg.header.stamp
                self.data.append(dict(topic=topic, delay=diff.to_nsec()))
            else:
                self.data.append(dict(topic=topic, delay=0))

        elif '/velodyne_packets' == topic:
            diff = time - msg.stamp
            self.data.append(dict(topic=topic, delay=diff.to_nsec()))

        elif '/tf' == topic and msg.transforms:
            diff = time - msg.transforms[0].header.stamp
            self.data.append(dict(topic=topic, delay=diff.to_nsec()))

    def cleanup(self):
        self.dataframe = pd.DataFrame(self.data)
        self.hdf_file.save(self.hdf_key, self.dataframe)


class CheckDataloggerDelayPlotter(Logger):
    def __init__(self, hdf_path='bags_statistics.hdf', console=True):
        Logger.__init__(self, file_log='CheckDataloggerDelayPlotter', console=console)
        self.hfd_file = Hdf(hdf_path)
        self.hdf_keys = self.hfd_file.keys()
        self._init_atom_register_class(_check_datalogger_delay_plotter_)

    def produce_plots(self):
        for key in self.hdf_keys:
            plot_folder = Folder('./plot')
            plot_path = File(plot_folder() / Path(key).name)
            self.generate_plots(self.hfd_file.read(key), str(plot_path()))

    def convert_to_ms(self, frame):
        frame['delay'] = frame['delay'] * 1e-6
        return frame

    def filter_zero_heading(self, frame):
        return frame[frame['delay'] < 100000 * 1e6]

    def reframe_bycolumn(self, frame):
        series = frame.groupby('topic')['delay'].apply(list)
        max_len = []
        col_name = []
        rows = series.shape[0]
        for r in range(0, rows):
            max_len.append(len(series[r]))
            col_name.append(series.index[r])

        reframe = pd.DataFrame(index=range(max(max_len)), columns=col_name)

        for r in range(0, rows):
            reframe[series.index[r]] = pd.Series(series[r])
        return reframe

    def generate_plots(self, frame, plot_path):
        out_type = 'pdf'
        frame = self.convert_to_ms(frame)
        frame = self.filter_zero_heading(frame)
        reframe = self.reframe_bycolumn(frame)
        self.log.debug(f"Generating Plot: {plot_path}_delay_complete.pdf")
        reframe.boxplot(vert=False, figsize=(50, 70), fontsize=20)
        plt.subplots_adjust(left=0.25)
        plt.xlim((-0.1, frame['delay'].max()))
        plt.savefig(plot_path + '_delay_complete.' + out_type, dpi=350, format=out_type, bbox_inches='tight')
        plt.clf()
        self.log.debug(f"Plot completed")
        self.log.debug(f"Generating Plot without outliers: {plot_path}_delay_nooutliers.pdf")
        reframe.boxplot(vert=False, figsize=(70, 70), sym='', showfliers=False, fontsize=20)
        plt.subplots_adjust(left=0.25)
        plt.xlim((-0.1, 100))
        plt.savefig(plot_path + '_delay_nooutliers.' + out_type, dpi=350, format=out_type, bbox_inches='tight')
        plt.clf()
        self.log.debug(f"Plot no outliers completed")

        with open(plot_path + '.info', 'w') as fd:
            fd.write("MIN\n" + str(reframe.min()))
            fd.write("\n\nMAX\n" + str(reframe.max()))
            fd.write("\n\nMEAN\n" + str(reframe.mean()))

        self.log.debug(f"Stats min, max and mean created: {plot_path}.info")
