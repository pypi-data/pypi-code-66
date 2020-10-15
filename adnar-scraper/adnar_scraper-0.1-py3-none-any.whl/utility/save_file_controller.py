import time
import settings

from adnar_scraper.utility.data_loader import DataLoader


class SaveFileController:
    def __init__(self, name, date_time, kind):
        self.name = name
        self.date_time = date_time

        folder_path = None

        if kind is 'shop':
            folder_path = settings.SHOP_DATABASE_PATH

        elif kind is 'item':
            folder_path = settings.ITEM_DATABASE_PATH

        self.base_path = folder_path + name + '/' + date_time + '/'
        DataLoader.create_if_folder_not_exists(path=self.base_path)

        self.saving_version = 0

    def save_data_memory_saving_version(self, process_num, data_set):
        saving_time = DataLoader.create_file_name()

        print("=" * 50)
        absolute_path = self.base_path + saving_time

        print('Process_' + str(process_num) + ' : saved ' + str(len(data_set)) + ' data')

        DataLoader.save_pickle_data(data=data_set, file_path=absolute_path)
        print("=" * 50)

    def save_data_each(self, process_num, data_set):
        print("=" * 50)
        absolute_path = self.base_path + str(process_num)

        try:
            data_list = DataLoader.load_pickle_data(file_path=absolute_path + '.pkl')

        except OSError as e:
            # 여기 고쳐야함.
            print(e)
            if e.errno is 2:
                data_list = []

        print('Process_' + str(process_num) + ' : loaded ' + str(len(data_list)) + ' data')

        for item in data_set:
            data_list.append(item)

        print('Process_' + str(process_num) + ' : saved ' + str(len(data_list)) + ' data')

        DataLoader.save_pickle_data(data=data_list, file_path=absolute_path)
        print("=" * 50)