"""
Batteries included. Classes and functions for manipulating users, guilds, channels and currency.
"""
from channeling import ChannelingException
from channeling import message_formatting as mf
from channeling import tools
from channeling.config import ChannelingConfig
from channeling.database import Database

from datetime import datetime
from random import random
import discord
import humanize
import json
import shlex
import time

conf = ChannelingConfig()

channel_price = 5000
channel_init_power = 2000
maintenance_cost = 2000
claim_price = 2000

class PowerEntity():

    uuid = None
    power = 0

    def __str__(self):
        return "Not implemented yet."

    def power_generate(self, power):
        if not self.uuid: return False
        self.load()
        self.power += power
        self.save()

    def power_burn(self, power):
        if not self.uuid: return False
        if power < 0: return False
        if self.power < power: return False
        self.load()
        self.power -= power
        self.save()
        return True

    def save(self):
        pass

    def from_tag(message, tag):
        entity_id = tools.generic_id_from_tag(tag)
        entity = None
        if entity_id['type'] == 'user':
            entity = User(entity_id['id'], message.guild.id)
        elif entity_id['type'] == 'channel':
            entity = Channel(entity_id['id'])
        return entity
 


class Guild():
    guild_id = None
    prefix = "ch"
    category_id = None
    items = {}

    def __init__(self, guild_id):
        if guild_id:
            self.load(guild_id)

    def load(self, guild_id=None):
        if guild_id: self.guild_id = guild_id
        with Database() as c:
            c.execute('INSERT OR IGNORE INTO guilds VALUES (?, "ch", NULL, "{}")', (self.guild_id,))
            c.execute("SELECT * FROM guilds WHERE guild_id=?", (self.guild_id,))
            self.guild_id, self.prefix, self.category_id, items_json = c.fetchone()
            self.items = json.loads(items_json)

    def save(self):
        with Database() as c:
            c.execute("""
                INSERT OR IGNORE INTO guilds VALUES(?, ?, ?, ?)
                """, (
                self.guild_id,
                self.prefix,
                self.category_id,
                json.dumps(self.items),
                ))
            c.execute("""
                UPDATE guilds SET prefix=?, category_id=?, items=?
                WHERE guild_id=?
                """, (
                self.prefix,
                self.category_id,
                json.dumps(self.items),
                self.guild_id,
                ))



class Channel(PowerEntity):
    channel_id = None
    uuid = None
    guild_id = None
    power = 0
    created = 0
    maintenance = 0
    items = {}

    def __init__(self, channel_id):
        self.load(channel_id)


    def __str__(self):
        if not self.uuid:
            return "{} 📦{}".format(
                self.get_tag(),
                self.items.get('power_packs', 0),
                )
        return "{} 🔋{} 📦{}\nOwner: {}\nCreated: {}\nNext maintenance: {}".format(
                self.get_tag(),
                self.power,
                self.items.get('power_packs', 0),
                self.get_owner_tag(),
                humanize.naturaltime(datetime.fromtimestamp(self.created)),
                humanize.naturaltime(datetime.fromtimestamp(self.maintenance)),
                )
    
    def load(self, channel_id=None):
        if channel_id: self.channel_id = str(channel_id)
        with Database() as c:
            c.execute("SELECT * FROM channels WHERE channel_id=?", (self.channel_id,))
            data = c.fetchone()
            if data:
                self.channel_id, self.uuid, self.guild_id, self.power, self.created, self.maintenance, items_json = data
                self.items = json.loads(items_json)

    def save(self):
        with Database() as c:
            c.execute("""
                INSERT OR IGNORE INTO channels VALUES(?, ?, ?, ?, ?, ?, ?)
                """, (
                self.channel_id,
                self.uuid,
                self.guild_id,
                self.power,
                self.created,
                self.maintenance,
                json.dumps(self.items),
                ))
            c.execute("""
                UPDATE channels SET uuid=?, guild_id=?, power=?, created=?, maintenance=?, items=?
                WHERE channel_id=?
                """, (
                self.uuid,
                self.guild_id,
                self.power,
                self.created,
                self.maintenance,
                json.dumps(self.items),
                self.channel_id,
                ))

    def get_tag(self):
        return tools.tag_from_channel_id(self.channel_id)
    
    def get_owner_tag(self):
        return tools.tag_from_uuid(self.uuid)

    def harvest(self, amount=None):
        try:
            amount = int(amount)
        except ValueError as e:
            return False
        self.load()
        if amount == None or amount > self.power:
            amount = self.power
        if amount <= 0: return False
        owner = User(self.uuid, self.guild_id)
        harvested_power = inefficiency(amount)
        owner.power_generate(harvested_power)
        self.power_burn(amount)
        return harvested_power 



