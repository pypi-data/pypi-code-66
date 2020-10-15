#!/usr/bin/env python3

import finplot as fplt
import yfinance as yf


df1 = yf.download('WMT', '2020-07-01')
df2 = yf.download('TWTR', '2020-07-01')

ax = fplt.create_plot()
p1 = fplt.candlestick_ochl(df1[['Open','Close','High','Low']], ax=ax)
p2 = fplt.candlestick_ochl(df2[['Open','Close','High','Low']], ax=ax.overlay(scale=1.0, y_axis='linear'))
p2.x_offset = 0.1
p2.colors.update(dict(
            bull_shadow = '#388d53',
            bull_frame  = '#205536',
            bull_body   = '#52b370',
            bear_shadow = '#d56161',
            bear_frame  = '#5c1a10',
            bear_body   = '#e8704f'))
fplt.show()
