""" Дескрипторы """
import logging
import sys
from ipaddress import ip_address

SERVER_LOGGER = logging.getLogger('server')


class Port:
    """ Дескриптор-валиидатор порта соединения """
    def __set__(self, instance, value):
        # проверка получения корретного номера порта для работы сервера.
        if not 1023 < value < 65536:
            SERVER_LOGGER.critical(
                f'Попытка запуска сервера с указанием неподходящего порта '
                f'{value}. Допустимы адреса с 1024 до 65535.')
            sys.exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name


class IpAddress:
    """ Дескриптор-валиидатор IP-адреса соединения """
    def __set__(self, instance, value):
        # проверка получения корретного номера ip адреса для работы сервера.
        if value:
            try:
                ip_address(value)
            except ValueError as err:
                SERVER_LOGGER.critical(
                    f'Попытка запуска сервера с указанием неподходящего ip адреса {err}')
                sys.exit(1)
        instance.__dict__[self.name] = value

    def __set_name__(self, owner, name):
        self.name = name
