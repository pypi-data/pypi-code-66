#  Copyright (C) 2020 Jakub Smetana <jakub/AT/smetana/DOT/ml>
#  =========
#  SPDX-License-Identifier: MPL-2.0
#  ---------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#  =========

from mcdbot.mcdbot import Mcdbot
from discord import Member, User
from typing import Union


def check_user(main: Mcdbot, user: Union[Member, User]):
    if isinstance(user, Member):
        return True
    if main.main_guild.get_member(user.id) is not None:
        return True
    return False
