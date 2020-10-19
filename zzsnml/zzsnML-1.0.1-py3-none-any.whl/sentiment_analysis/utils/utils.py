# -*- coding: utf-8 -*-
import pickle, os
from gensim.models import word2vec, KeyedVectors
import numpy as np
from sklearn.decomposition import PCA
from sklearn.externals import joblib
import jieba
import cx_Oracle
os.environ['NLS_LANG'] = 'SIMPLIFIED CHINESE_CHINA.UTF8'


_backend = 'jieba'
try:
	from jpype import *
	startJVM(getDefaultJVMPath(), "-Djava.class.path=/home/hongjp/hanlp/hanlp-portable-1.3.4.jar:/home/hongjp/hanlp", "-Xms1g", "-Xmx1g") # 启动JVM，Linux需替换分号;为冒号:
	HanLP = JClass('com.hankcs.hanlp.HanLP')
	_backend = 'hanlp'
	print('Using HanLP as Chinese sentence segmentation backend.')
except Exception as e:
	print('Fail to load `HanLP`. Using `jieba` as default Chinese sentence segmentation backend.')


def load_data_from_excel(excel_file, config):
	pass


def load_data_from_pickle(pickle_file):
	with open(pickle_file, 'rb') as f:
		data = pickle.load(f)
	return data


def load_stopwords(sw_file, encoding='utf-8'):
	with open(sw_file, 'r', encoding=encoding) as f:
		stopwords = f.read().strip().split('\n')
	return stopwords


def load_emotion_dict(emotion_dict_file):
	return load_data_from_pickle(emotion_dict_file)


def segment(data):
	def hanlp_cut(d):
		cut = HanLP.segment(d)
		t = [cut[i].word for i in range(len(cut))]
		return t

	if _backend == 'jieba':
		return [jieba.lcut(d) for d in data]
	else:  # _backend = 'hanlp'
		return [hanlp_cut(d) for d in data]


def train_test_split(X, y, ratio=0.8):
	X = np.array(X, copy=False)
	y = np.array(y, copy=False)
	assert X.shape[0] == len(y)
	N = X.shape[0]
	N_train = int(N * ratio)
	idx = np.arange(N)
	np.random.shuffle(idx)
	X_train = X[idx[:N_train]]
	X_test = X[idx[N_train:]]
	y_train = y[idx[:N_train]]
	y_test = y[idx[N_train:]]
	return (X_train, y_train), (X_test, y_test)


def compute_score(Y, predicted_Y, classes=[0, 1]):
	recall = {}
	precision = {}
	F1 = {}
	Y = np.array(Y, copy=False)
	predicted_Y = np.array(predicted_Y, copy=False)
	for key in classes:
		N_key = np.sum(Y == key)
		if N_key == 0:
			recall[key] = 0.0
		else:
			recall[key] = np.sum((Y == key)*(predicted_Y == key))/(N_key+0.0)
		N_predicted_pos = np.sum(predicted_Y == key)
		if N_predicted_pos == 0:
			precision[key] = 0.0
		else:
			precision[key] = np.sum((Y == key)*(predicted_Y == key))/(N_predicted_pos+0.0)
		F1[key] = 2*recall[key]*precision[key]/(recall[key]+precision[key])

	return {'recall': recall, 'precision': precision, 'F1': F1}


def print_score(score, title=None):
	if title:
		print('='*53)
		# print('|' + ' '*51 + '|')
		print('|{:^51s}|'.format(title[:51]))
		# print('|' + ' '*51 + '|')

	print('='*53)
	print('|{:^12s}|{:^12s}|{:^12s}|{:^12s}|'.format('class', 'recall', 'precision', 'F1'))
	for label in score['recall']:
		print('|{:^12s}|{:^12s}|{:^12s}|{:^12s}|'.format(
				str(label), '%.2f'%score['recall'][label], '%.2f'%score['precision'][label], '%.2f'%score['F1'][label]))
	print('='*53)


def print_multi_scores(score_list, title=None):
	N = len(score_list)
	assert N > 1  # when N=1, use print_score instead, otherwise, alignment might be troublesome, for len('precision') > 6.
	length = 12 + 5 + 6*N*3 + 2*3  # class_col + `|`*5 + score_col*N*3 + `/`*2*3
	if title:
		print('='*length)
		print(('|{:^%ds}|'%(length-2)).format(title[:length]))

	print('='*length)
	format_ = '|{:^12s}|' + ('{:^6s}/'*(N-1) + '{:^6s}|') * 3
	col_title_format = '|{:^12s}|' + '{:^%ds}|'%(N*6+2) * 3
	print(col_title_format.format('class', 'recall', 'precision', 'F1'))
	
	for label in score_list[0]['recall']:
		data = [str(label)]
		for obj in ['recall', 'precision', 'F1']:
			for score in score_list:
				data.append('%.2f'%score[obj][label])
		print(format_.format(*data))
	print('='*length)


class pca():
	def __init__(self, n_components=100):
		self.n_components = n_components
		self._pca = PCA(n_components=self.n_components)
		self._is_fitted = False

	def fit(self, X):
		self._pca.fit(X)
		self._is_fitted = True
		self.explained_variance_ratio_ = self._pca.explained_variance_ratio_
		self.ratio_ = np.sum(self.explained_variance_ratio_[:self.n_components])
	
	def transform(self, X):
		if self._is_fitted:
			return self._pca.transform(X)
		else:
			print('PCA has not yet been fitted. It would perform fitting on this data. ' + \
					'If this is not what you want, check your code, and fit the model first.')
			return self._pca.fit_transform(X)

	def save(self, save_to):
		joblib.dump(self._pca, save_to)

	# @staticmethod
	# def load(model_file):
	# 	_pca = joblib.load(model_file)
	# 	pca_ = pca(n_components=_pca.n_components_)
	# 	pca_._pca = _pca
	# 	pca_._is_fitted = True
	# 	pca_.explained_variance_ratio_ = _pca.explained_variance_ratio_
	# 	pca_.ratio_ = np.sum(pca_.explained_variance_ratio_[:pca_.n_components])
	# 	return pca_



def fetch_data_from_oracle(connection, from_date, to_date, label_map=None):
	print('Fetching data from remote oracle, this might take some time...')

	query = '''select b.title,b.content_no_tag,b.orientation as relevance from cis_ans_basedata b inner join cis_ans_basedata_type t on  (b.id=t.bid and t.delflag = 0 and (t.repeat=0 or t.repeat is null)) 
where B.Publish_Date > '%s' and B.Publish_Date < '%s' ''' % (from_date, to_date)
	cursor = connection.cursor()
	cursor.execute(query)
	data = []
	label = []

	def convert(col):
		if isinstance(col, cx_Oracle.LOB):
			return col.read().decode('utf-8')
		else:
			return col

	for i, record in enumerate(cursor):
		if i % 1000 == 0:
			print('.', end='', flush=True)
		title = convert(record[0])
		article = convert(record[1])
		emotion = convert(record[2])
		if article is None:
			continue
		else:
			if emotion is None:
				emotion = 1
			if title is not None:
				title = title.strip()
			else:
				title = ''
			article = article.strip()
		emotion = '负' if emotion == '2' else '非负'
		if label_map:
			emotion = label_map[emotion]  # for example, convert '负', '非负' to 0, 1 respectively
		
		data.append(title+'。'+article)
		label.append(emotion)
	connection.close()
	print('.')
	return data, label


def save_data(data, save_to_file):
	with open(save_to_file, 'wb') as f:
		pickle.dump(data, f)
