# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79

# Python compatibility:
from __future__ import absolute_import

# Zope:
from zope.sqlalchemy import register

# Local imports:
from .engine import DBSession

if DBSession is not None:
    register(DBSession)
