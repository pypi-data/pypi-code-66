from gsheets import Sheets
import matplotlib.pyplot as plt


class SheetsPlus(Sheets):
    """
    Extends Sheets for added functionalities.
    """

    def plot(self, df, x, y, img_name):
        """Plots graph between the x and y axis and saves the image on local disk.

        Args:
            x (str): X-axis for the graph
            y (str): Y-axis for the graph
            df (pandas.DataFrame) : Pandas DataFrame containing sheets data
        """
        plt.scatter(df[x], df[y])
        plt.xlabel(x)
        plt.ylabel(y)
        plt.savefig(f"{img_name}.jpg")
