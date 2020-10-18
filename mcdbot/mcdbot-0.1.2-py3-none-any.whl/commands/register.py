#  Copyright (C) 2020 Jakub Smetana <jakub/AT/smetana/DOT/ml>
#  =========
#  SPDX-License-Identifier: MPL-2.0
#  ---------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#  =========

from discord import Message

from mcdbot.errors.http_like_errors import ForbiddenError
from mcdbot.helpers import check_user
from mcdbot.mcdbot import Mcdbot
from mcdbot.redis import McStatus
from mcdbot.uuid import format_uuid, get_offline_player_uuid


async def register(main: Mcdbot, msg: Message, player: str, password: str = None):
    if check_user(main, msg.author):
        if await main.redis.get_mc_status(msg.author) is None:
            if password is None:
                status = McStatus.ONLINE
                profile = await main.mojang_api.get_profile(player)
                uuid = format_uuid(profile['id'])
                player = profile['name']
            else:
                status = McStatus.OFFLINE
                uuid = get_offline_player_uuid(player)
                main.rcon.authme_register(player, password)

            main.rcon.whitelist_add(uuid)

            if not await main.redis.set_mc(msg.author, status, player, uuid):
                raise RuntimeError
            else:
                return f"[OK] Registered player '{player}'" \
                       f"({'online' if status == McStatus.ONLINE else 'offline'} account)."
    else:
        raise ForbiddenError
