""" Метаклассы """
import dis


class ServerMain(type):
    """
    Метакласс, проверяющий что в результирующем классе нет клиентских
    вызовов таких как: connect. Также проверяется, что серверный
    сокет является TCP и работает по IPv4 протоколу.
    """

    def __init__(self, exampleclass, base, clsdict):
        methods = []
        attrs = []

        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    # print(i)
                    if i.opname == 'LOAD_GLOBAL':
                        methods.append(i.argval)
                    elif i.opname == 'LOAD_ATTR':
                        if i.argval not in attrs:
                            attrs.append(i.argval)
        # print(methods)
        # print(attrs)
        if 'connect' in methods:
            raise TypeError('Исполтьзование метода connect недопустимо в серверном классе')
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Некорректная инициализация сокета')
        # Добавил блок проверки  в метакласс сервера аналогично клиентскому метаклассу.
        if 'message_in' in methods or 'message_out' in methods:
            pass
        else:
            raise TypeError('Отсутствуют функции,обработки входящих и исходящих сообщений.')
        super().__init__(exampleclass, base, clsdict)


class ClientMain(type):
    """
    Метакласс, проверяющий что в результирующем классе нет серверных
    вызовов таких как: accept, listen. Также проверяется, что сокет не
    создаётся внутри конструктора класса.
    """

    def __init__(self, exampleclass, base, clsdict):
        methods = []
        for func in clsdict:
            try:
                ret = dis.get_instructions(clsdict[func])
            except TypeError:
                pass
            else:
                for i in ret:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        for command in ('accept', 'listen', 'socket'):
            if command in methods:
                raise TypeError('В классе клиента данные методы не используются')
        if 'message_in' in methods or 'message_out' in methods:
            pass
        else:
            raise TypeError('Отсутствуют функции,обработки входящих и исходящих сообщений.')
        super().__init__(exampleclass, base, clsdict)
