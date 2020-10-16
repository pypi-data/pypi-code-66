import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']


def CreateCredentials(stringname, sheetname):
    credentials = ServiceAccountCredentials.from_json_keyfile_name(stringname, scope)
    gc = gspread.authorize(credentials)
    wks = gc.open(sheetname).sheet1
    print(wks.get_all_records())
    df = pd.DataFrame.from_dict(wks.get_all_records())
    print(df)
    return df

CreateCredentials('newapilibrary-367ec85bcf11.json', 'testapisheet')    