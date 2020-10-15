import sys
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QLabel, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer
sys.path.append('../')
from server.delete_user import DelUserDialog
from server.add_user import RegisterUser
from server.config_window import ConfigWindow
from server.stat_window import StatWindow


class MainWindow(QMainWindow):
    '''Класс - основное окно сервера.'''

    def __init__(self, database, server, config):
        super().__init__()

        self.database = database

        self.server_thread = server
        self.config = config

        self.exitAction = QAction('Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(qApp.quit)

        self.refresh_button = QAction('Обновить список', self)

        self.config_btn = QAction('Настройки сервера', self)

        self.register_btn = QAction('Регистрация пользователя', self)

        self.remove_btn = QAction('Удаление пользователя', self)

        self.show_history_button = QAction('История клиентов', self)

        self.statusBar()
        self.statusBar().showMessage('Server Working')

        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(self.exitAction)
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)
        self.toolbar.addAction(self.register_btn)
        self.toolbar.addAction(self.remove_btn)

        self.setFixedSize(800, 600)
        self.setWindowTitle('Messaging Server alpha release')

        self.label = QLabel('Список подключённых клиентов:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        self.table_of_active_clients = QTableView(self)
        self.table_of_active_clients.move(10, 45)
        self.table_of_active_clients.setFixedSize(780, 400)

        self.timer = QTimer()
        self.timer.timeout.connect(self.create_users_model)
        self.timer.start(1000)

        self.refresh_button.triggered.connect(self.create_users_model)
        self.show_history_button.triggered.connect(self.show_statistics)
        self.config_btn.triggered.connect(self.server_config)
        self.register_btn.triggered.connect(self.reg_user)
        self.remove_btn.triggered.connect(self.rem_user)

        self.show()

    def create_users_model(self):
        '''Метод заполняющий таблицу активных пользователей.'''
        list_users = self.database.list_of_active_clients()
        list = QStandardItemModel()
        list.setHorizontalHeaderLabels(
            ['Имя Клиента', 'IP Адрес', 'Порт', 'Время подключения'])
        for row in list_users:
            user, ip, port, time = row
            user = QStandardItem(user)
            user.setEditable(False)
            ip = QStandardItem(ip)
            ip.setEditable(False)
            port = QStandardItem(str(port))
            port.setEditable(False)
            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)
            list.appendRow([user, ip, port, time])
        self.table_of_active_clients.setModel(list)
        self.table_of_active_clients.resizeColumnsToContents()
        self.table_of_active_clients.resizeRowsToContents()

    def show_statistics(self):
        '''Метод создающий окно со статистикой клиентов.'''
        global stat_window
        stat_window = StatWindow(self.database)
        stat_window.show()

    def server_config(self):
        '''Метод создающий окно с настройками сервера.'''
        global config_window
        config_window = ConfigWindow(self.config)

    def reg_user(self):
        '''Метод создающий окно регистрации пользователя.'''
        global reg_window
        reg_window = RegisterUser(self.database, self.server_thread)
        reg_window.show()

    def rem_user(self):
        '''Метод создающий окно удаления пользователя.'''
        global rem_window
        rem_window = DelUserDialog(self.database, self.server_thread)
        rem_window.show()
