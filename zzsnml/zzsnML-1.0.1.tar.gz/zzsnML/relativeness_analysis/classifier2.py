# -*- coding: utf-8 -*-
from __future__ import print_function
import xlrd
import numpy as np 
import scipy.sparse.csr
import scipy.sparse.csc
import pickle
# from gensim import models
import sys, os
from relativeness_analysis.utils import *
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.linear_model import SGDClassifier
from xgboost import XGBClassifier


class LogisticRegression(object):
	def __init__(self, label_dict, signature, learning_rate='optimal', penalty='l1', alpha=1e-3, eta0=0.0, class_weight='balanced', thres=0.5):
		self.label_dict = label_dict
		self.signature = signature
		self.lr = learning_rate
		self.penalty = penalty
		self.alpha = alpha
		self.eta0 = eta0
		self.class_weight = class_weight
		self.thres = thres
		self.loss = 'log'
		self.clf = None

	def set_signature(self, new_signature):
		self.signature = new_signature

	@staticmethod
	def train_test_split(X, Y, train_ratio=0.8):
		if not (isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray)):
			X = np.array(X, copy=False)
		N = X.shape[0]
		N_train = int(N*train_ratio)
		N_test = N - N_train
		assert N_train > 0 and N_test > 0, '训练集或测试集必须至少有一个样本'
		idx = np.random.permutation(N)
		return (X[idx[:N_train]], Y[idx[:N_train]]), (X[idx[N_train:]], Y[idx[N_train:]])

	def train(self, X, Y, save_to=None, initial_coef=None, initial_intercept=None, verbose=False):
		assert len(self.label_dict) == 2, 'It should have exactly two classes.'
		if isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray):
			data = X
		else:
			data = np.array(X, copy=False)
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			label = Y.todense()
		else:
			label = np.array(Y, copy=False)
		if len(np.unique(label)) == 1:
			print('Only contains one label, training stopped.')
			return

		# print('Training...')
		sgd = SGDClassifier(loss=self.loss, penalty=self.penalty, alpha=self.alpha, class_weight=self.class_weight, \
				learning_rate=self.lr, eta0=self.eta0, verbose=verbose)
		if initial_coef is None and initial_intercept is None:
			self.clf = sgd.fit(data, label, coef_init=initial_coef, intercept_init=initial_intercept)
		else:
			self.clf = sgd.fit(data, label)
		# print('Finished.')
		if save_to:
			# print('Saving model...')
			self.save(save_to)

	def save(self, save_to):
		file_name = save_to + ('-%s.lr' % self.signature)
		with open(file_name, 'wb') as f:
			pickle.dump((self.clf, self.label_dict, self.signature), f)

	@staticmethod
	def load(file_path):
		with open(file_path, 'rb') as f:
			clf, label_dict, signature = pickle.load(f)
		lr = LogisticRegression(label_dict, signature)
		lr.clf = clf
		return lr

	def predict(self, X, return_real_label=False):
		if not (isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray)):
			X = np.array(X, copy=False)
		if self.clf and X.shape[0] > 0:
			if len(X.shape) == 1:
				X = [X]
			prob = self.clf.predict_proba(X)
			label = np.ones((prob.shape[0],))
			label[prob[:,0] >= self.thres] = 0
			if return_real_label:
				return [self.label_dict[l] for l in label]
			else:
				return label
		else:
			if not self.clf:
				print('模型还没训练，请先训练模型')
			else:
				print('数据不能为空')

	def predict_proba(self, X):
		if not (isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray)):
			X = np.array(X, copy=False)
		if self.clf and X.shape[0] > 0:
			if len(X.shape) == 1:
				X = [X]
			prob = self.clf.predict_proba(X)
			return prob
		else:
			if not self.clf:
				print('模型还没训练，请先训练模型')
			else:
				print('数据不能为空')

	def report(self, X, Y, verbose=True):
		if not(isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray)):
			X = np.array(X, copy=False)
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			Y = Y.todense()
		else:
			Y = np.array(Y, copy=False)
		N = X.shape[0]
		assert len(Y) == N
		if not self.clf:
			print('模型还没训练，请先训练模型')
			return
		else:
			predicted_Y = self.predict(X)

		score = self.compute_score(Y, predicted_Y)
		recall = score['recall']
		precision = score['precision']
		F1 = score['F1']
		
		if verbose:
			for i in range(N):
				print('\tData id@%d, real label: %s, predicted label: %s' % \
						(i, self.label_dict[Y[i]], self.label_dict[predicted_Y[i]]))
		
		print('Correct rate: %s' % (np.mean(predicted_Y == Y)))

		for key in self.label_dict:
			print('Article num of label %s on training dataset: %s, recall: %.3f, precision: %.3f, F1: %.3f' % \
				(self.label_dict[key], np.sum(Y == key), recall[key], precision[key], F1[key]))

	def compute_score(self, Y, predicted_Y):
		recall = {}
		precision = {}
		F1 = {}
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			Y = Y.todense()
		else:
			Y = np.array(Y, copy=False)
		if isinstance(predicted_Y, scipy.sparse.csr.csr_matrix):
			predicted_Y = predicted_Y.todense()
		else:
			predicted_Y = np.array(predicted_Y, copy=False)
		for key in self.label_dict:
			N_key = np.sum(Y == key)
			if N_key == 0:
				recall[key] = 1.0
			else:
				recall[key] = np.sum((Y == key)*(predicted_Y == key))/(N_key+0.0)
			N_predicted_pos = np.sum(predicted_Y == key)
			if N_predicted_pos == 0:
				precision[key] = 1.0
			else:
				precision[key] = np.sum((Y == key)*(predicted_Y == key))/(N_predicted_pos+0.0)
			F1[key] = 2*recall[key]*precision[key]/(recall[key]+precision[key])

		return {'recall': recall, 'precision': precision, 'F1': F1}


