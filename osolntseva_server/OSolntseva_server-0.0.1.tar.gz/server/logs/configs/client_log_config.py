import logging
import sys
import os

from common.my_variables import LOGGING_LEVEL

sys.path.append('../')

'''создание формировщика логов(formatter)'''
CLIENT_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(filename)s %(message)s')

'''подготовка имени файла для логирования'''
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'client.log')

'''создание точек вывода логов'''
HANDLER_STREAM = logging.StreamHandler(sys.stderr)
HANDLER_STREAM.setFormatter(CLIENT_FORMATTER)
HANDLER_STREAM.setLevel(logging.ERROR)
LOG_FILE = logging.FileHandler(PATH, encoding='utf-8')
LOG_FILE.setFormatter(CLIENT_FORMATTER)

'''создание регистратора и настройка его'''
LOGGER = logging.getLogger('client')
LOGGER.addHandler(HANDLER_STREAM)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

'''отладка'''
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')