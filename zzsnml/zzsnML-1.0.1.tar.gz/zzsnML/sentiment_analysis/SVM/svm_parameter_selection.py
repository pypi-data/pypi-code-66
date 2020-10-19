# -*- coding: utf-8 -*-
import sys
sys.path.append('../../utils')
from utils import *
from word2vec_utils import *
from sklearn.svm import SVC
import os
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report


connection_string = 'cis/cis_zzsn9988@118.190.174.96:1521/orcl'
from_date = '2017-06-01'
to_date = '2017-08-03'
wordvec_file = '../../data/news.ten.zh.text.vector'
stopwords_file = '../../data/stop_words.txt'
data_file = '../../data/%s~%s.pkl' % (from_date, to_date)

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
n_components = 100
pca_ = pca(n_components=n_components)
pca_.fit(X_train)
# pca_.save('%s~%s.pca' % (from_date, to_date))
print('%s components can explain %.2f%% variance.' % (n_components, pca_.ratio_*100))
X_reduced_train = pca_.transform(X_train)
X_reduced_test = pca_.transform(X_test)

# train svm
# param_grid = [
#   {'C': [1, 10, 100, 1000], 'kernel': ['linear'], 'class_weight': ['balanced', None], 'probability': [True]},
#   {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001, 'auto'], 'kernel': ['rbf'], 'class_weight': ['balanced', None], 'probability': [True]},
#   {'C': [1, 10, 100, 1000], 'gamma': [0.001, 0.0001, 'auto'], 'kernel': ['sigmoid'], 'class_weight': ['balanced', None], 'probability': [True]},
#   {'C': [1, 10, 100, 1000], 'degree': [2, 3, 4], 'kernel': ['poly'], 'class_weight': ['balanced', None], 'probability': [True]}
#  ]
param_grid = [
  {'C': [5, 10, 20, 30], 'kernel': ['linear'], 'class_weight': ['balanced', None]},
  {'C': [5, 10, 20, 30], 'gamma': [0.001, 0.0001, 'auto'], 'kernel': ['rbf'], 'class_weight': ['balanced', None]},
  {'C': [5, 10, 20, 30], 'gamma': [0.001, 0.0001, 'auto'], 'kernel': ['sigmoid'], 'class_weight': ['balanced', None]},
  {'C': [5, 10, 20, 30], 'degree': [2, 3, 4], 'kernel': ['poly'], 'class_weight': ['balanced', None]}
 ]
print('Training SVM...')

scores = ['precision', 'recall', 'f1']

for score in scores:
	print("# Tuning hyper-parameters for %s" % score)
	print()

	clf = GridSearchCV(SVC(), param_grid, cv=5, n_jobs=5,
					   scoring='%s_macro' % score)
	clf.fit(X_reduced_train, y_train)

	print("Best parameters set found on development set:")
	print()
	print(clf.best_params_)
	print()
	print("Grid scores on development set:")
	print()
	means = clf.cv_results_['mean_test_score']
	stds = clf.cv_results_['std_test_score']
	for mean, std, params in zip(means, stds, clf.cv_results_['params']):
		print("%0.3f (+/-%0.03f) for %r"
			  % (mean, std * 2, params))
	print()

	print("Detailed classification report:")
	print()
	print("The model is trained on the full development set.")
	print("The scores are computed on the full evaluation set.")
	print()
	y_true, y_pred = y_test, clf.predict(X_reduced_test)
	print(classification_report(y_true, y_pred))
	print()
