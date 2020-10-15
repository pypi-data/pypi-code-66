import os
import sys
import logging
import argparse
from Cryptodome.PublicKey import RSA
from PyQt5.QtWidgets import QApplication, QMessageBox
import traceback

from client.main_window import ClientMainWindow
from client.start_dialog import UserDialog
from client.transport import TransportClient
from common.decorator import log
from common.errors import ServerError
from common.my_variables import IP_ADDRESS_DEFAULT, PORT_DEFAULT
from client.client_database import ClientDatabase


try:

    '''инициализация клиентского логера'''
    client_logger = logging.getLogger('client')

    @log
    def create_parser_arg():
        '''парсер аргументов'''
        parser = argparse.ArgumentParser()
        parser.add_argument('addr', default=IP_ADDRESS_DEFAULT, nargs='?')
        parser.add_argument('port', default=PORT_DEFAULT, type=int, nargs='?')
        parser.add_argument('-n', '--name', default='None', nargs='?')
        parser.add_argument('-p', '--password', default='', nargs='?')
        namespace = parser.parse_args(sys.argv[1:])
        address_server = namespace.addr
        port_server = namespace.port
        client_name = namespace.name
        client_passwd = namespace.password

        # проверка порта
        if not 1023 < port_server < 65536:
            client_logger.critical(
                f'Попытка запуска сервера с указанием неподходящего порта '
                f'{port_server}. Допустимы адреса с 1024 до 65535.')
            sys.exit(1)

        return address_server, port_server, client_name, client_passwd

    if __name__ == '__main__':

        address_server, port_server, client_name, client_passwd = create_parser_arg()
        client_logger.debug('аргументы загружены')

        client_app = QApplication(sys.argv)
        start_dialog = UserDialog()
        if not client_name or not client_passwd:

            client_app.exec_()
            # если пользователь ввёл имя и нажал ОК, то сохраняем ведённое и
            # удаляем объект, инааче выходим
            if start_dialog.ok_pressed:
                client_name = start_dialog.client_name.text()
                client_passwd = start_dialog.client_passwd.text()

            else:
                sys.exit(0)

        client_logger.info('Клиент запущен')

        # Загружаем ключи с файла, если же файла нет, то генерируем новую пару.
        dir_path = os.getcwd()
        key_file = os.path.join(dir_path, f'{client_name}.key')
        if not os.path.exists(key_file):
            keys = RSA.generate(2048, os.urandom)
            with open(key_file, 'wb') as key:
                key.write(keys.export_key())
        else:
            with open(key_file, 'rb') as key:
                keys = RSA.import_key(key.read())

        client_logger.debug("ключи успешно загружены.")

        database = ClientDatabase(client_name)

        # инициализация сокета и обмен
        try:
            transport = TransportClient(
                port_server,
                address_server,
                database,
                client_name,
                client_passwd,
                keys)
            client_logger.debug("Transport ready.")
        except ServerError as error:
            message = QMessageBox()
            message.critical(start_dialog, 'Ошибка сервера', error.text)
            sys.exit(1)
        transport.setDaemon(True)
        transport.start()

        # Удалим объект диалога за ненадобностью
        del start_dialog

        # создать GUI
        main_window = ClientMainWindow(database, transport, keys)
        main_window.make_connection(transport)
        main_window.setWindowTitle(
            f'Чат Программа alpha release - {client_name}')
        client_app.exec_()

        # если графическая оболочка закрылась, закрываем транспорт
        transport.transport_shutdown()
        transport.join()


except Exception as e:
    print('РћС€РёР±РєР°:\n', traceback.format_exc())
