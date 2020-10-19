# -*- coding: utf-8 -*-
from gensim.models import word2vec, KeyedVectors
import numpy as np


def sent2word(segResult, stopwords):
	"""
	Segment a sentence to words
	Delete stopwords
	"""

	newSent = []
	for word in segResult:
		if word in stopwords:
			continue
		else:
			newSent.append(word)

	return newSent


def getWordVecs(wordList, model):
	vecs = []
	for word in wordList:
		word = word.replace('\n', '')
		try:
			vecs.append(model[word])
		except KeyError:
			continue
	# vecs = np.concatenate(vecs)
	return np.array(vecs, dtype = 'float')


def buildVecs(data, stopwords, model):
	posInput = []
	for line in data:
		line = sent2word(line, stopwords)
		resultList = getWordVecs(line, model)
		# for each sentence, the mean vector of all its vectors is used to represent this sentence
		if len(resultList) != 0:
			resultArray = sum(np.array(resultList))/len(resultList)
			posInput.append(resultArray)

	return posInput


def load_wordvec(wordvec_file, binary=False):
	# model = word2vec.Word2Vec.load_word2vec_format(wordvec_file, binary=binary)
	model = KeyedVectors.load_word2vec_format(wordvec_file, binary=binary)
	return model
