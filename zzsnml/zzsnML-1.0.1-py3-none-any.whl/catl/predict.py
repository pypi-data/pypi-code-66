# -*- coding: utf-8 -*-
"""
Created on Tue Jun 5 2018

@author: WuDaqing
"""

from catl.utilities import single_predict

name = input('Please input the name of company: ')
title = input('Please input the title: ')
content = input('Please input the content: ')

Predict = single_predict(name=name,title=title,content=content)
prediction = Predict.predict() # prediction 是 '保留' 或者 '删除'

print('Text is '+prediction)

