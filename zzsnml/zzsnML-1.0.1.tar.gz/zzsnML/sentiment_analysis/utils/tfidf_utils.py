# -*- coding: utf-8 -*-
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer


class Vocabulary(object):
	def __init__(self, signature, min_word_len=2, name='voc'):
		self.signature = signature
		self.min_word_len = min_word_len
		self.name = name
		self.voc = dict()
		self.freq = dict()
		self.doc_freq = dict()
		self.oov = None
		self.size = 0
		self._fixed_voc = False

	def set_state(self, fixed=False):
		assert fixed in [True, False, 0, 1]
		self._fixed_voc = fixed

	def get_state(self):
		state = 'Fixed' if self._fixed_voc else 'Not fixed'
		return state

	def shuffle(self):
		self.check_state()
		idx = np.random.permutation(self.size)
		shuffled_voc = dict()
		shuffled_freq = dict()
		shuffled_doc_freq = dict()
		for key, id in self.voc.items():
			shuffled_voc[key] = idx[id]
			shuffled_freq[idx[id]] = self.freq[id]
			shuffled_doc_freq[idx[id]] = self.doc_freq[id]
		del self.voc, self.freq, self.doc_freq
		self.voc, self.freq, self.doc_freq = shuffled_voc, shuffled_freq, shuffled_doc_freq

	def _is_useless(self, x):
		if len(x) < self.min_word_len:
			return True
		if x.strip('''#&$_%^*-+=<>`~!@(（）)?？/\\[]{}—"';:：；，。,.‘’“”|…\n abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890''') == '':
			return True
		return False

	def update(self, words):
		if self._fixed_voc:
			raise Exception('Fixed vocabulary does not support update.')
		for word in words:
			if not self._is_useless(word):
				id = self.voc.get(word, None)
				if id is None:  # new word
					self.voc[word] = self.size
					self.freq[self.size] = 1
					self.doc_freq[self.size] = 0  # create doc_freq item
					self.size += 1
				else:
					self.freq[id] += 1
		for word in set(words): 
			if not self._is_useless(word):
				id = self.voc.get(word, None)
				if id is not None:
					self.doc_freq[id] += 1  # update doc_freq

	def get(self, word):
		return self.voc.get(word, self.oov)

	def __getitem__(self, word):
		return self.voc.get(word, self.oov)

	# def __setitem__(self, word, val):
	# 	self.voc.__setitem__(word, val)

	def __contains__(self, word):
		return self.voc.__contains__(word)

	def __iter__(self):
		return iter(self.voc)

	def __sizeof__(self):
		return self.voc.__sizeof__() + self.freq.__sizeof__() + self.signature.__sizeof__() + self.size.__sizeof__() + \
				self.name.__sizeof__() + self._fixed_voc.__sizeof__() + self.oov.__sizeof__() + self.doc_freq.__sizeof__()

	def __delitem__(self, word):  # delete would destory the inner representation
		if self._fixed_voc:
			raise Exception('Fixed vocabulary does not support deletion.')
		else:
			raise NotImplementedError

	def get_size(self):
		return self.size

	def clear(self):
		del self.voc, self.freq, self.doc_freq
		self.voc = dict()
		self.freq = dict()
		self.doc_freq = dict()
		self.size = 0
		self._fixed_voc = False

	def check_state(self):
		return len(self.voc) == self.size and len(self.freq) == self.size and len(self.doc_freq) == self.size

	def to_dict(self):
		return self.voc

	def set_signature(self, new_signature):
		self.signature = new_signature

	def remove(self, words_list):
		size = 0
		new_voc = {}
		new_freq = {}
		new_doc_freq = {}
		for word in self.voc:
			id = self.voc[word]
			if word in words_list:
				continue
			else:
				new_voc[word] = size
				new_freq[size] = self.freq[id]
				new_doc_freq[size] = self.doc_freq[id]
				size += 1
		self.size = size
		self.voc = new_voc
		self.freq = new_freq
		self.doc_freq = new_doc_freq


	def save(self, file_name=None):
		save_to = (file_name if file_name else self.name)+'-%s.voc'%self.signature
		with open(save_to, 'wb') as f:
			pickle.dump([self.voc, self.freq, self.doc_freq, self.size, self.min_word_len, \
				self.oov, self._fixed_voc, self.name, self.signature], f)

	@classmethod
	def load(cls, file_name):
		with open(file_name, 'rb') as f:
			[voc, freq, doc_freq, size, min_word_len, oov, _fixed, name, signature] = pickle.load(f)
		
		voc_from_file = cls(signature, name)
		voc_from_file.voc = voc
		voc_from_file.freq = freq
		voc_from_file.doc_freq = doc_freq
		voc_from_file.size = size
		voc_from_file.min_word_len = min_word_len
		voc_from_file.oov = oov
		voc_from_file._fixed_voc = _fixed
		voc_from_file.signature = signature
		return voc_from_file


class TfidfTransf():
	def __init__(self, signature, vocab=None, transformer_type='tfidf', transformer_norm='l2', vocab_name='vocab', min_word_len=2):
		self._type = transformer_type.lower()
		self._norm = transformer_norm.lower()
		self.signature = signature
		self.vocab_name = vocab_name
		self.min_word_len = min_word_len
		self.cv = None
		self.transformer = None
		if vocab:
			if isinstance(vocab, Vocabulary):
				self.vocab = vocab
			else:
				raise TypeError('Vocab needs input of type `Vocabulary`, but got %s.' % (type(vocab)))
		else:
			self.vocab = Vocabulary(signature, name=self.vocab_name, min_word_len=self.min_word_len)
	
	def update_vocab(self, data):
		for doc in data:
			self.vocab.update(doc)

	def set_state(self, fixed=False):
		self.vocab.set_state(fixed=fixed)
	
	def remove_from_vocab(self, words_or_vocab):
		self.vocab.remove(words_or_vocab)

	def fit(self, data):
		if self.vocab.get_size() == 0:
			print('Warning: Vocabulary is not yet built. It would built on this data.' + \
				' If this is what you want, please update vocab first.')
			self.update_vocab(data)

		self.vocab.set_state(fixed=True)
		self.cv = CountVectorizer(decode_error='replace', vocabulary=self.vocab.to_dict())
		if self._type == 'tf':
			self.transformer = TfidfTransformer(norm=self._norm, use_idf=False)
		else:
			self.transformer = TfidfTransformer(norm=self._norm, use_idf=True)
		
		return self.transformer.fit(self.cv.transform(data))

	def transform(self, data):
		if self.transformer and self.cv:
			return self.transformer.transform(self.cv.transform(data))
		else:
			print('Warning: The transformer has not yet been fitted. It would fit on this data.' + \
				'If this is not you want, please fit it first.')
			self.fit(data)
			return self.transform(data)

	def save(self, save_to):
		joblib.dump([self.vocab, self.cv, self.transformer], save_to)

	@staticmethod
	def load(cls, model_file):
		vocab, cv, transformer = joblib.load(f)
		model = cls(signature=vocab.signature, vocab=vocab)
		model.cv = cv
		model.transformer = transformer
		return model
