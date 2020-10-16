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
from mysql_operator import BackupOperator


class MigrateOperator:
    def __init__(self, target_hostname, target_port=3306, target_username='root', target_password='root',
                 hostname='localhost', port=3306, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password
        self.target_hostname = target_hostname
        self.target_port = target_port
        self.target_username = target_username
        self.target_password = target_password

    def _create_db(self, db_name, is_local=True):
        """
        create database
        :param db_name:
        :param is_local:
        :return:
        """
        if is_local:
            create_command = f'mysqladmin ' \
                             f'-h {self.hostname} ' \
                             f'-P {self.port} ' \
                             f'-u {self.username} ' \
                             f'-p{self.password} ' \
                             f'create {db_name}'
        else:
            create_command = f'mysqladmin ' \
                             f'-h {self.target_hostname} ' \
                             f'-P {self.target_port} ' \
                             f'-u {self.target_username} ' \
                             f'-p{self.target_password} ' \
                             f'create {db_name}'
        os.system(create_command)

    def export_database(self, db_name=None):
        """
        export database from local to remote server
        example:
            migrate_operator = MigrateOperator(hostname='localhost',
                                   port=3306,
                                   username='root',
                                   password='root',
                                   target_hostname='192.168.1.1',
                                   target_port=3306,
                                   target_username='root',
                                   target_password='root')
            migrate_operator.export_database()
            migrate_operator.export_database(db_name='foo_bar_db')

        :param db_name:
        :return:
        """
        if db_name:
            self._create_db(db_name=db_name, is_local=False)
            export_command = f'mysqldump ' \
                             f'-h {self.hostname} ' \
                             f'-P {self.port} ' \
                             f'-u {self.username} ' \
                             f'-p{self.password} {db_name} ' \
                             f'| mysql ' \
                             f'-h {self.target_hostname} ' \
                             f'-P {self.target_port} ' \
                             f'-u {self.target_username} ' \
                             f'-p{self.target_password} {db_name}'
        else:
            export_command = f'mysqldump ' \
                             f'-h {self.hostname} ' \
                             f'-P {self.port} ' \
                             f'-u {self.username} ' \
                             f'-p{self.password} ' \
                             f'--all-databases | mysql ' \
                             f'-h {self.target_hostname} ' \
                             f'-P {self.target_port} ' \
                             f'-u {self.target_username} ' \
                             f'-p{self.target_password}'
        os.system(export_command)
        print('EXPORT DATABASE FINISHED')

    def import_database(self, db_name=None):
        """
        import database from remote server to local
        example:
            migrate_operator = MigrateOperator(hostname='localhost',
                                   port=3306,
                                   username='root',
                                   password='root',
                                   target_hostname='192.168.1.1',
                                   target_port=3306,
                                   target_username='root',
                                   target_password='root')
            migrate_operator.import_database()
            migrate_operator.import_database(db_name='foo_bar_db')

        :param db_name:
        :return:
        """
        if db_name:
            self._create_db(db_name=db_name, is_local=True)
        backup_operator = BackupOperator(hostname=self.target_hostname,
                                         port=self.target_port,
                                         username=self.target_username,
                                         password=self.target_password)
        backup_operator.backup(db_name=db_name, filename='./tmp.sql')
        backup_operator = BackupOperator(hostname=self.hostname,
                                         port=self.port,
                                         username=self.username,
                                         password=self.password)
        backup_operator.restore(db_name=db_name, filename='./tmp.sql')
        os.system('rm ./tmp.sql')
        print('IMPORT DATABASE FINISHED')


if __name__ == '__main__':
    # init object
    migrate_operator = MigrateOperator(hostname='localhost',
                                       port=3306,
                                       username='root',
                                       password='root',
                                       target_hostname='192.168.1.1',
                                       target_port=3306,
                                       target_username='root',
                                       target_password='root')

    # import all database from target host
    migrate_operator.import_database()

    # import database『foo_bar_db』from target host
    migrate_operator.import_database(db_name='foo_bar_db')

    # export all database from to host
    migrate_operator.export_database()

    # export database『foo_bar_db』to target host
    migrate_operator.export_database(db_name='foo_bar_db')
