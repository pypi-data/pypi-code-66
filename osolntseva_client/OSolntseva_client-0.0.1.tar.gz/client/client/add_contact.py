import logging
import sys
import traceback

from PyQt5.QtWidgets import QDialog, QLabel, QComboBox, QPushButton
from PyQt5.QtCore import Qt

sys.path.append('../')


try:
    client_logger = logging.getLogger('client')

    class AddContactDialog(QDialog):
        '''
        Диалог добавления пользователя в список контактов.
        Предлагает пользователю список возможных контактов и
        добавляет выбранный в контакты.
        '''

        def __init__(self, transport, database):
            super().__init__()
            self.transport = transport
            self.database = database

            self.setFixedSize(350, 120)
            self.setWindowTitle('Выбрать контакт для добавления:')
            self.setAttribute(Qt.WA_DeleteOnClose)
            self.setModal(True)

            self.selector_label = QLabel(
                'Выберать контакт для добавления:', self)
            self.selector_label.setFixedSize(200, 20)
            self.selector_label.move(10, 0)

            self.selector = QComboBox(self)
            self.selector.setFixedSize(200, 20)
            self.selector.move(10, 30)

            self.btn_refresh = QPushButton('Обновить список', self)
            self.btn_refresh.setFixedSize(100, 30)
            self.btn_refresh.move(60, 60)

            self.btn_ok = QPushButton('Добавить', self)
            self.btn_ok.setFixedSize(100, 30)
            self.btn_ok.move(230, 20)

            self.btn_cancel = QPushButton('Отмена', self)
            self.btn_cancel.setFixedSize(100, 30)
            self.btn_cancel.move(230, 60)
            self.btn_cancel.clicked.connect(self.close)

            # Заполняем список возможных контактов
            self.possible_contacts_update()
            # Назначаем действие на кнопку обновить
            self.btn_refresh.clicked.connect(self.update_possible_contacts)

        # заполнить список возможных контактов
        def possible_contacts_update(self):
            '''Метод заполнения возможных контактов'''
            self.selector.clear()
            # множества всех контактов и контактов клиента
            contacts_list = set(self.database.get_contacts())
            users_list = set(self.database.get_users())
            # удаление самого себя из списка пользователей, чтобы нельзя было
            # добавить самого себя
            users_list.remove(self.transport.username)
            # добавление списока возможных контактов
            self.selector.addItems(users_list - contacts_list)

        # обновление возможных контактов, сначала известных, потом
        # предполагаемых
        def update_possible_contacts(self):
            '''Метод обновления спика возможных контактов'''
            try:
                self.transport.user_list_update()
            except OSError:
                pass
            else:
                client_logger.debug(
                    'Обновление списка пользователей с сервера выполнено')
                self.possible_contacts_update()

except Exception as e:
    print('РћС€РёР±РєР°:\n', traceback.format_exc())
