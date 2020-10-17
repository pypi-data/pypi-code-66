#  Copyright (C) 2020 Jakub Smetana <jakub/AT/smetana/DOT/ml>
#  =========
#  SPDX-License-Identifier: MPL-2.0
#  ---------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#  =========
from enum import Enum

from mcdbot.mcdbot import global_config
import aioredis


class UserStatus(Enum):
    OK = 0
    LOCKED = 1


class McStatus(Enum):
    ONLINE = 0
    OFFLINE = 1


class Redis(object):
    def __init__(self):
        self._redis = None

    async def start(self):
        self._redis = await aioredis.create_redis_pool(global_config.redis_url)

    async def stop(self):
        self._redis.close()
        await self._redis.wait_closed()

    @staticmethod
    def _key_user(user):
        return f"user:{user.id}"

    async def get_status(self, user):
        return await self._redis.hget(self._key_user(user), "status")

    async def get_mc_status(self, user):
        return await self._redis.hget(self._key_user(user), "mc-status")

    async def set_mc(self, user, status: McStatus, name, uuid):
        return await self._redis.hmset(self._key_user(user), {
            "mc-status": status.value,
            "mc-name": name,
            "mc-uuid": uuid
        })
