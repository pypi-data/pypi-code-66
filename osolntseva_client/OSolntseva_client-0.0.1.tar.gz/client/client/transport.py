import binascii
import hashlib
import hmac
import json
import logging
import socket
import sys
import threading
import time
import traceback
from PyQt5.QtCore import pyqtSignal, QObject
from common.errors import ServerError
from common.my_utils import send_message, get_message
from common.my_variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME,\
    PUBLIC_KEY, RESPONSE, ERROR, DATA, RESPONSE_511, MESSAGE, DESTINATIONS, MESSAGE_TEXT, \
    SENDER, GET_CONTACTS, LIST_INFO, USERS_REQUEST, PUBLIC_KEY_REQUEST, ADD_CONTACT, \
    REMOVE_CONTACT, EXIT

sys.path.append('../')


try:
    '''инициализация клиентского логера'''
    client_logger = logging.getLogger('client')

    # блокировка сокета и работы с базой данных
    socket_lock = threading.Lock()

    class TransportClient(threading.Thread, QObject):
        '''Класс реализующий транспортную подсистему клиентского
        модуля. Отвечает за взаимодействие с сервером.'''
        new_message = pyqtSignal(dict)
        message_205 = pyqtSignal()
        connection_lost = pyqtSignal()

        def __init__(self, port, ip_address, database, username, passwd, keys):
            #вызвать конструктор предка'''
            threading.Thread.__init__(self)
            QObject.__init__(self)

            # класс для работы с базой
            self.database = database
            # имя пользователя
            self.username = username
            # Пароль
            self.password = passwd

            # сокет для работы с сревером
            self.transport = None
            # Набор ключей для шифрования
            self.keys = keys
            # установка соединения
            self.connection_init(port, ip_address)
            # обновление таблицы известных пользователей и контактов
            try:
                self.user_list_update()
                self.contacts_list_update()
            except OSError as err:
                if err.errno:
                    client_logger.critical(f'Потеряно соединение с сервером.')
                    raise ServerError('Потеряно соединение с сервером!')
                client_logger.error(
                    'Timeout соединения при обновлении списков пользователей.')
            except json.JSONDecodeError:
                client_logger.critical(f'Потеряно соединение с сервером.')
                raise ServerError('Потеряно соединение с сервером!')
                # флаг продолжения работы транспорта
            self.running = True

        def connection_init(self, port, ip):
            '''Метод - инициализация соединения с сервером'''
            # инициализация сокета и сообщение серверу о появлении
            self.transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

            # таймаут для освобождения сокета
            self.transport.settimeout(5)

            # соединение с сервером, 5 попыток, ставим True, если удалось
            connected = False
            for i in range(5):
                client_logger.info(f'Попытка подключения №{i + 1}')
                try:
                    self.transport.connect((ip, port))
                except (OSError, ConnectionRefusedError):
                    pass
                else:
                    connected = True
                    client_logger.debug("подключение установлено.")
                    break
                time.sleep(1)

            # если соединиться не удалось - исключение
            if not connected:
                client_logger.critical(
                    'Не удалось установить соединение с сервером')
                raise ServerError(
                    'Не удалось установить соединение с сервером')

            client_logger.debug('Установлено соединение с сервером')

            # Запускаем процедуру авторизации
            # Получаем хэш пароля
            passwd_bytes = self.password.encode('utf-8')
            salt = self.username.lower().encode('utf-8')
            passwd_hash = hashlib.pbkdf2_hmac(
                'sha512', passwd_bytes, salt, 10000)
            passwd_hash_string = binascii.hexlify(passwd_hash)

            client_logger.debug(f'Passwd hash ready: {passwd_hash_string}')

            # Получаем публичный ключ и декодируем его из байтов
            pubkey = self.keys.publickey().export_key().decode('ascii')
            # Авторизируемся на сервере
            with socket_lock:
                presense = {
                    ACTION: PRESENCE,
                    TIME: time.time(),
                    USER: {
                        ACCOUNT_NAME: self.username,
                        PUBLIC_KEY: pubkey
                    }
                }
                client_logger.debug(f"Presense message = {presense}")

                # послать серверу приветственное сообщение и получить ответ,
                # что все нормально - либо исключение
                try:
                    send_message(self.transport, presense)
                    ans = get_message(self.transport)
                    client_logger.debug(f'Server response = {ans}.')
                    # Если сервер вернул ошибку, бросаем исключение.
                    if RESPONSE in ans:
                        if ans[RESPONSE] == 400:
                            raise ServerError(ans[ERROR])
                        elif ans[RESPONSE] == 511:
                            # Если всё нормально, то продолжаем процедуру
                            # авторизации.
                            ans_data = ans[DATA]
                            hash = hmac.new(
                                passwd_hash_string, ans_data.encode('utf-8'), 'MD5')
                            digest = hash.digest()
                            my_ans = RESPONSE_511
                            my_ans[DATA] = binascii.b2a_base64(
                                digest).decode('ascii')
                            send_message(self.transport, my_ans)
                            self.process_server_ans(
                                get_message(self.transport))
                except (OSError, json.JSONDecodeError) as err:
                    client_logger.debug(f'ошибка соединения.', exc_info=err)
                    raise ServerError(
                        'Сбой соединения в процессе авторизации.')

        def process_server_ans(self, message):
            '''Метод - обработка сообщения от сервера. генерация исключений при ошибке'''
            client_logger.debug(f'Разбор сообщения от сервера: {message}')

            # Если это подтверждение чего-либо
            if RESPONSE in message:
                if message[RESPONSE] == 200:
                    return
                elif message[RESPONSE] == 400:
                    raise ServerError(f'{message[ERROR]}')
                elif message[RESPONSE] == 205:
                    self.user_list_update()
                    self.contacts_list_update()
                    self.message_205.emit()
                else:
                    client_logger.debug(
                        f'Принят неизвестный код подтверждения {message[RESPONSE]}')

            # если это сообщение от пользователя добавляем в базу, даём сигнал
            # о новом сообщении
            elif ACTION in message and message[ACTION] == MESSAGE and SENDER in message and \
                    DESTINATIONS in message and MESSAGE_TEXT in message and \
                    message[DESTINATIONS] == self.username:
                client_logger.debug(
                    f'Получено сообщение от пользователя {message[SENDER]}:{message[MESSAGE_TEXT]}')
                self.new_message.emit(message)

        def contacts_list_update(self):
            '''Метод - обновление контакт-листа с сервера'''
            self.database.contacts_clear()
            client_logger.debug(
                f'Запрос контакт листа для пользователся {self.name}')
            req = {
                ACTION: GET_CONTACTS,
                TIME: time.time(),
                USER: self.username
            }
            client_logger.debug(f'Сформирован запрос {req}')
            with socket_lock:
                send_message(self.transport, req)
                ans = get_message(self.transport)
            client_logger.debug(f'Получен ответ {ans}')
            if RESPONSE in ans and ans[RESPONSE] == 202:
                for contact in ans[LIST_INFO]:
                    self.database.add_contact(contact)
            else:
                client_logger.error('Не удалось обновить список контактов.')

        def user_list_update(self):
            '''Метод - обновление таблицы известных пользователей'''
            client_logger.debug(
                f'Запрос списка известных пользователей {self.username}')
            req = {
                ACTION: USERS_REQUEST,
                TIME: time.time(),
                ACCOUNT_NAME: self.username
            }
            with socket_lock:
                send_message(self.transport, req)
                ans = get_message(self.transport)
            if RESPONSE in ans and ans[RESPONSE] == 202:
                self.database.add_users(ans[LIST_INFO])
            else:
                client_logger.error(
                    'Не удалось обновить список известных пользователей.')

        def key_request(self, user):
            '''Метод - запрос с сервера публичного ключа'''
            client_logger.debug(f'Запрос публичного ключа для {user}')
            req = {
                ACTION: PUBLIC_KEY_REQUEST,
                TIME: time.time(),
                ACCOUNT_NAME: user
            }
            with socket_lock:
                send_message(self.transport, req)
                ans = get_message(self.transport)
            if RESPONSE in ans and ans[RESPONSE] == 511:
                return ans[DATA]
            else:
                client_logger.error(
                    f'Не удалось получить ключ собеседника{user}.')

        def add_contact(self, contact):
            '''Метод - сообщение на сервер о добавлении нового контакта'''
            client_logger.debug(f'Создание контакта {contact}')
            req = {
                ACTION: ADD_CONTACT,
                TIME: time.time(),
                USER: self.username,
                ACCOUNT_NAME: contact
            }
            with socket_lock:
                send_message(self.transport, req)
                self.process_server_ans(get_message(self.transport))

        def remove_contact(self, contact):
            '''Метод - удаление клиент на сервере'''
            client_logger.debug(f'Удаление контакта {contact}')
            req = {
                ACTION: REMOVE_CONTACT,
                TIME: time.time(),
                USER: self.username,
                ACCOUNT_NAME: contact
            }
            with socket_lock:
                send_message(self.transport, req)
                self.process_server_ans(get_message(self.transport))

        def transport_shutdown(self):
            '''Метод - закрытие соединения, отправка сообщения о выходе'''
            self.running = False
            message = {
                ACTION: EXIT,
                TIME: time.time(),
                ACCOUNT_NAME: self.username
            }
            with socket_lock:
                try:
                    send_message(self.transport, message)
                except OSError:
                    pass
            client_logger.debug('Транспорт завершает работу.')
            time.sleep(0.5)

        def send_message(self, to, message):
            '''Метод - отправление сообщения на сервер'''
            message_dict = {
                ACTION: MESSAGE,
                SENDER: self.username,
                DESTINATIONS: to,
                TIME: time.time(),
                MESSAGE_TEXT: message
            }
            client_logger.debug(
                f'Сформирован словарь сообщения: {message_dict}')

            # необходимо дождаться освобождения сокета для отправки сообщения
            with socket_lock:
                send_message(self.transport, message_dict)
                self.process_server_ans(get_message(self.transport))
                client_logger.info(
                    f'Отправлено сообщение для пользователя {to}')

        def run(self):
            ''''Метод содержащий основной цикл работы транспортного потока.'''
            client_logger.debug(
                'Запущен процесс - приёмник собщений с сервера.')
            while self.running:
                # Отдыхаем секунду и снова пробуем захватить сокет.
                # если не сделать тут задержку, то отправка может достаточно
                # долго ждать освобождения сокета.
                time.sleep(1)
                message = None
                with socket_lock:
                    try:
                        self.transport.settimeout(0.5)
                        message = get_message(self.transport)
                    except OSError as err:
                        if err.errno:
                            client_logger.critical(
                                f'Потеряно соединение с сервером.')
                            self.running = False
                            self.connection_lost.emit()
                    # Проблемы с соединением
                    except (ConnectionError, ConnectionAbortedError, ConnectionResetError,\
                            json.JSONDecodeError, TypeError):
                        client_logger.debug(f'Потеряно соединение с сервером.')
                        self.running = False
                        self.connection_lost.emit()

                    finally:
                        self.transport.settimeout(5)
                # Если сообщение получено, то вызываем функцию обработчик:
                if message:
                    client_logger.debug(
                        f'Принято сообщение с сервера: {message}')
                    self.process_server_ans(message)


except Exception as e:
    print('РћС€РёР±РєР°:\n', traceback.format_exc())
