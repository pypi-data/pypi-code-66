from gsheets import Sheets
import matplotlib.pyplot as plt


class SheetsPlus(Sheets):
    """
    Inherits Gsheets library

    """
    def __getitem__(self):
        '''

        '''
        super().__init__()

    def plot(self, x, y):
        """Plots graph between x and y axis.

        Args:
            x (str): X-axis for the graph
            y (str): Y-axis for the graph
            df (pandas.DataFrame) : Pandas DataFrame containing sheets data
        """
        values = self._items[0]._values

        # x = df[x].sort_values(ascending=True)
        # y = df[y].sort_values(ascending=True)
        # plt.scatter(x, y)
        plt.savefig("temp.jpg")
