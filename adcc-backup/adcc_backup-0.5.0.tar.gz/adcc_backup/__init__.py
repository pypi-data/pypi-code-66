from pathlib import Path
from markipy.basic import Folder, Watcher, Logger

PKG_NAME = 'adcc_backup'
PKG_HOME_PATH = Path().home() / f'.{PKG_NAME}'
PKG_CFG_PATH = PKG_HOME_PATH / 'config'
PKG_LOG_PATH = PKG_HOME_PATH / 'log'

PKG_HOME_FOLDER = Folder(PKG_HOME_PATH)
PKG_CFG_FOLDER = Folder(PKG_CFG_PATH)
PKG_LOG_FOLDER = Folder(PKG_LOG_PATH)

PKG_HOME_WATCHER = Watcher(str(Folder))
PKG_HOME_WATCHER.start()

_adcclogger_ = {'class': 'AdccLogger', 'version': 1}


class AdccLogger(Logger):
    def __init__(self, console=False, file_log=None):
        Logger.__init__(self, console=console, file_log=file_log, log_path=PKG_LOG_FOLDER())
        self._init_atom_register_class(_adcclogger_)


from .config import Configuration
from .client import AdccRsync, EthEventProducer, EthEventConsumer
from .server import AutoBagFixer, ManualBagFixer
from . import scripts
