"""
Discord tools.
"""

import re

def uuid_from_tag(tag):
    m = re.match('<@!?([0-9]{18})>', tag)
    if m:
        return m.groups()[0]
    return None

def tag_from_uuid(uuid):
    return "<@!{}>".format(uuid)

def channel_id_from_tag(tag):
    m = re.match('<#([0-9]{18})>', tag)
    if m:
        return m.groups()[0]
    return None

def tag_from_channel_id(channel_id):
    return "<#{}>".format(channel_id)

def generic_id_from_tag(tag):
    generic_id = uuid_from_tag(tag)
    if generic_id: return { 'type': 'user', 'id': generic_id }
    generic_id = channel_id_from_tag(tag)
    if generic_id: return { 'type': 'channel', 'id': generic_id }
    return None

