# -*- coding: utf-8 -*-
from svm import *
import sys
sys.path.append('../../utils')
from augmentation_utils import *


'''
Currently, data augmentation makes result worse. Better augmentation method should be proposed.
'''


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
(X_cut_train, y_train), (X_cut_test, y_test) = train_test_split(data_cut, y)
X_train = buildVecs(X_cut_train, stopwords, model)
X_test = buildVecs(X_cut_test, stopwords, model)
N_train = len(y_train)


# load emotional dictionary
emotional_dict_file = '../../data/情感词典18级_1.pkl'
emotional_dict = load_emotion_dict(emotional_dict_file)

# data augmentation
X_aug, y_aug = avgvector_virtue_complementary_augmentation(X_cut_train, y_train, model, emotional_dict, \
						num_aug=10000, neg_aug_ratio=0.1, ratio=[0.2, 0.6, 0.2], min_virtue_sent_len=100)
X_train_combine = np.concatenate((X_train, X_aug), axis=0)
y_train_combine = np.concatenate((y_train, y_aug))
idx = np.random.permutation(X_train_combine.shape[0])
reverse_idx = np.argsort(idx)
X_train_combine = X_train_combine[idx]
y_train_combine = y_train_combine[idx]


# perform pca
print('Performing PCA...')
n_components = 100
pca_ = pca(n_components=n_components)
pca_.fit(X_train_combine)
pca_.save('model/%s~%s_comple_aug.pca' % (from_date, to_date))
print('%s components can explain %.2f%% variance.' % (n_components, pca_.ratio_*100))
X_reduced_train = pca_.transform(X_train_combine)
X_reduced_test = pca_.transform(X_test)

# train svm
print('Training SVM...')
clf = svm(C=2, probability=True)
clf.fit(X_reduced_train, y_train_combine)
clf.save('model/%s~%s_comple_aug.svm' % (from_date, to_date))

# score
y_pred_prob_train = clf.predict_proba(X_reduced_train[reverse_idx[:N_train]])
y_pred_prob_test = clf.predict_proba(X_reduced_test)
y_pred_train = y_pred_prob_train[:,0] < y_pred_prob_train[:,1]
y_pred_test = y_pred_prob_test[:,0] < y_pred_prob_test[:,1]
y_pred_train = y_pred_train.astype(np.int32)
y_pred_test = y_pred_test.astype(np.int32)
train_score = compute_score(y_train_combine[reverse_idx[:N_train]], y_pred_train, classes=[0, 1])
test_score = compute_score(y_test, y_pred_test, classes=[0, 1])

print_score(train_score, 'Train score of SVM classifier(+aug+PCA)')
print_score(test_score, 'Test score of SVM classifier(+aug+PCA)')

