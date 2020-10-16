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
import sys
from getopt import getopt

from mongo_operator.backup_operator import BackupOperator
from mongo_operator.cleanup_operator import CleanupOperator


class CliOperator:
    """
    How To Use:
        mongo-operator -b [backup database name]
        mongo-operator -d [dropped database name]
        mongo-operator -r [restored data folder]
    """

    @staticmethod
    def _backup(db_name):
        backup_operator = BackupOperator()
        backup_operator.backup(db_name=db_name)

    @staticmethod
    def _restore(folder_path):
        backup_operator = BackupOperator()
        backup_operator.restore(folder_path=folder_path)

    @staticmethod
    def _cleanup(db_name):
        cleanup_operator = CleanupOperator()
        cleanup_operator.drop_db(db_name=db_name)

    @classmethod
    def main(cls):
        opts, args = getopt(sys.argv[1:], 'hb:d:r:', ['help=', 'backup=', 'drop=', 'restore'])
        opts_dict = dict(opts)
        if len(opts_dict) > 2 or '-h' in opts_dict:
            sys.exit(cls.__doc__)
        if '-b' in opts_dict:
            cls._backup(db_name=opts_dict['-b'])
        if '-r' in opts_dict:
            cls._restore(folder_path=opts_dict['-r'])
        if '-d' in opts_dict:
            cls._cleanup(db_name=opts_dict['-d'])


if __name__ == '__main__':
    CliOperator.main()
