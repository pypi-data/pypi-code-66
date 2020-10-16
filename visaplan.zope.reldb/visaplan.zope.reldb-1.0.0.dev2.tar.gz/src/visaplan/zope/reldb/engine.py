# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79
# Python compatibility:
from __future__ import absolute_import

# Setup tools:
import pkg_resources

# Standard library:
from os.path import abspath

# Zope:
from App.config import getConfiguration as zope_getConfiguration
from zope.sqlalchemy import register

# 3rd party:
from sqlalchemy import create_engine
from sqlalchemy.exc import (
    DatabaseError,
    DBAPIError,
    OperationalError,
    SQLAlchemyError,
    )
from sqlalchemy.orm import scoped_session, sessionmaker

# Local imports:
from . import get_dsn

# Logging / Debugging:
from logging import getLogger

logger = getLogger('visaplan.zope.reldb.engine')


__all__ = [
        'engine',
        'DBSession',
        ]

# We try to provide useful error messages
# for database configuration problems ...

DB_CONNECT = get_dsn()
if DB_CONNECT:
    try:
        logger.info('Creating DB engine from DSN %(DB_CONNECT)r ...', locals())
        engine = create_engine(DB_CONNECT)
    except SQLAlchemyError as e:
        logger.error('Data source name (DSN) is probably wrong!')
        logger.exception(e)
        for ec in (OperationalError, DatabaseError, DBAPIError):
            if isinstance(e, ec):
                logger.info('This is a(n) %r', (ec.__name__,))
        engine = None
        DBSession = None
    else:
        logger.info('OK: DB engine is %(engine)r', locals())
        # https://pypi.org/project/zope.sqlalchemy/#full-example
        # "... we must use scoped sessions":
        DBSession = scoped_session(sessionmaker(bind=engine))
else:
    logger.error('No Data source name found! (zope.conf; <product-config reldb>)')
    engine = None
    DBSession = None
