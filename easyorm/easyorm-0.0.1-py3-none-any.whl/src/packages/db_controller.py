import json
from . import Model
from src.config import MODELS_SOURCE_PATH

class MetaModel(type):

    def __new__(metacls, classname, herited, contants):
        clsname = classname.lower()
        propertys = {}
        
        if 'model' in clsname :
            return type.__new__(metacls, clsname, herited, contants)
        else :
            with open(f'{MODELS_SOURCE_PATH}/{clsname}.json', 'r') as src:
                data = src.read()
                propertys = json.loads(data)
                model = Model(propertys)
                methods = model.generate(clsname)
                for meth in methods.keys():
                    propertys['properties'][meth]=methods[meth]

            # try:
            
            # except Exception as error:
            #     print(f'<:: debug ::> file {clsname} not exist <!>')
            # else :
                if clsname != f"{propertys['name']}".lower():
                    raise ValueError('Nom de la classe est non comforme a celle de la table')
                return type.__new__(metacls, clsname, herited, propertys['properties'])

    def __init__(cls, classname, herited, contants):
        type.__init__(cls, classname, herited, contants)

    def toggler(cls):
        pass