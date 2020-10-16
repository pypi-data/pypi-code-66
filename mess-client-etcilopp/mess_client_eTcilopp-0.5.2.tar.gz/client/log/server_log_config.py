import sys
import os
import logging
import logging.handlers

from common.variables import LOGGING_LEVEL
sys.path.append('../')


FORMATTER = logging.Formatter('%(asctime)-10s - %(levelname)s - %(filename)s - %(message)s')

PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')

FILE_HANDLER.setFormatter(FORMATTER)

LOG = logging.getLogger('server')
LOG.addHandler(FILE_HANDLER)
LOG.setLevel(LOGGING_LEVEL)


if __name__ == '__main__':
    LOG.critical('Критическая ошибка')
    LOG.error('Ошибка')
    LOG.debug('Отладочная информация')
    LOG.info('Информационное сообщение')