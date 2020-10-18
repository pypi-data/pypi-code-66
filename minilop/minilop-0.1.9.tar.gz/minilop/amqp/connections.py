import sys
import uuid
from typing import List

import pika
from loguru import logger
from pika import BlockingConnection
from pika.adapters.blocking_connection import BlockingChannel
from pika.exceptions import StreamLostError, ChannelClosed, ChannelWrongStateError

from minilop.amqp.components import Queue, Exchange
from minilop.amqp.exceptions import AMQPPublishError

logger.add(sys.stdout)

log = logger.bind(name='minilop', service=__name__)


class ExchangeQueueBinding:
    def __init__(self, queue: str, exchange: str, routing_keys: List[str] = None):
        self.queue = queue
        self.exchange = exchange
        self.routing_keys = routing_keys


class ExchangeExchangeBinding:
    def __init__(self, source_exchange: str, destination_exchange: str, routing_keys: List[str] = None):
        self.source_exchange = source_exchange
        self.destination_exchange = destination_exchange
        self.routing_keys = routing_keys


# https://bitbucket.org/fbanke/basic_consumer/src/master/datadriven_basic_consumer/basic_consumer.py
class AMQPConnection:
    def __init__(self, host: str, port: int, username: str, password: str, vhost: str,
                 queues: List[Queue] = None,
                 exchanges: List[Exchange] = None,
                 queue_bindings: List[ExchangeQueueBinding] = None,
                 exchange_bindings: List[ExchangeExchangeBinding] = None):

        queues = [] if queues is None else queues
        exchanges = [] if exchanges is None else exchanges
        queue_bindings = [] if queue_bindings is None else queue_bindings
        exchange_bindings = [] if exchange_bindings is None else exchange_bindings

        # RabbitMQ parameter
        self.__host = host
        self.__port = port
        self.__username = username
        self.__password = password
        self.__vhost = vhost
        self.__connection: BlockingConnection = None
        self.__channel: BlockingChannel = None
        self.__consumer_tag = None

        self.__queue_set = set(q.name for q in queues)
        self.__exchange_set = set(e.name for e in exchanges)

        self.__cur_deliver_tag = None

        for binding in queue_bindings:
            if binding.queue not in self.__queue_set:
                raise ValueError(f"queue {binding.queue} does not exists")
            if binding.exchange not in self.__exchange_set:
                raise ValueError(f"exchange {binding.exchange} does not exists")

        for binding in exchange_bindings:
            if binding.source_exchange not in self.__exchange_set:
                raise ValueError(f"exchange {binding.source_exchange} does not exists")
            if binding.destination_exchange not in self.__exchange_set:
                raise ValueError(f"exchange {binding.destination_exchange} does not exists")

        self.__connect()

        # declare queue
        for queue in queues:
            queue.declare(self.__channel)

        # declare exchange
        for exchange in exchanges:
            exchange.declare(self.__channel)

        # binding exchange to queue by each routing_key
        if queue_bindings:
            for binding in queue_bindings:
                for routing_key in binding.routing_keys:
                    # binding exchange to queue
                    self.__channel.queue_bind(queue=binding.queue,
                                              exchange=binding.exchange,
                                              routing_key=routing_key)

        # binding exchange to exchange by each routing_key
        if exchange_bindings:
            for binding in exchange_bindings:
                for routing_key in binding.routing_keys:
                    # bind exchange to exchange
                    self.__channel.exchange_bind(source=binding.source_exchange,
                                                 destination=binding.destination_exchange,
                                                 routing_key=routing_key)

    def __connect(self):
        log.info(
            f"Connecting to RabbitMQ host={self.__host}:{self.__port} user={self.__username} vhost={self.__vhost}")
        self.__connection = pika.BlockingConnection(
            pika.ConnectionParameters(host=self.__host,
                                      port=self.__port,
                                      virtual_host=self.__vhost,
                                      credentials=pika.PlainCredentials(
                                          username=self.__username,
                                          password=self.__password)))
        log.info("Creating channel")
        self.__channel = self.__connection.channel()
        log.debug("Successfully established connection")
        # todo: add connecting exception?

    def publish(self, exchange: str, routing_key: str, body, headers: dict = None):
        try:
            self.__channel.basic_publish(exchange=exchange,
                                         routing_key=routing_key,
                                         body=body,
                                         properties=pika.BasicProperties(headers=headers))
        except (StreamLostError, ChannelClosed, ChannelWrongStateError) as error:
            log.info("Reconnecting to RabbitMQ")
            self.__connect()
            log.debug(f"{type(error).__name__}: retry publishing, message={body}")
            self.publish(exchange=exchange,
                         routing_key=routing_key,
                         body=body,
                         headers=headers)
        except Exception as error:
            log.error(f"Unexpected error: {type(error).__name__}, from message {body}")
            raise AMQPPublishError(f"{type(error).__name__}: cannot publish message")

    def consume(self, queue: str, callback, prefetch_count: int = 1):
        def __callback(channel, method, properties, body):
            try:
                callback_result = callback(channel, method, properties, body)
                if callback_result is not None and callback_result is False:
                    self.__channel.basic_nack(delivery_tag=method.delivery_tag)
                else:
                    self.__channel.basic_ack(delivery_tag=method.delivery_tag)
            except Exception as callback_error:
                log.error(f"{type(callback_error).__name__}: callback error")
                self.__channel.basic_nack(delivery_tag=method.delivery_tag)

        self.__channel.basic_qos(prefetch_count=prefetch_count)
        self.__cur_deliver_tag = str(uuid.uuid4())
        self.__channel.basic_consume(queue=queue,
                                     on_message_callback=__callback,
                                     auto_ack=False,
                                     consumer_tag=self.__cur_deliver_tag)

        try:
            self.__channel.start_consuming()
        except (KeyboardInterrupt, InterruptedError) as error:
            log.info(f"{type(error).__name__}: consumer interrupted")
            self.stop_consuming()
        except ChannelClosed as error:
            log.error(f"{type(error).__name__}: channel is closed by broker")
        finally:
            log.info("consumer closed")

    def stop_consuming(self):
        log.info("Stopping consumer")
        if self.__cur_deliver_tag is not None:
            self.__channel.basic_cancel(consumer_tag=self.__cur_deliver_tag)
            self.__channel.stop_consuming()
