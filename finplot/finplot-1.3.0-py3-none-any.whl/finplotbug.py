#!/usr/bin/env python3
import finplot as fplt
import pandas as pd
df=pd.read_csv('finplotbug.csv',index_col=0,infer_datetime_format=True,parse_dates=True)
myfplt = fplt.plot(df)
fplt.set_y_scale(yscale='log')
fplt.show()
