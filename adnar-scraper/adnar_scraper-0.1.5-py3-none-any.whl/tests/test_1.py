from adnar_scraper.utility.data_loader import DataLoader

try :
    k = DataLoader.load_pickle_data(file_path='sdfsdf')

except OSError as e:
    # 여기 고쳐야함.
    print(e)
    if e.errno is 2:
        data_list = []

print('loaded ' + str(len(data_list)) + ' data')