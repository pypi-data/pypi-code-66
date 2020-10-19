# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, flash, redirect, url_for, request, abort, session
from werkzeug.utils import secure_filename
import time
import os, sys
# sys.path.append('./app/SVM/')
from sentiment_analysis.svm_app import predict_one
from sentiment_analysis.SVM.svm import svm
import warnings
warnings.filterwarnings('ignore')
DEBUG = False
PORT = 8008
HOST = '0.0.0.0'

app = Flask(__name__)
app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True
app.secret_key = 'skfasmknfdhflm-vkllsbzdfmkqo3ooishdhzo295949mfw,fk'

# APP_ROOT = os.path.abspath('.')


@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

## This function is not for sentiment analysis
# @app.route('/api/', methods=('GET', 'POST'))
# def get_result():
#     # title = request.args.get('title', '')
#     # content = request.args.get('content', '')
#     # company = request.args.get('company', '')
#     # if title == '' and content == '':
#     #     return '-2'
#     # _content = title + '。' + content
#     # # print(_content)
#     # relevant = test(_content, company)
#     # return relevant
#     file_path = request.args.get('file_path', None)
#     _all = request.args.get('_all', True)
#     prefix = request.args.get('prefix', './')
#     if file_path is None:
#         return '必须给定输入文件！'
#     if type(_all) == str:
#         _all = _all.lower()
#         if _all == 'false':
#             _all = False
#         elif _all == 'true':
#             _all = True
#         else:
#             return '_all参数错误，只能取值True或者False。'
#     print(file_path, _all, prefix)
#     result_file = main(file_path, _all=_all, prefix=prefix)
#     return result_file

@app.route('/api2/', methods=('GET', 'POST'))
def get_single_result():
    title = request.form['title']
    content = request.form['content']
    if title == '' and content == '':
        return '-1'
    _content = title + '。' + content
    # print(_content)
    sentiment = predict_one(_content)
    return sentiment

@app.route('/train/', methods=('GET', 'POST'))
def begin_train():
    connection_string = request.form['connection_string']
    from_date = request.form['from_date']
    to_date = request.form['to_date']
    try:
        if (connection_string is None) and (from_date is None) and (to_date is None):
            print(r'正在使用默认参数训练模型，connection_string为cis/cis_zzsn9988@114.116.91.1:1521/orcl, from_date为2017-06-01, to_date为2017-06-15')
            svm.train()
        elif (connection_string == '') and (from_date == '') and (to_date == ''):
            print(r'正在使用默认参数训练模型，connection_string为cis/cis_zzsn9988@114.116.91.1:1521/orcl, from_date为2017-06-01, to_date为2017-06-15')
            svm.train()
        else:
            print(r'正在使用指定参数训练模型，connection_string为%s, from_date为%s, to_date为%s' %(connection_string, from_date, to_date))
            svm.train(connection_string, from_date, to_date)
    except Exception as e:
        return 'train fail'
    else:
        return 'train success'
# if __name__ == '__main__':
app.run(debug=DEBUG, host=HOST, port=PORT)
