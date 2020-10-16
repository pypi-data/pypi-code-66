from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, DateTime, \
    ForeignKey
import datetime
from sqlalchemy.orm import mapper, sessionmaker, aliased

SERVER_DATABASE = 'sqlite:///server_base.db3'


class ServerDatabase:
    def __init__(self):
        self.database_engine = create_engine(
            SERVER_DATABASE, echo=False, pool_recycle=7200)
        self.metadata = MetaData()
        users_tbl = Table('Users', self.metadata,
                          Column('id', Integer, primary_key=True),
                          Column('name', String, unique=True),
                          Column('last_login', DateTime)
                          )

        active_users_tbl = Table(
            'Active_users', self.metadata, Column(
                'id', Integer, primary_key=True), Column(
                'user', ForeignKey('Users.id'), unique=True), Column(
                'ip_address', String), Column(
                    'port', Integer), Column(
                        'login_time', DateTime))

        user_login_history = Table('Login_history', self.metadata,
                                   Column('id', Integer, primary_key=True),
                                   Column('name', ForeignKey('Users.id')),
                                   Column('date_time', DateTime),
                                   Column('ip', String),
                                   Column('port', String)
                                   )
        user_contact_list_tbl = Table(
            'Contact_list', self.metadata, Column(
                'id', Integer, primary_key=True), Column(
                'user', ForeignKey('Users.id')), Column(
                'contact', ForeignKey('Users.id')), Column(
                    'date_added', DateTime))

        self.metadata.create_all(self.database_engine)

        mapper(self.AllUsers, users_tbl)
        mapper(self.ActiveUsers, active_users_tbl)
        mapper(self.LoginHistory, user_login_history)
        mapper(self.ContactList, user_contact_list_tbl)

        Session = sessionmaker(bind=self.database_engine)
        self.session = Session()

        self.session.query(self.ActiveUsers).delete()
        self.session.commit()

    class AllUsers:
        def __init__(self, username):
            self.name = username
            self.last_login = datetime.datetime.now()
            self.id = None

    class ActiveUsers:
        def __init__(self, user_id, ip_address, port, login_time):
            self.user = user_id
            self.ip_address = ip_address
            self.port = port
            self.login_time = login_time
            self.id = None

    class LoginHistory:
        def __init__(self, name, date, ip, port):
            self.id = None
            self.name = name
            self.date_time = date
            self.ip = ip
            self.port = port

    class ContactList:
        def __init__(self, user, contact, date_created):
            self.id = None
            self.user = user
            self.contact = contact
            self.date_created = date_created

    def user_login(self, username, ip_address, port):
        print(username, ip_address, port)
        rez = self.session.query(self.AllUsers).filter_by(name=username)
        if rez.count():
            user = rez.first()
            user.last_login = datetime.datetime.now()
        else:
            user = self.AllUsers(username)
            self.session.add(user)
            self.session.commit()

        new_active_user = self.ActiveUsers(
            user.id, ip_address, port, datetime.datetime.now())
        self.session.add(new_active_user)

        history = self.LoginHistory(
            user.id, datetime.datetime.now(), ip_address, port)
        self.session.add(history)

        self.session.commit()

    def user_logout(self, username):
        user = self.session.query(
            self.AllUsers).filter_by(
            name=username).first()
        if user:
            self.session.query(
                self.ActiveUsers).filter_by(
                user=user.id).delete()
            self.session.commit()

    def users_list(self):
        query = self.session.query(
            self.AllUsers.name,
            self.AllUsers.last_login,
        )
        return query.all()

    def active_users_list(self):
        query = self.session.query(
            self.AllUsers.name,
            self.ActiveUsers.ip_address,
            self.ActiveUsers.port,
            self.ActiveUsers.login_time
        ).join(self.AllUsers)
        return query.all()

    def active_users_names_list(self):
        query = self.session.query(
            self.AllUsers.name,
            self.ActiveUsers.ip_address
        ).join(self.AllUsers)
        return query.all()

    def login_history(self, username=None):
        query = self.session.query(self.AllUsers.name,
                                   self.LoginHistory.date_time,
                                   self.LoginHistory.ip,
                                   self.LoginHistory.port
                                   ).join(self.AllUsers)
        if username:
            query = query.filter(self.AllUsers.name == username)
        return query.all()

    def add_contact(self, user, contact):
        user_id = self.session.query(
            self.AllUsers).filter_by(
            name=user).first()
        contact_id = self.session.query(
            self.AllUsers).filter_by(
            name=contact).first()
        if not contact_id:
            return f'client {contact} not found'
        new_contact = self.ContactList(
            user_id.id, contact_id.id, datetime.datetime.now())
        self.session.add(new_contact)
        self.session.commit()

    # def get_contactList(self, user):
    #     query = self.session.query(
    #         self.ContactList.user,
    #         self.ContactList.contact
    #     ).join(self.AllUsers, id == ContactList.user)
    #     return query.all()

    def get_contactList(self, user):
        res = []
        a1 = aliased(self.AllUsers)
        a2 = aliased(self.AllUsers)
        query = self.session.query(
            a1.name,
            a2.name,
            self.ContactList.user,
            self.ContactList.contact,
        ).join(a1, self.ContactList.user == a1.id).\
            join(a2, self.ContactList.contact == a2.id).\
            filter(a1.name == user)
        for el in query.all():
            res.append(el[1])
        return res


if __name__ == '__main__':
    test_db = ServerDatabase()

    test_db.user_login('client_1', '192.168.1.4', 8888)
    test_db.user_login('client_2', '192.168.1.5', 7777)
    test_db.user_login('client_3', '192.168.1.5', 7773)
    test_db.user_login('client_4', '192.168.1.5', 7774)
    test_db.user_login('client_5', '192.168.1.5', 7775)

    # print(test_db.active_users_list())

    # test_db.user_logout('client_1')
    # test_db.user_logout('client_3')

    # print(test_db.active_users_list())

    # test_db.add_contact('client_1', 'client_2')
    # test_db.add_contact('client_1', 'client_3')
    # test_db.add_contact('client_1', 'client_4')
    # test_db.add_contact('client_1', 'client_5')
    #
    #
    # test_db.add_contact('client_5', 'client_2')
    # test_db.add_contact('client_5', 'client_4')

    print(test_db.get_contactList('client_1'))
    print(test_db.get_contactList('client_5'))
