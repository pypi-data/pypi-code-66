import numpy as np
import matplotlib.pyplot as plt
from adnar_scraper.utility.data_loader import DataLoader
import regex as re


class ShopAnalyzer:
    def __init__(self):
        pass

    @staticmethod
    def show_shop_count_graph(data_set, grad):
        x_data = []
        y_data = []

        for idx, data in enumerate(data_set):
            if int(re.sub(pattern=',', repl='', string=data['item_count'])) >= 60000:
                continue

            print(idx/len(data_set) * 100)
            is_in_list = False

            for x_idx, x in enumerate(x_data):
                if int(re.sub(pattern=',', repl='', string=data['item_count'])) == x:
                    is_in_list = True
                    y_data[x_idx] += 1
                    break

            if is_in_list is False:
                x_data.append(int(re.sub(pattern=',', repl='', string=data['item_count'])))
                y_data.append(1)

        # filter data
        x_data.reverse()
        y_data.reverse()

        splited_x_data = [100, 200, 300, 400, 500, 600, 700, 800, 900, 1000]
        splited_y_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for idx_x, x in enumerate(splited_x_data):
            splited_x_data[idx_x] = int(splited_x_data[idx_x] / grad)

        for idx_x, x in enumerate(x_data):
            if y_data[idx_x] >= 1:
                formal_splited = 0

                if x > splited_x_data[-1]:
                    splited_y_data[-1] += 1

                else:
                    for splited_x_idx, splited_x in enumerate(splited_x_data):
                        if formal_splited <= x <  splited_x:
                            splited_y_data[splited_x_idx] += y_data[idx_x]

                        formal_splited = splited_x


        # Plot data
        print(splited_x_data)
        print(splited_y_data)

        sum_y = 0

        for y in splited_y_data:
            sum_y += y

        print(len(data_set))
        print(sum_y)

        splited_x_data = np.array(splited_x_data)
        splited_y_data = np.array(splited_y_data)

        # Plot Graph
        plt.plot(splited_x_data, splited_y_data, 'ro')
        plt.grid()

        fig = plt.gcf()

        fig.savefig('shop_graph.png')

        #plt.show()


if __name__ == "__main__":
    # x~100
    data_set = DataLoader().load_pickle_data(filepath='../database/shop/shop_FashionCloth_ver_1.pkl')
    analyzer = ShopAnalyzer()

    analyzer.show_shop_count_graph(data_set=data_set, grad=100)
