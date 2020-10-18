import os

if os.name == 'nt':
    # If Windows
    #LOCAL_DATABASE_PATH = "D:/local_database/"
    LOCAL_DATABASE_PATH = "E:/databases/ver_1/local_database/"

else:
    # If Linux
    #LOCAL_DATABASE_PATH = "/home/discoverious/Documents/local_database/"
    LOCAL_DATABASE_PATH = "/media/discoverious/Backup Plus/databases/ver_1/local_database/"

SHOP_DATABASE_PATH = LOCAL_DATABASE_PATH + "shop_database/"
ITEM_DATABASE_PATH = LOCAL_DATABASE_PATH + "item_database/"
ERROR_LOG_DATABASE_PATH = LOCAL_DATABASE_PATH + "error_log_database/"
UTILITY_DATABASE_PATH = LOCAL_DATABASE_PATH + "utility_database/"
MODEL_DATABASE_PATH = LOCAL_DATABASE_PATH + "model_database/"
PROCESSED_DATA_DATABASE_PATH = LOCAL_DATABASE_PATH + "processed_data_database/"



