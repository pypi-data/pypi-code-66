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

import json
import os


class BackupOperator:
    def __init__(self, hostname='localhost', port=27017, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def backup(self, db_name=None, collection=None, query_=None, folder_path=None):
        """
        backup mongo with specific database and collection
        example:
            backup_operator = BackupOperator()
            backup_operator.backup(db_name='foo_bar_db', collection='hello_world')
        :param db_name:
        :param collection:
        :param query_:
        :param folder_path:
        :return:
        """
        backup_dict = {
            '--host': self.hostname,
            '--port': self.port,
            '-u': self.username,
            '-p': self.password,
            '--authenticationDatabase': 'admin',
            '--forceTableScan': ''
        }
        if db_name:
            backup_dict.update({'-d': db_name})
        if collection:
            backup_dict.update({'-c': collection})
        if query_ and isinstance(query_, dict):
            query_string = json.dumps(query_).replace('"', '\\"')
            query_string = f'"{query_string}"'
            backup_dict.update({'-q': query_string})

        arg_string = ' '.join([f'{arg} {value}' for arg, value in backup_dict.items()])
        if folder_path:
            backup_command = f'mongodump -o {folder_path} {arg_string}'
        else:
            backup_command = f'mongodump {arg_string}'
        os.system(backup_command)
        print('BACKUP FINISHED')

    def restore(self, db_name=None, collection=None, folder_path=None, is_dropped=False):
        """
        restore mongo from specific folder
        example:
            backup_operator = BackupOperator()
            backup_operator.restore()
        :param db_name:
        :param collection:
        :param folder_path:
        :param is_dropped:
        :return:
        """
        restore_dict = {
            '--host': self.hostname,
            '--port': self.port,
            '-u': self.username,
            '-p': self.password,
            '--authenticationDatabase': 'admin'
        }
        if db_name:
            restore_dict.update({'-d': db_name})
        if collection:
            restore_dict.update({'-c': collection})
        if is_dropped:
            restore_dict.update({'--drop': ''})

        arg_string = ' '.join([f'{arg} {value}' for arg, value in restore_dict.items()])
        if folder_path:
            restore_command = f'mongorestore {folder_path} {arg_string}'
        else:
            restore_command = f'mongorestore {arg_string}'
        os.system(restore_command)
        print('RESTORE FINISHED')


if __name__ == '__main__':
    # init object
    backup_operator = BackupOperator()

    # loading test database
    backup_operator.restore(folder_path='../mongo_init/', is_dropped=True)

    # backup database
    backup_operator.backup(folder_path='../mongo_init/')

    # backup specific collection
    backup_operator.backup(db_name='foo_bar', collection='foo_bar')

    # backup specific collection with query
    backup_operator.backup(db_name='foo_bar', collection='foo_bar', query_={'items': 'phone'})
