#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 9:18
# @Author  : 程婷婷
# @FileName: app1.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
import pandas as pd
from flask import Flask, g, render_template, flash, redirect, url_for, request, abort, session
from de_duplication.minhash_duplication import calculate_minhash_result
import de_duplication.process
import traceback

DEBUG = False
PORT = 8019
HOST = '0.0.0.0'
# HOST = '127.0.0.1'

app = Flask(__name__)
@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

@app.route('/minhash/', methods=('GET', 'POST'))
def get_prediction():
    data = request.form.get('data')
    if (data is None):
        print('id或文章为空')
        return ('id或文章为空')
    try:
        df = pd.DataFrame()
        id, context = [], []
        data = process.text_process(data)
        print(data)
        for index in data:
            id.append(index[1])
            context.append(index[0])
        df['context'] = context
        df['id'] = id
        duplication_json = calculate_minhash_result(df)
    except:
        return traceback.print_exc()
    return duplication_json
# if __name__ == '__main__':
app.run(debug=DEBUG, host=HOST, port=PORT)
