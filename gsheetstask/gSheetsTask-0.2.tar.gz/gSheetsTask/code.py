import gspread
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import getpass
import os
#Enter the Google Sheet name as sheet_name
#Enter one attribute name in x_axis
#Enter another attribute name in y_axis
#Enter the name of the image file you want to store in pc as chart_name
def sheet_charts(sheet_name,x_axis,y_axis,chart_name):
	username = getpass.getuser()
	path1 = 'C:/Users/'+username+'/Downloads/service_account.json'
	#setting connection with sheets using service_account credentials
	#credentials stored in Downloads folder
	gc = gspread.service_account(path1)
	#creating spread sheet instance sh
	sh = gc.open(sheet_name)
	#accessing worksheet
	x2=sh.get_worksheet(0)
	#copying worksheet contents in pandas dataframe 'records'
	records = pd.DataFrame.from_dict(x2.get_all_records())
	#creating plot
	fig= plt.subplots(figsize=(12,6))
	sns_plot=sns.barplot(x=x_axis,y=y_axis,data=records)
	#saving the plot in png format
	path2='C:/Users/'+username
	os.chdir(path2)
	sns_plot.figure.savefig(chart_name+".png")
	print("chart saved in the current directory")