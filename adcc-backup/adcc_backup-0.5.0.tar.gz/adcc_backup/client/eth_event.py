from time import sleep

from markipy.basic import File, ThreadProducer, ThreadConsumer

from adcc_backup import PKG_LOG_PATH
from .rsync import AdccRsync

_eth_event_producer_ = {'class': 'EthEventProducer', 'version': 1}

_eth_event_consumer_ = {'class': 'EthEventConsumer', 'version': 1}


class EthEventProducer(ThreadProducer):
    def __init__(self, eth_interface, channel, console=True):
        ThreadProducer.__init__(self, task_name='EthEventProducer', channel=channel, daemon=True, console=console,
                                log_path=PKG_LOG_PATH)
        self._init_atom_register_class(_eth_event_producer_)
        self.eth_int = eth_interface
        self.eth_state = File(f'/sys/class/net/{eth_interface}/operstate', console=console)
        self.eth_up = False

    def task(self):
        sleep(0.33)
        state = str(self.eth_state.read())
        if 'up' in state:
            if self.eth_up is False:
                self.log.debug(f'Eth: {self.lightblue(self.eth_int)} change to {self.green("UP")}')
                self.produce(True)
                self.eth_up = True
        else:
            if self.eth_up:
                self.log.debug(f'Eth: {self.lightblue(self.eth_int)} change to {self.red("DOWN")}')
                self.eth_up = False

    def isUp(self):
        return self.eth_up


class EthEventConsumer(ThreadConsumer):
    def __init__(self, cfg, channel, console=True):
        ThreadConsumer.__init__(self, task_name='EthEventConsumer', channel=channel, daemon=True, console=console,
                                log_path=PKG_LOG_PATH)
        self._init_atom_register_class(_eth_event_consumer_)
        self.rsync = AdccRsync(cfg)

    def task(self, val):
        self.log.debug("Requested upload.")
        self.rsync.upload()
        self.log.debug("Upload completed.")
