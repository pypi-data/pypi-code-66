# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import cProfile
import pstats
try:
    from StringIO import StringIO  # for Python 2
except ImportError:
    from io import StringIO  # for Python 3

from timeit import default_timer as timer
from django.db import connection, reset_queries
from django.core.exceptions import ImproperlyConfigured

"""
Example:


from django_profiler.profile import Profiler

with Profiler(name='my-profiler', lines_limit=10):
    print("Hello World!")

Output:
# Hello World!
#
# Profiler: my-profiler
# 
# Number of Queries : 0
# Finished in : 0.00s
#          2 function calls in 0.000 seconds
# 
#    Ordered by: cumulative time
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 profiling.py:45(__exit__)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#
"""


class Profiler(object):
    def __init__(self, name=None, sort='cumulative', lines_limit=None):
        self.name = name
        self.start_queries = 0
        self.sort = sort
        self.pr = cProfile.Profile()
        self.lines_limit = lines_limit
        self.django_is_configured = True
        try:
            len(connection.queries)
        except ImproperlyConfigured:
            self.django_is_configured = False
        else:
            self.django_is_configured = True

    def __enter__(self):
        if self.django_is_configured:
            reset_queries()
            self.start_queries = len(connection.queries)
        else:
            self.start_queries = 0
        self.start = timer()
        self.pr.enable()

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.pr.disable()
        s = StringIO()
        ps = pstats.Stats(self.pr, stream=s).sort_stats(self.sort)
        end = timer()
        if self.django_is_configured:
            end_queries = len(connection.queries)
        else:
            end_queries = 0
        print("\nProfiler: {}\n".format(self.name))
        print("Number of Queries : {}".format(end_queries - self.start_queries))
        print("Finished in : {:.2f}s".format(end - self.start))
        ps.print_stats(self.lines_limit)
        print(s.getvalue())
