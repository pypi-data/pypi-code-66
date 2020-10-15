import sys
import os
import logging.handlers

sys.path.append('../')
from common.variables import LOGGING_LEVEL

# создаём формировщик логов (formatter):
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s %(lineno)d')

# Подготовка имени файла для логирования
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)
FILE_HANDLER = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf8', interval=1, when='D')
FILE_HANDLER.setFormatter(FORMATTER)

# создаём регистратор и настраиваем его
logger = logging.getLogger('server')
logger.addHandler(STREAM_HANDLER)
logger.addHandler(FILE_HANDLER)
logger.setLevel(LOGGING_LEVEL)

if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')