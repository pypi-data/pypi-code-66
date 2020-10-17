import mysql.connector as msql

class DB_MySql :
    
    def __init__(self, **args):
        try:
            self.__db = msql.connect(**args)
        except msql.errors.ProgrammingError as error:
            query = f"""CREATE DATABASE {args['database']} """
            try:
                source_db = msql.connect(host=args['host'], user=args['user'], password=args['password'])
                cursor = source_db.cursor()
                cursor.execute(query)
                cursor.close()
            except Exception as error:
                print(f'Erreur serveur de base de données \n{error}')
            else:
                self.__db = msql.connect(**args)
        else:
            pass
        
    def  execute(self, query, method):
        cursor = self.__db.cursor()
        cursor.execute(query)
        
        if method == 'GET':
            data = []
            for els in cursor:
                data.append(els)
            cursor.close()
            return data
        
        if method == 'POST':
            self.__db.commit()
            cursor.close()