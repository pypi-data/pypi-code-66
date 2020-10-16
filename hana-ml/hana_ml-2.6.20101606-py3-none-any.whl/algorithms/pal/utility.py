"""
This module contains Python API of utility functions.
"""
try:
    import configparser
except ImportError:
    import ConfigParser as configparser
import logging

#pylint: disable=bare-except

class Settings:
    """
    Configuration of logging level
    """
    settings = None
    user = None
    @staticmethod
    def load_config(config_file):
        """
        Load HANA credentials.
        """
        Settings.settings = configparser.ConfigParser()
        Settings.settings.read(config_file)
        try:
            url = Settings.settings.get("hana", "url")
        except:
            url = ""
        try:
            port = Settings.settings.getint("hana", "port")
        except:
            port = 0
        try:
            pwd = Settings.settings.get("hana", "passwd")
        except:
            pwd = ''
        try:
            Settings.user = Settings.settings.get("hana", "user")
        except:
            Settings.user = ""
        Settings._init_logger()
        return url, port, Settings.user, pwd

    @staticmethod
    def _set_log_level(logger, level):
        if level == 'info':
            logger.setLevel(logging.INFO)
        else:
            if level == 'warn':
                logger.setLevel(logging.WARN)
            else:
                if level == 'debug':
                    logger.setLevel(logging.DEBUG)
                else:
                    logger.setLevel(logging.ERROR)

    @staticmethod
    def _init_logger():
        logging.basicConfig()
        for module in ["hana_ml.ml_base", 'hana_ml.dataframe', 'hana_ml.algorithms.pal']:
            try:
                level = Settings.settings.get("logging", module)
            except:
                level = "error"
            logger = logging.getLogger(module)
            Settings._set_log_level(logger, level.lower())

    @staticmethod
    def set_log_level(level='info'):
        """
        Set logging level.

        Parameters
        ----------

        level : {'info', 'warn', 'debug', 'error'}
        """
        logging.basicConfig()
        for module in ["hana_ml.ml_base", 'hana_ml.dataframe', 'hana_ml.algorithms.pal']:
            logger = logging.getLogger(module)
            Settings._set_log_level(logger, level)