class User(PowerEntity):
    uuid = None
    guild_id = None
    power = 0
    active_1 = 0
    active_10 = 0
    items = {}

    def __init__(self, uuid=None, guild_id=None):
        if uuid and guild_id:
            self.load(uuid, guild_id)
    
    def load(self, uuid=None, guild_id=None):
        if uuid: self.uuid = str(uuid)
        if guild_id: self.guild_id = str(guild_id)
        with Database() as c:
            c.execute('INSERT OR IGNORE INTO users VALUES (?, ?, 0, 0, 0, "{}")', (self.uuid, self.guild_id))
            c.execute("SELECT * FROM users WHERE uuid=? AND guild_id=?;", (self.uuid, self.guild_id))
            self.uuid, self.guild_id, self.power, self.active_1, self.active_10, items_json = c.fetchone()
            self.items = json.loads(items_json)
    
    def save(self):
        with Database() as c:
            c.execute("""
                INSERT OR IGNORE INTO users VALUES(?, ?, ?, ?, ?, ?)
                """, (
                self.uuid,
                self.guild_id,
                self.power,
                self.active_1,
                self.active_10,
                json.dumps(self.items),
                ))
            c.execute("""
                UPDATE users SET power=?, active_1=?, active_10=?, items=?
                WHERE uuid=? AND guild_id=?
                """, (
                self.power,
                self.active_1,
                self.active_10,
                json.dumps(self.items),
                self.uuid,
                self.guild_id,
                ))

    def __str__(self):
        channels = self.get_channel_tags()
        last_active_timestamp = max(self.active_1, self.active_10)
        last_active = "Never"
        if last_active_timestamp:
            last_active = humanize.naturaltime(datetime.fromtimestamp(last_active_timestamp))
        return "{} 🔋{}\nOwns channels: {}\nLast power earned: {}".format(
                self.get_tag(),
                self.power,
                " ".join(channels) if channels else "None",
                last_active,
                )

    def set_active_1(self, t):
        self.load()
        self.active_1 = t
        self.save()

    def set_active_10(self, t):
        self.load()
        self.active_10 = t
        self.save()
    
    def get_tag(self):
        return tools.tag_from_uuid(self.uuid)
    
    def get_channel_ids(self):
        channels = []
        with Database() as c:
            c.execute("SELECT channel_id FROM channels WHERE uuid=? AND guild_id=?;", (self.uuid, self.guild_id))
            channels = list(map(lambda x: x[0], c.fetchall()))
        return channels

    def get_channel_tags(self):
        return list(map(lambda x: tools.tag_from_channel_id(x), self.get_channel_ids()))

    async def talk(self, message):
        msg_time = message.created_at.timestamp()
        chan = Channel(message.channel.id)
        multiplier = 1
        if chan.uuid == str(message.author.id):
            return
        if chan.uuid:
            multiplier = 2
            if chan.maintenance < msg_time:
                chan.load()
                chan.power -= maintenance_cost
                chan.maintenance = msg_time + 7*24*60*60
                chan.save()
                if chan.power <= 0:
                    owner = User(chan.uuid, message.guild.id)
                    return await message.channel.send(
                        mf.warn("{} your channel is underpowered and can be claimed!".format(
                            owner.get_tag()
                            )))
            if chan.power < 0:
                return
        if msg_time - self.active_1 >= 60:
            self.set_active_1(msg_time)
            self.power_generate(1 * multiplier)
            chan.power_generate(1)
            return await drop_power_pack(message)
        if msg_time - self.active_10 >= 10*60:
            self.set_active_10(msg_time)
            self.power_generate(50 * multiplier)
            chan.power_generate(50)
            return await drop_power_pack(message)

