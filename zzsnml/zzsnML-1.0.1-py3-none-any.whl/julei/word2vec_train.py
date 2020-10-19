# -*- coding: utf-8 -*-
"""
Created on Wed April 17 22:06:20 2019

@author: Wu-Daqing
"""
import os
import time
import logging
import gensim
from julei.segment import Segment
class Word2vec:
    def __init__(self):
        pass
    def make_model(self):

        logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
        text = gensim.models.word2vec.LineSentence('result/segment/data_segment.txt')
        model = gensim.models.word2vec.Word2Vec(sentences=text,size=100,window=5,min_count=5,workers=5,sg=0,iter=20)
        if os.path.isdir('result/word2vec/') == False:
            os.makedirs(r'result/word2vec/')
        model.save('result/word2vec/wordvector_model')
        return model
# word2vec = Word2vec()
# word2vec.make_model()