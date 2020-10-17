import json
from src.config import MODELS_SOURCE_PATH

class Modul:

    @classmethod
    def run(cls):
        quiz = ''
        json_data = {}
        has_finish = True
        all_data = {}

        with open('src/server/assets/moduls_quiz.json', 'r') as src:
            data = src.read()
            all_data = json.loads(data)

        item_data = {}

        for item in all_data.keys() :
            quiz = all_data[item]
            if type(quiz) == dict:
                if item == 'properties':
                    property_name = 'null'
                    while property_name != '':
                        property_name = input('Nom de la propriete : ')
                        if property_name != '' :
                            values = cls.dict_quiz(quiz)
                            item_data[property_name] = values
                            # print(item_data)
                            # json_data[item][property_name] = values
                else :
                    values = cls.dict_quiz(quiz)
                    json_data[item] = values
            else :
                values = cls.simple_quiz(quiz)
                json_data[item] = values
        
        json_data['properties'] = item_data
        file_name = f"{json_data['name']}".lower()
        # json_formated = json.load(json_data)
        

        #Operation de enregistrement propriétées du module en format json
        with open(f'{MODELS_SOURCE_PATH}/{file_name}.json', 'a') as src:
            data_ftd = str(json_data)
            data_ftd = data_ftd.replace("'","\"")
            src.write(data_ftd)
            # json.dump(data_ftd, src, indent=4)
        

        #Operation d'inclusion du module dans le programme 
        with open(f'src/modules/lunch.py', 'a+') as src:
            class_property = ''
            for item in json_data['properties']:
                class_property+=f'\t\tself.{item} = None\n'

            discrip = '"""\n\t-> get()\n\t-> add()\n\t-> findOne()\n\t-> find()\n\t-> remove()\n\t-> execute()\n\t"""'
            script_of_moduel = f"\n\nclass {file_name.capitalize()}(metaclass=MetaModel):\n"
            script_of_moduel+=f"\t{discrip}\n"
            script_of_moduel+="\tdef __init__(self):\n"
            script_of_moduel+=f"{class_property}"
            src.write(script_of_moduel)
        

        with open(f'{MODELS_SOURCE_PATH}/{file_name}.py', 'a') as src:
            
            doc_model = '\t"""\n'
            for item in json_data['properties']:
                doc_model+=f"\t\# {item} <{json_data['properties'][item]['type']}>\n"
            doc_model += '\t"""\n'

            model_meth = "\tdef save(self):\n"
            model_meth+= "\t\tpass\n"
            model_meth+= "\tdef put(self):\n"
            model_meth+= "\t\tpass\n"
            model_meth+= "\tdef get(self):\n"
            model_meth+= "\t\tpass\n"
            model_meth+= "\tdef delete(self):\n"
            model_meth+= "\t\tpass\n"

            script_of_moduel = f"from src.modules import {file_name.capitalize()}"
            script_of_moduel+= f"\n\nclass {file_name.capitalize()}Model({file_name.capitalize()}):\n"
            script_of_moduel+=f"{doc_model}"
            script_of_moduel+=f"{model_meth}"
            src.write(script_of_moduel)



    @classmethod
    def get_python_type(cls, value):
        list_type = {
            "string" : str,
            "integer" : int,
            "boolean" : bool,
            "float": float
        }
    
    @classmethod
    def dict_quiz(cls, data):
        resp = {}
        val = None
        for els in data.keys() :
            question = data[els]
            val = input(question)
            if val == "True" or val == "False":
                resp[els] = val.lower()
            resp[els] = val       
        return resp
                

    @classmethod
    def simple_quiz(cls, data):
        resp = input(data)
        return resp