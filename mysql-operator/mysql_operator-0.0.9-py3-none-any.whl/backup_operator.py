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
from datetime import datetime


class BackupOperator:
    def __init__(self, hostname='localhost', port=3306, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def _create_db(self, db_name):
        """
        create database
        :param db_name:
        :return:
        """
        create_command = f'mysqladmin ' \
                         f'-h {self.hostname} ' \
                         f'-P {self.port} ' \
                         f'-u {self.username} ' \
                         f'-p{self.password} ' \
                         f'create {db_name}'
        os.system(create_command)

    def backup(self, dbs=None, db_name=None, tables=None,
               filename='backup_{date}.sql'.format(date=datetime.now().date())):
        """
        backup mysql with specific databases and tables
        example:
            backup_operator = BackupOperator(hostname='127.0.0.1', username='root', password='root')
            backup_operator.backup()
            backup_operator.backup(dbs=['foo_bar_db', 'hello_world_db'])
            backup_operator.backup(db_name='foo_bar_db', filename='foo_bar_bak_test.sql')
            backup_operator.backup(db_name='foo_bar_db', tables=['foo_user', 'bar_store'], filename='foo_bar_bak_test.sql')

        :param dbs:
        :param db_name:
        :param tables:
        :param filename:
        :return:
        """
        if tables and not isinstance(tables, list):
            raise TypeError('type of tables must be list')

        if dbs:
            for db in dbs:
                self._create_db(db_name=db)
            # backup multiple databases
            dump_command = f'mysqldump ' \
                           f'-h {self.hostname} ' \
                           f'-P {self.port} ' \
                           f'-u {self.username} ' \
                           f'-p{self.password} ' \
                           f'--databases {" ".join(dbs)} > {filename}'
        else:
            if db_name:
                self._create_db(db_name=db_name)
                # backup specific database with multiple tables
                if tables:
                    dump_command = f'mysqldump ' \
                                   f'-h {self.hostname} ' \
                                   f'-P {self.port} ' \
                                   f'-u {self.username} ' \
                                   f'-p{self.password} ' \
                                   f'{db_name} {" ".join(tables)} > {filename}'
                else:
                    # backup all tables in specific database
                    dump_command = f'mysqldump -h ' \
                                   f'{self.hostname} ' \
                                   f'-P {self.port} ' \
                                   f'-u {self.username} ' \
                                   f'-p{self.password} ' \
                                   f'{db_name} > {filename}'
            else:
                # backup all databases
                dump_command = f'mysqldump ' \
                               f'-h {self.hostname} ' \
                               f'-P {self.port} ' \
                               f'-u {self.username} ' \
                               f'-p{self.password} ' \
                               f'--all-databases > {filename}'

        os.system(dump_command)
        print('BACKUP FINISHED')

    def filter_backup(self, db_name, table_name, filter_,
                      filename='backup_{date}.sql'.format(date=datetime.now().date())):
        """
        backup mysql with specific table with query
        example:
            backup_operator = BackupOperator(hostname='127.0.0.1', username='root', password='root')
            backup_operator.filter_backup(db_name='foo_bar_db',
                                          table_name='bar_store',
                                          filter_="id <= 2 AND branch like '%Jammu%'")

        :param db_name:
        :param table_name:
        :param filter_:
        :param filename:
        :return:
        """
        dump_command = f'mysqldump ' \
                       f'-h {self.hostname} ' \
                       f'-P {self.port} ' \
                       f'-u {self.username} ' \
                       f'-p{self.password} ' \
                       f'-w "{filter_}" ' \
                       f'{db_name} {table_name} > {filename}'

        os.system(dump_command)
        print('BACKUP FINISHED')

    def pattern_backup(self, db_name, pattern, filename='backup_{date}.sql'.format(date=datetime.now().date())):
        """
        backup mysql with specific database and table name with regex
        example:
            backup_operator = BackupOperator(hostname='127.0.0.1', username='root', password='root')
            backup_operator.pattern_backup(db_name='foo_bar_db', pattern='%foo%')

        :param db_name:
        :param pattern:
        :param filename:
        :return:
        """
        select_command = f'mysql -NB ' \
                         f'-h {self.hostname} ' \
                         f'-P {self.port} ' \
                         f'-u {self.username} ' \
                         f'-p{self.password} -e ' \
                         f'"SELECT table_name FROM information_schema.tables ' \
                         f'WHERE table_schema = \'{db_name}\' AND table_name like \'{pattern}\';"' \
                         f'> tables.txt'
        os.system(select_command)
        dump_command = f'mysqldump ' \
                       f'-h {self.hostname} ' \
                       f'-P {self.port} ' \
                       f'-u {self.username} ' \
                       f'-p{self.password} ' \
                       f'{db_name} `cat tables.txt` > {filename}'

        os.system(dump_command)

        os.system('rm tables.txt')
        print('BACKUP FINISHED')

    def restore(self, filename, db_name=None):
        """
        restore mysql backup to database with specific file
            backup_operator = BackupOperator(hostname='127.0.0.1', username='root', password='root')
            backup_operator.restore(filename='my_backup.sql', db_name='foo_bar_db')

        :param filename:
        :param db_name:
        :return:
        """
        if db_name:
            self._create_db(db_name=db_name)
            restore_command = f'mysql ' \
                              f'-h {self.hostname} ' \
                              f'-P {self.port} ' \
                              f'-u {self.username} ' \
                              f'-p{self.password} {db_name} < {filename}'
        else:
            restore_command = f'mysql ' \
                              f'-h {self.hostname} ' \
                              f'-P {self.port} ' \
                              f'-u {self.username} ' \
                              f'-p{self.password} < {filename}'
        os.system(restore_command)
        print('RESTORE FINISHED')


if __name__ == '__main__':
    # init object
    backup_operator = BackupOperator(hostname='localhost', port=3306, username='root', password='root')

    # loading test database
    backup_operator.restore(filename='../init.sql')

    # backup all database
    backup_operator.backup()

    # backup multiple databases
    backup_operator.backup(dbs=['foo_bar_db', 'hello_world_db'])

    # backup database『foo_bar_db』
    backup_operator.backup(db_name='foo_bar_db', filename='foo_bar_bak_test.sql')

    # backup database『foo_bar_db』with tables ['foo_user', 'bar_store']
    backup_operator.backup(db_name='foo_bar_db', tables=['foo_user', 'bar_store'], filename='foo_bar_bak_test.sql')

    # backup database『foo_bar_db』with table which table name like '%foo%'
    backup_operator.pattern_backup(db_name='foo_bar_db', pattern='%foo%', filename='foo_bar_bak_test.sql')

    # backup database『foo_bar_db』with table 'bar_store' where id <= 2 AND branch '%Jammu%'
    backup_operator.filter_backup(db_name='foo_bar_db',
                                  table_name='bar_store',
                                  filter_="id <= 2 AND branch like '%Jammu%'",
                                  filename='foo_bar_bak_test.sql')

    # restore backup
    backup_operator.restore(db_name='foo_bar_db', filename='foo_bar_bak_test.sql')
