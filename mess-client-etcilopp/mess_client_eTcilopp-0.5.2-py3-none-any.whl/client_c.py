# Программа-клиент
import sys
import json
import socket
import time
import logging
import log.client_log_config
from decorators import Log
import threading
from metaclasses import ClientMaker
import form

from common.variables import ACTION, PRESENCE, TIME, USER, ACCOUNT_NAME, RESPONSE, \
    ERROR, DEFAULT_IP_ADDRESS, DEFAULT_PORT, SENDER, MESSAGE, MESSAGE_TEXT, DESTINATION

from common.utils import get_message, send_message


class Client(metaclass=ClientMaker):
    def __init__(self, ip, port, socket, client_name):
        self.ip = ip
        self.port = port
        self.client_name = client_name
        self.s = socket

    def process_answer(self, message):
        """
        Функция читает ответ сервера
        :param message:
        :return:
        """
        if RESPONSE in message:
            if message[RESPONSE] == 200:
                return '200 : OK'
            return f'400 : {message[ERROR]}'
        raise ValueError

    def create_message(self, sock, recipient, message):
        if recipient == "0":
            sock.close()
            # CLIENT_LOGGER.info('Exiting.')
            sys.exit(0)
        elif (recipient == 'Server' or recipient == 'server') and message == '1':
                return {
                    ACTION: 'command1',
                    SENDER: self.client_name,
                    DESTINATION: recipient,
                    TIME: time.time(),
                    MESSAGE_TEXT: message
                }

        # if message == '2':
        #        message = input("enter new client's name: ")
        #         return {
        #             ACTION: 'command2',
        #             SENDER: self.client_name,
        #             DESTINATION: recipient,
        #             TIME: time.time(),
        #             MESSAGE_TEXT: message
        #         }
        # else:
        message_dict = {
                ACTION: MESSAGE,
                SENDER: self.client_name,
                DESTINATION: recipient,
                TIME: time.time(),
                MESSAGE_TEXT: message
            }
        # CLIENT_LOGGER.debug(f'Message dict created: {message_dict}')
        return message_dict

    def message_from_server(self, transport):
        # print(f'{self.client_name} is listening.')
        # while True:
        try:
            message = get_message(transport)
            # CLIENT_LOGGER.info(f'Received generic message: {message}')
        except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
            # CLIENT_LOGGER.error(f'Connection with Server was lost.')
            sys.exit(1)
        else:
            # CLIENT_LOGGER.info(f'Started processing message from server: {message}')
            if ACTION in message and message[ACTION] == MESSAGE and \
                    SENDER in message and MESSAGE_TEXT in message and \
                    message[DESTINATION] == self.client_name:
                return(f'{message[SENDER]}: {message[MESSAGE_TEXT]}')
                # print(f'\n{self.client_name} received message from user '
                #         f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
                # CLIENT_LOGGER.info(f'Received message from user '
                #                    f'{message[SENDER]}:\n{message[MESSAGE_TEXT]}')
            else:
                return
                # return f'Received message from server: {message}'

    def message_out(self, transport, recipient, message):
        # while True:
        try:
            message_dict = self.create_message(transport, recipient, message)
            # CLIENT_LOGGER.debug(f'Preparing to send message {message_dict} '
            #                     f'to the client {message_dict[DESTINATION]}')
            send_message(transport, message_dict)
            # CLIENT_LOGGER.debug(f'Sent message to the server')
        except (ConnectionResetError, ConnectionError, ConnectionAbortedError):
            print(f'Connection with Server was lost.')
            # CLIENT_LOGGER.error(f'Connection with Server was lost.')
            sys.exit(1)

    def run_client(self):
        # CLIENT_LOGGER.info(f'Started client.')

        # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # s.connect((self.ip, self.port))
        # message_to_server = self.create_presence_respond()
        # send_message(s, message_to_server)
        # CLIENT_LOGGER.info(f'Sent message to the Server: {message_to_server}')
        try:
            answer = self.process_answer(get_message(self.s))
            # CLIENT_LOGGER.info(f'Received answer from server: {answer}')
            print(answer)
        except (ValueError, json.JSONDecodeError):
            # CLIENT_LOGGER.error('Message from server cannot be decoded')
            print('Message from server cannot be decoded')
        else:
            # receive_thread = threading.Thread(target=self.message_from_server, args=(self.s,))
            # receive_thread.daemon = True
            # receive_thread.start()
            self.message_from_server(self.s)

            # send_thread = threading.Thread(target=self.message_out, args=(self.s,))
            # send_thread.daemon = True
            # send_thread.start()

            # while True:
            #     time.sleep(1)
            #     if receive_thread.is_alive() and send_thread.is_alive():
            #         continue
            #     break


def main(name):

    CLIENT_LOGGER = logging.getLogger('client')
    ip = DEFAULT_IP_ADDRESS
    port = DEFAULT_PORT
    client_name = name

    for idx in range(len(sys.argv)):
        if sys.argv[idx] == '-address':
            ip = sys.argv[idx + 1]
        elif sys.argv[idx] == '-port':
            port = int(sys.argv[idx + 1])
        elif sys.argv[idx] == '-name':
            client_name = sys.argv[idx + 1]
    # if client_name == USER:
    #     client_name = input('Enter client\'s name: ')

    if (port > 1024 or port < 65535) and client_name:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip, port))
        message_to_server = create_presence_respond(client_name)
        send_message(s, message_to_server)

        client = Client(ip, port, s, client_name)
        # client.run_client()
        return client
    else:
        CLIENT_LOGGER.critical(f'Used illegal port or illegal client mode.')
        print('Used illegal port or illegal client mode.')


@Log()
def create_presence_respond(account_name='Guest'):
    """
    Функция формирует запрос о присутствии клиента
    :param account_name:
    :return:
    """
    msg = {
        ACTION: PRESENCE,
        TIME: time.time(),
        USER: {
            ACCOUNT_NAME: account_name
        }
    }
    return msg


if __name__ == '__main__':
    main()
