# Server connect property
PARAM = {}
import json

with open('src/server/data_source.json') as src:
    data = src.read()
    PARAM = json.loads(data)


SERVER_CONFIG = {
    'database': PARAM['dbname'], 
    'host': PARAM['host'], 
    'user': PARAM['user'], 
    'password': PARAM['password']
}

LOCAL_SQLITE_DB = "bin/"

MODELS_SOURCE_PATH = "clients"