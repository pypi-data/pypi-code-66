#!/usr/bin/env python3

import finplot as fplt
import pandas as pd
import yfinance as yf


def plot_years(daily_returns):
    years = list(daily_returns.groupby(pd.Grouper(freq="Y"))) # split daily returns into year
    for i,(yn,dfy) in enumerate(years):
        dates = years[-2][1].index # last year's dates
        dates = dates[-len(dfy):] if i == 0 else dates[:len(dfy)] # first & last year are incomplete
        prices = dfy.Close.reset_index(drop=True).iloc[:len(dates)] # truncate leap years
        yield fplt.plot(dates, prices, legend=str(yn).partition('-')[0])


def valign_plots(x):
    df = plots[0].datasrc.df
    for col,plot in zip(df.columns[1:], plots):
        v = df.loc[x, col]
        if v > -1e10: # skip NaNs
            plot.update_data(df[col]-v)


def mmove(x, y, xtext, ytext):
    valign_plots(x)
    return xtext.partition('-')[2], ytext


btc = yf.download('VOW.DE', '2014-05-01')
daily_returns = (btc.pct_change()*100).rolling(90).mean() # smooth daily returns over three months
fplt.create_plot('Mouse hover center daily Wolksvagen returns (90 day smooth)', maximize=False)
plots = list(plot_years(daily_returns))
fplt.add_crosshair_info(mmove)
fplt.show()
