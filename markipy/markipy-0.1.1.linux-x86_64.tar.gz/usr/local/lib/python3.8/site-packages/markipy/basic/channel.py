from queue import Queue


class Channel:

    def __init__(self, size=12500):
        self.queue_size = size
        self.finish = False
        self.channel = Queue(self.queue_size)
        self.empty = Queue.empty

    def get(self, timeout=5):
        try:
            return self.channel.get(block=True, timeout=timeout)
        except Exception:
            return self.empty

    def put(self, var):
        self.channel.put(var, block=True)

    def task_done(self):
        self.channel.task_done()

    def set_finish(self):
        self.finish = True

    def get_finish(self):
        return self.finish

    def wait_completion_task(self):
        self.channel.join()
        self.set_finish()

    def is_full(self):
        return self.channel.full()

    def is_empty(self):
        return self.channel.empty()
