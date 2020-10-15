import dis


class ServerVerifier(type):
    '''
    Метакласс, проверяющий что в результирующем классе нет клиентских
    вызовов таких как: connect. Также проверяется, что серверный
    сокет является TCP и работает по IPv4 протоколу.
    '''

    def __init__(cls, name, bases, dct):
        # Список методов, которые используются в функциях класса:
        methods = []
        # Атрибуты, вызываемые функциями классов
        attrs = []
        for func in dct:
            # Пробуем
            try:
                res = dis.get_instructions(dct[func])
                # Если не функция то ловим исключение
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы и
                # атрибуты.
                for i in res:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
                    if i.opname == 'LOAD_ATTR':
                        if i.argval not in attrs:
                            attrs.append(i.argval)
        # Если обнаружено использование недопустимого метода connect,
        # генерируем исключение:
        if 'connect' in methods:
            raise TypeError('Недопустимый метод')
        # Если сокет не инициализировался константами SOCK_STREAM(TCP)
        # AF_INET(IPv4), тоже исключение.
        if not ('SOCK_STREAM' in attrs and 'AF_INET' in attrs):
            raise TypeError('Нет вызовов функций, работающих с сокетами')
        super().__init__(name, bases, dct)


class ClientVerifier(type):
    '''
    Метакласс, проверяющий что в результирующем классе нет серверных
    вызовов таких как: accept, listen. Также проверяется, что сокет не
    создаётся внутри конструктора класса.
    '''

    def __init__(cls, name, bases, dct):
        # Список методов, которые используются в функциях класса:
        methods = []
        for func in dct:
            # Пробуем
            try:
                res = dis.get_instructions(dct[func])
                # Если не функция то ловим исключение
            except TypeError:
                pass
            else:
                # Раз функция разбираем код, получая используемые методы.
                for i in res:
                    if i.opname == 'LOAD_GLOBAL':
                        if i.argval not in methods:
                            methods.append(i.argval)
        # Если обнаружено использование недопустимого метода accept, listen,
        # socket бросаем исключение:
        for method in ('accept', 'listen', 'socket'):
            if method in methods:
                raise TypeError("Недопустимый метод")
        # Вызов get_message или send_message из utils считаем корректным
        # использованием сокетов
        if 'get_message' in methods or 'send_message' in methods:
            pass
        else:
            raise TypeError(
                'Отсутствуют вызовы функций, работающих с сокетами.')
        super().__init__(name, bases, dct)
