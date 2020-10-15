#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

TELEPORT_SHA = "786e399511525889778d2a3e64bc5d18f7ecddf6eaac684c224249657f404b76" \
    if os.getenv("ALLOENV") == "TEST" \
    else "996d90b8691278667a3b08d9869fca77a0474fe9d0eefa7001a9bfd43a9ddcc2"

ALLO_INFO_PATH = '/tmp/allo-infos.yml'

CONFIG_PATH = "/etc/allo-config.dict"

ALLO_URL = "10.81.41.1:3025" \
    if os.getenv("ALLOENV") == "TEST" \
    else "teleport.libriciel.fr:443"

API_PATH = "https://{}/v1/webapi".format("10.81.41.1:3080") \
    if os.getenv("ALLOENV") == "TEST" \
    else "https://{}/api/client".format(ALLO_URL)

CODEPRODUIT = {
    "i-Parapheur": "IP",
    "Pastell": "PA"
}
