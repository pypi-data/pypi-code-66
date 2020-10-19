# -*- encoding: utf-8 -*-
import numpy as np
import jieba
import xlrd
import sys, time
import pickle
from relativeness_analysis.vocabulary import Vocabulary
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_selection import SelectFpr, mutual_info_classif, SelectPercentile
import scipy.linalg
from sklearn.base import BaseEstimator, TransformerMixin


class data_processor(object):
	def __init__(self, data, transformer='tf', transformer_norm='l2'):
		self.data = data
		transformer = transformer.lower()
		assert transformer in ['tf', 'tfidf']
		self.transformer_type = transformer
		self.transformer_norm = transformer_norm
		self.transformer = None
		# if not self.for_test:
		# 	if vocab is not None:
		# 		if type(vocab) == Vocabulary:
		# 			self.vocab = vocab
		# 			self.vocab.set_state(fixed=False)
		# 		else:
		# 			raise Exception('`vocab` should be of type `Vocabulary`.')
		# 	else:
		# 		self.vocab = Vocabulary(signature=int(time.time()), name='vocab')

	def reset(self):
		self.transformer = None
		self.cv = None

	def preprocess(self, _all=False, _emotion=False):
		processed_data = {}
		processed_label = {}
		processed_label_dict = {}
		label_set = ['保留', '删除']
		label_dict = {0: '保留', 1: '删除'}
		reverse_label_dict = {'保留': 0, '删除': 1}
		# only_have_one_label_key = []
		if _all:
			if not _emotion:  # _all=True, _emotion=False
				processed_data['all'] = []
				processed_label['all'] = []
				processed_label_dict['all'] = label_dict
				for key in self.data:
					# processed_data['all'] += [' '.join(jieba.lcut(record[0])) for record in data[key]]
					if len(processed_data.get('all')) == 0:
						processed_data['all'] = np.array([' '.join(jieba.lcut(record[0])) for record in self.data[key]])
					else:
						processed_data['all'] = np.hstack((processed_data['all'], [' '.join(jieba.lcut(record[0])) for record in self.data[key]]))
					label = [record[1] for record in self.data[key]]

					if len(processed_label.get('all')) == 0:
						processed_label['all'] = np.array([reverse_label_dict[l] for l in label])
					else:
						processed_label['all'] = np.hstack((processed_label['all'], [reverse_label_dict[l] for l in label]))
					# processed_label['all'] += [reverse_label_dict[l] for l in label]

			else:  # _all=True, _emotion=True
				processed_data['all-非负'] = []
				processed_data['all-负'] = []
				processed_label['all-非负'] = []
				processed_label['all-负'] = []
				processed_label_dict['all-非负'] = processed_label_dict['all-负'] = label_dict
				for key in self.data:
					if len(processed_data.get('all-非负')) == 0:
						processed_data['all-非负'] = np.array([' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='非负'])
						processed_label['all-非负'] = np.array([reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='非负'])
					else:
						processed_data['all-非负'] = np.hstack((processed_data['all-非负'], \
								[' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='非负']))
						processed_label['all-非负'] = np.hstack((processed_label['all-非负'], \
								[reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='非负']))
					if len(processed_data.get('all-负')) == 0:
						processed_data['all-负'] = np.array([' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='负'])
						processed_label['all-负'] = np.array([reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='负'])
					else:
						processed_data['all-负'] = np.hstack((processed_data['all-负'], \
								[' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='负']))
						processed_label['all-负'] = np.hstack((processed_label['all-负'], \
								[reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='负']))
					
		else:
			for key in self.data:
				if not _emotion:  # _all=False, _emotion=False
					processed_data[key] = [' '.join(jieba.lcut(record[0])) for record in self.data[key]]
					label = [record[1] for record in self.data[key]]
					# if len(set(label_set) - set(label)) != 0:
					# 	print('%s: Only have one label(%s)' % (key, label[0]))
					# 	only_have_one_label_key.append(key)

					# assert len(set(label_set) - set(label)) == 0, 'It should have exactly two classes.'
					# label_dict = {}
					# reverse_label_dict = {}
					# for i, k in enumerate(label_set):
					# 	label_dict[i] = k
					# 	reverse_label_dict[k] = i

					# processed_label[key] = [reverse_label_dict[l] for l in label]
					processed_label[key] = np.array([reverse_label_dict[l] for l in label])
					processed_label_dict[key] = label_dict
					processed_data[key] = np.array(processed_data[key])
				else:  # _all=False, _emotion=True
					processed_data[key+'-非负'] = np.array([' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='非负'])
					processed_data[key+'-负'] = np.array([' '.join(jieba.lcut(record[0])) for record in self.data[key] if record[2]=='负'])
					processed_label[key+'-非负'] = np.array([reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='非负'])
					processed_label[key+'-负'] = np.array([reverse_label_dict[record[1]] for record in self.data[key] if record[2]=='负'])
					processed_label_dict[key+'-非负'] = label_dict
					processed_label_dict[key+'-负'] = label_dict
				# processed_data[key] = processed_data[key]
			
		return processed_data, processed_label, processed_label_dict

	def update_vocab(self, vocab, processed_data):
		if type(processed_data) == dict:
			for key in processed_data:
				for record in processed_data[key]:
					vocab.update(record.split(' '))
		else:
			for record in processed_data:
				vocab.update(record.split(' '))
		assert vocab.check_state(), 'Something wrong with vocabulary.'

	def transform(self, vocab, data, label, with_feature_selection=False, feature_selection_method='FDA', binary=False):
		vocab.set_state(fixed=True)
		assert feature_selection_method in ['FDA', 'SelectPercentile']
		if not self.transformer:
			self.cv = CountVectorizer(decode_error='replace', vocabulary=vocab.to_dict(), binary=binary)
			if self.transformer_type == 'tf':
				self.transformer = TfidfTransformer(norm=self.transformer_norm, use_idf=False)
			else:
				self.transformer = TfidfTransformer(norm=self.transformer_norm, use_idf=True)
		if type(data) == dict:
			transformed_data = {}
			for key in data:
				if with_feature_selection:
					if feature_selection_method == 'FDA':
						transformed_data[key] = FDA().fit_transform(
															self.transformer.transform(self.cv.transform(data[key])), label[key]
														)
					else:
						transformed_data[key] = SelectPercentile(mutual_info_classif, 20).fit_transform(
															self.transformer.transform(self.cv.transform(data[key])), label[key]
														)
				else:
					transformed_data[key] = self.transformer.transform(self.cv.transform(data[key]))
		else:
			if with_feature_selection:
				if feature_selection_method == 'FDA':
					transformed_data = FDA().fit_transform(
															self.transformer.transform(self.cv.transform(data)), label
														)
				else:
					transformed_data = SelectPercentile(mutual_info_classif, 20).fit_transform(
															self.transformer.transform(self.cv.transform(data)), label
														)
			else:
				transformed_data = self.transformer.transform(self.cv.transform(data))
		return transformed_data


class FDA(BaseEstimator, TransformerMixin):

	def __init__(self, alpha=1e-4):
		'''Fisher discriminant analysis
		Arguments:
		----------
		alpha : float
			Regularization parameter
		'''

		self.alpha = alpha


	def fit(self, X, Y):
		'''Fit the LDA model
		Parameters
		----------
		X : array-like, shape [n_samples, n_features]
			Training data
		Y : array-like, shape [n_samples]
			Training labels
		Returns
		-------
		self : object
		'''
		

		n, d_orig           = X.shape
		classes             = np.unique(Y)

		assert(len(Y) == n)

		if isinstance(X, scipy.sparse.csr.csr_matrix):
			mean_global 	= X.mean(axis=0)
		else:
			mean_global     = np.mean(X, axis=0, keepdims=True)
		scatter_within      = self.alpha * np.eye(d_orig)
		scatter_between     = np.zeros_like(scatter_within)

		for c in classes:
			n_c             = np.sum(Y==c)
			if n_c < 2:
				continue
			if isinstance(X, scipy.sparse.csr.csr_matrix):
				mu_diff 	= X[Y==c].mean(axis=0) - mean_global
			else:
				mu_diff     = np.mean(X[Y==c], axis=0, keepdims=True) - mean_global
			scatter_between = scatter_between + n_c * np.dot(mu_diff.T, mu_diff)
			if isinstance(X, scipy.sparse.csr.csr_matrix):
				scatter_within  = scatter_within  + n_c * np.cov(X[Y==c].todense(), rowvar=0)
			else:
				scatter_within  = scatter_within  + n_c * np.cov(X[Y==c], rowvar=0)

		e_vals, e_vecs      = scipy.linalg.eig(scatter_between, scatter_within)

		self.e_vals_        = e_vals
		self.e_vecs_        = e_vecs
		
		self.components_    = e_vecs.T

		return self

	def transform(self, X):
		'''Transform data by FDA
		Parameters
		----------
		X : array-like, shape [n_samples, n_features]
			Data to be transformed
		Returns
		-------
		X_new : array, shape (n_samples, n_atoms)
		'''

		return X.dot(self.components_.T)

	def fit_transform(self, X, Y):
		self.fit(X, Y)
		return self.transform(X)


def test():
	# file_path = 'D:\\学习\\研究生\\文本挖掘项目\\舆情正负面判别\\舆情标引信息-20170104.xlsx'
	file_path = 'test.xlsx'
	idx_dict = {}
	idx_dict['content_begin_with'] = 1
	idx_dict['article_col'] = 1  # 内容在excel文件的哪一列(下标从0开始)
	idx_dict['title_col'] = 0  # 标题在excel的哪一列(下标从0开始)
	idx_dict['relativeness_col'] = 5  # 相关性在excel的哪一列(下标从0开始)
	idx_dict['topic_col'] = 4  # 企业在excel的哪一列(下标从0开始)

	vocab = Vocabulary(signature=123, name='test', min_word_len=2)
	dp = data_processor(file_path, config=idx_dict, for_test=False)
	processed_data, processed_label, processed_label_dict = dp.preprocess(_all=True)
	dp.update_vocab(vocab, processed_data)
	print(vocab.get_size())
	for i, word in enumerate(vocab):
		if i < 20:
			id = vocab[word]
			print('[%s] id: %s, freq: %s, doc_freq: %s' % (word, id, vocab.freq[id], vocab.doc_freq[id]))
		else:
			break
	vocab.save('vocab')

	transformed_data = dp.transform(vocab, processed_data['all'])
	print(transformed_data.shape)


if __name__ == '__main__':
	test()