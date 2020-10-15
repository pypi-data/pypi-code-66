import os
from PyQt5.QtWidgets import QDialog, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox
from PyQt5.QtCore import Qt


class WindowConfig(QDialog):
    ''' Класс - основные настройки окна сервера'''

    def __init__(self, config):
        super().__init__()
        self.config = config
        self.initUI()

    def initUI(self):
        self.setFixedSize(365, 260)
        self.setWindowTitle('Настройки сервера')
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setModal(True)

        # запись о файле бд
        self.db_path_label = QLabel('Путь до файла базы данных: ', self)
        self.db_path_label.move(10, 10)
        self.db_path_label.setFixedSize(240, 15)

        # стока с путем базы
        self.db_path = QLineEdit(self)
        self.db_path.setFixedSize(250, 20)
        self.db_path.move(10, 30)
        self.db_path.setReadOnly(True)

        # кнопка выбора пути
        self.db_path_select = QPushButton('Обзор...', self)
        self.db_path_select.move(275, 28)

        # метка с именем поля файла бд
        self.db_file_label = QLabel('Имя файла базы данных: ', self)
        self.db_file_label.move(10, 68)
        self.db_file_label.setFixedSize(180, 15)

        # поле для ввода имени файла
        self.db_file = QLineEdit(self)
        self.db_file.move(200, 66)
        self.db_file.setFixedSize(150, 20)

        # метка с номером порта
        self.port = QLineEdit(self)
        self.port.move(200, 108)
        self.port.setFixedSize(150, 20)

        # поля д/ввода номера порта
        self.port = QLineEdit(self)
        self.port.move(200, 108)
        self.port.setFixedSize(150, 20)

        # метка с адресом соединений
        self.ip_label = QLabel('С какого IP принимаем соединения:', self)
        self.ip_label.move(10, 148)
        self.ip_label.setFixedSize(180, 15)

        # метка с напоминанием о пустом поле
        self.ip_label_note = QLabel(
            ' оставьте это поле пустым, чтобы\n принимать соединения с любых адресов.',
            self)
        self.ip_label_note.move(10, 168)
        self.ip_label_note.setFixedSize(500, 30)

        # поле д/ввода ip
        self.ip = QLineEdit(self)
        self.ip.move(200, 148)
        self.ip.setFixedSize(150, 20)

        # кнопка сохранения настроек
        self.save_btn = QPushButton('Сохранить', self)
        self.save_btn.move(190, 220)

        # кнопка закрытия окна
        self.close_button = QPushButton('Закрыть', self)
        self.close_button.move(275, 220)
        self.close_button.clicked.connect(self.close)

        self.db_path_select.clicked.connect(self.open_file_dialog)

        self.show()
        self.db_path.insert(self.config['SETTINGS']['Database_path'])
        self.db_file.insert(self.config['SETTINGS']['Database_file'])
        self.port.insert(self.config['SETTINGS']['Default_port'])
        self.ip.insert(self.config['SETTINGS']['Listen_Address'])
        self.save_btn.clicked.connect(self.save_server_config)

    def open_file_dialog(self):
        '''Метод - обработка открытия окна выбора папки'''
        global dialog
        dialog = QFileDialog(self)
        path = dialog.getExistingDirectory()
        path = path.replace('/', '\\')
        self.db_path.clear()
        self.db_path.insert(path)

    def save_server_config(self):
        '''Метод сохранения настроек. Проверка правильности введенных данных, если правильно сохраняет
         ini файл'''
        global config_window
        message = QMessageBox()
        self.config['SETTINGS']['Database_path'] = self.db_path.text()
        self.config['SETTINGS']['Database_file'] = self.db_file.text()
        try:
            port = int(self.port.text())
        except ValueError:
            message.warning(self, 'Ошибка', 'Порт должен быть числом')
        else:
            self.config['SETTINGS']['Listen_Address'] = self.ip.text()
            if 1023 < port < 65536:
                self.config['SETTINGS']['Default_port'] = str(port)
                dir_path = os.getcwd()
                dir_path = os.path.join(dir_path, '..')
                with open(f"{dir_path}/{'server.ini'}", 'w') as conf:
                    self.config.write(conf)
                    message.information(
                        self, 'OK', 'Настройки успешно сохранены!')
            else:
                message.warning(
                    self, 'Ошибка', 'Порт должен быть от 1024 до 65536')
