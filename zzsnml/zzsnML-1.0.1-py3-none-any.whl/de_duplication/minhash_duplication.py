#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/9/14 15:37
# @Author  : 程婷婷
# @FileName: text_sim.py
# @Software: PyCharm
from datasketch import MinHash
from zhon.hanzi import punctuation
import jieba
import pandas as pd
import json
Amazon_split = []
Google_split = []

b_split = []

def split_line(line):
    # 对行进行分词，去除标点符号，按空白字符分词
    table = str.maketrans('', '', punctuation)
    wipe_line = line.translate(table)
    split_line = jieba.lcut(wipe_line)
    return split_line
# def read_txt(path='a.txt'):
# # 读入amazon数据集并分词，以列表保存原数据行和分词结果
#     with open(path, encoding='utf-8') as Amazon:
#         for line in Amazon.readlines():
#             line = line.rstrip('\n')
#             Amazon_split.append([line, split_line(line)])
# 定义计算两行文本jaccard相似度的函数
def calculate_jaccard(text1,text2):
    # 计算两行文本的jaccard相似度
    minihash1, minihash2 = MinHash(), MinHash()
    for word in text1:
        minihash1.update(word.encode('utf-8'))
    for word in text2:
        minihash2.update(word.encode('utf-8'))
    return minihash1.jaccard(minihash2)


def calculate_minhash_result(df):
    duplication_list =[]
    a_split = []
    ids = []
    for line in df['context']:
        line = line.strip()
        a_split.append([line, jieba.lcut(line)])
    df['a_split'] = a_split
    # 对数据行进行匹配
    for i in range(len(df['a_split'])):
        start = i + 1
        for j in range(start, len(df['a_split']), 1):
            present_jaccard = calculate_jaccard(a_split[i][1], a_split[j][1])
            if present_jaccard >= 0.7:
                if ([int(df['id'][i]),  int(df['id'][j])]) not in ids:
                    duplication_list.append({'ids': [int(df['id'][i]),  int(df['id'][j])], 'context1': a_split[i][0], 'context2': a_split[j][0]})
                    ids.append([int(df['id'][i]),  int(df['id'][j])])
    return json.dumps(duplication_list, ensure_ascii=False)
