#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/10/9 14:39
# @Author  : 程婷婷
# @FileName: process.py
# @Software: PyCharm
import re
import pandas as pd
import json
import emoji
a = r'<h1>青岛双星控股股东双星集团</h1><p>响了青岛市属国有企业混改第一枪……10月9日，青岛双星<span style="font-size: 24px;">股价应声涨停，显示了市场对于这一举动的期待。</span></p><p><span style="font-size: 24px;">作为国资大省,山东省国有企业三年混改计划和青岛市国有企业改革正<span style="font-family: 隶书, SimLi; font-size: 24px;">步入深水区,双星集</span></span><span style="font-family: 隶书, SimLi;">团一级企业层面混改的启动,或掀起新一轮山东国企改革浪潮。值得注意的是,与此前的混改更多在二级、三级子公司层面相比,此次混改进一步深化,企业集团层面的混改成为国企改革攻坚重点合法权益得不到充分保护 ●由于国有企业和民营企业文化理念不同，双方混合后在管理方式、具体操作等方面存在矛盾，向现代企业制度转轨比较艰难 融合之路 ●省属企业新投资项目，原则上投资主体必须是现有混合所有制企业或新引进非国有资本合作企业 ●研究建立以资本收益为主的考核指标体系，支持混改企业按市场化原则进合法权益得不到充分保护 ●由于国有企业和民营企业文化理念不同，双方混合后在管理方式、具体操作等方面存在矛盾，向现代企业制度转轨比较艰难 融合之路 ●省属企业新投资项目，原则上投资主体必须是现有混合所有制企业或新引进非国有资本合作企业 ●研究建立以资本收益为主的考核指标体系，支持混改企业按市场化原则进</span>。打响了青岛市属国有企业混改第一枪。10月9日,青岛双星<span style="font-size: 24px;">股价应声涨停,显示了市场对于这一举动的期待。</p><h1>双星集团的混改实验</h1><p>省属企业新投资项目，原则上投资主体必须是现有混合所有制企业或新引进非国有资本合作企业</p>'

def filter_emoji(context):
    #过滤表情
    chars = ''
    text = emoji.demojize(context)
    for i in range(9636, 11217):
        chars += chr(i)
    chars = '[' + chars
    chars = chars + ']'
    rules = re.compile(chars)
    text = rules.sub('。', text)
    return text

def clean_tag(context):
    rule = re.compile('</h[0-9]+>', re.S)
    context = rule.sub('\n', context)
    rule1 = re.compile('</p>', re.S)
    context = rule1.sub('\n', context)
    rules = re.compile('<[^>]+>', re.S)
    text = rules.sub('', context)
    text = filter_emoji(text)
    text = text.split('\n')
    data = []
    for i in text:
        data.append((i,text.index(i)))
    return data

def split_sentence(tup):
    index1 = tup[1]
    context = tup[0]
    context = re.sub('([。！？\?])([^”’])', r"\1\n\2", context)  # 单字符断句符
    context = re.sub('(\.{6})([^”’])', r"\1\n\2", context)  # 英文省略号
    context = re.sub('(\…{2})([^”’])', r"\1\n\2", context)  # 中文省略号
    context = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', context)
    # 如果双引号前有终止符，那么双引号才是句子的终点，把分句符\n放到双引号后，注意前面的几句都小心保留了双引号
    para = context.rstrip()  # 段尾如果有多余的\n就去掉它
    # 很多规则中会考虑分号;，但是这里我把它忽略不计，破折号、英文双引号等同样忽略，需要的再做些简单调整即可。
    sentences = para.split('\n')
    data = []
    for i in sentences:
        data.append((i,index1))
    return data

def text_process(context):
    data = clean_tag(context)
    text = []
    for index in data:
        text.extend(split_sentence(index))
    # context = map(lambda x: split_sentence(x), df['text'])
    return text

print(text_process(a))