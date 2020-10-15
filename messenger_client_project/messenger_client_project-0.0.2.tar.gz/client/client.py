import argparse
import os
import sys
import logging
from Crypto.PublicKey import RSA
from PyQt5.QtWidgets import QApplication, QMessageBox
from common.variables import DEFAULT_IP_ADDRESS, DEFAULT_PORT
from common.errors import ServerError
from common.decor import log
from client.database_client import DatabaseClient
from client.transit import ClientTransit
from client.main_window import ClientMainWindow
from client.start_dialog import UserNameDialog

logger = logging.getLogger('client')


@log
def create_arg_parser():
    '''
    Парсер аргументов командной строки, возвращает кортеж из 4 элементов
    адрес сервера, порт, имя пользователя, пароль.
    Выполняет проверку на корректность номера порта.
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('addr', default=DEFAULT_IP_ADDRESS, nargs='?')
    parser.add_argument('port', default=DEFAULT_PORT, type=int, nargs='?')
    parser.add_argument('-n', '--name', default=None, nargs='?')
    parser.add_argument('-p', '--password', default='', nargs='?')
    namespace = parser.parse_args(sys.argv[1:])
    server_ip_address = namespace.addr
    server_port = namespace.port
    client_name = namespace.name
    client_passwd = namespace.password

    if not 1023 < server_port < 65536:
        logger.critical(
            f'Попытка запуска клиента с неподходящим номером порта: {server_port}. '
            f'Допустимы адреса с 1024 до 65535. Клиент завершается.')
        sys.exit(1)

    return server_ip_address, server_port, client_name, client_passwd


if __name__ == '__main__':
    server_ip_address, server_port, client_name, client_passwd = create_arg_parser()
    logger.debug('Args loaded')

    client_app = QApplication(sys.argv)

    start_dialog = UserNameDialog()
    if not client_name or not client_passwd:
        client_app.exec_()
        if start_dialog.ok_pressed:
            client_name = start_dialog.client_name.text()
            client_passwd = start_dialog.client_passwd.text()
            logger.debug(
                f'Using USERNAME = {client_name}, PASSWD = {client_passwd}.')
        else:
            sys.exit(0)

    logger.info(
        f'Запущен клиент с парамертами: адрес сервера: {server_ip_address} , порт: {server_port}, '
        f'имя пользователя: {client_name}')

    dir_path = os.getcwd()
    key_file = os.path.join(dir_path, f'{client_name}.key')
    if not os.path.exists(key_file):
        keys = RSA.generate(2048, os.urandom)
        with open(key_file, 'wb') as key:
            key.write(keys.export_key())
    else:
        with open(key_file, 'rb') as key:
            keys = RSA.import_key(key.read())

    logger.debug("Keys sucsessfully loaded.")

    database = DatabaseClient(client_name)

    try:
        transit = ClientTransit(
            server_port,
            server_ip_address,
            database,
            client_name,
            client_passwd,
            keys)
        logger.debug("Transit ready.")
    except ServerError as error:
        message = QMessageBox()
        message.critical(start_dialog, 'Ошибка сервера', error.text)
        sys.exit(1)
    transit.setDaemon(True)
    transit.start()

    del start_dialog

    main_window = ClientMainWindow(database, transit, keys)
    main_window.make_connection(transit)
    main_window.setWindowTitle(f'Чат Программа alpha release - {client_name}')
    client_app.exec_()

    transit.transit_closed()
    transit.join()
