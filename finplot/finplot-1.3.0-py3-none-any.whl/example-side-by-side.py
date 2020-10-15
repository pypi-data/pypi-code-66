#!/usr/bin/env python3

import finplot as fplt
from functools import lru_cache
from PyQt5.QtWidgets import QGraphicsView, QComboBox, QLabel
from PyQt5.QtGui import QApplication, QGridLayout
from threading import Thread
import yfinance as yf


app = QApplication([])
win = QGraphicsView()
win.setWindowTitle('TradingView wannabe #2')
layout = QGridLayout()
win.setLayout(layout)
win.resize(900, 600)

combo1 = QComboBox()
combo1.setEditable(True)
[combo1.addItem(i) for i in 'AMRK FB GFN REVG TSLA TWTR WMT CT=F GC=F ^FTSE ^N225 EURUSD=X ETH-USD'.split()]
layout.addWidget(combo1, 0, 0, 1, 1)
info1 = QLabel()
layout.addWidget(info1, 0, 1, 1, 1)

combo2 = QComboBox()
combo2.setEditable(True)
[combo2.addItem(i) for i in 'AMRK FB GFN REVG TSLA TWTR WMT CT=F GC=F ^FTSE ^N225 EURUSD=X ETH-USD'.split()]
layout.addWidget(combo2, 0, 2, 1, 1)
info2 = QLabel()
layout.addWidget(info2, 0, 3, 1, 1)

ax1, ax2 = fplt.create_plot_widget(win, init_zoom_periods=100, rows=2)
win.axs = [ax1, ax2] # finplot requres this property
layout.addWidget(ax1.ax_widget, 1, 0, 1, 2)
layout.addWidget(ax2.ax_widget, 1, 2, 1, 2)


@lru_cache(maxsize=15)
def download1(symbol):
    return yf.download(symbol, '2020-01-01')

@lru_cache(maxsize=15)
def download2(symbol):
    return yf.download(symbol, '2020-06-01')

@lru_cache(maxsize=100)
def get_name(symbol):
    return yf.Ticker(symbol).info['shortName']

plots1 = []
def update1(txt):
    df = download1(txt)
    if len(df) < 20: # symbol does not exist
        return
    info1.setText('Loading symbol name...')
    price = df['Open Close High Low'.split()]
    ma20 = df.Close.rolling(20).mean()
    ma50 = df.Close.rolling(50).mean()
    volume = df['Open Close Volume'.split()]
    if not plots1:
        plots1.append(fplt.candlestick_ochl(price, ax=ax1))
        plots1.append(fplt.plot(ma20, legend='MA-20', ax=ax1))
        plots1.append(fplt.plot(ma50, legend='MA-50', ax=ax1))
        plots1.append(fplt.volume_ocv(volume, ax=ax1.overlay()))
    else:
        plots1[0].update_data(price)
        plots1[1].update_data(ma20)
        plots1[2].update_data(ma50)
        plots1[3].update_data(volume)
    Thread(target=lambda: info1.setText(get_name(txt))).start() # slow, so use thread

plots2 = []
def update2(txt):
    df = download2(txt)
    if len(df) < 20: # symbol does not exist
        return
    info2.setText('Loading symbol name...')
    price = df['Open Close High Low'.split()]
    ma20 = df.Close.rolling(20).mean()
    ma50 = df.Close.rolling(50).mean()
    volume = df['Open Close Volume'.split()]
    if not plots2:
        plots2.append(fplt.candlestick_ochl(price, ax=ax2))
        plots2.append(fplt.plot(ma20, legend='MA-20', ax=ax2))
        plots2.append(fplt.plot(ma50, legend='MA-50', ax=ax2))
        plots2.append(fplt.volume_ocv(volume, ax=ax2.overlay()))
    else:
        plots2[0].update_data(price)
        plots2[1].update_data(ma20)
        plots2[2].update_data(ma50)
        plots2[3].update_data(volume)
    Thread(target=lambda: info2.setText(get_name(txt))).start() # slow, so use thread
    

combo1.currentTextChanged.connect(update1)
update1(combo1.currentText())

combo2.currentTextChanged.connect(update2)
update2(combo2.currentText())


fplt.show(qt_exec=False) # prepares plots when they're all setup
win.show()
app.exec_()
