# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

"""Utilities for the GWDataFind Server
"""

import re
import threading
import time
from collections import defaultdict
from os.path import getmtime


from ligo.segments import (segment, segmentlist)

__author__ = 'Duncan Macleod <duncan.macleod@ligo.org>'


class FileManager(threading.Thread):
    """Common methods for caching files in memory
    """
    def sleep(self):
        """Wait until next iteration
        """
        self.logger.debug("sleeping for {0} seconds".format(self.sleeptime))
        start = time.time()
        while time.time() - start < self.sleeptime:
            time.sleep(.5)
            if self.shutdown:
                self.state = 'SHUTDOWN'
                return

    def run(self):
        """Continuously read and update the cache
        """
        last = 0
        while True:
            if self.shutdown:
                return

            try:
                mod = getmtime(self.path)
            except OSError as exc:
                self.logger.error("unable to determine modification time of "
                                  "{0}: {1}".format(self.path, str(exc)))
                mod = 0

            if last < mod:  # file changed since last iteration
                try:
                    self.parse()
                except (TypeError, ValueError) as exc:
                    self.logger.error("exception in parse{0}: {1}".format(
                        self.path, str(exc)))
                else:
                    last = time.time()
            else:
                self.logger.debug('cache file unchanged since last iteration')
            self.sleep()


class CacheManager(FileManager):
    """Thread to continuously update the diskcache in memory
    """
    def __init__(self, parent, path, sleeptime=60,
                 site_exclude=None, site_include=None,
                 frametype_exclude=None, frametype_include=None):
        super().__init__(name=type(self).__name__)
        self.path = path

        # create logger
        self.logger = parent.logger

        # create lock and flags
        self.lock = threading.Lock()
        self.shutdown = False
        self.ready = False

        # create cache
        self.cache = defaultdict(dict)

        # time between iterations
        self.sleeptime = sleeptime

        # record exclusion filters
        self.patterns = {key: self._parse_pattern(value) for key, value in [
             ('site_exclude', site_exclude),
             ('site_include', site_include),
             ('frametype_exclude', frametype_exclude),
             ('frametype_include', frametype_include),
        ]}

    @staticmethod
    def _parse_pattern(pattern):
        if pattern is None:
            pattern = []
        if not isinstance(pattern, list):
            pattern = [pattern]
        return [re.compile(reg) for reg in pattern]

    def _update(self, cache):
        self.logger.debug('updating frame cache with lock...')
        self.lock.acquire()
        self.cache = cache
        self.lock.release()
        self.logger.debug('updated frame cache with {} entries'.format(
            len(cache)))
        # self.logger.debug(str(cache))
        for ext in cache.keys():
            self.logger.info('{0:s} - {1:d}'.
                             format(ext, len(cache[ext])))  # extension eg gwf
        for site in cache[ext].keys():
            self.logger.info('{0:s} - {1:d}'.
                             format(site, len(cache[ext][site])))  # eg H, L
            for tag in cache[ext][site].keys():
                self.logger.info('{0:s} - {1:d}'.
                                 format(tag, len(cache[ext][site][tag])))
        self.logger.debug('lock released')

    def exclude(self, site, tag):
        """Return `True` if this site and tag combination should be excluded
        """
        for var, key in ((site, 'site'), (tag, 'frametype')):
            pat = '{0}_exclude'.format(key)
            for regex in self.patterns[pat]:
                if regex.search(var):  # positive match
                    return pat
            pat = '{0}_include'.format(key)
            for regex in self.patterns[pat]:
                if not regex.search(var):  # negative match
                    return pat

    def parse(self):
        """Read the frame cache from the path
        """
        self.logger.info('Parsing frame cache from {0}'.format(self.path))
        exclusions = {key: 0 for key in self.patterns}
        nlines = 0
        cache = {}

        with open(self.path, 'rb') as fobj:
            for line in fobj:
                site, tag, path, dur, ext, segments = self._parse_line(line)
                exclude = self.exclude(site, tag)
                if exclude:  # record why excluded
                    exclusions[exclude] += 1
                    continue
                cache.setdefault(ext, {})
                cache[ext].setdefault(site, {})
                cache[ext][site].setdefault(tag, {})
                cache[ext][site][tag][(path, int(dur))] = segments
                nlines += 1

        self.logger.info('Parsed {0} lines from frame cache file'.format(
            nlines))
        for key, count in exclusions.items():
            self.logger.debug('excluded {0} lines with {1}'.format(count, key))

        # store new cache
        self._update(cache)
        self.ready = True  # can now be used

    @staticmethod
    def _parse_line(line):
        """Parse one line from the frame cache file
        """
        try:
            if isinstance(line, bytes):
                line = line.decode('utf-8')

            # parse line
            header, modt, count, times = line.strip().split(' ', 3)
            hdr_list = header.split(',')
            # old style datafind files assume gwf
            if len(hdr_list) == 5:
                hdr_list.append('gwf')
            path, site, tag, _, dur, ext = tuple(hdr_list)

            # format times
            times = list(map(int, times[1:-1].strip().split(' ')))
            segments = segmentlist(map(
                segment, (times[i:i+2] for i in range(0, len(times), 2))))
        except Exception as ex:
            ermsg = 'Error parsing line "{0}"\n {1} - {2}'.\
                format(line, ex.__class__.name, str(ex))
            raise AssertionError(ermsg)
        return site, tag, path, dur, ext, segments


class GridmapManager(FileManager):
    """Thread to continuously update the grid-mapfile in memory
    """
    def __init__(self, parent, path, sleeptime=600):
        super().__init__(name=type(self).__name__)
        self.path = path

        # create logger
        self.logger = parent.logger

        # create lock and flags
        self.lock = threading.Lock()
        self.shutdown = False
        self.ready = False

        # create cache
        self.cache = []

        # time between iterations
        self.sleeptime = sleeptime

    def _update(self, cache):
        self.logger.debug('updating grid map cache with lock...')
        self.lock.acquire()
        self.cache = cache
        self.lock.release()
        self.logger.debug('updated grid map cache with {} entries'.format(
            len(cache)))
        # self.logger.debug(str(cache))
        self.logger.debug('lock released')

    def parse(self):
        """Read the grid-map file from the path
        """
        self.logger.info('Parsing grid map file from {0}'.format(self.path))
        nlines = 0
        cache = []

        with open(self.path, 'r') as fobj:
            for line in fobj:
                subject = self._parse_line(line)
                cache.append(subject)
                nlines += 1

        self.logger.info('Parsed {0} lines from grid map file'.format(nlines))

        # store new cache
        self._update(cache)
        self.ready = True  # can now be used

    @staticmethod
    def _parse_line(line):
        """Parse one line from the grid map file
        """
        parts = line.strip().split('"')
        if len(parts) in {2, 3}:
            return parts[1]
        if len(parts) == 1:
            return parts[0]
        raise RuntimeError("error parsing grid map file line: {!r}".format(
            line))
