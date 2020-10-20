from .io import BagWriter, BagReader

from markipy.basic import Channel, Performance

_bag_fixer_ = {'class': 'BagFixer', 'version': 2}


def fix_bag(input_bag_path, output_bag_path):
    channel = Channel()
    # Create Bag reader
    reader = BagReader(input_bag_path, channel)
    # Create Bag
    fixer = BagFixer(output_bag_path, channel)
    # Start workers
    reader.start()
    fixer.start()
    # Wait workers
    reader.join()
    fixer.join()


class BagFixer(BagWriter):
    def __init__(self, bag_path, channel):
        BagWriter.__init__(self, bag_path, channel)
        self._init_atom_register_class(_bag_fixer_)

    header_not_set = []

    def task(self, val):
        if val:
            topic = val[0]
            msg = val[1]
            time = val[2]
            if msg._has_header:
                if msg.header.stamp.secs > 0:
                    self.add(topic, msg, msg.header.stamp)
                else:
                    if topic not in self.header_not_set:
                        self.log.error(
                            f"Header is not set correctly! Using now the datalogger time for topic: {self.orange(topic)}. Take care next time.")
                        self.header_not_set.append(topic)
                    msg.header.stamp = time
                    self.add(topic, msg, time)
            else:
                if '/velodyne_packets' == topic:
                    self.add(topic, msg, msg.stamp)
                elif '/tf' == topic and msg.transforms:
                    self.add(topic, msg, msg.transforms[0].header.stamp)
                else:
                    self.add(topic, msg, time)

    @Performance.collect
    def cleanup(self):
        self.reindex()
        self.flush()
        self.bag.close()
        self.log.debug(f"Finish writing fixed {self.green(self.bagFile())}")
