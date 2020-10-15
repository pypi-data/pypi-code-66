""" Окно настроек. """
import os

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, \
    QPushButton, QFileDialog, QMessageBox


class ConfigWindow(QDialog):
    """Класс окно настроек."""

    def __init__(self, config):
        super().__init__()
        self.close_button = QPushButton('Закрыть', self)
        self.save_btn = QPushButton('Сохранить', self)
        self.ip_field = QLineEdit(self)
        self.ip_label_note = QLabel(' оставьте это поле пустым, чтобы\n'
                                    'принимать соединения с любых адресов.', self)
        self.ip_label = QLabel('С какого IP принимаем соединения:', self)
        self.port_field = QLineEdit(self)
        self.port_label = QLabel('Номер порта для соединений:', self)
        self.db_file_field = QLineEdit(self)
        self.db_file_label = QLabel('Имя файла базы данных: ', self)
        self.db_path_btn = QPushButton('Обзор...', self)
        self.db_path_field = QLineEdit(self)
        self.db_path_label = QLabel('Путь до файла базы данных: ', self)
        self.config = config
        self.init_ui()

    def init_ui(self):
        """Настройки окна"""
        self.setFixedSize(430, 300)
        self.setWindowTitle('Настройки сервера')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        # Надпись о файле базы данных:
        self.db_path_label.move(10, 10)
        self.db_path_label.setFixedSize(240, 15)

        # Строка с путём базы
        self.db_path_field.setFixedSize(280, 20)
        self.db_path_field.move(10, 30)
        self.db_path_field.setReadOnly(True)

        # Кнопка выбора пути.
        self.db_path_btn.move(300, 28)

        # Метка с именем поля файла базы данных
        self.db_file_label.move(10, 65)
        self.db_file_label.setFixedSize(180, 20)

        # Поле для ввода имени файла
        self.db_file_field.move(280, 66)
        self.db_file_field.setFixedSize(140, 20)

        # Метка с номером порта
        self.port_label.move(10, 108)
        self.port_label.setFixedSize(240, 15)

        # Поле для ввода номера порта
        self.port_field.move(280, 108)
        self.port_field.setFixedSize(140, 20)

        # Метка с адресом для соединений
        self.ip_label.move(10, 148)
        self.ip_label.setFixedSize(265, 15)

        # Метка с напоминанием о пустом поле.
        self.ip_label_note.move(10, 170)
        self.ip_label_note.setFixedSize(500, 40)

        # Поле для ввода ip
        self.ip_field.move(280, 148)
        self.ip_field.setFixedSize(140, 20)

        # Кнопка сохранения настроек
        self.save_btn.move(170, 240)

        # Кнапка закрытия окна
        self.close_button.move(290, 240)
        self.close_button.clicked.connect(self.close)

        self.db_path_btn.clicked.connect(self.open_file_dialog)

        self.show()

        self.db_path_field.insert(self.config['SETTINGS']['Database_path'])
        self.db_file_field.insert(self.config['SETTINGS']['Database_file'])
        self.port_field.insert(self.config['SETTINGS']['Default_port'])
        self.ip_field.insert(self.config['SETTINGS']['Listen_Address'])
        self.save_btn.clicked.connect(self.save_server_config)

    def open_file_dialog(self):
        """Метод обработчик открытия окна выбора папки."""
        dialog = QFileDialog(self)
        path = dialog.getExistingDirectory()
        path = path.replace('/', '\\')
        self.db_path_field.clear()
        self.db_path_field.insert(path)

    def save_server_config(self):
        """
        Метод сохранения настроек.
        Проверяет правильность введённых данных и
        если всё правильно сохраняет ini файл.
        """
        message = QMessageBox()
        self.config['SETTINGS']['Database_path'] = self.db_path_field.text()
        self.config['SETTINGS']['Database_file'] = self.db_file_field.text()
        try:
            port = int(self.port_field.text())
        except ValueError:
            message.warning(self, 'Ошибка', 'Порт должен быть числом')
        else:
            self.config['SETTINGS']['Listen_Address'] = self.ip_field.text()
            if 1023 < port < 65536:
                self.config['SETTINGS']['Default_port'] = str(port)
                dir_path = os.path.dirname(os.path.realpath(__file__))
                dir_path = os.path.join(dir_path, '../..')
                with open(f"{dir_path}/{'server_settings.ini'}", 'w') as conf:
                    self.config.write(conf)
                    message.information(
                        self, 'OK', 'Настройки успешно сохранены!')
            else:
                message.warning(
                    self, 'Ошибка', 'Порт должен быть от 1024 до 65536')
