import json
import traceback
from telethon import TelegramClient
from telethon.sessions.memory import MemorySession
from telethon import events

from .bot_logging import introduce_myself
from .data import Data

from . import utils

class Bot:
    steps = {}
    callback_commands = {}
    getting_input = {}

    def __init__(self, data = None):
        if data == None:
            data = Data
        self.data = data


    def on(self, step = '*', command = '*', callback = None, input_mode = None):
        def inner(function):
            if callback:
                self.callback_commands[callback] = function
            elif input_mode:
                self.getting_input[input_mode] = function
            else:
                self.steps.setdefault(step, {})
                self.steps[step][command] = function
            return function
        return inner


    async def connect(self, api_id, api_hash, bot_token):
        self.client = await TelegramClient(
    		MemorySession(),
    		api_id,
    		api_hash
    	).start(bot_token=bot_token)

        me = await self.client.get_me()
        introduce_myself(me)


    async def run_forever(self):
        nml, cql = self.get_functions()
        self.client.on(events.NewMessage(incoming=True))(nml)
        self.client.on(events.CallbackQuery)(cql)
        await self.client.run_until_disconnected()


    def get_functions(self):

        def enable_traceback(handler):
            async def inner(event):
                try:
                    await handler(event)
                except Exception:
                    traceback.print_exc()
            return inner


        @enable_traceback
        async def new_message_listener(event) -> None:
            data = await self.data.build(event)

            message_text = event.message.message
            current_step = await data.current_step()
            input_mode = await data.current_input_mode()

            print(f'map[{current_step}][{message_text}]')

            async def find_command_on_step(step):
                commands = self.steps.get(step)
                if commands:
                    func = commands.get(message_text) or self.getting_input.get(input_mode) or commands.get('*')
                    if func:
                        result = await func(event, data)
                        if result != None:
                            print(type(result))
                            if type(result) == tuple:
                                text, buttons = result
                                await event.respond(
                                    text,
                                    buttons = utils.wrap_inline(buttons)
                                )
                        return True

            (await find_command_on_step(current_step)) or \
            (await find_command_on_step('*'))



        @enable_traceback
        async def callback_query_listener(event) -> None:
            data = await self.data.build(event)

            command, *arguments = json.loads(event.data.decode('utf-8'))

            print(command, arguments)
            func = self.callback_commands.get(command)
            if func:
                result = await func(event, data, *arguments)
                print(type(result))
                if result != None:
                    if type(result) == tuple:
                        text, buttons = result
                        await event.edit(
                            text,
                            buttons = utils.wrap_inline(buttons)
                        )

        return new_message_listener, callback_query_listener
