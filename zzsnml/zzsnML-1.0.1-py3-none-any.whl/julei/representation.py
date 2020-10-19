# -*- coding: utf-8 -*-
"""
Created on Wed April 17 22:06:20 2019

@author: Wu-Daqing
"""
import time
import os
import pickle
import numpy as np
import gensim
from julei.tfidf import Tfidf
from julei.word2vec_train import Word2vec
class Representation:
    def __init__(self):
        pass

    def make_dir(self):
        if os.path.isdir('result/representation/') == False:
            os.makedirs(r'result/representation/')

    def load_pkl(self):
        with open('result/tfidf/tfidf.pkl','rb') as load1:
            tfidf = pickle.load(load1)
        with open('result/tfidf/vocabulary_tfidf.pkl','rb') as load2:
            vocabulary = pickle.load(load2)
        return tfidf,vocabulary

    def load_embedding(self):
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'开始导入腾讯公开中文词向量（200维）')
        file_path = os.path.dirname(os.path.realpath(__file__))
        path = os.path.join(file_path, 'data/Tencent_AILab_ChineseEmbedding.txt')
        model_tencent = gensim.models.KeyedVectors.load_word2vec_format(path, binary=False)
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'完成导入腾讯公开中文词向量（200维）')
        vocabulary_tencent = model_tencent.wv.vocab.keys()

        print(time.strftime('%Y-%m-%d %H:%M:%S'),'开始导入当前数据训练中文词向量（100维）')
        word2vector = Word2vec()
        model_w2v = word2vector.make_model()
        # model_w2v = gensim.models.Word2Vec.load('result/word2vec/wordvector_model')
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'完成导入当前数据训练中文词向量（100维）')
        vocabulary_w2v = model_w2v.wv.vocab.keys()
        return model_tencent,vocabulary_tencent,model_w2v,vocabulary_w2v

    def count_embedding(self):
        tfidf1 = Tfidf()
        tfidf,vocabulary = tfidf1.count_tfidf()
        # tfidf,vocabulary = self.load_pkl()
        model_tencent,vocabulary_tencent,model_w2v,vocabulary_w2v = self.load_embedding()
        num_data = tfidf.shape[0]
        V = tfidf.shape[1]
        vector_matrix = np.zeros((V,300))
        count = 0
        for word in vocabulary:
            if word in vocabulary_tencent:
                vector_tencent = model_tencent.wv.word_vec(word)
            else:
                vector_tencent = np.random.randn(200)
            if word in vocabulary_w2v:
                vector_w2v = model_w2v.wv.word_vec(word)
            else:
                vector_w2v = np.random.randn(100)
            vector = np.concatenate((vector_tencent,vector_w2v))
            vector_matrix[count] = vector
            count += 1
            if (count+1) % 10000 == 0:
                print(time.strftime('%Y-%m-%d %H:%M:%S'),'第',count,'个词向量计算完毕')
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'第',count,'个词向量计算完毕')
        self.make_dir()
        with open('result/representation/vector_matrix.pkl', 'wb') as save1:
            pickle.dump(vector_matrix, save1, protocol=4)
        return num_data,vector_matrix

    def text_represent(self):
        num_data,vector_matrix = self.count_embedding()
        print(num_data)
        tfidf,vocabulary = self.load_pkl()
        text_representation = np.zeros((num_data,300))
        for i in range(num_data):
            tmp = tfidf[i].toarray()
            weighted_average_vector = np.dot(tmp,vector_matrix)
            text_representation[i] = weighted_average_vector
            if (i+1)%10000 == 0 or (i+1) == num_data:
                print(time.strftime('%Y-%m-%d %H:%M:%S'),'第',i+1,'条文本表示计算完毕')
        with open('result/representation/text_representation.pkl','wb') as save2:
            pickle.dump(text_representation,save2,protocol=4)
        print(num_data)
        return text_representation
# rep = Representation()
# rep.text_represent()