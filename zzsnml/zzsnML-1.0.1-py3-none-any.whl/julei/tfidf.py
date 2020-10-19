# -*- coding: utf-8 -*-
"""
Created on Wed April 17 22:06:20 2019

@author: Wu-Daqing
"""

import time
import os
import pickle
from julei.segment import Segment
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
class Tfidf:
    def make_dir(self):
        if os.path.isdir('result/tfidf/') == False:
            os.makedirs(r'result/tfidf/')

    def load_data(self):
        seg = Segment()
        vocabulary_segment = seg.dump_pkl()
        seg.data_segment()
        # with open('result/segment/vocabulary_segment.pkl','rb') as load1:
        #     vocabulary_segment = pickle.load(load1)
        data = []
        for line in open('result/segment/data_segment.txt','rb'):
            string = line.decode('utf-8-sig')
            string_list = string.split(' ')
            tmp  = []
            for word in string_list:
                if vocabulary_segment[word] < 5:
                    continue
                else:
                    tmp.append(word)
            data.append(' '.join(tmp))
        return data

    def count_tfidf(self):
        tf_transformer = CountVectorizer(ngram_range=(1,1))
        tfidf_transformer = TfidfTransformer(norm='l2',use_idf=True,smooth_idf=True)
        data = self.load_data()
        tf = tf_transformer.fit_transform(data)
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'TF计算完毕')
        tfidf = tfidf_transformer.fit_transform(tf) # 'scipy.sparse.csr.csr_matrix'
        print(time.strftime('%Y-%m-%d %H:%M:%S'),' TFIDF计算完毕')
        self.make_dir()
        with open('result/tfidf/tfidf.pkl','wb') as save1:
            pickle.dump(tfidf,save1,protocol=4)
        #    pickle.dump(tfidf,save1,protocol=4)
        vocabulary_tfidf = tf_transformer.get_feature_names()
        with open('result/tfidf/vocabulary_tfidf.pkl','wb') as save2:
            pickle.dump(vocabulary_tfidf,save2)
        return tfidf,vocabulary_tfidf