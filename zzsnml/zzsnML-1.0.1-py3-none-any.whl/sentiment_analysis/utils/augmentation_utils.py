# -*- coding: utf-8 -*-
from tfidf_utils import Vocabulary
import numpy as np
import time


def avgvector_virtue_augmentation(cut_data, label, model, emotion_dict, num_aug=10000, neg_aug_ratio=0.8, \
			ratio=[0.3, 0.5, 0.2], min_virtue_sent_len=10, max_virtue_sent_len=500):  
	'''ratio: [p1, p2, p3], p1: prob of words from related emotion dict; p2: prob of words from related vocab;
							p3: prob of words from opposite vocab.
	'''
	assert len(cut_data) == len(label)
	assert min_virtue_sent_len <= max_virtue_sent_len and min_virtue_sent_len >= 1

	signature = int(time.time())

	neg_vocab = Vocabulary(signature=signature, name='negative')
	pos_vocab = Vocabulary(signature=signature, name='positive')
	vocab_dict = {0: neg_vocab, 1: pos_vocab}  # label=0 stands for negative

	for i, d in enumerate(cut_data):
		vocab_dict[label[i]].update(d)

	emotion_dict_ = {'neg': [], 'pos': []}
	for word, strength in emotion_dict.items():
		if strength <= 0:
			emotion_dict_['neg'].append(word)
		else:
			emotion_dict_['pos'].append(word)


	num_neg = max(int(num_aug * neg_aug_ratio), 1)
	num_pos = max(num_aug - num_neg, 1)

	aug_data = []
	aug_label = []
	neg_words = list(neg_vocab.voc.keys())
	neg_words_prob = list(neg_vocab.voc.values())
	neg_words_prob = np.array(neg_words_prob) / np.sum(neg_words_prob)
	pos_words = list(pos_vocab.voc.keys())
	pos_words_prob = list(pos_vocab.voc.values())
	pos_words_prob = np.array(pos_words_prob) / np.sum(pos_words_prob)
	sents_len = np.random.randint(min_virtue_sent_len, max_virtue_sent_len, size=num_neg)
	for i in range(num_neg):
		d_ = []
		n_neg_related_vocab_words = int(ratio[1]*sents_len[i])
		n_neg_opposite_vocab_words = int(ratio[2]*sents_len[i])
		n_neg_emotion_words = sents_len[i] - n_neg_opposite_vocab_words - n_neg_related_vocab_words
		# words from emotion dict
		d_.extend(np.random.choice(emotion_dict_['neg'], replace=True, size=n_neg_emotion_words))
		# words from related vocab
		d_.extend(np.random.choice(neg_words, replace=True, p=neg_words_prob, size=n_neg_related_vocab_words))
		# words from opposite vocab
		d_.extend(np.random.choice(pos_words, replace=True, p=pos_words_prob, size=n_neg_opposite_vocab_words))
		vec_ = 0
		actual_len = 0.
		for word in d_:
			try:
				vec_ = vec_ + model[word]
				actual_len += 1
			except KeyError:
				continue
		if actual_len > 0:
			aug_data.append(vec_/actual_len)
			aug_label.append(0)

	sents_len = np.random.randint(min_virtue_sent_len, max_virtue_sent_len, size=num_pos)
	for i in range(num_pos):
		d_ = []
		n_pos_related_vocab_words = int(ratio[1]*sents_len[i])
		n_pos_opposite_vocab_words = int(ratio[2]*sents_len[i])
		n_pos_emotion_words = sents_len[i] - n_pos_opposite_vocab_words - n_pos_related_vocab_words
		# words from emotion dict
		d_.extend(np.random.choice(emotion_dict_['pos'], replace=True, size=n_pos_emotion_words))
		# words from related vocab
		d_.extend(np.random.choice(pos_words, replace=True, p=pos_words_prob, size=n_pos_related_vocab_words))
		# words from opposite vocab
		d_.extend(np.random.choice(neg_words, replace=True, p=neg_words_prob, size=n_pos_opposite_vocab_words))
		vec_ = 0
		actual_len = 0.
		for word in d_:
			try:
				vec_ = vec_ + model[word]
				actual_len += 1
			except KeyError:
				continue
		if actual_len > 0:
			aug_data.append(vec_/actual_len)
			aug_label.append(0)

	return aug_data, aug_label


