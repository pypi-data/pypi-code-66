#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""A wrapper class for the mops database"""
import os
import sys

PACKAGE_PARENT = ".."
SCRIPT_DIR = os.path.dirname(
    os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__)))
)  # isort:skip # noqa # pylint: disable=wrong-import-position
sys.path.append(
    os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT))
)  # isort: skip # noqa # pylint: disable=wrong-import-position

import tinydb  # type: ignore # isort: skip # noqa # pylint: disable=wrong-import-position


class MopsDB():

    def __init__(self, db_path):
        self._db = tinydb.TinyDB(db_path + "mop_db.json")

    def join(self, mop):
        mop_key = self._db.insert(mop.__dict__)
        mop.key = mop_key
        self._db.update(mop, doc_key=[mop_key])
        return mop_key

    def fetch(self, mop_key):
        return self._db.get(doc_key=mop_key)
