#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 9:18
# @Author  : 程婷婷
# @FileName: app.py
# @Software: PyCharm
# -*- coding: utf-8 -*-
from flask import Flask, g, render_template, flash, redirect, url_for, request, abort, session
from ner.extract import Extract
import pandas as pd
import traceback
import json
import os
DEBUG = False
PORT = 8018
HOST = '0.0.0.0'
# HOST = '127.0.0.1'

app = Flask(__name__)
file_path = os.path.dirname(os.path.realpath(__file__))
txt_path = r'./data/feature_dict.txt'
province_path = r'./data/province.txt'
country_path = 'data/国家名称.xlsx'
country_df = pd.read_excel(os.path.join(file_path,country_path), header=None)[0].tolist()
country_df.remove('中国')
extract = Extract(country=country_df)
province = extract.read_txt(os.path.join(file_path, province_path))
money_feature = extract.read_txt(os.path.join(file_path,txt_path))
address_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/address_filter.txt'))
capacity_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/capacity_filter.txt'))
entity_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/entity_filter.txt'))
money_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/money_filter.txt'))
project_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/project_filter.txt'))
state_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/state_filter.txt'))
time_filter = extract.read_txt(os.path.join(file_path,r'./data/filter/time_filter.txt'))
address_pattern = extract.read_txt(os.path.join(file_path,'./data/pattern/address_pattern.txt'))
capacity_pattern = extract.read_txt(os.path.join(file_path,'./data/pattern/capacity_pattern.txt'))
money_pattern = extract.read_txt(os.path.join(file_path,r'./data/pattern/money_pattern.txt'))
state_pattern = extract.read_txt(os.path.join(file_path,r'./data/pattern/state_pattern.txt'))
time_pattern = extract.read_txt(os.path.join(file_path,r'./data/pattern/time_pattern.txt'))
state_no_words = extract.read_txt(os.path.join(file_path,r'./data/filter/state_no_words.txt'))
model = HanLP.newSegment('crf').enableOrganizationRecognize(True)
@app.route('/', methods=('GET', 'POST'))
def index():
    return ''

def get_return_info(money_results=None, address_results=None, capacity_results=None,jia=None, yi=None, project_results=None, country_results=None, state_results=None, time_results=None):
    return json.dumps({'项目金额': money_results, '项目地址': address_results, '设计产能': capacity_results, '执行机构':jia ,'企业':yi,'项目名称': project_results,
                       '涉及国家':country_results, '项目状态':state_results, '项目周期':time_results}, ensure_ascii=False)

@app.route('/extract/', methods=('GET', 'POST'))
def get_prediction():
    title =str(request.form.get('title'))
    text = request.form.get('text')
    print(title)
    if len(title)==0:
        print('文章标题为空')
        return get_return_info('文章标题为空')
    if len(text)==0:
        print('文章内容为空')
        return get_return_info('文章内容为空')
    if (title is None) and (text is not None):
        print('文章标题为空')
        return get_return_info('文章标题为空')
    if (title is  not None) and (text is None):
        print('文章内容为空')
        return get_return_info('文章内容为空')
    try:
        global_sentences = extract.segment_para(para=text)
        money_results = extract.money_pattern(global_sentences=global_sentences, filter_list=money_filter, money_pattern=money_pattern, money_feature=money_feature)
        address_results = extract.address_pattern(global_sentences=global_sentences, filter_list=address_filter, address_pattern=address_pattern)
        capacity_results = extract.capacity_pattern(global_sentences=global_sentences, filter_list=capacity_filter, capacity_pattern=capacity_pattern)
        jia, yi = extract.org_patterns(global_sentences=global_sentences, filter_list=entity_filter, province=province, model=model)
        # org_results.append(jia)
        # org_results1.append(yi)
        project_results = extract.pro(global_sentences=global_sentences, title=title, objects=project_filter, filter_list=project_filter)
        country_results = extract.country_pattern(title=title, para=text)
        state_results = extract.state(global_sentences=global_sentences, title=title, filter_list=state_filter, state_pattern=state_pattern,  state_no_words= state_no_words)
        time_results = extract.time1(global_sentences=global_sentences, filter_list=time_filter, time_pattern=time_pattern)
    except:
        return get_return_info(traceback.print_exc())
    return get_return_info(money_results, address_results, capacity_results, jia, yi, project_results, country_results, state_results, time_results)
# if __name__ == '__main__':
app.run(debug=DEBUG, host=HOST, port=PORT)