def avgvector_virtue_complementary_augmentation(cut_data, label, model, emotion_dict, num_aug=10000, neg_aug_ratio=0.8, \
			ratio=[0.3, 0.5, 0.2], min_virtue_sent_len=10, max_virtue_sent_len=500):  
	'''ratio: [p1, p2, p3], p1: prob of words from opposite emotion dict; p2: prob of words from opposite vocab;
							p3: prob of words from related vocab.
	'''
	assert len(cut_data) == len(label)
	assert min_virtue_sent_len <= max_virtue_sent_len and min_virtue_sent_len >= 1

	signature = int(time.time())

	neg_vocab = Vocabulary(signature=signature, name='negative')
	pos_vocab = Vocabulary(signature=signature, name='positive')
	vocab_dict = {0: neg_vocab, 1: pos_vocab}  # label=0 stands for negative

	for i, d in enumerate(cut_data):
		vocab_dict[label[i]].update(d)

	emotion_dict_ = {'neg': [], 'pos': []}
	for word, strength in emotion_dict.items():
		if strength <= 0:
			emotion_dict_['neg'].append(word)
		else:
			emotion_dict_['pos'].append(word)


	num_neg = max(int(num_aug * neg_aug_ratio), 1)
	num_pos = max(num_aug - num_neg, 1)

	aug_data = []
	aug_label = []
	neg_words = list(neg_vocab.voc.keys())
	neg_words_prob = list(neg_vocab.voc.values())
	neg_words_prob = np.array(neg_words_prob) / np.sum(neg_words_prob)
	pos_words = list(pos_vocab.voc.keys())
	pos_words_prob = list(pos_vocab.voc.values())
	pos_words_prob = np.array(pos_words_prob) / np.sum(pos_words_prob)
	sents_len = np.random.randint(min_virtue_sent_len, max_virtue_sent_len, size=num_neg)
	for i in range(num_neg):
		d_ = []
		n_neg_opposite_vocab_words = int(ratio[1]*sents_len[i])
		n_neg_related_vocab_words = int(ratio[2]*sents_len[i])
		n_pos_emotion_words = sents_len[i] - n_neg_opposite_vocab_words - n_neg_related_vocab_words
		# words from emotion dict
		d_.extend(np.random.choice(emotion_dict_['pos'], replace=True, size=n_pos_emotion_words))
		# words from related vocab
		d_.extend(np.random.choice(neg_words, replace=True, p=neg_words_prob, size=n_neg_related_vocab_words))
		# words from opposite vocab
		d_.extend(np.random.choice(pos_words, replace=True, p=pos_words_prob, size=n_neg_opposite_vocab_words))
		vec_ = 0
		actual_len = 0.
		for word in d_:
			try:
				vec_ = vec_ + model[word]
				actual_len += 1
			except KeyError:
				continue
		if actual_len > 0:
			aug_data.append(vec_/actual_len)
			aug_label.append(2)  # new label: fake

	sents_len = np.random.randint(min_virtue_sent_len, max_virtue_sent_len, size=num_pos)
	for i in range(num_pos):
		d_ = []
		n_pos_opposite_vocab_words = int(ratio[1]*sents_len[i])
		n_pos_related_vocab_words = int(ratio[2]*sents_len[i])
		n_neg_emotion_words = sents_len[i] - n_pos_opposite_vocab_words - n_pos_related_vocab_words
		# words from emotion dict
		d_.extend(np.random.choice(emotion_dict_['neg'], replace=True, size=n_neg_emotion_words))
		# words from related vocab
		d_.extend(np.random.choice(pos_words, replace=True, p=pos_words_prob, size=n_pos_related_vocab_words))
		# words from opposite vocab
		d_.extend(np.random.choice(neg_words, replace=True, p=neg_words_prob, size=n_pos_opposite_vocab_words))
		vec_ = 0
		actual_len = 0.
		for word in d_:
			try:
				vec_ = vec_ + model[word]
				actual_len += 1
			except KeyError:
				continue
		if actual_len > 0:
			aug_data.append(vec_/actual_len)
			aug_label.append(2)  # new label: fake

	return aug_data, aug_label

