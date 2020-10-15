#!/usr/bin/env python3


import finplot as fplt
import numpy as np
import pandas as pd


# 1. replace default axis with your own
def my_timestamp_str(df, row):
    row = max(0, min(len(df)-1, int(row))) # clamp
    col = 0 # or 'timestamp' or whatever is your datetime column name
    s = str(pd.to_datetime(df.loc[row, col], unit='ms'))
    return s.partition(' ')[2].partition('.')[0] # only time without milliseconds

class MyAxis(fplt.EpochAxisItem):
    def tickStrings(self, values, scale, spacing):
        return [my_timestamp_str(self.vb.datasrc.df, value) for value in values]

ax = fplt.create_plot()
ax.setAxisItems({'bottom': MyAxis(vb=ax.vb, orientation='bottom')})

# 2. plot something
timestamp = np.linspace(1_602_172_653_135, 1_602_173_653_135, 500)
y = np.random.random(len(timestamp))
fplt.plot(timestamp, y, ax=ax)

# 3. fix the crosshair X text too
def update_crosshair_text(x, y, xtext, ytext):
    return xtext.partition(' ')[2], ytext
fplt.add_crosshair_info(update_crosshair_text)

fplt.show()
