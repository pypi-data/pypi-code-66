from adnar_scraper.utility.data_loader import DataLoader
from adnar_scraper import settings
import os
import json


class DatabaseController:
    def __init__(self, selected_database):
        if selected_database is 'item':
            self.base_path = settings.ITEM_DATABASE_PATH

        elif selected_database is 'shop':
            self.base_path = settings.SHOP_DATABASE_PATH

        elif selected_database is 'processed_data':
            self.base_path = settings.PROCESSED_DATA_DATABASE_PATH

        print('-')
        print(self.base_path)

    @staticmethod
    def view_data_set(data_set):
        for data in data_set:
            print(data)

    @staticmethod
    def get_merged_data_set(data_set_list):
        merged_data_set = []

        for data_set in data_set_list:
            merged_data_set += data_set

        return merged_data_set

    @staticmethod
    def filter_useless_items(data_set):
        while True:
            useless_item_found = False
            del_index = 0

            for idx, item in enumerate(data_set):
                if item is ['item_name', 'info_list', 'image_link', 'main_category', 'sub_category', 'category_name']:
                    useless_item_found = True
                    del_index = idx
                    break

            del data_set[del_index]

            if useless_item_found is False:
                break

        return data_set

    @staticmethod
    def get_unique_json_data_set(data_set):
        str_data_set = []

        for data in data_set:
            str_data_set.append(json.dumps(data))

        str_data_set = set(str_data_set)

        filtered_data_list = []

        for data in str_data_set:
            filtered_data_list.append(json.loads(data))

        return filtered_data_list

    @staticmethod
    def get_splited_data_path(db_name, split_rank):
        top = db_name

        folder_list = []

        for root, dirs, files in os.walk(top, topdown=False):
            for name in dirs:
                folder_list.append({'path': os.path.join(root, name), 'files': None})

        for folder in folder_list:
            folder['files'] = [x[-1] for x in os.walk(folder['path'])][0]

        # Get all path & size
        sum_size = 0

        all_file_path = []
        for folder in folder_list:
            for file_name in folder['files']:
                file_size = os.path.getsize(folder['path'] + '/' + file_name)
                sum_size += file_size

                all_file_path.append({'file_path':folder['path'] + '/' + file_name, 'file_size':file_size})

        # Split by file size
        each_split_rank = sum_size // split_rank

        splited_file_path_list = []

        splited_file_path = []
        splited_file_size = 0

        for idx, file_data in enumerate(all_file_path):
            if splited_file_size <= each_split_rank:
                splited_file_size += file_data['file_size']
                splited_file_path.append(file_data['file_path'])

                if idx is len(all_file_path)-1 :
                    splited_file_path_list.append(splited_file_path)

            else :
                splited_file_path_list.append(splited_file_path)

                splited_file_path = [file_data['file_path']]
                splited_file_size = file_data['file_size']

        return splited_file_path_list

    @staticmethod
    def get_all_data_in_path(db_name):
        top = db_name

        folder_list = []

        for root, dirs, files in os.walk(top, topdown=False):
            for name in dirs:
                folder_list.append({'path': os.path.join(root, name), 'files': None})

        for folder in folder_list:
            folder['files'] = [x[-1] for x in os.walk(folder['path'])][0]

        # Load all & Integrate data
        all_data = []

        for folder in folder_list:
            for file_name in folder['files']:
                try :
                    print('Data Loaded from "' + folder['path'] + '/' + file_name + '"')
                    all_data += DataLoader.load_pickle_data(file_path=folder['path'] + '/' + file_name)

                except Exception as e :
                    print(e)

        print('All data Length: ' + str(len(all_data)))

        return all_data
