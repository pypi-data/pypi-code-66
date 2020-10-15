""" Окно с историей пользователей. """
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QDialog, QPushButton, QTableView


class StatWindow(QDialog):
    """ Класс - окно с историей пользователей. """

    def __init__(self, database):
        super().__init__()

        self.history_table = QTableView(self)
        self.close_button = QPushButton('Закрыть', self)
        self.database = database
        self.init_ui()

    def init_ui(self):
        # Настройки окна:
        self.setWindowTitle('Статистика клиентов')
        self.setFixedSize(800, 500)
        self.setAttribute(Qt.WA_DeleteOnClose)

        # Кнапка закрытия окна
        self.close_button.move(350, 450)
        self.close_button.clicked.connect(self.close)

        # Лист с собственно историей
        self.history_table.move(10, 10)
        self.history_table.setFixedSize(780, 420)

        self.create_stat_model()

    def create_stat_model(self):
        """Метод реализующий заполнение таблицы статистикой сообщений."""
        # Список записей из базы
        stat_list = self.database.message_history()

        # Объект модели данных:
        lst = QStandardItemModel()
        lst.setHorizontalHeaderLabels(
            ['Имя Клиента',
             'Последний раз входил',
             'Сообщений отправлено',
             'Сообщений получено'])
        for row in stat_list:
            user, last_seen, sent, received = row
            user = QStandardItem(user)
            user.setEditable(False)
            last_seen = QStandardItem(str(last_seen.replace(microsecond=0)))
            last_seen.setEditable(False)
            sent = QStandardItem(str(sent))
            sent.setEditable(False)
            received = QStandardItem(str(received))
            received.setEditable(False)
            lst.appendRow([user, last_seen, sent, received])
        self.history_table.setModel(lst)
        self.history_table.resizeColumnsToContents()
        self.history_table.resizeRowsToContents()
