"""
All available commands aggregated in one scope.
To fetch a command use: get_command(cmd)
"""

from channeling import ChannelingException
from channeling import batteries
from channeling import message_formatting as mf
from channeling.batteries import cmd_channel
from channeling.batteries import cmd_grab
from channeling.batteries import cmd_info
from channeling.batteries import cmd_power
from channeling.batteries import cmd_set
from channeling.batteries import cmd_stats
from channeling.cmd_joke import cmd_joke
from channeling.config import ChannelingConfig
import channeling

import json
import os
import shlex
import sys
import time

conf = ChannelingConfig()
batteries.__db_init__()

@conf.debug
async def cmd_version(message):
    """Display version number and info.
    Usage: `version`
    """
    return await message.channel.send(mf.info(channeling.__version__))

@conf.debug
async def cmd_help(message):
    """Display help.
    Usage: `help [COMMAND]`
    """
    line = shlex.split(message.content)
    help_string = ""
    if len(line) == 3:
        try:
            cmd = get_command(line[2])
        except:
            return await message.channel.send(mf.error(
                "Can't display help for unknown command: {}".format(line[2])))
        help_string = os.linesep.join([s for s in cmd.__doc__.splitlines() if s.strip()])
        return await message.channel.send(mf.info(help_string))
    help_string = "Channeling commands:\n\n"
    all_commands = get_all_commands()
    for command_name in all_commands:
        help_string += "{} - {}\n".format(
                command_name,
                all_commands[command_name].__doc__.split("\n")[0]
                )
    help_string += "\nUse `help COMMAND` to display more info on specific command."
    return await message.channel.send(mf.info(help_string))

@conf.debug
async def cmd_bugreport(message):
    """Report a bug.
    Usage: `bugreport Text information about the bug you encountered.`
    """
    conf.logger.info(json.dumps({
        'timestamp': message.created_at.timestamp(),
        'type': 'bugreport',
        'author_name': message.author.display_name,
        'author_id': message.author.id,
        'channel_name': message.channel.name,
        'channel_id': message.channel.id,
        'guild_name': message.guild.name,
        'guild_id': message.guild.id,
        'content': message.content
        }))
    return await message.channel.send(mf.info("Your help in improving channeling bot is very appreciated!"))

def get_command(cmd):
    return getattr(sys.modules[__name__], 'cmd_'+cmd)

def get_all_commands():
    all_commands = {}
    for x in dir(sys.modules[__name__]):
        if x.startswith("cmd_"):
            all_commands[x[4:]] = get_command(x[4:])
    return all_commands

async def parse(message):
    guild = batteries.Guild(message.guild.id)
    await general_processing(message)
    line = []
    try:
        line = shlex.split(message.content)
    except ValueError as e:
        line = message.content.split()
    if not len(line):
        return
    if line[0] != guild.prefix:
        return None
    if len(line) == 1:
        return await cmd_help(message)
    cmd = line[1]
    try:
        return await get_command(cmd)(message)
    except AttributeError as e:
        conf.logger.debug(json.dumps({
            'timestamp': str(time.time()),
            'type': 'unknown_cmd',
            'content': message.content,
            'error': str(e)
            }))
        return await message.channel.send(
            mf.error("Unknown command '{}'. Use 'help' for list of available commands.".format(cmd)))

async def general_processing(message):
    if not message.author.bot:
        return await batteries.User(message.author.id, message.guild.id).talk(message)