async def drop_power_pack(message):
    if random() < 0.95: return
    chan = Channel(message.channel.id)
    chan.items['power_packs'] = chan.items.get('power_packs', 0) + 1
    chan.save()
    return await message.channel.send(mf.info("🔋📦 - use grab to get some powah!"))

def inefficiency(amount):
    return int(amount * (0.2 + 0.6 * random()))

@conf.debug
async def cmd_set(message):
    """Set variables to new values.
    Usage: `set VARIABLE VALUE`
    """
    line = shlex.split(message.content)
    if len(line) != 4:
        return await message.channel.send(
            mf.error("Bad arguments. Use 'help set' to see usage."))
    variable = line[2]
    new_value = line[3]
    if variable == 'prefix':
        guild = Guild(message.guild.id)
        guild.prefix = new_value
        guild.save()
        return await message.channel.send(
                mf.info("Prefix is now set to: {}".format(new_value)))
    return await message.channel.send(
        mf.error("Unknown variable {}. Use 'help set' to see usage.".format(variable)))


@conf.debug
async def cmd_stats(message):
    """Deprecated. Same as `info`."""
    await message.channel.send(mf.info("`stats` command is deprecated and will be removed in the future. Use `info` instead."))
    return await cmd_info(message)

@conf.debug
async def cmd_info(message):
    """Display information about user or channel.
    Usage: `info [USER_TAG | CHANNEL_TAG]`
    If you omit tag argument, your user info will be shown.
    """
    line = shlex.split(message.content)
    entity = None
    if len(line) == 2:
        entity = User(message.author.id, message.guild.id)
    elif len(line) == 3:
        entity = PowerEntity.from_tag(message, line[2])
    if not entity:
        return await message.channel.send(mf.error("Bad arguments. Use `help info` for more info."))
    return await message.channel.send(mf.info(str(entity)))


#
# Channel actions
#
async def channel_error_message(message):
    return await message.channel.send(mf.error("Bad arguments or unknown channel sub-command. Use `help channel` for more info"))
async def channel_unknown_message(message):
    return await message.channel.send(mf.warn("This channel is uncharted."))

async def channel_make(message):
    user = User(message.author.id, message.guild.id)
    line = shlex.split(message.content)
    if user.power < channel_price:
        return await message.channel.send(
            mf.warn("You need to have {} 🔋 to make a channel.".format(channel_price)))
    guild = Guild(message.guild.id)
    category = discord.utils.find(
            lambda c: str(c.id) == guild.category_id, message.guild.categories)
    if not category:
        category = await message.guild.create_category("🔋Channeling", reason="Channeling bot.")
        guild.category_id = str(category.id)
        guild.save()
    channel_name = '-'.join(message.author.name.split())
    if len(line) > 3:
        channel_name = "-".join(line[3:])
    new_channel = await message.guild.create_text_channel(channel_name, category=category, reason="Channeling bot: {}".format(message.author.name))
    if not new_channel:
        return await message.channel.send(mf.error("Created a Non channel....."))
    if not user.power_burn(channel_price):
        return await message.channel.send(mf.error("Could not make new channel."))
    chan = Channel(new_channel.id)
    now = time.time()
    chan.uuid = user.uuid
    chan.guild_id = user.guild_id
    chan.created = now
    chan.maintenance = now + 7*24*60*60
    chan.save()
    chan.power_generate(channel_init_power)
    return await message.channel.send(mf.info("{} created channel {}".format(
        user.get_tag(),
        chan.get_tag(),
        )))

async def channel_info(message):
    line = shlex.split(message.content)
    if len(line) != 3:
        return await channel_error_message(message)
    entity = Channel(message.channel.id)
    return await message.channel.send(mf.info(str(entity)))

