# -*- coding: utf-8 -*
"""
      ┏┓       ┏┓
    ┏━┛┻━━━━━━━┛┻━┓
    ┃      ☃      ┃
    ┃  ┳┛     ┗┳  ┃
    ┃      ┻      ┃
    ┗━┓         ┏━┛
      ┗┳        ┗━┓
       ┃          ┣┓
       ┃          ┏┛
       ┗┓┓┏━━━━┳┓┏┛
        ┃┫┫    ┃┫┫
        ┗┻┛    ┗┻┛
    God Bless,Never Bug
"""
import os
from mongo_operator import BackupOperator


class MigrateOperator:
    def __init__(self, target_hostname, target_port=27017, target_username='root', target_password='root',
                 hostname='localhost', port=27017, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.target_hostname = target_hostname
        self.target_port = target_port
        self.target_username = target_username
        self.target_password = target_password

    def export_database(self, db_name=None):
        """
        export database to target host
        example:
            migrate_operator = MigrateOperator(hostname='localhost',
                                   port=27017,
                                   username='root',
                                   password='root',
                                   target_hostname='192.168.1.1',
                                   target_port=27017,
                                   target_username='root',
                                   target_password='root')
            migrate_operator.export_database()
            migrate_operator.export_database(db_name='foo_bar')

        :param db_name:
        :return:
        """
        backup_operator = BackupOperator(hostname=self.hostname,
                                         port=self.port,
                                         username=self.username,
                                         password=self.password)
        backup_operator.backup(db_name=db_name, folder_path='./tmp')

        backup_operator = BackupOperator(hostname=self.target_hostname,
                                         port=self.target_port,
                                         username=self.target_username,
                                         password=self.target_password)
        if db_name:
            backup_operator.restore(db_name=db_name, folder_path=f'./tmp/{db_name}')
        else:
            backup_operator.restore(db_name=db_name, folder_path='./tmp')

        os.system('rm -rf ./tmp')
        print('EXPORT DATABASE FINISHED')

    def import_database(self, db_name=None):
        """
        import database from target host
        example:
            migrate_operator = MigrateOperator(hostname='localhost',
                                   port=27017,
                                   username='root',
                                   password='root',
                                   target_hostname='192.168.1.1',
                                   target_port=27017,
                                   target_username='root',
                                   target_password='root')
            migrate_operator.import_database()
            migrate_operator.import_database(db_name='foo_bar')

        :param db_name:
        :return:
        """
        backup_operator = BackupOperator(hostname=self.target_hostname,
                                         port=self.target_port,
                                         username=self.target_username,
                                         password=self.target_password)
        backup_operator.backup(db_name=db_name, folder_path='./tmp')

        backup_operator = BackupOperator(hostname=self.hostname,
                                         port=self.port,
                                         username=self.username,
                                         password=self.password)

        if db_name:
            backup_operator.restore(db_name=db_name, folder_path=f'./tmp/{db_name}')
        else:
            backup_operator.restore(db_name=db_name, folder_path='./tmp')
        os.system('rm -rf ./tmp')
        print('IMPORT DATABASE FINISHED')


if __name__ == '__main__':
    # init object
    migrate_operator = MigrateOperator(hostname='localhost',
                                       port=27017,
                                       username='root',
                                       password='root',
                                       target_hostname='192.168.1.1',
                                       target_port=27017,
                                       target_username='root',
                                       target_password='root')

    # import all database from target host
    migrate_operator.import_database()

    # import『foo_bar』database from target host
    migrate_operator.import_database(db_name='foo_bar')

    # export all database from to host
    migrate_operator.export_database()

    # export『foo_bar』database to target host
    migrate_operator.export_database(db_name='foo_bar')
