import threading
import logging
import select
import socket
import json
import hmac
import binascii
import os
from common.descr import CheckPort
from common.my_utils import send_message, get_message
from common.my_variables import MAX_CONECT, DESTINATIONS, ACTION, PRESENCE, TIME,\
    USER, MESSAGE, MESSAGE_TEXT, SENDER, RESPONSE_200, RESPONSE_400, ERROR, EXIT, ACCOUNT_NAME,\
    GET_CONTACTS, RESPONSE_202, LIST_INFO, ADD_CONTACT, REMOVE_CONTACT, USERS_REQUEST,\
    PUBLIC_KEY_REQUEST, RESPONSE_511, DATA, RESPONSE, PUBLIC_KEY, RESPONSE_205


# инициализация логирования сервера
server_logger = logging.getLogger('server')


class MessageProcessor(threading.Thread):
    '''Основной класс сервера. Принимает содинения, словари - пакеты
    от клиентов, обрабатывает поступающие сообщения.
    Работает в качестве отдельного потока.'''
    port = CheckPort()

    def __init__(self, address_listen, port_listen, database):
        self.addr = address_listen
        self.port = port_listen

        # база данных сервера
        self.database = database

        # сокет, через кот осущ работа
        self.sock = None

        # список клиентов
        self.clients = []

        # сокеты
        self.listen_sockets = None
        self.error_sockets = None

        # флаг продолжения работы
        self.running = True

        # сопоставление имен и соответствующим им сокетам
        self.names = dict()

        super().__init__()

    def run(self):
        '''Основной цикл потока'''
        self.socket_init()

        while self.running:
            # ждем полключение, если таймаут вышел - исключение
            try:
                client, address_client = self.sock.accept()
                server_logger.info(
                    f'Установлено соедение с ПК {address_client}')
            except OSError:
                pass
            else:
                server_logger.info(
                    f'2Установлено соедение с ПК {address_client}')
                client.settimeout(5)
                self.clients.append(client)

            recv_data_lst = []
            send_data_lst = []
            err_lst = []

            # проверить наличие ждущих клиентов
            try:
                if self.clients:
                    recv_data_lst, self.listen_sockets, self.error_sockets = select.select(
                        self.clients, self.clients, [], 0)
            except OSError as err:
                server_logger.error(f'Ошибка работы с сокетами: {err.errno}')

            # принять сообщения и если там есть сообщения - положить в словарь,
            # если ошибка - исключит клиента
            if recv_data_lst:
                for client_with_message in recv_data_lst:
                    try:
                        self.processing_message_client(
                            get_message(client_with_message), client_with_message)
                    except (OSError, json.JSONDecodeError, TypeError) as err:
                        server_logger.info(
                            f'Клиент {client_with_message.getpeername()} отключился от сервера.1',
                            exc_info=err)
                        self.remove_client(client_with_message)

    def remove_client(self, client):
        '''Метод - обработка клиента, с которым прервана связь'''
        server_logger.info(
            f'Клиент {client.getpeername()} отключился от сервера.1')
        for name in self.names:
            if self.names[name] == client:
                self.database.user_logout(name)
                del self.names[name]
                break
        self.clients.remove(client)
        client.close()

    def socket_init(self):
        '''Инициализация сокета'''
        server_logger.info(
            f'Запущен сервер, порт для подключений: {self.port}, адрес с которого принимаются'
            f' подключения: {self.addr}. Если адрес не указан, принимаются соединения '
            f'с любых адресов.')

        # создание сокета и прописание параметров
        transport = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        transport.bind((self.addr, self.port))
        transport.settimeout(0.5)

        # прослушивание сокета
        self.sock = transport
        self.sock.listen(MAX_CONECT)

    def create_process_message(self, message):
        '''Метод - адресная отправка определенному клиенту'''
        if message[DESTINATIONS] in self.names and self.names[message[DESTINATIONS]
                                                              ] in self.listen_sockets:
            try:
                send_message(self.names[message[DESTINATIONS]], message)
                server_logger.info(
                    f'Сообщение отправлено пользователю {message[DESTINATIONS]} '
                    f'от {message[SENDER]}')
            except BaseException:
                self.remove_client(message[DESTINATIONS])
        elif message[DESTINATIONS] in self.names and self.names[message[DESTINATIONS]] not in \
                self.listen_sockets:
            server_logger.error(
                f'Связь с клиентом {message[DESTINATIONS]} была потеряна. '
                f'Соединение закрыто')
            self.remove_client(self.names[message[DESTINATIONS]])
        else:
            server_logger.error(
                f'Отправка сообщения не возможна, пользователь {message[DESTINATIONS]}'
                f' Не заргегистрирован')

    def processing_message_client(self, message, client):
        '''обработчик сообщений от клиентов, принимет словарь - сообщение от клиента,
        проверяет корректронсть, возвращает словарь-ответ для клиента
        '''
        server_logger.debug(f'Рpазбор сообщения от клиента: {message}')
        # если сообщение о присутствии, то принимаем и отвечаем
        if ACTION in message and message[ACTION] == PRESENCE and TIME in message and\
                USER in message:
            # вызов функции авторизации
            self.autorize_user(message, client)
        # если сообщение - отправляем получателю
        elif ACTION in message and message[ACTION] == MESSAGE and DESTINATIONS in message and TIME\
                in message and SENDER in message and MESSAGE_TEXT in message and \
                self.names[message[SENDER]] == client:
            if message[DESTINATIONS] in self.names:
                self.database.process_message(
                    message[SENDER], message[DESTINATIONS])
                self.create_process_message(message)
                try:
                    send_message(client, RESPONSE_200)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'Пользователь не зарегистрирован на сервере.'
                try:
                    send_message(client, response)
                except OSError:
                    pass
            return

        # Если клиент выходит
        elif ACTION in message and message[ACTION] == EXIT and ACCOUNT_NAME in message and \
                self.names[message[ACCOUNT_NAME]] == client:

            server_logger.info(
                f'Клиент {message[ACCOUNT_NAME]} корректно отключился от сервера.')
            self.remove_client(client)

        # если это запрос контакт-листа
        elif ACTION in message and message[ACTION] == GET_CONTACTS and USER in message and \
                self.names[message[USER]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = self.database.get_contacts(message[USER])
            try:
                send_message(client, response)
            except OSError:
                self.remove_client(client)
        # если это добавление контакта
        elif ACTION in message and message[ACTION] == ADD_CONTACT and ACCOUNT_NAME in message and \
                USER in message and self.names[message[USER]] == client:
            self.database.add_contact(message[USER], message[ACCOUNT_NAME])
            try:
                send_message(client, RESPONSE_200)
            except BaseException:
                self.remove_client(client)
        # если это удаление контакта
        elif ACTION in message and message[ACTION] == REMOVE_CONTACT and ACCOUNT_NAME in message \
                and USER in message and self.names[message[USER]] == client:
            self.database.remove_contact(message[USER], message[ACCOUNT_NAME])
            try:
                send_message(client, RESPONSE_200)
            except BaseException:
                self.remove_client(client)
        # если это запрос известных пользователей
        elif ACTION in message and message[ACTION] == USERS_REQUEST and ACCOUNT_NAME in message \
                and self.names[message[ACCOUNT_NAME]] == client:
            response = RESPONSE_202
            response[LIST_INFO] = [user[0]
                                   for user in self.database.users_list()]
            try:
                send_message(client, response)
            except BaseException:
                self.remove_client(client)

        # если запрос публичного ключа пользов-я
        elif ACTION in message and message[ACTION] == PUBLIC_KEY_REQUEST and ACCOUNT_NAME \
                in message:
            response = RESPONSE_511
            response[DATA] = self.database.get_pubkey(message[ACCOUNT_NAME])
            # может быть, что ключа ещё нет (пользователь никогда не логинился,
            # тогда шлём 400)
            if response[DATA]:
                try:
                    send_message(client, response)
                except OSError:
                    self.remove_client(client)
            else:
                response = RESPONSE_400
                response[ERROR] = 'Нет публичного ключа для данного пользователя'
                try:
                    send_message(client, response)
                except OSError:
                    self.remove_client(client)

        # иначе bad request
        else:
            response = RESPONSE_400
            response[ERROR] = 'Запрос некорректен.'
            try:
                send_message(client, response)
            except OSError:
                self.remove_client(client)

    def autorize_user(self, message, sock):
        '''Метод - реализация авторизации пользователя'''
        server_logger.debug(f'начало процесса авторизации для {message[USER]}')
        # если имя занято - возвращаем ответ 400
        if message[USER][ACCOUNT_NAME] in self.names.keys():
            response = RESPONSE_400
            response[ERROR] = 'Имя пользователя уже занято.'
            try:
                server_logger.debug(f'пользователь занят, отправка {response}')
                send_message(sock, response)
            except OSError:
                server_logger.debug('OS Error')
                pass
            self.clients.remove(sock)
            sock.close()

        # проверка того, что пользователь зарегистрирован на сервере
        elif not self.database.check_user(message[USER][ACCOUNT_NAME]):
            response = RESPONSE_400
            response[ERROR] = 'Пользователь не зарегистрирован.'
            try:
                server_logger.debug(
                    f'неизвестный пользователь, отправка {response}')
                send_message(sock, response)
            except OSError:
                pass
            self.clients.remove(sock)
            sock.close()

        else:
            server_logger.debug(
                'корректный пользователь, начало изменения пароля.')
            # иначе отвечаем 511 и проводим процедуру авторизации
            #словарь - заготовка
            message_auth = RESPONSE_511
            # набор байтов в hex представлении
            random_str = binascii.hexlify(os.urandom(64))
            # в словарь байты нельзя, декодируем (json.dumps -> TypeError)
            message_auth[DATA] = random_str.decode('ascii')
            # создать хэш пароля и связки с рандомной строкой, сохраняем
            # серверную версию ключа
            hash = hmac.new(
                self.database.get_hash(
                    message[USER][ACCOUNT_NAME]),
                random_str,
                'MD5')
            digest = hash.digest()
            server_logger.debug(f'Auth message = {message_auth}')
            try:
                # обмен с клиентом
                send_message(sock, message_auth)
                ans = get_message(sock)
            except OSError as err:
                server_logger.debug('Error in auth, data:', exc_info=err)
                sock.close()
                return
            client_digest = binascii.a2b_base64(ans[DATA])
            # если ответ клиента корректный - сохраняем его в список
            # пользователей
            if RESPONSE in ans and ans[RESPONSE] == 511 and hmac.compare_digest(
                    digest, client_digest):
                self.names[message[USER][ACCOUNT_NAME]] = sock
                client_ip, client_port = sock.getpeername()
                try:
                    send_message(sock, RESPONSE_200)
                except OSError:
                    self.remove_client(message[USER][ACCOUNT_NAME])
                # добавляем пользователя в список активных и если у него изменился открытый ключ
                # сохраняем новый
                self.database.user_login(
                    message[USER][ACCOUNT_NAME],
                    client_ip,
                    client_port,
                    message[USER][PUBLIC_KEY])
            else:
                response = RESPONSE_400
                response[ERROR] = 'Неверный пароль.'
                try:
                    send_message(sock, response)
                except OSError:
                    pass
                self.clients.remove(sock)
                sock.close()

    def service_update_lists(self):
        '''Метод - отправка сервисоного сообщения 205 клиентам'''
        for client in self.names:
            try:
                send_message(self.names[client], RESPONSE_205)
            except OSError:
                self.remove_client(self.names[client])
