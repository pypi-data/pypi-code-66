# -*- coding: utf-8 -*-
import sys
# sys.path.append('../../utils')
from sentiment_analysis.utils.utils import *
from sentiment_analysis.utils.word2vec_utils import *
from sklearn.svm import SVC
from sklearn.externals import joblib
import os
import cx_Oracle
class svm():
	def __init__(self, label_dict=None, probability=True, C=5, kernel='rbf', degree=3, gamma='auto', coef0=0.0):
		self.label_dict = label_dict
		self.probability = probability
		self.C = C
		self.kernel = kernel
		self.degree = degree
		self.gamma = gamma
		self.coef0 = coef0
		self._svm = SVC(C=self.C, probability=self.probability, class_weight='balanced', kernel=self.kernel, \
						degree=self.degree, gamma=self.gamma, coef0=self.coef0)

	def fit(self, X, y):
		self._svm.fit(X, y)

	def predict(self, X, return_real_label=False):
		if return_real_label:
			assert self.label_dict is not None
			return [self.label_dict[p] for p in self._svm.predict(X)]
		return self._svm.predict(X)

	def predict_proba(self, X):
		if self.probability:
			return self._svm.predict_proba(X)
		else:
			raise ValueError('If you want to get the predict probability, fit svm with probability=True.')

	def save(self, save_to):
		joblib.dump(self._svm, save_to)


# if __name__ == '__main__':
	def train(connection_string = 'cis/cis_zzsn9988@114.116.91.1:1521/orcl', from_date = '2017-06-01', to_date = '2017-08-03'):
		# connection_string = 'cis/cis_zzsn9988@118.190.174.96:1521/orcl'
		wordvec_file = './data/news.ten.zh.text.vector'
		stopwords_file = './data/stop_words.txt'
		data_file = './data/%s~%s.pkl' % (from_date, to_date)
		if os.path.exists(data_file):
			data_cut, y = load_data_from_pickle(data_file)
		else:
			# connect database
			ora_conn = cx_Oracle.connect(connection_string)
			# fetch data
			data, y = fetch_data_from_oracle(ora_conn, from_date, to_date, label_map={'负': 0, '非负': 1})
			# cut data
			data_cut = segment(data)
			save_data([data_cut, y], data_file)

		# doc2vec: average vector
		print('Loading word vectors...')
		model = load_wordvec(wordvec_file, binary=False)
		stopwords = load_stopwords(stopwords_file, encoding='utf-8')
		X = buildVecs(data_cut, stopwords, model)
		(X_train, y_train), (X_test, y_test) = train_test_split(X, y)

		# perform pca
		print('Performing PCA...')
		dir_path = os.path.join(os.getcwd(),'./model')
		if not os.path.isdir(dir_path):
			os.makedirs(dir_path)
		n_components = 100
		pca_ = pca(n_components=n_components)
		pca_.fit(X_train)
		pca_.save('model/%s~%s.pca' % (from_date, to_date))
		print('%s components can explain %.2f%% variance.' % (n_components, pca_.ratio_*100))
		X_reduced_train = pca_.transform(X_train)
		X_reduced_test = pca_.transform(X_test)

		# train svm
		print('Training SVM...')
		clf = svm(C=5, probability=True)
		clf.fit(X_reduced_train, y_train)
		clf.save('model/%s~%s.svm' % (from_date, to_date))

		# score
		y_pred_train = clf.predict(X_reduced_train)
		y_pred_test = clf.predict(X_reduced_test)
		train_score = compute_score(y_train, y_pred_train, classes=[0, 1])
		test_score = compute_score(y_test, y_pred_test, classes=[0, 1])

		print_score(train_score, 'Train score of SVM classifier(+PCA)')
		print_score(test_score, 'Test score of SVM classifier(+PCA)')

