from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QLabel, QTableView
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtCore import QTimer
from server.add_user import UserRegister
from server.config_window import WindowConfig
from server.delete_user import DeleteUserDialog
from server.statistic_window import StatisticWindow


class MainWindow(QMainWindow):
    '''Класс - основное окно сервера'''

    def __init__(self, database, server, config):
        # конструктор предка
        super().__init__()

        # бд сервера
        self.database = database

        self.server_thread = server
        self.config = config

        # ярлык входа
        self.exitAction = QAction('Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.triggered.connect(qApp.quit)

        # обновление списка клиентов
        self.refresh_button = QAction('Обновить список', self)

        # настройки сервера
        self.config_btn = QAction('Настройки сервера', self)

        # регистрация пользователя
        self.register_btn = QAction('Регистрация пользователя', self)

        # удаление пользователя
        self.remove_btn = QAction('Удаление пользователя', self)

        # выовд истории сообщений
        self.show_history_button = QAction('История клиентов', self)

        # статусбар
        self.statusBar()
        self.statusBar().showMessage('Server Working')

        # тулбар
        self.toolbar = self.addToolBar('MainBar')
        self.toolbar.addAction(self.exitAction)
        self.toolbar.addAction(self.refresh_button)
        self.toolbar.addAction(self.show_history_button)
        self.toolbar.addAction(self.config_btn)
        self.toolbar.addAction(self.register_btn)
        self.toolbar.addAction(self.remove_btn)

        # настройки окна
        self.setFixedSize(800, 600)
        self.setWindowTitle('Messaging Server alpha release')

        # надпись о списке подключенных пользователей
        self.label = QLabel('Список подключённых клиентов:', self)
        self.label.setFixedSize(240, 15)
        self.label.move(10, 25)

        # окно со списком подключенных клиентов
        self.active_clients_table = QTableView(self)
        self.active_clients_table.move(10, 45)
        self.active_clients_table.setFixedSize(780, 400)

        # таймерю обновление спсика 1 раз в сек
        self.timer = QTimer()
        self.timer.timeout.connect(self.create_users_model)
        self.timer.start(1000)

        # связь кнопок с процедурами
        self.refresh_button.triggered.connect(self.create_users_model)
        self.show_history_button.triggered.connect(self.show_statistics)
        self.config_btn.triggered.connect(self.server_config)
        self.register_btn.triggered.connect(self.reg_user)
        self.remove_btn.triggered.connect(self.rem_user)

        self.show()

    def create_users_model(self):
        '''Метод - заполнение таблицы активных пользователей'''
        list_users = self.database.active_users_list()
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
            # уберать милисекунды из строки времени
            time = QStandardItem(str(time.replace(microsecond=0)))
            time.setEditable(False)
            list.appendRow([user, ip, port, time])
        self.active_clients_table.setModel(list)
        self.active_clients_table.resizeColumnsToContents()
        self.active_clients_table.resizeRowsToContents()

    def show_statistics(self):
        '''Метод создающий окно со статистикой клиентов'''
        global stat_window
        stat_window = StatisticWindow(self.database)
        stat_window.show()

    def server_config(self):
        '''Метод создающий окно с настройками сервера'''
        global config_window
        # создать окно и занести в него текущие параметры
        config_window = WindowConfig(self.config)

    def reg_user(self):
        '''Мето создающий окно регистрации пользователя'''
        global reg_window
        reg_window = UserRegister(self.database, self.server_thread)
        reg_window.show()

    def rem_user(self):
        '''Метод создающий Окно удаления пользователя'''
        global rem_window
        rem_window = DeleteUserDialog(self.database, self.server_thread)
        rem_window.show()
