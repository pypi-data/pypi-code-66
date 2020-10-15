""" Утилиты """
import json
import sys
from common.decorators import log
from common.vars import MAX_PACKAGE_LENGTH, ENCODING

sys.path.append('../../')


@log
def message_in(client):
    """
    Функция приёма и декодирования сообщения принимает байты выдаёт словарь,
    если принято что-то другое отдаёт ошибку значения
    :param client:
    :return:
    """

    encoded_response = client.recv(MAX_PACKAGE_LENGTH)
    json_response = encoded_response.decode(ENCODING)
    response = json.loads(json_response)
    if isinstance(response, dict):
        return response
    raise TypeError


@log
def message_out(sock, message):
    """
    Функция кодирования и отправки сообщения принимает словарь и отправляет его
    :param sock:
    :param message:
    :return:
    """

    json_message = json.dumps(message)
    encoded_message = json_message.encode(ENCODING)
    sock.send(encoded_message)
