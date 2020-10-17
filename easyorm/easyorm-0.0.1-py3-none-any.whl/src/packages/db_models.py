from src.config import SERVER_CONFIG, MODELS_SOURCE_PATH
from .list_db_type import LIST_TYPE
from src.packages import DB_Sqlit, DB_MySql, DB_Mongo

__SERVER__ = None

class Model:
    
    def __init__(self, filedata):
        self.__data__ = filedata
        self.__tablename__ = f"{self.__data__['name']}".lower()
        self.__create__()
   

    def __create__(self):
        global __SERVER__
        if self.__data__ != None :
            self.__data_source = self.__data__['option']['dataSource']
            self.__module_property__ = self.__data__['properties']
            dbname = self.__data__['option']['dbname']
            
            if  self.__data_source == 'db_sqlite_source':
                __SERVER__ = DB_Sqlit(dbname)
                
            if  self.__data_source == 'db_mysql_source':
                __SERVER__ = DB_MySql(**SERVER_CONFIG) 
            
            if  self.__data_source == 'db_mongo_source':
                __SERVER__ = DB_Mongo(**SERVER_CONFIG)  
            
            self.__connect__()     
    
    
    def __connect__(self): 
        try: 
            if  self.__data_source == 'db_mongo_source':
                self.__db_collect =  __SERVER__.create_collection(self.__data__['name'])
            else:
                query = self.__create_query_table__()
                __SERVER__.execute(query, 'POST')
        except Exception as error:
            pass
            # print('Error __connect__', error)


    def execute(self, query, method):
        global __SERVER__
        if  self.__data_source == 'db_mongo_source':
           return __SERVER__.execute(query, method)
        else :
            return __SERVER__.execute(query, method)
    
    
    def __create_query_table__(self):
        property_length = len(self.__module_property__)
        query = f"""CREATE TABLE {self.__tablename__} (\n"""

        if self.__data_source == 'db_mysql_source':
            query += "id int PRIMARY KEY Auto_increment,\n"
        
        if self.__data_source == 'db_sqlite_source':
            query += "id INTEGER PRIMARY KEY AUTOINCREMENT,\n" 
            
        cpt = 0
        for item in self.__module_property__:
            cpt+=1
            propertyItem = self.__module_property__[item]
            default_value = lambda x : 'NOT NULL' if self.get_boolean_value(x) else ''
            index_value = lambda x : 'UNIQUE' if self.get_boolean_value(x) else ''
            list_value = LIST_TYPE[self.__data_source]
            if cpt == property_length:
                query += f"{item} {list_value[propertyItem['type']]}({propertyItem['length']}) {default_value(propertyItem['required'])} {index_value(propertyItem['index'])}"
            else :
                query += f"{item} {list_value[propertyItem['type']]}({propertyItem['length']}) {default_value(propertyItem['required'])} {index_value(propertyItem['index'])},\n"
        
        query+="""\n)"""  
        return query
    

    @classmethod
    def get_classname(cls):
        classname = f'{cls.__class__}'.replace("<class '__main__.", "")
        classname = classname.replace("'>", "").lower()
        return classname


    def get_boolean_value(self, value):
        list_bool = {
            "true" : True,
            "True" : True,
            "False" : False,
            "false" : False
        }

        if value in list_bool.keys():
            return list_bool[value]
        return False


    def get_python_type(self, value):
        list_type = {
            "string" : str,
            "integer" : int,
            "boolean" : bool,
            "float": float
        }
        
        if value in list_type.keys():
            return list_type[value]
        return False


    def gets(self, method='GET',**ctrl):
        """
        Cette methode permet de recuperer toute les occurences
        d une table et elle retourne un dictionnaire

        Exemple :
        voiture = Voiture()
        result = voiture.gets()
        print(result)
        """
        query = f"SELECT * FROM {self.__tablename__}"
        return self.execute(query, method)


    def remove_id(self, _id_):
        """
        Cette methode permet de suprimer une occurence
        d une table et elle retourne la valeur de occurence
        ou False quand elle n'a pas marché

        Exemple :
        voiture = Voiture()
        result = voiture.remove(2)
        print(result)
        """
        result = self.search(key='id', value=_id_)

        if len(result) > 0 :
            query = f"DELETE FROM {self.__tablename__} WHERE id={_id_}"
            print(query)
            self.execute(query, 'POST')
            return result
        else :
            return False

    
    def search_id(self, key, value, **parms):
        """
        Cette methode permet de rechercher une occurence
        specifique  dans la table et elle retourne un dictionnaire

        Exemple :
        voiture = Voiture()
        result = voiture.search(key="marque", value="BMW", limit=(1,10), order="crs")
        print(result)
        """
        if type(value) != str:
            query = f"SELECT * FROM {self.__tablename__} WHERE {key}={value}"
        else :
            query = f'SELECT * FROM {self.__tablename__} WHERE {key}="{value}"'
        return self.execute(query, "GET")
    

    def add(self, method='POST', **args):

        import json

        query = f"INSERT INTO {self.__tablename__} VALUES(NULL, "
        
        try:
            with open(f'{MODELS_SOURCE_PATH}/{self.__tablename__}.json') as src:
                data = src.read()
                jsonData = json.loads(data)
                allsproperties = jsonData['properties']
            
            for key in args.keys():
                if args[key] == None:
                    raise ValueError('Les champs n ont pas bien ete renseigné ')
        
        
            for key in args.keys():
                if key in allsproperties.keys() :
                    attrib = allsproperties[key]
                    typeof = self.get_python_type(attrib['type'])
                    if not (typeof and typeof == type(args[key])):
                        raise ValueError(f"Type non conforme variable {key}\n saisie : {type(args[key])} =>attendu : {attrib['type']}")
                else :
                    raise ValueError(f"Type de variable introuvable")
            
        except Exception as error:
            print("Error ", error)
        else:

            format_values = ""
            cpt = 0
            for key in args.keys():
                cpt+=1
                if cpt>= len(args):
                    format_values += f'"{args[key]}"'
                else :
                    format_values += f'"{args[key]}",'
            
            query+=f"{format_values})"
            print(query)
            self.execute(query, method)
           
    def generate(self, classname):
        global __SERVER__
        list_getted = {
            'execute' : self.execute,
            'remove' : self.remove_id,
            'find' : self.gets,
            'add' : self.add,
            'findOne' : self.search_id,
            '__python_type__' : self.get_python_type,
            '__tablename__' : classname,
            'db_connect' : __SERVER__,
            }
        return list_getted