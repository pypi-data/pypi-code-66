#  Copyright (C) 2020 Jakub Smetana <jakub/AT/smetana/DOT/ml>
#  =========
#  SPDX-License-Identifier: MPL-2.0
#  ---------
#  This Source Code Form is subject to the terms of the Mozilla Public
#  License, v. 2.0. If a copy of the MPL was not distributed with this
#  file, You can obtain one at https://mozilla.org/MPL/2.0/.
#  =========

from mcdbot.config import Config, default_config_obj
from mcdbot.mcdbot import Mcdbot
import json
import sys
from loguru import logger


if __name__ == '__main__':
    logger.info("Starting up...")
    path = 'mcdbot_config.json'
    try:
        path = sys.argv[1]
    except IndexError:
        pass

    try:
        config = Config(**json.load(open(path, 'r')))
    except FileNotFoundError:
        json.dump(default_config_obj, open(path, 'w'))
        raise RuntimeError("Please configure me in the newly created file.")

    Mcdbot(config).run()
