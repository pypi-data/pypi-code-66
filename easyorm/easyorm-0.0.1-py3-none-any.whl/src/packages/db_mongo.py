from pymongo import MongoClient

class DB_Mongo:
    
    def __init__(self, **args):
        db = MongoClient(host=args['host'], port=27017)
        self.__db = db[args['dbname']]
            
    
    def create_collection(self, collection):
        self.__db[collection]
       
    def  execute(self, collection, values, method):
        db_collect = self.__db[collection]
        if method == 'GET':
            data = db_collect.find()
            return data
        
        if method == 'POST':
            db_collect.insert_one(values)