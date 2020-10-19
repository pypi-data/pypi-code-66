import asyncio
import signal
from typing import List


class AioThing:
    def __init__(self):
        self.deps: List[AioThing] = []
        self._shutting_down = False
        self.started = False
        self.start = self._guard_start(self.start)
        self.stop = self._guard_stop(self.stop)

    def _guard_start(self, fn):
        async def guarded_fn(*args, **kwargs):
            if self.started:
                return
            self.started = True
            for aw in self.deps:
                await aw.start(*args, **kwargs)
            return await fn(*args, **kwargs)
        return guarded_fn

    def _guard_stop(self, fn):
        async def guarded_fn(*args, **kwargs):
            if not self.started or self._shutting_down:
                return
            self._shutting_down = True
            r = await fn(*args, **kwargs)
            for aw in reversed(self.deps):
                await aw.stop(*args, **kwargs)
            self.started = False
            self._shutting_down = False
            return r
        return guarded_fn

    async def start(self, *args, **kwargs):
        pass

    async def stop(self, *args, **kwargs):
        pass


class AioRootThing(AioThing):
    def __init__(self):
        super().__init__()
        self._shutting_down = False

    def setup_hooks(self):
        for sig in (signal.SIGTERM, signal.SIGINT):
            asyncio.get_event_loop().add_signal_handler(
                sig, lambda: asyncio.get_event_loop().create_task(self.on_shutdown()),
            )

    async def on_shutdown(self):
        if self._shutting_down:
            return
        await self.stop()
        await asyncio.get_event_loop().shutdown_asyncgens()
        tasks = [t for t in asyncio.all_tasks() if t is not asyncio.current_task()]
        await asyncio.gather(*tasks, return_exceptions=True)
