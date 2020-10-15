import os
import sys
import logging
import logging.handlers

from common.my_variables import LOGGING_LEVEL
sys.path.append('../')


'''создание формировщика логов(formatter)'''
SERVER_FORMATTER = logging.Formatter('%(asctime)s %(levelname)s %(message)s')

'''подготовка имени файла для логирования'''
PATH = os.path.dirname(os.path.abspath(__file__))
PATH = os.path.join(PATH, 'server.log')

'''создание точек вывода логов'''
HANDLER_STREAM = logging.StreamHandler(sys.stderr)
HANDLER_STREAM.setFormatter(SERVER_FORMATTER)
HANDLER_STREAM.setLevel(logging.ERROR)
LOG_FILE = logging.handlers.TimedRotatingFileHandler(PATH, encoding='utf-8', interval=1, when='D')
LOG_FILE.setFormatter(SERVER_FORMATTER)

'''создание регистратора и настройка его'''
LOGGER = logging.getLogger('server')
LOGGER.addHandler(HANDLER_STREAM)
LOGGER.addHandler(LOG_FILE)
LOGGER.setLevel(LOGGING_LEVEL)

'''отладка'''
if __name__ == '__main__':
    LOGGER.critical('Критическая ошибка')
    LOGGER.error('Ошибка')
    LOGGER.debug('Отладочная информация')
    LOGGER.info('Информационное сообщение')