async def channel_harvest(message):
    line = shlex.split(message.content)
    chan = Channel(message.channel.id)
    if not chan.uuid: return await channel_unknown_message(message)
    if chan.uuid != str(message.author.id):
        return await message.channel.send(mf.warn("Only channel owner can harvest power."))
    if chan.power <= 0:
        return await message.channel.send(mf.info("There is no power to be harvested."))
    if len(line) != 4:
        return await channel_error_message(message)
    amount = None
    try:
        amount = int(line[3])
    except ValueError as e:
        return await channel_error_message(message)
    if amount == None: amount = chan.power
    harvested_power = chan.harvest(amount)
    return await message.channel.send(mf.info(
        "Harvested {} out of {} 🔋.".format(harvested_power, amount)))

async def channel_attack(message):
    line = shlex.split(message.content)
    chan = Channel(message.channel.id)
    user = User(message.author.id, message.guild.id)
    if user.power <= 0:
        return await message.channel.send(mf.warn("You are powerless!"))
    amount = None
    if not chan.uuid:
        return await channel_unknown_message(message)
    if user.uuid == chan.uuid:
        return await message.channel.send(mf.warn("This is your own channel, silly!"))
    if len(line) > 4:
        return await channel_error_message(message)
    if len(line) == 3:
        amount = int(chan.power/0.8)
    if len(line) == 4:
        try:
            amount = int(line[3])
        except ValueError as e:
            return await channel_error_message(message)
    amount = min(amount, user.power)
    if not amount or amount <= 0:
        return await channel_error_message(message)
    if chan.power <= 0:
        return await message.channel.send(
                mf.info("The channel is unpowered. You can claim it now."))
    user.power_burn(amount)
    burned = inefficiency(amount)
    if burned > chan.power:
        chan.load()
        chan.power -= burned
        chan.save()
    else:
        chan.power_burn(burned)
    return await message.channel.send(mf.info(
        "{} WARNING\n{} burned 🔋{} from channel.{}".format(
            tools.tag_from_uuid(chan.uuid),
            user.get_tag(),
            burned,
            "" if chan.power>0 else "\n**Channel power is down!**"*3,
            )))


async def channel_claim(message):
    chan = Channel(message.channel.id)
    user = User(message.author.id, message.guild.id)
    if chan.uuid:
        if chan.uuid == user.uuid:
            return await message.channel.send(mf.warn("You already own this channel."))
        if chan.power > 0:
            return await message.channel.send(mf.warn(
                "Channel is still powered. Use `channel attack`."))
    if user.power < claim_price:
        return await message.channel.send(mf.warn(
            "You need 🔋{} to claim a channel.".format(claim_price)))
    now = time.time()
    chan.uuid = user.uuid
    chan.guild_id = user.guild_id
    chan.created = now
    chan.maintenance = now + 7*24*60*60
    chan.save()
    chan.power = channel_init_power
    chan.save()
    user.power_burn(claim_price)
    return await message.channel.send(mf.info(
        "All bow to {} the new owner of {}.".format(
            user.get_tag(),
            chan.get_tag(),
            )))


async def channel_transfer(message):
    line = shlex.split(message.content)
    if len(line) != 4:
        return await channel_error_message(message)
    chan = Channel(message.channel.id)
    if not chan.uuid: return await channel_unknown_message(message)
    if chan.uuid != str(message.author.id):
        return await message.channel.send(mf.error("Only channel owner can transfer channel."))
    new_owner_id = tools.uuid_from_tag(line[3])
    if not new_owner_id:
        return await channel_error_message(message)
    chan.uuid = new_owner_id
    chan.save()
    return await message.channel.send(mf.info("Channel transfered to {}.".format(line[3])))

