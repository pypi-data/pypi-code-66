# -*- coding: utf-8 -*- äöü vim: ts=8 sts=4 sw=4 si et tw=79

# Python compatibility:
from __future__ import absolute_import

# 3rd party:
from sqlalchemy import MetaData, inspect

# Local imports:
from .engine import DBSession, engine
from .sql import delete as DELETE
from .sql import generate_dicts
from .sql import insert as INSERT
from .sql import query as QUERY
from .sql import select as SELECT
from .sql import update as UPDATE

# Logging / Debugging:
from logging import getLogger

logger = getLogger('visaplan.zope.reldb.legacy')

if engine is not None:
    inspector = inspect(engine)
    metadata = MetaData(bind=engine)


class SQLWrapper(object):
    """
    Ersetzt den bisherigen Adapter sqlwrapper
    """

    def __init__(self, *args, **kwargs):
        """
        This class is aimed as a drop-in replacement for the functionality
        provided by visaplan.plone.sqlwrapper; therefore, the constructor
        needs to accept a contxt argument
        (regardless of the fact that it is probably never used).

        So, currently all additional arguments are ignored!
        This might change; there might be e.g. some possibility to specify
        a default schema / search path somehow (most likely using a
        keyword-only argument).
        """
        if DBSession is None:
            raise ValueError('No Data Source Name (DSN) configured! '
                    '(zope.conf; <product-config reldb>)')
        self.session = DBSession()

    def __enter__(self):
        self.connection = self.session #.begin()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        pass

    def insert(self, *args, **kwargs):
        """
        INSERT
        """
        returning = kwargs.get('returning')
        mask, query_data = INSERT(*args, **kwargs)
        res = self.connection.execute(mask, query_data)
        if returning:
            return generate_dicts(res)
        else:
            return res

    def update(self, *args, **kwargs):
        """
        """
        returning = kwargs.get('returning')
        mask, query_data = UPDATE(*args, **kwargs)
        res = self.connection.execute(mask, query_data)
        if returning:
            return generate_dicts(res)
        else:
            return res

    def delete(self, *args, **kwargs):
        """
        """
        returning = kwargs.get('returning')
        mask, query_data = DELETE(*args, **kwargs)
        res = self.connection.execute(mask, query_data)
        if returning:
            return generate_dicts(res)
        else:
            return res

    def select(self, *args, **kwargs):
        """
        Construct a SELECT query and generate the results
        """
        maxrows = kwargs.pop('maxrows', None)
        if maxrows is not None:
            logger.warn("Currently we don't do anything about maxrows!"
                        ' (%(maxrows)r)', locals())
        mask, query_data = SELECT(*args, **kwargs)
        res = self.connection.execute(mask, query_data)
        for row in generate_dicts(res):
            yield row

    def query(self, clause, *args, **kwargs):
        """
        Construct a SELECT query and generate the results
        """
        maxrows = kwargs.pop('maxrows', None)
        if maxrows is not None:
            logger.warn("Currently we don't do anything about maxrows!"
                        ' (%(maxrows)r)', locals())
        mask, query_data = QUERY(*args, **kwargs)
        res = self.connection.execute(mask, query_data)
        for row in generate_dicts(res):
            yield row
