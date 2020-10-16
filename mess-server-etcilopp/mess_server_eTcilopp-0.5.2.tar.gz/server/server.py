import select
import sys
import socket
import json
import time
import logging

from common.variables import ACTION, ACCOUNT_NAME, RESPONSE, MAX_CONNECTIONS, \
    PRESENCE, TIME, USER, ERROR, DEFAULT_PORT, DEFAULT_IP_ADDRESS, MESSAGE, \
    MESSAGE_TEXT, SENDER, DESTINATION

from common.utils import get_message, send_message


def process_client_message(message, message_list, client):
    SERVER_LOGGER.info(f'Reading message from:: {client}: {message}')
    if ACTION in message and message[ACTION] == PRESENCE and TIME in message \
            and USER in message:
        SERVER_LOGGER.info(f'Client {client} will get RESPONSE: 200')
        send_message(client, {RESPONSE: 200})
        return
    elif ACTION in message and message[ACTION] == MESSAGE and TIME in message and MESSAGE_TEXT in message:
        message_list.append((message[SENDER], message[DESTINATION], message[MESSAGE_TEXT]))
        SERVER_LOGGER.info(f'message list updated: {message_list}')
        return
    else:
        SERVER_LOGGER.info(f'Bad request will be returned to {client}')
        send_message(client, {
            RESPONSE: 400,
            ERROR: 'Bad Request'
        })
        return


def handle_client_message(message):
    if ACTION in message and \
            message[ACTION] == PRESENCE and \
            TIME in message and \
            USER in message and \
            message[USER][ACCOUNT_NAME] == 'Guest':
        return {RESPONSE: 200}
    return {
        RESPONSE: 400,
        ERROR: 'Bad Request'
    }


def run_server(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((ip, port))
    SERVER_LOGGER.info('Server started')
    s.settimeout(0.5)
    s.listen(MAX_CONNECTIONS)

    clients = []
    messages = []

    while True:
        try:
            client, client_addr = s.accept()
        except OSError:
            pass
        else:
            clients.append(client)
            SERVER_LOGGER.info(f'Established connection with client {client_addr}')
            print(f'Established connection with client {client_addr}')

        recv_data_list = []
        send_data_list = []
        err_list = []

        try:
            if clients:
                recv_data_list, send_data_list, err_list = select.select(clients, clients, [], 0)
        except OSError:
            pass

        if recv_data_list:
            for client_with_message in recv_data_list:
                try:
                    process_client_message(get_message(client_with_message), messages, client_with_message)
                except:
                    SERVER_LOGGER.info(f'Client_ {client_with_message.getpeername()} disconnected from Server.')
                    SERVER_LOGGER.info(f'messages: {messages}')
                    SERVER_LOGGER.info(f'client_with_message: {client_with_message}')
                    clients.remove(client_with_message)

        if messages and send_data_list:
            message = {
                ACTION: MESSAGE,
                SENDER: messages[0][0],
                TIME: time.time(),
                DESTINATION: messages[0][1],
                MESSAGE_TEXT: messages[0][2]
            }
            del messages[0]
            for waiting_client in send_data_list:
                try:
                    send_message(waiting_client, message)
                except:
                    SERVER_LOGGER.info(f'Client {waiting_client.getpeername()} disconnected from server.')
                    clients.remove(waiting_client)


if __name__ == '__main__':
    ip = DEFAULT_IP_ADDRESS
    server_port = DEFAULT_PORT
    SERVER_LOGGER = logging.getLogger('server')

    for idx in range(len(sys.argv)):
        if sys.argv[idx] == '-a':
            ip = sys.argv[idx + 1]
        elif sys.argv[idx] == '-p':
            server_port = int(sys.argv[idx + 1])

    if server_port > 1024 or server_port < 65535:
        run_server(ip, server_port)
    else:
        SERVER_LOGGER.critical(f'Used port {server_port}: Only ports from 1024 to 65535 are allowed')
        print('Only ports from 1024 to 65535 are allowed.')
