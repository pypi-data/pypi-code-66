#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 17:01
# @Author  : 程婷婷
# @FileName: feature_word.py
# @Software: PyCharm
import jieba.posseg as pseg  # 词性标注
import pandas as pd
import os
class FeatureWord():
    def read_file(self, filename, column):
        df = pd.read_excel(filename)
        df1 = df.dropna(subset=[column])
        flags = []
        features= []
        print(len(df1[column]))
        for sent in df1[column]:
            sent = str(sent).replace(' ', '')
            psegs = []
            feature = []
            words = pseg.cut(str(sent))
            for word, flag in words:
                psegs.append(flag)
                feature.append(word)
            flags.append(psegs)
            features.append(feature[-1])
        return features
    def write_txt(self, filename, features):
        if os.path.exists(os.path.dirname(filename)) == False:
            os.mkdir(os.path.dirname(filename))
        f =  open(filename, 'w', encoding='utf-8')
        for i in features:
            f.write(i + '\n')
        f.close()
# feature_word = FeatureWord()
# features = set(feature_word.read_file(filename=r'C:\Users\lenovo\Desktop\work\2020-07-13\一带一路_0706.xls', column='合同金额'))
# feature_word.write_txt('./data/feature_dict.txt', features)