class xgboost(object):
	def __init__(self, label_dict, signature, lr=0.1, reg_alpha=0, reg_lambda=1, objective='binary:logitraw', \
				with_sample_weight=True, subsample=1, min_child_weight=1, scale_pos_weight=1, thres=0.5):
		self.lr = lr
		self.label_dict = label_dict
		self.signature = signature
		self.reg_alpha = reg_alpha
		self.reg_lambda = reg_lambda
		self.objective = objective
		self.with_sample_weight = with_sample_weight
		self.min_child_weight = min_child_weight
		self.scale_pos_weight = scale_pos_weight
		self.thres = thres
		self.clf = None

	def set_signature(self, new_signature):
		self.signature = new_signature
	
	def train(self, X, Y, save_to=None):
		assert len(self.label_dict) == 2, 'It should have exactly two classes.'
		if isinstance(X, scipy.sparse.csr.csr_matrix):
			data = X.tocsc()
		elif isinstance(X, np.ndarray):
			data = X
		else:
			data = np.array(X, copy=False)
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			label = Y.todense()
		else:
			label = np.array(Y, copy=False)
		if len(np.unique(label)) == 1:
			print('Only contains one label, training stopped.')
			return

		N_0 = np.sum(label == 0)
		N_1 = np.sum(label == 1)
		w_0 = (N_0 + N_1) / (2. * N_0)
		w_1 = (N_0 + N_1) / (2. * N_1)
		# w_0 = w_0 * 1.3
		# w_1 = w_1 / 1.1
		# print(w_0, w_1)
		# print('Training...')
		self.clf = XGBClassifier(reg_alpha=self.reg_alpha, reg_lambda=self.reg_lambda, objective=self.objective, \
						min_child_weight=self.min_child_weight, scale_pos_weight=self.scale_pos_weight, learning_rate=self.lr)
		if self.with_sample_weight:
			self.clf.fit(data, label, sample_weight=[w_0 if l == 0 else w_1 for l in label])
		else:
			self.clf.fit(data, label)
		# print('Finished.')
		if save_to:
			# print('Saving model...')
			self.save(save_to)

	def save(self, save_to):
		file_name = save_to + ('-%s.xgb' % self.signature)
		with open(file_name, 'wb') as f:
			pickle.dump((self.clf, self.label_dict, self.signature), f)

	@staticmethod
	def load(file_path):
		with open(file_path, 'rb') as f:
			clf, label_dict, signature = pickle.load(f)
		xgb = xgboost(label_dict, signature)
		xgb.clf = clf
		return xgb

	def predict(self, X, return_real_label=False):
		prob = self.predict_proba(X)
		label = np.ones((prob.shape[0],))
		label[prob[:,0] >= self.thres] = 0
		if return_real_label:
			return [self.label_dict[l] for l in label]
		else:
			return label

	def predict_proba(self, X):
		if not (isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray) or isinstance(X, scipy.sparse.csc.csc_matrix)):
			X = np.array(X, copy=False)
		if isinstance(X, scipy.sparse.csr.csr_matrix):
			X = X.tocsc()
		if self.clf and X.shape[0] > 0:
			if len(X.shape) == 1:
				X = [X]
			prob = self.clf.predict_proba(X)
			return prob
		else:
			if not self.clf:
				print('模型还没训练，请先训练模型')
			else:
				print('数据不能为空')

	def report(self, X, Y, verbose=True):
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			Y = Y.todense()
		else:
			Y = np.array(Y, copy=False)
		N = X.shape[0]
		assert len(Y) == N
		if not self.clf:
			print('模型还没训练，请先训练模型')
			return
		else:
			predicted_Y = self.predict(X)

		score = self.compute_score(Y, predicted_Y)
		recall = score['recall']
		precision = score['precision']
		F1 = score['F1']
		
		if verbose:
			for i in range(N):
				print('\tData id@%d, real label: %s, predicted label: %s' % \
						(i, self.label_dict[Y[i]], self.label_dict[predicted_Y[i]]))
		
		print('Correct rate: %s' % (np.mean(predicted_Y == Y)))

		for key in self.label_dict:
			print('Article num of label %s on training dataset: %s, recall: %.3f, precision: %.3f, F1: %.3f' % \
				(self.label_dict[key], np.sum(Y == key), recall[key], precision[key], F1[key]))

	@staticmethod
	def train_test_split(X, Y, train_ratio=0.8):
		if not (isinstance(X, scipy.sparse.csr.csr_matrix) or isinstance(X, np.ndarray) or isinstance(X, scipy.sparse.csc.csc_matrix)):
			X = np.array(X, copy=False)
		N = X.shape[0]
		N_train = int(N*train_ratio)
		N_test = N - N_train
		assert N_train > 0 and N_test > 0, '训练集或测试集必须至少有一个样本'
		idx = np.random.permutation(N)
		return (X[idx[:N_train]], Y[idx[:N_train]]), (X[idx[N_train:]], Y[idx[N_train:]])

	def compute_score(self, Y, predicted_Y):
		recall = {}
		precision = {}
		F1 = {}
		if isinstance(Y, scipy.sparse.csr.csr_matrix):
			Y = Y.todense()
		else:
			Y = np.array(Y, copy=False)
		if isinstance(predicted_Y, scipy.sparse.csr.csr_matrix):
			predicted_Y = predicted_Y.todense()
		else:
			predicted_Y = np.array(predicted_Y, copy=False)
		for key in self.label_dict:
			N_key = np.sum(Y == key)
			if N_key == 0:
				recall[key] = 1.0
			else:
				recall[key] = np.sum((Y == key)*(predicted_Y == key))/(N_key+0.0)
			N_predicted_pos = np.sum(predicted_Y == key)
			if N_predicted_pos == 0:
				precision[key] = 1.0
			else:
				precision[key] = np.sum((Y == key)*(predicted_Y == key))/(N_predicted_pos+0.0)
			F1[key] = 2*recall[key]*precision[key]/(recall[key]+precision[key])

		return {'recall': recall, 'precision': precision, 'F1': F1}


