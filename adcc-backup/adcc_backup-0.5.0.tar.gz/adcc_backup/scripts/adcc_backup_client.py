
from markipy.basic import Channel

from adcc_backup import Configuration
from adcc_backup import EthEventProducer, EthEventConsumer


def adcc_backup_client_main():
    print('Main-adcc_backup')
    cfg = Configuration('default')
    if cfg:
        upload_channel = Channel()
        event_producer = EthEventProducer(eth_interface=cfg.get_eth_client(), channel=upload_channel, console=True)
        event_producer.start()

        event_consumer = EthEventConsumer(cfg=cfg, channel=upload_channel)
        event_consumer.start()

        event_producer.join()
        event_consumer.join()
