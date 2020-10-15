import os
from datetime import datetime

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Text, DateTime
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy.sql import default_comparator


class DatabaseClient:
    '''
    Класс - оболочка для работы с базой данных клиента.
    Использует SQLite базу данных, реализован с помощью
    SQLAlchemy ORM и используется классический подход.
    '''

    class KnownClients:
        '''
        Класс - отображение для таблицы всех пользователей.
        '''

        def __init__(self, user):
            self.id = None
            self.username = user

    class MessagesHistory:
        '''
        Класс - отображение для таблицы статистики переданных сообщений.
        '''

        def __init__(self, contact, direction, message):
            self.id = None
            self.contact = contact
            self.direction = direction
            self.message = message
            self.date = datetime.now()

    class ClientContacts:
        '''
        Класс - отображение для таблицы контактов.
        '''

        def __init__(self, contact):
            self.id = None
            self.name = contact

    # Конструктор класса:
    def __init__(self, name):
        # Создаём движок базы данных, поскольку разрешено несколько
        # клиентов одновременно, каждый должен иметь свою БД
        # Поскольку клиент мультипоточный необходимо отключить
        # проверки на подключения с разных потоков,
        # иначе sqlite3.ProgrammingError
        path = os.getcwd()
        filename = f'client_{name}.db3'
        self.database_engine = create_engine(
            f'sqlite:///{os.path.join(path, filename)}',
            echo=False,
            pool_recycle=7200,
            connect_args={
                'check_same_thread': False})

        # Создаём объект MetaData
        self.metadata = MetaData()

        # Создаём таблицу известных пользователей
        table_of_clients = Table('Known_clients', self.metadata,
                                 Column('id', Integer, primary_key=True),
                                 Column('username', String)
                                 )

        # Создаём таблицу истории сообщений
        table_of_messages_history = Table('Messages_history', self.metadata,
                                          Column('id', Integer, primary_key=True),
                                          Column('contact', String),
                                          Column('direction', String),
                                          Column('message', Text),
                                          Column('date', DateTime)
                                          )

        # Создаём таблицу контактов
        table_of_clients_contacts = Table('Client_contacts', self.metadata,
                                          Column('id', Integer, primary_key=True),
                                          Column('name', String, unique=True)
                                          )

        # Создаём таблицы
        self.metadata.create_all(self.database_engine)

        # Создаём отображения
        mapper(self.KnownClients, table_of_clients)
        mapper(self.MessagesHistory, table_of_messages_history)
        mapper(self.ClientContacts, table_of_clients_contacts)

        # Создаём сессию
        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        # Необходимо очистить таблицу контактов, т.к. при запуске они
        # подгружаются с сервера.
        self.session.query(self.ClientContacts).delete()
        self.session.commit()

    def add_contact(self, contact):
        '''Метод добавляющий контакт в базу данных.'''
        if not self.session.query(
                self.ClientContacts).filter_by(
                name=contact).count():
            contact_row = self.ClientContacts(contact)
            self.session.add(contact_row)
            self.session.commit()

    def contacts_clear(self):
        '''Метод очищающий таблицу со списком контактов.'''
        self.session.query(self.ClientContacts).delete()

    def delete_contact(self, contact):
        '''Метод удаляющий определённый контакт.'''
        self.session.query(
            self.ClientContacts).filter_by(
            name=contact).delete()

    def add_clients(self, users_list):
        '''Метод заполняющий таблицу известных пользователей.'''
        self.session.query(self.KnownClients).delete()
        for user in users_list:
            user_row = self.KnownClients(user)
            self.session.add(user_row)
        self.session.commit()

    def save_message(self, contact, direction, message):
        '''Метод сохраняющий сообщение в базе данных.'''
        message_row = self.MessagesHistory(contact, direction, message)
        self.session.add(message_row)
        self.session.commit()

    def get_client_contacts(self):
        '''Метод возвращающий список всех контактов.'''
        return [
            contact[0] for contact in self.session.query(
                self.ClientContacts.name).all()]

    def get_known_clients(self):
        '''Метод возвращающий список всех известных пользователей.'''
        return [
            user[0] for user in self.session.query(
                self.KnownClients.username).all()]

    def check_known_client(self, user):
        '''Метод проверяющий существует ли пользователь.'''
        if self.session.query(
                self.KnownClients).filter_by(
                username=user).count():
            return True
        else:
            return False

    def check_contact(self, contact):
        '''Метод проверяющий существует ли контакт.'''
        if self.session.query(
                self.ClientContacts).filter_by(
                name=contact).count():
            return True
        else:
            return False

    def get_history_of_messages(self, contact):
        '''Метод возвращающий историю сообщений с определённым пользователем.'''
        query = self.session.query(
            self.MessagesHistory).filter_by(
            contact=contact)
        return [(history_row.contact,
                 history_row.direction,
                 history_row.message,
                 history_row.date) for history_row in query.all()]


# отладка
if __name__ == '__main__':
    test_db = DatabaseClient('test1')
    for i in ['test3', 'test4', 'test5']:
        test_db.add_contact(i)
    test_db.add_contact('test4')
    test_db.add_clients(['test1', 'test2', 'test3', 'test4', 'test5'])
    test_db.save_message('test2', 'in', f'Привет! я тестовое сообщение от {datetime.now()}!')
    test_db.save_message('test2', 'out', f'Привет! я другое тестовое сообщение от {datetime.now()}!')
    print(test_db.get_client_contacts())
    print(test_db.get_known_clients())
    print(test_db.check_known_client('test1'))
    print(test_db.check_known_client('test10'))
    print(test_db.get_history_of_messages('test2'))
    print(
        sorted(
            test_db.get_history_of_messages('test2'),
            key=lambda item: item[3]))
    print(test_db.get_history_of_messages('test3'))
    test_db.delete_contact('test4')
    print(test_db.get_client_contacts())
