"""
Global configuration.
"""


from channeling import singleton

from functools import wraps
import configparser
import json
import logging
import os
import time

log_path = '/var/log/channeling/channeling.log'

@singleton
class ChannelingConfig():
    logger = None
   
    def __init__(self):
        try:
            logger_handler = logging.FileHandler(log_path)
            using_file = True
        except PermissionError as e:
            using_file = False
            logger_handler = logging.StreamHandler()
        logger_fmt = logging.Formatter('%(message)s')
        logger_handler.setFormatter(logger_fmt)
        self.logger = logging.getLogger('channeling')
        self.logger.addHandler(logger_handler)
        self.logger.setLevel(logging.INFO)
        self.logger.debug("Loaded config singleton.")
        self.config = configparser.ConfigParser()
        self.config.read(self.config_path)
        self.logger.debug(json.dumps({
            'timestamp': str(time.time()),
            'type': 'conf',
            'content': 'Initiated config. Logging into {}'.format(
                log_path if using_file else 'stdout'
                )
            }))

    def __save(self):
        with open(self.config_path, 'w') as cf:
            self.config.write(cf)

    def __get_value(self, section, option):
        try:
            value = self.config.get(section, option)
        except (configparser.NoSectionError, configparser.NoOptionError) as e:
            value = input("Provide value for {}:{}\n".format(section,option))
            self.__set_value(section, option, value)
        return value
    def __set_value(self, section, option, value):
        self.logger.debug("Updating {}:{} value in config.".format(section, option))
        if not self.config.has_section(section):
            self.config[section] = {}
        self.config.set(section, option, value)
        self.__save()

    def debug(self, function):
        @wraps(function) # Needed to pass the doc string.
        def wrapper(*args, **kwargs):
            self.logger.debug(json.dumps({
                'timestamp': str(time.time()),
                'type': 'cmd',
                'content': function.__name__
                }))
            return function(*args, **kwargs)
        return wrapper

    @property
    def config_path(self):
        if os.path.isfile(os.path.expanduser("~/.channeling")):
            return os.path.expanduser("~/.channeling")
        return "/etc/channeling/channeling.conf"

    @property
    def discord_token(self, section="auth", option="discord_token"):
        return self.__get_value(section, option)
    @discord_token.setter
    def set_discord_token(self, value, section="auth", option="discord_token"):
        self.__set_value(section, option, value)

    @property
    def database_type(self, section="storage", option="database_type"):
        return self.__get_value(section, option)
    @database_type.setter
    def set_database_type(self, value, section="storage", option="database_type"):
        self.__set_value(section, option, value)

    @property
    def database_path(self, section="storage", option="database_path"):
        return self.__get_value(section, option)
    @database_type.setter
    def set_database_path(self, value, section="storage", option="database_path"):
        self.__set_value(section, option, value)

