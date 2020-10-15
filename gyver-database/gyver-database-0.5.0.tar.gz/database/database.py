import sqlite3


class DB:
    def __init__(self, dbname: str, debug=False):
        """Создать или открыть объект БД

        Args:\n
            dbname (str): Имя БД, с расширением,как полный так и относительный путь.
            debug (bool, optional): Вывод сгенерированого SQL в консоль для дебага. Defaults to False.
        """
        self.db = sqlite3.connect(dbname)
        self.sql = self.db.cursor()
        self.debug = debug
        if self.debug:
            print('init good')

    def create_table(self, table: str, structure):
        """Создать новую таблицу, если такая уже есть то просто ничего не произойдёт

        Args:\n
            table (str): Имя новой таблицы
            structure (dict): словарь {'название поля':'его тип'}
        """
        self.table = table
        self.columns = structure
        query = f'CREATE TABLE IF NOT EXISTS {self.table}'
        print(query)
        query += ' ('
        length = len(structure)
        loop = 0
        for i in structure:
            loop += 1
            if loop == length:
                query += i.__str__() + ' '
            else:
                query += i.__str__() + ','
        query += ')'

        self.sql.execute(query)
        if self.debug:
            print(query)
        self.db.commit()

    def get_tables(self):
        query = 'SELECT name FROM sqlite_master WHERE type = "table"'
        self.sql.execute(query)
        if self.debug:
            print(query)
        return self.sql.fetchall()

    def del_table(self, table=''):
        if table == '':
            table = self.table
        query = 'DROP TABLE IF EXISTS {}'.format(table)
        self.sql.execute(query)
        if self.debug == True:
            print(query)
        self.db.commit()

    def set_default_table(self, table: str):
        self.table = table
        if self.debug == True:
            print('setted default: ' + table)

    def have_write(self, column: str, value, table=None):
        if table == None:
            table = self.table
        query = 'SELECT ' + column + ' FROM ' + table + ' WHERE ' + column + ' = "{}"'.format(value)
        self.sql.execute(query)
        if self.sql.fetchone() is None:
            if self.debug:
                print(query)
                print(False)
            return False
        else:
            if self.debug:
                print(query)
                print(True)
            return True

    def write(self, *data, table=None):
        """
        Запись в таблицу

        Args:

            data(args): данные для записи через запятую
            table(str): имя таблицы

        """
        if table is None:
            table = self.table

        query = 'INSERT INTO ' + table

        query += ' VALUES ('
        length2 = len(data)
        loop = 0
        for obj in data:
            loop += 1
            if loop == length2:
                query += "'" + str(obj) + "')"
            else:
                query += "'" + str(obj) + "', "

        if self.debug:
            print(query)
        self.sql.execute(query)
        self.db.commit()

    def edit(self, value, id_value, column, id_column=None, table=None):
        if table is None:
            table = self.table
        if id_column is None:
            id_column = column
        query = 'UPDATE {0} SET {1} = "{2}" WHERE {3} = "{4}"'.format(table, column, value, id_column, id_value)
        self.sql.execute(query)
        if self.debug:
            print(query)
        self.db.commit()

    def delete(self, id_value, id_column, table=None):
        if table is None:
            table = self.table
        query = 'DELETE FROM {0} WHERE {1} = "{2}"'.format(table, id_column, id_value)
        self.sql.execute(query)
        if self.debug:
            print(query)
        self.db.commit()

    def get_all(self, value='*', table=None):
        if table is None:
            table = self.table
        query = f'SELECT {value} FROM ' + table
        self.sql.execute(query)
        if self.debug:
            print(query)
        return self.sql.fetchall()

    def get_line(self, id_value, id_column, getval=None, returnone=True, table=None):
        if table is None:
            table = self.table
        if getval is None:
            getval = '*'
        query = 'SELECT {0} FROM {1} WHERE {2} = "{3}"'.format(getval, table, id_column, id_value)

        self.sql.execute(query)
        if self.debug:
            print(query)
        if returnone:
            return self.sql.fetchone()
        else:
            return self.sql.fetchall()

    def get_columns(self, table=None):
        if table is None:
            table = self.table
        query = 'PRAGMA table_info({})'.format(table)
        self.sql.execute(query)
        names = [i[1] for i in self.sql.fetchall()]
        # names = self.sql.fetchall()
        if self.debug:
            print(query)
        return names
        # if table == None:
        #     table = self.table
        # query = 'SELECT * FROM ' + table
        # self.sql.execute(query)
        # names = [member[0] for member in self.sql.description]
        # if self.debug == True:
        #     print(query)
        # return names

    def get_columns_type(self, table=None):
        if table is None:
            table = self.table
        query = 'PRAGMA table_info({})'.format(table)
        self.sql.execute(query)
        names = [i[2] for i in self.sql.fetchall()]
        # names = self.sql.fetchall()
        if self.debug:
            print(query)
        return names
