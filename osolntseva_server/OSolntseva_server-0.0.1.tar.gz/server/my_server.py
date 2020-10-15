import os
import sys
import argparse
import configparser
import logging
import traceback
from PyQt5.QtWidgets import QApplication
from PyQt5.QtCore import Qt
from common.decorator import log
from server.serv_database import ServerRepository
from server.core import MessageProcessor
from server.main_window import MainWindow
from common.my_variables import PORT_DEFAULT

try:
    # инициализация логирования сервера
    server_logger = logging.getLogger('server')

    @log
    def create_parser_arg(default_port, default_address):
        '''парсер агументов'''
        server_logger.debug(
            f'Инициализация парсера аргументов коммандной строки: {sys.argv}')
        parser = argparse.ArgumentParser()
        parser.add_argument('-p', default=default_port, type=int, nargs='?')
        parser.add_argument('-a', default=default_address, nargs='?')
        parser.add_argument('--no_gui', action='store_true')
        namespace = parser.parse_args(sys.argv[1:])
        port_listen = namespace.p
        address_listen = namespace.a
        gui_flag = namespace.no_gui
        server_logger.debug('Аргументы успешно загружены.')
        return address_listen, port_listen, gui_flag

    @log
    def config_load():
        '''Парсер ini файла'''
        config = configparser.ConfigParser()
        dir_path = os.getcwd()
        config.read(f"{dir_path}/{'server.ini'}")
        # Если конфиг файл загружен правильно, запускаемся, иначе конфиг по
        # умолчанию.
        if 'SETTINGS' in config:
            return config
        else:
            config.add_section('SETTINGS')
            config.set('SETTINGS', 'Default_port', str(PORT_DEFAULT))
            config.set('SETTINGS', 'Listen_Address', '')
            config.set('SETTINGS', 'Database_path', '')
            config.set('SETTINGS', 'Database_file', 'server_database.db3')
            return config

    @log
    def main():
        ''' Загрузка параметров командной строки, если нет параметров, то задаем занчения
         по умолчаниюю. Обрабатываем порт: server.py -p 8079 -a 192.168.1.37'''
        # загрузка файла конфигурации сервера
        config = config_load()

        # загрузка параметров командной строки
        address_listen, port_listen, gui_flag = create_parser_arg(
            config['SETTINGS']['Default_port'], config['SETTINGS']['Listen_Address'])

        # инициализация базы данных
        database = ServerRepository(
            os.path.join(
                config['SETTINGS']['Database_path'],
                config['SETTINGS']['Database_file']))

        # создать экземпляр сервера и его запуск
        server = MessageProcessor(address_listen, port_listen, database)
        server.daemon = True
        server.start()

        if gui_flag:
            while True:
                command = input('Введите exit для завершения работы сервера.')
                if command == 'exit':
                    # Если выход, то завршаем основной цикл сервера.
                    server.running = False
                    server.join()
                    break

        # Если не указан запуск без GUI, то запускаем GUI:
        else:
            # Создаём графическое окуружение для сервера:
            server_app = QApplication(sys.argv)
            server_app.setAttribute(Qt.AA_DisableWindowContextHelpButton)
            main_window = MainWindow(database, server, config)

            # Запускаем GUI
            server_app.exec_()

            # По закрытию окон останавливаем обработчик сообщений
            server.running = False

    if __name__ == '__main__':
        main()

except Exception as e:
    print('РћС€РёР±РєР°:\n', traceback.format_exc())