def test():
	# file_path = 'D:\\学习\\研究生\\文本挖掘项目\\舆情正负面判别\\舆情标引信息-20170104.xlsx'  
	file_path = 'test.xlsx'
	idx_dict = {}
	idx_dict['content_begin_with'] = 1
	idx_dict['article_col'] = 1  # 内容在excel文件的哪一列(下标从0开始)
	idx_dict['title_col'] = 0  # 标题在excel的哪一列(下标从0开始)
	idx_dict['relativeness_col'] = 5  # 相关性在excel的哪一列(下标从0开始)
	idx_dict['topic_col'] = 4  # 企业在excel的哪一列(下标从0开始)

	vocab = Vocabulary(signature=123, name='vocab', min_word_len=2)
	dp = data_processor(file_path, config=idx_dict, for_test=False, transformer_norm='l2')
	processed_data, processed_label, processed_label_dict = dp.preprocess(_all=True)

	dp.update_vocab(vocab, processed_data)
	# # shuffle the vocabulary, this does not affect the results that much
	# dp.vocab.shuffle()
	transformed_data = dp.transform(vocab, processed_data)
	vocab.save('vocab')

	LR = LogisticRegression(label_dict=processed_label_dict['all'], signature=vocab.signature, thres=0.4)
	(X_train, Y_train), (X_test, Y_test) = LR.train_test_split(transformed_data['all'], processed_label['all'], train_ratio=0.8)
	LR.train(X_train, Y_train, save_to='test_clf')

	print('On training dataset:')
	LR.report(X_train, Y_train)
	print('On test dataset:')
	LR.report(X_test, Y_test)

	Y_test_predicted = LR.predict(X_test)
	print(LR.compute_score(Y_test, Y_test_predicted))

	print(LR.clf.coef_.shape, LR.clf.intercept_.shape)


if __name__ == '__main__':
	test()