#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 18:13
# @Author  : 程婷婷
# @FileName: text_sim2.py
# @Software: PyCharm
from simhash import Simhash
import pandas as pd
import json
from zhon.hanzi import punctuation
def simhash_similarity(text1, text2):
    a_simhash = Simhash(text1)
    b_simhash = Simhash(text2)
    max_hashbit = max(len(bin(a_simhash.value)), len(bin(b_simhash.value)))
    # 汉明距离
    distince = a_simhash.distance(b_simhash)
    similar = 1-distince/max_hashbit
    return similar

# 分词
def split_line(line):
    table = str.maketrans('','',punctuation)
    wipe_line = line.translate(table)
    return wipe_line

def calculate_simhash_result(df):
    duplication_list =[]
    ids = []
    for i in range(len(df['context'])):
        start = i+1
        for j in range(start,len(df['context']),1):
            con = split_line(df['context'][i])
            con2 = split_line(df['context'][j])
            similar = simhash_similarity(con, con2)
            if similar >= 0.7:
                if ([int(df['id'][i]), int(df['id'][j])]) not in ids:
                    duplication_list.append({'ids': [int(df['id'][i]), int(df['id'][j])], 'context1':df['context'][i], 'context2':df['context'][j]})
                    ids.append([int(df['id'][i]), int(df['id'][j])])
    return json.dumps(duplication_list, ensure_ascii=False)
