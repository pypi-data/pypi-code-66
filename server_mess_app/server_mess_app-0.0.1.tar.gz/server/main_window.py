""" Основное окно сервера. """

import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication, QLabel, QTableView

from server.add_user import RegisterUser
from server.cl_history_window import StatWindow
from server.remove_user import DelUserDialog
from server.window_config import ConfigWindow


class MainWindow(QMainWindow):
    """Класс - основное окно сервера."""

    def __init__(self, database, server, config):
        # Конструктор предка
        super().__init__()

        # База данных сервера
        self.database = database

        self.server_thread = server
        self.config = config

        # Ярлык выхода
        self.exitAction = QAction('Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(qApp.quit)

        # Кнопка обновить список клиентов
        self.refresh_button = QAction('Обновить список', self)

        # Кнопка настроек сервера
        self.config_btn = QAction('Настройки сервера', self)

        # Кнопка регистрации пользователя
        self.register_btn = QAction('Регистрация пользователя', self)

        # Кнопка удаления пользователя
        self.remove_btn = QAction('Удаление пользователя', self)

        # Кнопка вывести историю сообщений
        self.show_history_button = QAction('История клиентов', self)

        # Статусбар
        self.statusBar()
        self.statusBar().showMessage('Server Working')

        # Тулбар
        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(self.exitAction)
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)
        self.toolbar.addAction(self.register_btn)
        self.toolbar.addAction(self.remove_btn)

        # Настройки геометрии основного окна
        # Поскольку работать с динамическими размерами мы не умеем, и мало
        # времени на изучение, размер окна фиксирован.
        self.setFixedSize(800, 600)
        self.setWindowTitle('Messaging Server alpha release')

        # Надпись о том, что ниже список подключённых клиентов
        self.label = QLabel('Список подключённых клиентов:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        # Окно со списком подключённых клиентов.
        self.active_clients_table = QTableView(self)
        self.active_clients_table.move(10, 45)
        self.active_clients_table.setFixedSize(780, 400)

        # Таймер, обновляющий список клиентов 1 раз в секунду
        self.timer = QTimer()
        self.timer.timeout.connect(self.create_users_model)
        self.timer.start(1000)

        self.stat_window = None
        self.config_window = None
        self.reg_window = None
        self.rem_window = None

        # Связываем кнопки с процедурами
        self.refresh_button.triggered.connect(self.create_users_model)
        self.show_history_button.triggered.connect(self.show_statistics)
        self.config_btn.triggered.connect(self.server_config)
        self.register_btn.triggered.connect(self.reg_user)
        self.remove_btn.triggered.connect(self.rem_user)

        # Последним параметром отображаем окно.
        self.show()

    def create_users_model(self):
        """Метод заполняющий таблицу активных пользователей."""
        users_list = self.database.active_users_list()
        lst = QStandardItemModel()
        lst.setHorizontalHeaderLabels(['Имя клиента', 'IP адрес', 'Порт', 'Время подключения'])
        for row in users_list:
            client, ip_address, port, connection_time = row
            client = QStandardItem(client)
            client.setEditable(False)
            ip_address = QStandardItem(ip_address)
            ip_address.setEditable(False)
            port = QStandardItem(str(port))
            port.setEditable(False)
            connection_time = QStandardItem(str(connection_time.replace(microsecond=0)))
            connection_time.setEditable(False)
            lst.appendRow([client, ip_address, port, connection_time])
        self.active_clients_table.setModel(lst)
        self.active_clients_table.resizeColumnsToContents()
        self.active_clients_table.resizeRowsToContents()

    def show_statistics(self):
        """Метод создающий окно со статистикой клиентов."""
        self.stat_window = StatWindow(self.database)
        self.stat_window.show()

    def server_config(self):
        """Метод создающий окно с настройками сервера."""
        # Создаём окно и заносим в него текущие параметры
        self.config_window = ConfigWindow(self.config)

    def reg_user(self):
        """Метод создающий окно регистрации пользователя."""
        self.reg_window = RegisterUser(self.database, self.server_thread)
        self.reg_window.show()

    def rem_user(self):
        """Метод создающий окно удаления пользователя."""
        self.rem_window = DelUserDialog(self.database, self.server_thread)
        self.rem_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    # ex = MainWindow()
    # ex.statusBar().showMessage('Test Shows')
    # test_list = QStandardItemModel(ex)
    # test_list.setHorizontalHeaderLabels(['Имя Клиента', 'IP Адрес', 'Порт', 'Время подключения'])
    # test_list.appendRow([QStandardItem('Alex'),
    #                      QStandardItem('127.0.0.1'),
    #                      QStandardItem('7567'),
    #                      QStandardItem('18:10 12.01.1990')
    #                      ])
    # test_list.appendRow([QStandardItem('Dima'),
    #                      QStandardItem('127.0.0.12'),
    #                      QStandardItem('7569'),
    #                      QStandardItem('18:12 12.01.1990')
    #                      ])
    # ex.active_clients_table.setModel(test_list)
    # ex.active_clients_table.resizeColumnsToContents()
    # message = QMessageBox()
    # message.show()
    print('START')
    app.exec_()
    print('END')
    # app = QApplication(sys.argv)

    # dial = ConfigWindow()
    # app.exec_()
