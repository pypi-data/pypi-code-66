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
    def __init__(self, hostname='localhost', port=3306, username='root', password='root'):
        self.hostname = hostname
        self.port = port
        self.username = username
        self.password = password

    def _fk_switch(self, switch=0):
        """
        foreign_key_checks switcher
        :param switch:
        :return:
        """
        command = f'mysql ' \
                  f'-h {self.hostname} ' \
                  f'-P {self.port} ' \
                  f'-u {self.username} ' \
                  f'-p{self.password} ' \
                  f'-e "SET FOREIGN_KEY_CHECKS = {switch}";'
        os.system(command)

    def drop(self, db_name, tables=None, keep_db=True):
        """
        drop tables with specific database, set keep_db as False to drop tables with database
        example:
            cleanup_operator = CleanupOperator(hostname='localhost', port=3306, username='root', password='root')

            cleanup_operator.drop(db_name='foo_bar_db')
            cleanup_operator.drop(db_name='hello_world_db', keep_db=False)
            cleanup_operator.drop(db_name='foo_bar_db', tables=['foo_user', 'bar_weather'])

        :param db_name:
        :param tables:
        :param keep_db:
        :return:
        """
        self._fk_switch(switch=0)
        if tables:
            tables_string = "','".join(tables)
            drop_command = f'mysql -NB ' \
                           f'-h {self.hostname} ' \
                           f'-P {self.port} ' \
                           f'-u {self.username} ' \
                           f'-p{self.password} ' \
                           f'-e ' \
                           f'"SELECT table_name FROM information_schema.tables WHERE table_schema = \'{db_name}\' ' \
                           f'AND table_name in (\'{tables_string}\');" | ' \
                           f'xargs -I {{}} ' \
                           f'mysql ' \
                           f'-h {self.hostname} ' \
                           f'-P {self.port} ' \
                           f'-u {self.username} ' \
                           f'-p{self.password} {db_name} ' \
                           f'-e ' \
                           f'"DROP TABLE {{}}";'
        else:
            if keep_db:
                drop_command = f'mysql -NB ' \
                               f'-h {self.hostname} ' \
                               f'-P {self.port} ' \
                               f'-u {self.username} ' \
                               f'-p{self.password} ' \
                               f'-e ' \
                               f'"SELECT table_name FROM information_schema.tables WHERE table_schema = \'{db_name}\';" | ' \
                               f'xargs -I {{}} ' \
                               f'mysql ' \
                               f'-h {self.hostname} ' \
                               f'-P {self.port} ' \
                               f'-u {self.username} ' \
                               f'-p{self.password} {db_name} ' \
                               f'-e ' \
                               f'"DROP TABLE {{}}";'
            else:
                drop_command = f'mysql ' \
                               f'-h {self.hostname} ' \
                               f'-P {self.port} ' \
                               f'-u {self.username} ' \
                               f'-p{self.password} ' \
                               f'-e ' \
                               f'"DROP DATABASE {db_name}"'
        os.system(drop_command)
        self._fk_switch(switch=1)
        print("CLEANUP FINISHED")

    def pattern_drop(self, db_name, pattern):
        """
        drop tables by pattern with specific database
        example:
            cleanup_operator = CleanupOperator(hostname='localhost', port=3306, username='root', password='root')
            cleanup_operator.pattern_drop(db_name='foo_bar_db', pattern='%foo%')

        :param db_name:
        :param pattern:
        :return:
        """
        self._fk_switch(switch=0)
        drop_command = f'mysql -NB ' \
                       f'-h {self.hostname} ' \
                       f'-P {self.port} ' \
                       f'-u {self.username} ' \
                       f'-p{self.password} ' \
                       f'-e ' \
                       f'"SELECT table_name FROM information_schema.tables WHERE table_schema = \'{db_name}\' ' \
                       f'AND table_name like \'{pattern}\';" | ' \
                       f'xargs -I {{}} ' \
                       f'mysql ' \
                       f'-h {self.hostname} ' \
                       f'-P {self.port} ' \
                       f'-u {self.username} ' \
                       f'-p{self.password} {db_name} ' \
                       f'-e ' \
                       f'"DROP TABLE {{}}";'
        os.system(drop_command)
        self._fk_switch(switch=1)
        print("CLEANUP FINISHED")


if __name__ == '__main__':
    # init object
    cleanup_operator = CleanupOperator(hostname='localhost', port=3306, username='root', password='root')

    # drop all tables in『foo_bar_db』
    cleanup_operator.drop(db_name='foo_bar_db')

    # drop database『hello_world_db』
    cleanup_operator.drop(db_name='hello_world_db', keep_db=False)

    # drop tables ['foo_user', 'bar_weather'] in『foo_bar_db』
    cleanup_operator.drop(db_name='foo_bar_db', tables=['foo_user', 'bar_weather'])

    # drop tables in『foo_bar_db』 which table name like '%foo%'
    cleanup_operator.pattern_drop(db_name='foo_bar_db', pattern='%foo%')
