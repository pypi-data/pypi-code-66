import sqlite3
from src.config import LOCAL_SQLITE_DB as local_db_file

class DB_Sqlit :
    
    def __init__(self, dbname):
        self.__db = sqlite3.connect(f'{local_db_file}/{dbname}.db')

    def execute(self, query, method):
        cursor = self.__db.cursor()
        
        if method == 'GET':  
            resp = cursor.execute(query)
            return resp.fetchall()
    
        if method == 'POST':
            cursor.execute(query)
            cursor.close()
            self.__db.commit()