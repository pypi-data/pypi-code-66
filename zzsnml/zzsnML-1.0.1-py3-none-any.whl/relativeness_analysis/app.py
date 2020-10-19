# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, flash, redirect, url_for, request, abort, session
import os
from relativeness_analysis.relevant_analysis import main, test
from relativeness_analysis.manager import test as train_test
import warnings
warnings.filterwarnings('ignore')
DEBUG = False
PORT = 8006
HOST = '0.0.0.0'

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = 'skfasmknfdhflm-vkllsbzdfmkqo3ooishdhzo295949mfw,fk'

# APP_ROOT = os.path.abspath('.')

@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

@app.route('/api/', methods=('GET', 'POST'))
def get_result():
    # title = request.args.get('title', '')
    # content = request.args.get('content', '')
    # company = request.args.get('company', '')
    # if title == '' and content == '':
    #     return '-2'
    # _content = title + '。' + content
    # # print(_content)
    # relevant = test(_content, company)
    # return relevant
    file_path = request.form.get('file_path', None)
    _all = request.form.get('_all', True)
    prefix = request.form.get('prefix', './')
    if file_path is None:
        return '必须给定输入文件！'
    if type(_all) == str:
        _all = _all.lower()
        if _all == 'false':
            _all = False
        elif _all == 'true':
            _all = True
        else:
            return '_all参数错误，只能取值True或者False。'
    print(file_path, _all, prefix)
    result_file = main(file_path, _all=_all, prefix=prefix)
    return result_file

@app.route('/api2/', methods=('GET', 'POST'))
def get_single_result():
    title = request.form['title']
    print(title)
    content = request.form['content']
    company = request.form['company']
    if title == '' and content == '':
        return '-2'
    _content = title + '。' + content
    # print(_content)
    relevant = test(_content, company)
    return relevant

@app.route('/train/', methods=('GET', 'POST'))
def train():
    connection_string = request.form['connection_string']
    begin_date = request.form['begin_date']
    end_date = request.form['end_date']
    try:
        if (connection_string is None) and (begin_date is None) and (end_date is None):
            print(r'正在使用默认参数训练模型，connection_string为cis/cis_zzsn9988@114.116.91.1:1521/orcl, begin_date为2017-03-01, end_date为2017-07-13')
            train_test()
        elif (connection_string == '') and (begin_date == '') and (end_date == ''):
            print(r'正在使用默认参数训练模型，connection_string为cis/cis_zzsn9988@114.116.91.1:1521/orcl, begin_date为2017-03-01, end_date为2017-07-13')
            train_test()
        else:
            print(r'正在使用指定参数训练模型，connection_string为%s, begin_date为%s, end_date为%s' % (connection_string, begin_date, end_date))
            train_test(connection_string, begin_date, end_date)
    except Exception as e:
        return 'train fail'
    else:
        return 'train success'
app.run(debug=DEBUG, host=HOST, port=PORT)
