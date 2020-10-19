"""
Channeling main module.
"""
from channeling import ChannelingException
from channeling.commands import parse
from channeling.config import ChannelingConfig
import channeling as app

import asyncio
import click
import discord
import json
import logging
import os
import sys
import textwrap
import time

class ChannelingClient(discord.Client):
    conf = ChannelingConfig()
    async def on_ready(self):
        self.conf.logger.info(json.dumps({
            'timestamp': str(time.time()),
            'type': 'system',
            'content': f'{self.user} has connected to Discord!'
            }))
    async def on_message(self, message):
        self.conf.logger.info(json.dumps({
            'timestamp': message.created_at.timestamp(),
            'type': 'message',
            'author_name': message.author.display_name,
            'author_id': message.author.id,
            'channel_name': message.channel.name,
            'channel_id': message.channel.id,
            'guild_name': message.guild.name,
            'guild_id': message.guild.id,
            'content': message.content
            }))
        if message.author == self.user:
            return
        await parse(message)

@click.group()
@click.version_option(version=app.__version__,
    message="%(prog)s %(version)s - {}".format(app.__copyright__))
@click.option('-d', '--debug', is_flag=True,
    help="Enable debug mode with output of each action in the log.")
@click.pass_context
def cli(ctx, **kwargs): # pragma: no cover
    conf = ChannelingConfig()
    if ctx.params.get('debug'):
        conf.logger.setLevel(logging.DEBUG)

@cli.command()
@click.option('-t', '--token', required=False, default="",
    help="Authorization token.")
def run(**kwargs): # pragma: no cover
    "Run bot service."
    conf = ChannelingConfig()
    token = kwargs['token'] if kwargs['token'] else conf.discord_token
    if not token:
        raise ChannelingException("No token provided. Create config file or use --token parameter.")
    client = ChannelingClient()
    try:
        client.run(token)
    except discord.errors.LoginFailure as e:
        conf.logger.error(json.dumps({
            'timestamp': str(time.time()),
            'type': 'system',
            'content': str(e)
            }))


@cli.command()
def setup(**kwargs):
    """Setup systemd service file and common service directories."""
    service_file_contents = textwrap.dedent("""
        [Unit]
        Description=Channeling - Discord bot
        After=network.target
        
        [Service]
        Environment="LC_ALL=C.UTF-8"
        Environment="LANG=C.UTF-8"
        ExecStart=/usr/local/bin/channeling run
        Restart=on-failure
        
        [Install]
        WantedBy=multi-user.target
        """)
    if os.geteuid() != 0:
        print("You need to run this command as root or with sudo.")
        sys.exit(1)
    import pathlib
    pathlib.Path("/etc/systemd/system").mkdir(parents=True, exist_ok=True)
    pathlib.Path("/etc/channeling").mkdir(parents=True, exist_ok=True)
    pathlib.Path("/var/lib/channeling").mkdir(parents=True, exist_ok=True)
    pathlib.Path("/var/log/channeling").mkdir(parents=True, exist_ok=True)
    with open("/etc/systemd/system/channeling.service","w+") as f:
        f.write(service_file_contents)


if __name__ == '__main__': # pragma: no cover
    cli()

