import logging
import sys
import os

sys.path.append('../')
from common.variables import LOGGING_LEVEL

# создаём формировщик логов (formatter):
FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s %(threadName)s')

# Подготовка имени файла для логирования
PATH = os.getcwd()
PATH = os.path.join(PATH, 'client.log')

# создаём потоки вывода логов
STREAM_HANDLER = logging.StreamHandler(sys.stderr)
STREAM_HANDLER.setFormatter(FORMATTER)
STREAM_HANDLER.setLevel(logging.INFO)
FILE_HANDLER = logging.FileHandler(PATH, encoding='utf-8')
FILE_HANDLER.setFormatter(FORMATTER)

# создаём регистратор и настраиваем его
logger = logging.getLogger('client')
logger.addHandler(STREAM_HANDLER)
logger.addHandler(FILE_HANDLER)
logger.setLevel(LOGGING_LEVEL)

# отладка
if __name__ == '__main__':
    logger.critical('Test critical event')
    logger.error('Test error ivent')
    logger.debug('Test debug ivent')
    logger.info('Test info ivent')