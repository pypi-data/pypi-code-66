from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, \
    DateTime, ForeignKey, Text
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator


class ServerDatabase:
    '''
    Класс - оболочка для работы с базой данных сервера.
    Использует SQLite базу данных, реализован с помощью
    SQLAlchemy ORM и используется классический подход.
    '''

    class AllClients:
        '''Класс - отображение таблицы всех пользователей.'''

        def __init__(self, username, passwd_hash):
            self.id = None
            self.name = username
            self.last_login = datetime.now()
            self.passwd_hash = passwd_hash
            self.pubkey = None

    class ActiveClients:
        '''Класс - отображение таблицы активных пользователей.'''

        def __init__(self, user_id, ip_address, port, login_time):
            self.id = None
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time

    class ClientsLoginHistory:
        '''Класс - отображение таблицы истории входов.'''

        def __init__(self, name, date, ip_address, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip_address = ip_address
            self.port = port

    class ClientsContacts:
        '''Класс - отображение таблицы контактов пользователей.'''

        def __init__(self, user, contact):
            self.id = None
            self.user = user
            self.contact = contact

    class ClientsActionsHistory:
        '''Класс - отображение таблицы истории действий.'''

        def __init__(self, user):
            self.id = None
            self.user = user
            self.sent = 0
            self.received = 0

    def __init__(self, path):
        # Создаём движок базы данных
        self.database_engine = create_engine(
            f'sqlite:///{path}',
            echo=False,
            pool_recycle=7200,
            connect_args={
                'check_same_thread': False})

        # Создаём объект MetaData
        self.metadata = MetaData()

        # Создаём таблицу пользователей
        table_of_all_clients = Table('Clients', self.metadata,
                                     Column('id', Integer, primary_key=True),
                                     Column('name', String, unique=True),
                                     Column('last_login', DateTime),
                                     Column('passwd_hash', String),
                                     Column('pubkey', Text)
                                     )

        # Создаём таблицу активных пользователей
        table_of_active_clients = Table('Active_clients', self.metadata,
                                        Column('id', Integer, primary_key=True),
                                        Column('user', ForeignKey('Clients.id'), unique=True),
                                        Column('ip_address', String),
                                        Column('port', Integer),
                                        Column('login_time', DateTime)
                                        )

        # Создаём таблицу истории входов
        table_of_clients_login_history = Table('Clients_login_history', self.metadata,
                                               Column('id', Integer, primary_key=True),
                                               Column('name', ForeignKey('Clients.id')),
                                               Column('date_time', DateTime),
                                               Column('ip_address', String),
                                               Column('port', String)
                                               )

        # Создаём таблицу контактов пользователей
        table_of_clients_contacts = Table('Clients_contacts', self.metadata,
                                          Column('id', Integer, primary_key=True),
                                          Column('user', ForeignKey('Clients.id')),
                                          Column('contact', ForeignKey('Clients.id'))
                                          )

        # Создаём таблицу статистики пользователей
        table_of_clients_actions_history = Table('Clients_actions_history', self.metadata,
                                                 Column('id', Integer, primary_key=True),
                                                 Column('user', ForeignKey('Clients.id')),
                                                 Column('sent', Integer),
                                                 Column('received', Integer)
                                                 )

        # Создаём таблицы
        self.metadata.create_all(self.database_engine)

        # Создаём отображения
        mapper(self.AllClients, table_of_all_clients)
        mapper(self.ActiveClients, table_of_active_clients)
        mapper(self.ClientsLoginHistory, table_of_clients_login_history)
        mapper(self.ClientsContacts, table_of_clients_contacts)
        mapper(self.ClientsActionsHistory, table_of_clients_actions_history)

        # Создаём сессию
        SESSION = sessionmaker(bind=self.database_engine)
        self.session = SESSION()

        # Если в таблице активных пользователей есть записи, то их необходимо
        # удалить
        self.session.query(self.ActiveClients).delete()
        self.session.commit()

    def client_login(self, username, ip_address, port, key):
        '''
        Метод выполняющийся при входе пользователя, записывает в базу факт входа
        Обновляет открытый ключ пользователя при его изменении.
        '''
        # Запрос в таблицу пользователей на наличие там пользователя с таким
        # именем
        res = self.session.query(self.AllClients).filter_by(name=username)

        # Если имя пользователя уже присутствует в таблице, обновляем время последнего входа
        # и проверяем корректность ключа. Если клиент прислал новый ключ,
        # сохраняем его.
        if res.count():
            user = res.first()
            user.last_login = datetime.now()
            if user.pubkey != key:
                user.pubkey = key
        # Если нету, то генерируем исключение
        else:
            raise ValueError('Пользователь не зарегистрирован.')

        # Теперь можно создать запись в таблицу активных пользователей о факте
        # входа.
        new_active_client = self.ActiveClients(
            user.id, ip_address, port, datetime.now())
        self.session.add(new_active_client)

        # и сохранить в историю входов
        history_of_input = self.ClientsLoginHistory(
            user.id, datetime.now(), ip_address, port)
        self.session.add(history_of_input)

        # Сохрраняем изменения
        self.session.commit()

    def add_user(self, name, passwd_hash):
        '''
        Метод регистрации пользователя.
        Принимает имя и хэш пароля, создаёт запись в таблице статистики.
        '''
        user_row = self.AllClients(name, passwd_hash)
        self.session.add(user_row)
        self.session.commit()
        history_row = self.ClientsActionsHistory(user_row.id)
        self.session.add(history_row)
        self.session.commit()

    def delete_user(self, name):
        '''Метод удаляющий пользователя из базы.'''
        user = self.session.query(
            self.AllClients).filter_by(
            name=name).first()
        self.session.query(
            self.ActiveClients).filter_by(
            user=user.id).delete()
        self.session.query(
            self.ClientsLoginHistory).filter_by(
            name=user.id).delete()
        self.session.query(
            self.ClientsContacts).filter_by(
            user=user.id).delete()
        self.session.query(
            self.ClientsContacts).filter_by(
            contact=user.id).delete()
        self.session.query(
            self.ClientsActionsHistory).filter_by(
            user=user.id).delete()
        self.session.query(self.AllClients).filter_by(name=name).delete()
        self.session.commit()

    def get_hash(self, name):
        '''Метод получения хэша пароля пользователя.'''
        user = self.session.query(
            self.AllClients).filter_by(
            name=name).first()
        return user.passwd_hash

    def get_pubkey(self, name):
        '''Метод получения публичного ключа пользователя.'''
        user = self.session.query(
            self.AllClients).filter_by(
            name=name).first()
        return user.pubkey

    def check_client(self, name):
        '''Метод проверяющий существование пользователя.'''
        if self.session.query(
                self.AllClients).filter_by(
            name=name).count():
            return True
        else:
            return False

    def client_logout(self, username):
        '''Метод фиксирующий отключения пользователя.'''
        # Запрашиваем пользователя, что покидает нас
        user = self.session.query(
            self.AllClients).filter_by(
            name=username).first()
        # Удаляем его из таблицы активных пользователей.
        self.session.query(
            self.ActiveClients).filter_by(
            user=user.id).delete()
        # Применяем изменения
        self.session.commit()

    def message_transmission(self, sender, receiver):
        '''Метод записывающий в таблицу статистики факт передачи сообщения.'''
        # Получаем ID отправителя и получателя
        sender = self.session.query(
            self.AllClients).filter_by(
            name=sender).first().id
        receiver = self.session.query(
            self.AllClients).filter_by(
            name=receiver).first().id
        # Запрашиваем строки из истории и увеличиваем счётчики
        sender_row = self.session.query(
            self.ClientsActionsHistory).filter_by(
            user=sender).first()
        sender_row.sent += 1
        receiver_row = self.session.query(
            self.ClientsActionsHistory).filter_by(
            user=receiver).first()
        receiver_row.received += 1

        self.session.commit()

    def add_contact(self, user, contact):
        '''Метод добавления контакта для пользователя.'''
        # Получаем ID пользователей
        user = self.session.query(
            self.AllClients).filter_by(
            name=user).first()
        contact = self.session.query(
            self.AllClients).filter_by(
            name=contact).first()

        # Проверяем что не дубль и что контакт может существовать (полю
        # пользователь мы доверяем)
        if not contact or self.session.query(
                self.ClientsContacts).filter_by(
            user=user.id,
            contact=contact.id).count():
            return

        # Создаём объект и заносим его в базу
        contact_row = self.ClientsContacts(user.id, contact.id)
        self.session.add(contact_row)
        self.session.commit()

    # Функция удаляет контакт из базы данных
    def delete_contact(self, user, contact):
        '''Метод удаления контакта пользователя.'''
        # Получаем ID пользователей
        user = self.session.query(
            self.AllClients).filter_by(
            name=user).first()
        contact = self.session.query(
            self.AllClients).filter_by(
            name=contact).first()

        # Проверяем что контакт может существовать (полю пользователь мы
        # доверяем)
        if not contact:
            return

        # Удаляем требуемое
        self.session.query(self.ClientsContacts).filter(
            self.ClientsContacts.user == user.id,
            self.ClientsContacts.contact == contact.id
        ).delete()
        self.session.commit()

    def list_of_clients(self):
        '''Метод возвращающий список известных пользователей со временем последнего входа.'''
        # Запрос строк таблицы пользователей.
        query = self.session.query(
            self.AllClients.name,
            self.AllClients.last_login
        )
        # Возвращаем список кортежей
        return query.all()

    def list_of_active_clients(self):
        '''Метод возвращающий список активных пользователей.'''
        # Запрашиваем соединение таблиц и собираем кортежи имя, адрес, порт,
        # время.
        query = self.session.query(
            self.AllClients.name,
            self.ActiveClients.ip_address,
            self.ActiveClients.port,
            self.ActiveClients.login_time
        ).join(self.AllClients)
        # Возвращаем список кортежей
        return query.all()

    def login_history(self, username=None):
        '''Метод возвращающий историю входов.'''
        # Запрашиваем историю входа
        query = self.session.query(
            self.AllClients.name,
            self.ClientsLoginHistory.date_time,
            self.ClientsLoginHistory.ip_address,
            self.ClientsLoginHistory.port
        ).join(self.AllClients)
        # Если было указано имя пользователя, то фильтруем по нему
        if username:
            query = query.filter(self.AllClients.name == username)
            # Возвращаем список кортежей
        return query.all()

    def list_of_contacts(self, username):
        '''Метод возвращающий список контактов пользователя.'''
        # Запрашивааем указанного пользователя
        user = self.session.query(
            self.AllClients).filter_by(
            name=username).one()

        # Запрашиваем его список контактов
        query = self.session.query(
            self.ClientsContacts,
            self.AllClients.name).filter_by(
            user=user.id).join(
            self.AllClients,
            self.ClientsContacts.contact == self.AllClients.id)

        # выбираем только имена пользователей и возвращаем их.
        return [contact[1] for contact in query.all()]

    def messages_history(self):
        '''Метод возвращающий статистику сообщений.'''
        query = self.session.query(
            self.AllClients.name,
            self.AllClients.last_login,
            self.ClientsActionsHistory.sent,
            self.ClientsActionsHistory.received
        ).join(self.AllClients)
        # Возвращаем список кортежей
        return query.all()


# Отладка
if __name__ == '__main__':
    test_db = ServerDatabase('../server_database.db3')
    test_db.client_login('1111', '192.168.1.38', 8080)
    test_db.client_login('McG2', '192.168.1.38', 8081)
    print(test_db.list_of_clients())
    # print(test_db.list_of_active_clients())
    # test_db.client_logout('McG')
    # print(test_db.login_history('re'))
    # test_db.add_contact('test2', 'test1')
    # test_db.add_contact('test1', 'test3')
    # test_db.add_contact('test1', 'test6')
    # test_db.delete_contact('test1', 'test3')
    test_db.message_transmission('dsfdsfdsffds', 'SAdADSqwe')
    print(test_db.messages_history())
