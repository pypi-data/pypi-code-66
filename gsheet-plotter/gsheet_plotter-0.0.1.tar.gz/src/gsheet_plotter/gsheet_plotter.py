from gsheet_api import GSheetAPI
import os.path
import matplotlib.pyplot as plt
import logging
import warnings
import pandas as pd

class GSheetPlotter(object):

    """
    Easily visualize your google sheet.

    Important:
        -Credentials required are the Google Service Account json file

    Usage Example:
        gplotter=GSheetPlotter(...) #initialize the class
        gplotter.fetch_data(...) #fetch the data from the sheet
        gplotter.plot_graph(...) #plot the graph between two columns
        gplotter.fetch_and_plot(...) #fetch and plot the graph using one function
    """

    def __init__(self,creds,sheet_id,tab_name):
        """
        Inits the GSheetsPlotter Class and sets the current working sheet and current working tab.

        Args:
            creds(str): JSON file path entered as a string.
            sheet_id(str): Sheet Id found in the Google Sheet URL
            tab_name(str): Name of the tab to use within the Google Sheet.

        Raises:
            FileNotFoundError: JSON credential file not found.
            ApiError: Sheet with the given Id not found
            WorkSheetNotFound: Worksheet with the given tab name not found
            TypeError: Missing required positional argument
        """
        self.creds = creds
        self.sheet_id = sheet_id
        self.tab_name = tab_name
        if not os.path.exists(self.creds):
            raise(FileNotFoundError("File with path '{}' not found".format(creds)))
        self.sheet = GSheetAPI(self.creds,self.sheet_id,self.tab_name)
        self.data= pd.DataFrame()

    def fetch_data(self,col_list):
        """
        Fetches the data from the sheet and converts it to a dataframe

        Args:
            col_list(list): List of ints representing the column number to extract (eg. range(0,3) for [0, 1, 2] or [0, 1, 2])
        
        Raises:
            TypeError: Missing required positional argument
            ValueError: Columns expected not found, data type of the column number is not int or passed argument is not list like.
        """
        self.col_list = col_list
        df = self.sheet.sheet_to_df(self.col_list,header=0,evaluate_formulas=False)
        self.data=df
            
    def plot_graph(self,x_col_name,y_col_name):
        """
        Plots the graph between two columns and save it as a .png file

        Note- 1. Generates a warning when any of the column is not numeric type
              2. Prints a message on successfully saving the graph

        Args: 
            x_col_name(str): Name of the column for x-axis
            y_col_name(str): Name of the column for y-axis

        Raises:
            RuntimeError: No data to plot
            TypeError: Missing required positional argument
            KeyError: Column with the name does not exist
        """

        if self.data.empty:
            raise RuntimeError("You have no data to plot.")
        else:
            try:
                if self.data[x_col_name].dtype not in ('int','float'):
                    warnings.warn("Column {} is not numeric type.".format(x_col_name))
                if self.data[y_col_name].dtype not in ('int','float'):
                    warnings.warn("Column {} is not numeric type.".format(y_col_name))
                plt.plot(self.data[x_col_name],self.data[y_col_name])
                plt.xlabel(self.data.columns[0])
                plt.ylabel(self.data.columns[1])
                filename= x_col_name + '_' + y_col_name + '.png'
                plt.savefig(filename)
                print("Your graph is saved as {}".format(filename))
            except KeyError as e:
                raise(e)
    
    def fetch_and_plot_graph(self,col_list):
        """
        Fetches the data from the sheet,converts it to a dataframe.
        Plots the graph between two columns and save it to a .png file.

        Note- 1. Generates a warning when any of the column is not numeric type
              2. Prints a message on successfully saving the graph
        
        Args:
            col_list(list): List of ints representing the column number to extract (eg. range(0,2) for [0, 1] or [0, 1])
        
        Raise:
            TypeError: Missing required positional argument
            ValueError: Columns expected not found, data type of the column number is not int or passed argument is not list like or column list size is not equal to 2.
            RuntimeError: No data to plot

        """
        if len(col_list)!=2:
            raise ValueError("Column list size is not equal to 2")
        self.fetch_data(col_list)
        if self.data.empty:
            raise RuntimeError("You have no data to plot.")
        else:
            if self.data.iloc[0].dtype not in ('int','float'):
                warnings.warn("Column at index 0 is not numeric type.")
            if self.data.iloc[1].dtype not in ('int','float'):
                warnings.warn("Column at index 1 is not numeric type.")
            plt.plot(self.data.iloc[:,0],self.data.iloc[:,1])
            x_col_name=self.data.columns[0]
            y_col_name=self.data.columns[1]
            plt.xlabel(x_col_name)
            plt.ylabel(y_col_name)
            filename= x_col_name + '_' + y_col_name + '.png'
            print("Your graph is saved as {}".format(filename))
            plt.savefig(filename)
