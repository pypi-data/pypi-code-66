# -*- coding: utf-8 -*-
import sys
# sys.path.append('./SVM/')
# sys.path.append('./utils/')
from sentiment_analysis.SVM.svm import *
from sentiment_analysis.utils.utils import *
from sentiment_analysis.utils.word2vec_utils import *
from sklearn.externals import joblib
import os


# setup
file_path = os.getcwd()
stopwords_file = os.path.join(file_path, 'data/stop_words.txt')
pca_model_file = os.path.join(file_path, 'SVM/model/2017-06-01~2017-08-03.pca')
svm_model_file = os.path.join(file_path, 'SVM/model/2017-06-01~2017-08-03.svm')
stopwords = load_stopwords(stopwords_file, encoding='utf-8')
wordvec_file = os.path.join(file_path, 'data/news.ten.zh.text.vector')
def load(wordvec_file, pca_model_file, svm_model_file):
	# doc2vec: average vector
	print('Loading word vectors...')
	model = load_wordvec(wordvec_file, binary=False)

	# load pca model
	pca_ = joblib.load(pca_model_file)

	# load svm model
	clf = joblib.load(svm_model_file)

	# label map
	label_map = {0: '负', 1: '非负'}
	return model, pca_, clf, label_map

def predict_one(data):
	model, pca_, clf, label_map = load(wordvec_file, pca_model_file, svm_model_file)
	data_cut = segment([data])
	X = buildVecs(data_cut, stopwords, model)
	X_reduced = pca_.transform(X)
	pred = clf.predict(X_reduced)
	pred_label = label_map[pred[0]]
	return pred_label
