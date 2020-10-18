from dataclasses import dataclass

from pika.adapters.blocking_connection import BlockingChannel


@dataclass
class Queue:
    name: str
    passive: bool = False
    durable: bool = True
    exclusive: bool = False
    auto_delete = False
    arguments: dict = None

    def declare(self, channel: BlockingChannel):
        channel.queue_declare(queue=self.name,
                              passive=self.passive,
                              durable=self.durable,
                              exclusive=self.exclusive,
                              auto_delete=self.auto_delete,
                              arguments=self.arguments)


@dataclass
class Exchange:
    name: str
    type: str
    passive: bool = False
    durable: bool = True
    auto_delete: bool = False
    internal: bool = False
    arguments: dict = None

    def declare(self, channel: BlockingChannel):
        channel.exchange_declare(exchange=self.name,
                                 exchange_type=self.type,
                                 passive=self.passive,
                                 durable=self.durable,
                                 auto_delete=self.auto_delete,
                                 internal=self.internal,
                                 arguments=self.arguments)
