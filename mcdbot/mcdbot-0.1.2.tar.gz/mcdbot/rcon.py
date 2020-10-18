#  Copyright (C) 2020 Jakub Smetana <jakub/AT/smetana/DOT/ml>
#  =========
#  SPDX-License-Identifier: MPL-2.0
#  ---------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#  =========

from mcdbot.mcdbot import global_config
from asyncrcon import AsyncRCON
from loguru import logger


class Rcon(object):
    def __init__(self):
        self._rcon = AsyncRCON(global_config.rcon_address, global_config.rcon_password)

    async def start(self):
        await self._rcon.open_connection()

    async def stop(self):
        self._rcon.close()

    async def authme_register(self, player, password):
        cmd = f"/authme register {player} {password}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/authme register {player} **** => '''{out}'''")

    async def authme_unregister(self, player):
        cmd = f"/authme unregister {player}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/authme register {player} **** => '''{out}'''")

    async def authme_password(self, player, password):
        cmd = f"/authme password {player} {password}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/authme password {player} **** => '''{out}'''")

    async def authme_lastlogin(self, player):
        cmd = f"/authme lastlogin {player}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/authme lastlogin {player} => '''{out}'''")

    async def authme_accounts(self, player):
        cmd = f"/authme accounts {player}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/authme accounts {player} => '''{out}'''")

    async def save_off(self):
        cmd = f"/save-off"
        out = await self._rcon.command(cmd)
        logger.debug(f"/save-off => '''{out}'''")

    async def save_on(self):
        cmd = f"/save-on"
        out = await self._rcon.command(cmd)
        logger.debug(f"/save-on => '''{out}'''")

    async def save_all_flush(self):
        cmd = f"/save-all flush"
        out = await self._rcon.command(cmd)
        logger.debug(f"/save-all flush => '''{out}'''")

    async def whitelist_add(self, entity: str):
        cmd = f"/whitelist add {entity}"
        out = await self._rcon.command(cmd)
        logger.debug(f"/whitelist add {entity} => '''{out}'''")
