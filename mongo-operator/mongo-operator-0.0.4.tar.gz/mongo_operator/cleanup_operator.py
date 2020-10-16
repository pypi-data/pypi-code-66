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


class CleanupOperator:
    def __init__(self, hostname='localhost', port=27017, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def drop_db(self, db_name):
        """
        drop specific database
        example:
            cleanup_operator = CleanupOperator()
            cleanup_operator.drop_db(db_name='foo_bar')
        :param db_name:
        :return:
        """
        drop_dict = {
            '--host': self.hostname,
            '--port': self.port,
            '-u': self.username,
            '-p': self.password,
            '--authenticationDatabase': 'admin',
            '--eval': '"db.dropDatabase()"'
        }
        arg_string = ' '.join([f'{arg} {value}' for arg, value in drop_dict.items()])
        drop_command = f'mongo {db_name} {arg_string}'
        os.system(drop_command)

        print('DROP DATABASE FINISHED')

    def drop_collection(self, db_name, collection):
        """
        drop specific collection
        example:
            cleanup_operator = CleanupOperator()
            cleanup_operator.drop_collection(db_name='foo_bar', collection='foo_bar')
        :param db_name:
        :param collection:
        :return:
        """
        drop_dict = {
            '--host': self.hostname,
            '--port': self.port,
            '-u': self.username,
            '-p': self.password,
            '--authenticationDatabase': 'admin',
            '--eval': f'"db.{collection}.drop()"'
        }
        arg_string = ' '.join([f'{arg} {value}' for arg, value in drop_dict.items()])
        drop_command = f'mongo {db_name} {arg_string}'
        os.system(drop_command)

        print('DROP COLLECTION FINISHED')


if __name__ == '__main__':
    # init object
    cleanup_operator = CleanupOperator()

    # drop 'foo_bar' table in foo_bar
    cleanup_operator.drop_collection(db_name='foo_bar', collection='foo_bar')

    # drop foo_bar database
    cleanup_operator.drop_db(db_name='foo_bar')
