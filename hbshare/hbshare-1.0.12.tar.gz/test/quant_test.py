#!/usr/bin/python
#coding:utf-8

"""
@author: Meng.lv
@contact: meng.lv@howbuy.com
@software: PyCharm
@file: quant_test.py.py
@time: 2020/10/20 16:13
"""
from datetime import datetime, timedelta
import hbshare as hbs

def main():

    hbs.set_token("eTFrL1JzRVI3WGJycEp2cXFCczhwZz09")

    end_date = datetime(2020, 10, 9).date()
    start_date = end_date - timedelta(days=365 * 2 + 7)
    start_date2 = end_date - timedelta(days=365 + 7)

    tab = hbs.gen_tab(end_date=end_date, class0='cta')
    #tab.render('summary.html')
    html_content = tab.render_embed()
    print("%html {}".format(html_content))


if __name__ == "__main__":
    main()