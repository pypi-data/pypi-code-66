# -*- coding: utf-8 -*-
# Copyright (2019) Cardiff University
# Licensed under GPLv3+ - see LICENSE

"""The GWDataFind server app
"""

import time

from configobj import ConfigObj
import logging

from flask import Flask

from .cache import CacheManager, GridmapManager
from .config import get_config_path

from . import views

__version__ = '1.0.1'


class DataFlask(Flask):
    def __init__(self, import_name, configpath, *args, **kwargs):
        super().__init__(import_name, *args, **kwargs)
        self.logger.setLevel(logging.INFO)
        lfh = logging.FileHandler('/tmp/gwdatafind.log', mode='w')
        self.logger.addHandler(lfh)

        self.config.update(ConfigObj(configpath))

        # create thread to read cache file and start
        CacheMan = self._init_cache_manager(self.config)
        CacheMan.setDaemon(True)
        CacheMan.start()

        # create thread to read grid map file and start
        GridMapMan = self._init_gridmap_manager(self.config)
        GridMapMan.setDaemon(True)
        GridMapMan.start()

    def _init_cache_manager(self, conf):
        section = conf['LDRDataFindServer']
        cachefile = section['framecachefile']
        patterns = {
            key.rsplit('_', 1)[0]: section[key] for
            key in section.keys() if key.endswith('_pattern')
        }
        sleeptime = float(section.get('framecachetimeout', 60))
        self.cache_manager = CacheManager(self, cachefile, sleeptime=sleeptime,
                                          **patterns)
        return self.cache_manager

    def _init_gridmap_manager(self, conf):
        section = conf['LDRDataFindServer']
        gridmapfile = section['gridmapcachefile']
        sleeptime = float(section.get('gridmapcachetimeout', 600))
        self.gridmap_manager = GridmapManager(self, gridmapfile,
                                              sleeptime=sleeptime)
        return self.gridmap_manager

    def get_cache_data(self, *keys):
        self.logger.info('get_cache_data - keys: {0}'.format(keys))
        while not self.cache_manager.ready:
            # cache file is not ready
            self.logger.debug("Waiting for frame cache...")
            time.sleep(.5)
        self.cache_manager.lock.acquire()
        try:
            return self._get_cache_data(keys)
        finally:
            self.cache_manager.lock.release()

    def _get_cache_data(self, keys):
        keys = list(keys)
        last = keys.pop(-1)
        if not keys:
            return self.cache_manager.cache.get(last, {})
        ent = self.cache_manager.cache.get(keys.pop(0), {})
        for key in keys:
            ent = ent[key]
        return ent.get(last, {})

    def get_gridmap_data(self):
        self.logger.info('get_gridmap_data')
        while not self.gridmap_manager.ready:
            # cache file is not ready
            self.logger.debug("Waiting for gridmap cache...")
            time.sleep(.5)
        self.gridmap_manager.lock.acquire()
        try:
            return self.gridmap_manager.cache
        finally:
            self.gridmap_manager.lock.release()

    def shutdown(self):
        self.cache_manager.lock.acquire()
        self.gridmap_manager.lock.acquire()
        self.cache_manager.shutdown = True
        self.gridmap_manager.shutdown = True
        self.cache_manager.lock.release()
        self.gridmap_manager.lock.release()
        self.cache_manager.join()
        self.gridmap_manager.join()


def create_app():
    """Create an instance of the application
    """
    app = DataFlask(__name__, get_config_path())
    config_path = get_config_path()
    app = DataFlask(__name__, config_path)
    app.logger.setLevel(logging.INFO)
    app.register_blueprint(views.blueprint)
    app.logger.info('Config path: {0} name: {1}'.format(config_path, __name__))
    return app
