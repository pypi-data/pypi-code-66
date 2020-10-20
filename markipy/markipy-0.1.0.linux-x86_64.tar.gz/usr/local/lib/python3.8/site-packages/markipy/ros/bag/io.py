import rosbag
from tqdm import tqdm

from markipy.basic import Logger, Performance
from markipy.basic import ThreadProducer, ThreadConsumer
from markipy.basic import File

_ibag_ = {'class': 'IBag', 'version': 3}
_bag_writer_ = {'class': 'BagWriter', 'version': 4}
_bag_reader_ = {'class': 'BagReader', 'version': 4}
_bag_raw_reader_ = {'class': 'BagRawReader', 'version': 4}


class TryToGetInfoWithTheBagStillClose(Exception):
    def __init__(self, ibag):
        ibag.log.error(f'Call info on the bag still close: {ibag.bagFile()}')


class IBag(Logger):

    def __init__(self, bagPath, mode, console):
        Logger.__init__(self, file_log='IBag', console=console)
        self._init_atom_register_class(_ibag_)
        self.bagFile = File(bagPath)
        self.mode = mode
        self.end = 0
        self.len = 0
        self.bag = None
        self.__bag_open__ = False

    @Performance.collect
    def __open__(self):
        log_mode = 'read' if 'r' in self.mode else 'write'
        self.log.debug(f'Opening {self.cyan(self.bagFile)} in {self.green(log_mode)} mode.')

        self.bag = rosbag.Bag(str(self.bagFile()), self.mode, allow_unindexed=True)
        if self.mode == 'r':
            self.end = self.bag.get_end_time()
            try:
                self.len = self.bag.get_message_count()
            except Exception as e:
                self.log.error(f'Error in bag getting message count: {e}')
        self.__bag_open__ = True

    @Performance.collect
    def info(self):
        self.log.debug('Requested info')
        if self.__bag_open__:
            return self.bag.get_type_and_topic_info().topics
        else:
            raise TryToGetInfoWithTheBagStillClose(self)

    @Performance.collect
    def __len__(self):
        return self.len

    @Performance.collect
    def read(self, **kargs):
        assert self.mode == 'r'
        for topic, msg, time in tqdm(self.bag.read_messages(kargs), total=self.len, dynamic_ncols=True):
            yield topic, msg, time

    @Performance.collect
    def raw(self):
        assert self.mode == 'r'
        for topic, msg, time in tqdm(self.bag.read_messages(raw=True), total=self.len, dynamic_ncols=True):
            yield topic, msg, time

    def add(self, topic, msg, time):
        assert self.mode == 'w'
        self.bag.write(topic, msg, time)

    @Performance.collect
    def reindex(self):
        self.log.debug(f"{self.violet('Reindexing')}")
        progress = tqdm(total=self.bag.size, dynamic_ncols=True)
        for x in self.bag.reindex():
            progress.update(x)
        progress.close()

    @Performance.collect
    def flush(self):
        self.log.debug(f"{self.violet('Flushing')}")
        self.bag.flush()


class BagReader(IBag, ThreadProducer):
    __bag_reader_version__: str = '3'

    def __init__(self, bag_path, channel, console=True):
        IBag.__init__(self, bag_path, 'r', console)
        ThreadProducer.__init__(self, channel, 'BagReader', console)
        self._init_atom_register_class(_bag_reader_)

    def init(self):
        self.__open__()

    def task(self):
        try:
            for topic, msg, t in self.read():
                self.produce([topic, msg, t])
            self.set_finish()
        except Exception as e:
            self.log.error(f"Error in task -> {e}")


class BagRawReader(IBag, ThreadProducer):
    def __init__(self, bag_path, channel, console=True):
        IBag.__init__(self, bag_path, 'r', console)
        ThreadProducer.__init__(self, channel, 'BagRawReader', console=console)
        self._init_atom_register_class(_bag_raw_reader_)

    def init(self):
        self.__open__()

    def task(self):
        for topic, msg, t in self.raw():
            self.produce([topic, msg, t])
        self.set_finish()

    def cleanup(self):
        self.bag.close()
        self.log.debug(f'Finish raw reading {self.bagFile}')


class BagWriter(IBag, ThreadConsumer):
    def __init__(self, bag_path, channel, console=True):
        IBag.__init__(self, bag_path, mode='w', console=console)
        ThreadConsumer.__init__(self, channel, 'BagWriter', console=console)
        self._init_atom_register_class(_bag_writer_)

    def add(self, topic, msg, t):
        self.bag.write(topic, msg, t)

    def init(self):
        self.__open__()

    def task(self, val):
        self.add(*val)

    def cleanup(self):
        self.reindex()
        self.flush()
        self.bag.close()
        self.log.debug(f'Finish writing {self.green(self.bagFile())}')
