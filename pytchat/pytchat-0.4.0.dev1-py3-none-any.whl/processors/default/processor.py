import asyncio
import json
import time
from .custom_encoder import CustomEncoder
from .renderer.textmessage import LiveChatTextMessageRenderer
from .renderer.paidmessage import LiveChatPaidMessageRenderer
from .renderer.paidsticker import LiveChatPaidStickerRenderer
from .renderer.legacypaid import LiveChatLegacyPaidMessageRenderer
from .renderer.membership import LiveChatMembershipItemRenderer
from .. chat_processor import ChatProcessor
from ... import config

logger = config.logger(__name__)


class Chat:
    def json(self) -> str:
        return json.dumps(vars(self), ensure_ascii=False, cls=CustomEncoder)


class Chatdata:

    def __init__(self, chatlist: list, timeout: float, abs_diff):
        self.items = chatlist
        self.interval = timeout
        self.abs_diff = abs_diff

    def tick(self):
        if self.interval == 0:
            time.sleep(1)
            return
        time.sleep(self.interval / len(self.items))

    async def tick_async(self):
        if self.interval == 0:
            await asyncio.sleep(1)
            return
        await asyncio.sleep(self.interval / len(self.items))

    def yield_items(self):
        starttime = time.time()

        for c in self.items:
            next_chattime = c.timestamp / 1000
            tobe_disptime = self.abs_diff + next_chattime
            wait_sec = tobe_disptime - time.time()
            # allow 3 seconds delay.
            if wait_sec < -3:
                wait_sec = 0
            # for smooth display.
            elif wait_sec < 0:
                wait_sec = 0.05
            
            time.sleep(wait_sec)
        
            yield c

        stop_interval = time.time() - starttime
        if stop_interval < 3:
            time.sleep(3 - stop_interval)

    def json(self) -> str:
        return json.dumps([vars(a) for a in self.items], ensure_ascii=False, cls=CustomEncoder)


class DefaultProcessor(ChatProcessor):
    def __init__(self):
        self.first = True
        self.abs_diff = 0
        self.renderers = {
            "liveChatTextMessageRenderer": LiveChatTextMessageRenderer(),
            "liveChatPaidMessageRenderer": LiveChatPaidMessageRenderer(),
            "liveChatPaidStickerRenderer": LiveChatPaidStickerRenderer(),
            "liveChatLegacyPaidMessageRenderer": LiveChatLegacyPaidMessageRenderer(),
            "liveChatMembershipItemRenderer": LiveChatMembershipItemRenderer()
        }

    def process(self, chat_components: list):

        chatlist = []
        timeout = 0

        if chat_components:
            for component in chat_components:
                timeout += component.get('timeout', 0)
                chatdata = component.get('chatdata')
                if chatdata is None:
                    continue
                for action in chatdata:
                    if action is None:
                        continue
                    if action.get('addChatItemAction') is None:
                        continue
                    item = action['addChatItemAction'].get('item')
                    if item is None:
                        continue
                    chat = self._parse(item)
                    if chat:
                        chatlist.append(chat)
        
        if self.first and chatlist:
            self.abs_diff = time.time() - chatlist[0].timestamp / 1000
            self.first = False

        chatdata = Chatdata(chatlist, float(timeout), self.abs_diff)

        return chatdata

    def _parse(self, item):
        try:
            key = list(item.keys())[0]
            renderer = self.renderers.get(key)
            if renderer is None:
                return None
            renderer.setitem(item.get(key), Chat())
            renderer.settype()
            renderer.get_snippet()
            renderer.get_authordetails()
            rendered_chatobj = renderer.get_chatobj()
            renderer.clear()
        except (KeyError, TypeError) as e:
            logger.error(f"{str(type(e))}-{str(e)} item:{str(item)}")
            return None
        
        return rendered_chatobj
