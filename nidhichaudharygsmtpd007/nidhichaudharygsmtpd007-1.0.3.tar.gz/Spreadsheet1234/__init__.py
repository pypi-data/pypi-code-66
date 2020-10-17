import gspread
import pandas as pd
import matplotlib.pyplot as plt
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


def createcredentials(stringname, sheetname):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(stringname, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(sheetname).sheet1
    d = wks.get_all_records()
    return d

def createDF(d):
    df = pd.DataFrame(d)
    return df

def plotBar(df, x_axis, y_axis):
    plt.bar(df[x_axis], df[y_axis])
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    legend = plt.legend(loc='upper left')
    plt.show()

def plotLine(df, x_axis, y_axis):
    plt.plot(df[x_axis], df[y_axis], color = 'green', linestyle='dotted', marker='>', 
    markerfacecolor='blue', markersize=3)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    legend = plt.legend(loc='upper left')
    plt.show()    

def plotScatter(df, x_axis, y_axis, colors):
    plt.scatter(df[x_axis], df[y_axis], s = 100, c = colors, cmap='Greens',
     edgecolor='black', alpha=0.75, linewidth=1, label = y_axis)
    cbar = plt.colorbar()
    cbar.set_label(x_axis)
    y_mean = [df[y_axis].mean()]*len(df[x_axis])
    meanY = 'Mean:' + str(df[y_axis].mean())
    plt.plot(df[x_axis],y_mean, linestyle='--', color = 'red', linewidth = 5, label = meanY)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    legend = plt.legend(loc='upper left')
    plt.show()    