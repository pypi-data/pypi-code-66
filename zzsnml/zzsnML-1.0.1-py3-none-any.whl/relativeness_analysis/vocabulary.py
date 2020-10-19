# -*- coding: utf-8 -*-
import pickle
import numpy as np 


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


def test():
	x = ['哈哈', '测试', '嘿', '嗨', '早上好', '哈哈', '嘿', '下午好', '测试', '你好', 'test', 'c', 'm']
	voc = Vocabulary(signature=123, name='test', min_word_len=1)
	voc.update(x)
	print(voc.__class__.__name__)
	print(voc.get('哈哈'), voc.get('测试'))
	print(voc['早上好'], voc['c'])
	print(voc.__sizeof__())
	print('Voc size: %s' % voc.size)
	print('`c` in voc: %s, `哈哈` in voc: %s' % ('c' in voc, '哈哈' in voc))

	try:
		del voc['a']
		del voc['哈哈']
	except Exception as e:
		print(e)
	
	voc.clear()
	voc.update(x)
	voc.update(x)
	print(voc.voc)
	print(voc.freq)
	voc.save('voc_test.voc')
	voc = Vocabulary.load('voc_test.voc')
	print('Voc size: %s' % voc.size)
	print(voc.voc)
	print(voc.freq)
	print(voc.doc_freq)
	voc.shuffle()
	print(voc.voc)
	print(voc.freq)
	print(voc.doc_freq)


if __name__ == '__main__':
	test()