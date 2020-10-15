import requests, json, sseclient, rx
from rx.scheduler import NewThreadScheduler
import rx.operators as ops

scheduler = NewThreadScheduler()


class MagixHttpClient:
    """Waltz-Controls Magix client based on HTTP transport

    Example:
        >>> client = MagixHttpClient(magix_host)#http://localhost:8080 by default
        >>> client.observe().subscribe(lambda event: print(json.loads(event.data)))
        >>> client.broadcast({'hello':'world'})

    Args:
        magix_host: Magix host URL
    """

    def __init__(self, magix_host='http://localhost:8080'):
        self.magix_broadcast = magix_host + '/magix/api/broadcast'
        self.magix_subscribe = magix_host + '/magix/api/subscribe'
        sse = sseclient.SSEClient(self.magix_subscribe)
        self.stream = rx.from_iterable(sse, scheduler=scheduler).pipe(
            ops.publish()
        )
        self.stream.connect()

    def broadcast(self, message):
        encoded_message = json.dumps(message).encode('utf-8')
        # TODO fire and forget
        requests.post(self.magix_broadcast, data=encoded_message, headers={'Content-Type': 'application/json'})
        pass

    def observe(self, channel='message'):
        return self.stream.pipe(
            ops.filter(lambda event: event.event == channel)
        )