@conf.debug
async def cmd_channel(message):
    """Channel command.
    You can create your personal channel. People that talk in it generate 🔋 for themselves as well as channel itself. Owner can then harvest 🔋 from their channel.
    Channels owner does not generate power while talking in their own channel to prevent spam for stonks.
    The channel gets locked down every week unless it has enough power in it to pay maintenance costs.
    
    Usage:
    `channel info` - Same as `info CHANNEL_TAG`.
    `channel make [channel name]` - Make a new channel.
    `channel claim` - Claim existing channel without owner or powerless channel.
    `channel attack [AMOUNT]` - Use AMOUNT of your own 🔋 to burn part of enemy channel's 🔋.
    `channel harvest [AMOUNT]` - Harvest power from owned channel with random efficiency.
    `channel transfer USER_TAG` - Transfer channel to new user.
    """
    line = shlex.split(message.content)
    if len(line) <= 2:
        return await channel_error_message(message)
    subcommand = line[2]
    chan = Channel(message.channel.id)
    if not chan.uuid and not subcommand in ('make', 'claim', 'info'):
        return await channel_unknown_message(message)
    if subcommand == 'info':
        return await channel_info(message)
    if subcommand == 'make':
        return await channel_make(message)
    if subcommand == 'claim':
        return await channel_claim(message)
    elif subcommand == 'harvest':
        return await channel_harvest(message)
    elif subcommand == 'transfer':
        return await channel_transfer(message)
    elif subcommand == 'attack':
        return await channel_attack(message)
    return await channel_error_message(message)

@conf.debug
async def cmd_grab(message):
    """Grab power pack dropped in the channel.
    Usage: `grab`
    """
    chan = Channel(message.channel.id)
    if chan.items.get('power_packs', 0) <= 0:
        return await message.channel.send(
            mf.warn("Nothing to grab."))
    chan.items['power_packs'] = chan.items.get('power_packs', 0) - 1
    chan.save()
    power_up = int(random() * 400 + 100)
    user = User(message.author.id, message.guild.id)
    user.power_generate(power_up)
    return await message.channel.send(
        mf.info("Ha! Free energy! {} just got {}🔋.".format(
            user.get_tag(),
            power_up
            )))


#
# Currency actions
#
@conf.debug
async def cmd_power(message):
    """Transfer power cells to another user or channel.
    Usage: `power AMOUNT (USER_TAG | CHANNEL_TAG)`
    Amounts can only be positive integers.
    """
    line = shlex.split(message.content)
    if len(line) != 4:
        return await message.channel.send(
            mf.error("Bad arguments. Use 'help power' to see usage."))
    try:
        amount = int(line[2])
    except ValueError as e:
        return await message.channel.send(
            mf.error("Bad arguments. Use 'help power' to see usage."))
    recipient = PowerEntity.from_tag(message, line[3])
    if type(recipient) == User and recipient.uuid == message.author.id:
        return await message.channel.send(
            mf.error("Tryin to be smart again, Zanny boi?"))
    if not amount or not recipient or amount <= 0:
        return await message.channel.send(
            mf.error("Bad arguments. Use 'help power' to see usage."))
    payer = User(message.author.id, message.guild.id)
    if payer.power_burn(amount):
        recipient.power_generate(amount)
        return await message.channel.send(mf.info("{} powered up {} with 🔋{}".format(
            payer.get_tag(), recipient.get_tag(), amount)))
    return await message.channel.send(mf.warn("Insufficient power."))


#
# Database table definitions
#
def __db_init__():
    with Database() as c:
        c.execute("""
            CREATE TABLE IF NOT EXISTS guilds (
                guild_id TEXT PRIMARY KEY,
                prefix TEXT DEFAULT "ch",
                category_id TEXT,
                items TEXT
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                uuid TEXT NOT NULL,
                guild_id TEXT NOT NULL,
                power INT DEFAULT 0,
                active_1 FLOAT DEFAULT 0,
                active_10 FLOAT DEFAULT 0,
                items TEXT,
                PRIMARY KEY (uuid, guild_id)
            )
        """)
        c.execute("""
            CREATE TABLE IF NOT EXISTS channels (
                channel_id TEXT NOT NULL PRIMARY KEY,
                uuid TEXT,
                guild_id TEXT NOT NULL,
                power INT DEFAULT 1,
                created INT DEFAULT 0,
                maintenance INT DEFAULT 0,
                items TEXT
            )
        """)

