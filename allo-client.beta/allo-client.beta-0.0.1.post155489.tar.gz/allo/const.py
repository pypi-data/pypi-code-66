#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import os

ALLO_INFO_PATH = '/tmp/allo-infos.yml'

CONFIG_PATH = "/etc/allo-config.dict"

ALLO_URL = "10.81.41.1:3025" \
    if os.getenv("ALLOENV") == "TEST" \
    else "allo.dev.libriciel.fr:443"

API_PATH = "https://{}/v1/webapi".format("10.81.41.1:3080") \
    if os.getenv("ALLOENV") == "TEST" \
    else "https://{}/api/client".format(ALLO_URL)

CODEPRODUIT = {
    "i-Parapheur": "IP",
    "Pastell": "PA"
}
