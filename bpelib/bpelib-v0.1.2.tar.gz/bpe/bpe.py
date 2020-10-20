import os
import re
import pickle
import collections
import numpy as np
from tqdm import tqdm
from typing import List, Tuple, Dict, Iterable
from abc import ABC, abstractmethod, abstractproperty
try:
    import bpelib.bpe.libc as bpelibc
except ImportError as import_error:
    print(import_error)
    print("Continuing without c libraries ...")
    bpelibc = None


class WordFreq(Dict[bytes, int]):
    def merge_pair(self, pair: Tuple[bytes, bytes]) -> None:
        """
        Merges the most frequent pair (or any, for that matter) into the provided word-freq dictionary.

        :param pair: the most frequent 'byte pair' in the dictionary
        :return: the merged word-freq dictionary
        """

        # create a valid regular expression from the provided most-frequent-pair
        bigrams = re.escape(b' '.join(pair))
        # create a regex object with negative lookbehind and lookahead around our regex string
        # no non-space character is allowed to precede or follow our regex string
        p = re.compile(rb'(?<!\S)' + bigrams + rb'(?!\S)')

        for word in self.copy():
            if p.search(word):
                w_out = p.sub(b''.join(pair), word)
                self[w_out] = self.pop(word)


class _BPE_template(ABC):
    """
    Template class for Byte Pair Encoder

    Learns to encode any given word, to a series of learned substrings.

    Note: do not use this class directly
    """
    # there should not be any unknown bytes
    __all_bytes: Dict[bytes, int] = {bytes([i]): i for i in range(256)}
    # whether to show the learning process or not
    mute = False

    @staticmethod
    def all_bytes() -> Dict[bytes, int]:
        return _BPE_template.__all_bytes.copy()

    def __eq__(self, other: '_BPE_template'):
        if not isinstance(other, _BPE_template):
            return False

        return (self._vocab == other._vocab and self._merges == other._merges and
                self._vocab_size == other._vocab_size and self._eow == other._eow and self._sow == other._sow)

    @abstractmethod
    def __call__(self, *args, **kwargs): ...

    def _vocab_add(self, item: bytes) -> None:
        """
        Adds a key to the internal vocabulary, with incrementing integer value.

        :param item: the item to add to the vocabulary
        """
        if item not in self._vocab:
            self._vocab[item] = self._vocab_size
            self._vocab_size += 1

    def init(self) -> None:
        """
        Initialize or reinitialize the learned merge operations and vocabulary.
        """

        # initialize the vocabulary
        self._vocab = BPE.all_bytes()
        self._vocab_size = len(self._vocab)
        self._vocab_add(self._sow)
        self._vocab_add(self._eow)
        # initialize the dictionary containing the merge operations
        self._merges: Dict[Tuple[bytes, bytes], int] = dict()

    def _learn_encoding_impl(self, corpus: Iterable[bytes], max_vocab_size: int):
        # returns frequency of each word
        self._word_freq = collections.Counter(corpus)
        # convert word_freq object to dictionary
        self._word_freq = WordFreq(self._word_freq)

        max_it_num = max_vocab_size - 258
        iterator = tqdm(range(max_it_num),
                        desc='Learning BPE ...', ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute)

        for i in iterator:
            # compute frequency of bigrams in a corpus
            pairs = BPE._make_pairs(self._word_freq)

            # no more byte pairs found -> end loop
            if not pairs:
                iterator.n = max_it_num
                iterator.close()
                break

            # compute the best pair
            best = max(pairs, key=pairs.get)

            # merge the most frequent pair in corpus
            self._word_freq.merge_pair(best)

            # append to merge dict
            self._merges[best] = i
            # convert a tuple to a string, then append to vocabulary
            new_byte = b''.join(best)
            self._vocab_add(new_byte)

    @staticmethod
    def _make_pairs(word_freq: WordFreq) -> Dict[Tuple[bytes, bytes], int]:
        """
        Computes frequency of a pair of characters or character sequences.

        :param word_freq: dictionary containing each word and its frequencies
        :return: frequency of each pair
        """

        # any unknown key defaults to 'calling int()', so basically it is zero
        pairs = collections.defaultdict(int)

        # iterate all word frequency dictionary items
        for word, freq in word_freq.items():
            # unique symbols in a word
            symbols = word.split()

            # counting pairs
            for i in range(len(symbols) - 1):
                pairs[symbols[i], symbols[i + 1]] += freq

        return pairs

    @abstractmethod
    def encode(self, word): ...

    @abstractmethod
    def decode(self, word): ...

    def save(self, directory: str = './') -> None:
        """
        Saves vocabulary and merge operations to a specified folder.

        :param directory: the folder to save the BPE data
        """

        # extract subdirectory names
        directory = os.path.abspath(directory)
        sub_dirs = directory.split(os.path.sep)

        # create the subdirectories as needed
        cdir = ''
        for sub in sub_dirs:
            cdir += sub + os.path.sep

            if not os.path.isdir(cdir):
                os.mkdir(cdir)

        # save the files
        pickle.dump(self._vocab, open(directory + os.path.sep + '__vocab__', 'wb'), pickle.HIGHEST_PROTOCOL)
        pickle.dump(self._merges, open(directory + os.path.sep + '__merges__', 'wb'), pickle.HIGHEST_PROTOCOL)

    def load(self, directory: str) -> None:
        """
        Loads the vocabulary and the learned merge operations based on previous model.

        :param directory: the folder where we last saved our data
        """

        self._vocab = pickle.load(open(directory + os.path.sep + '__vocab__', 'rb'))
        self._merges = pickle.load(open(directory + os.path.sep + '__merges__', 'rb'))
        self._vocab_size = len(self._vocab)

    @property
    def vocab(self): ...

    @property
    def merges(self): ...

    @property
    def sow(self): ...

    @property
    def eow(self): ...


class BPE(_BPE_template):
    """
    Byte Pair Encoder class for string inputs

    Learns to encode any given word, to a series of learned substrings.
    """

    def __call__(self, word: str, encode: bool = None, encoding: str = None) -> str:
        # try guessing what we want (a very basic guess based on sow and eow tokens)
        if encode is None:
            # get or set encoding
            encoding = encoding if encoding else self._enc

            # try finding Start or End Of Word token
            if word.find(self._sow.decode(encoding)) < 0 or word.find(self._eow.decode(encoding)) < 0:
                return self.encode(word, encoding)
            else:
                return self.decode(word, encoding)

        if encode:
            return self.encode(word, encoding)
        else:
            return self.decode(word, encoding)

    def __init__(self,
                 corpus: Iterable[str] = None,
                 max_vocab_size: int = 4096,
                 sow: str = '<w/>',
                 eow: str = '</w>',
                 encoding: str = 'utf8'
                 ):
        """
        Constructor of Byte Pair Encoding class, will start learning bpe if corpus is provided.

        :param corpus: a list of tokens or words
        :param max_vocab_size: allowed dictionary size
        :param sow: start of word token
        :param eow: end of word token
        :param encoding: the encoding of the corpus, or the text to be learned
        """

        self._max_vocab_size = max_vocab_size
        self._sow = bytes(sow, encoding=encoding)
        self._eow = bytes(eow, encoding=encoding)
        self._enc = encoding
        self._word_freq = None

        self._vocab: Dict[bytes, int] = dict()
        self._vocab_size: int = 0
        self._merges: Dict[Tuple[bytes, bytes], int] = dict()
        self.init()

        if corpus:
            # learn the byte pair encoding
            self.learn_encoding(corpus, max_vocab_size, encoding)

    def learn_encoding(self,
                       corpus: Iterable[str],
                       max_vocab_size: int = None,
                       encoding: str = None
                       ):
        """
        Starts the learning of byte pair encodings in a given corpus.

        :param corpus: a list of tokens or words
        :param max_vocab_size: allowed dictionary size
        :param encoding: the encoding of the corpus, or the text to be learned
        """

        # get or set encoding
        encoding = encoding if encoding else self._enc
        # get or set the maximum size of the vocabulary and bpe merges
        max_vocab_size = max_vocab_size if max_vocab_size else self._max_vocab_size

        # split the word into characters, string is iterable so it can be further 'joined' with spaces
        # also appends End Of Word token at the end of each token
        b_corpus = [bytes(token, encoding=encoding) for token in tqdm(
            corpus, desc='Conversion to bytes ...', ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute
        )]

        if bpelibc:
            iterator_obj = tqdm(b_corpus, desc='Splitting bytes ...',
                                ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute)
            b_corpus = bpelibc.split_bytes_in_iterable_and_add_boundary(iterator_obj, self._sow, self._eow)
        else:
            b_corpus = [
                self._sow + b' ' +
                b' '.join(np.frombuffer(token, dtype=np.int8)) +
                b' ' + self._eow for token in tqdm(
                    b_corpus, desc='Splitting bytes ...', ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute
                )]

        self._learn_encoding_impl(b_corpus, max_vocab_size)

    def encode(self, word: str, encoding: str = None) -> str:
        """
        Helps to encode a word, with the learned Byte Pair Encoding.

        :param word: the word or words to be encoded
        :param encoding: original encoding of the string, if not provided,
        the one from the constructor will be used (or the default one -> utf8)
        :return: the encoded word
        """

        # get or set encoding
        encoding = encoding if encoding else self._enc
        # convert the given string to bytes
        b_word = bytes(word, encoding=encoding)

        # support the case of multiple words
        words = word.split(' ')
        b_words = b_word.split(b' ')

        # iterate over the list of words
        for i, (w, bw) in enumerate(zip(words, b_words)):
            # if the byte word could be found in the vocabulary
            if self._sow + bw + self._eow in self._vocab:
                words[i] = self._sow.decode(encoding=encoding) + w + self._eow.decode(encoding=encoding)
                continue

            # split byte by byte
            bw = self._sow + b' ' + b' '.join(np.frombuffer(bw, dtype=np.int8)) + b' ' + self._eow
            # dummy dictionary
            word_freq = WordFreq({bw: 1})

            # compute frequency
            pairs = self._make_pairs(word_freq)
            # extract keys
            pairs = pairs.keys()
            # find the pairs available in the learned operations
            match_items = [(i, self._merges[i]) for i in pairs if i in self._merges]

            # continue until there are pairs to merge
            while len(match_items) != 0:
                items, indices = zip(*match_items)

                # choose the most frequent learned operation (the merge list is an ordered list by default)
                # the most frequent merges will be on the front
                best_index = indices.index(min(indices))
                best_merge = items[best_index]
                # merge the best pair
                word_freq.merge_pair(best_merge)

                # compute frequency
                pairs = self._make_pairs(word_freq)
                # extract keys
                pairs = pairs.keys()
                # find the pairs available in the learned operations
                match_items = [(i, self._merges[i]) for i in pairs if i in self._merges]

            # extract the only one word in the dictionary
            words[i] = list(word_freq.keys())[0].decode(encoding=encoding)

        # return the joined, encoded words
        return ' '.join(words)

    def decode(self, word: str, encoding: str = None) -> str:
        """
        Helps to decode an encoded word.

        :param word: a word to decode
        :param encoding: original encoding of the string, if not provided,
        the one from the constructor will be used (or the default one -> utf8)
        :return: the decoded word
        """

        # get or set encoding
        encoding = encoding if encoding else self._enc
        # convert the given string to bytes
        b_word = bytes(word, encoding=encoding)

        re_sow = re.escape(self._sow)
        re_eow = re.escape(self._eow)

        # create a regex object with positive lookbehind and lookahead around our regex string
        p = re.compile(rb'(?<=' + re_sow + rb').*?(?=' + re_eow + rb')')
        b_words: List[bytes] = p.findall(b_word)

        b_words = [b.replace(b' ', b'') for b in b_words]
        words = [b.decode(encoding=encoding) for b in b_words]

        return ' '.join(words)

    @property
    def vocab(self) -> Dict[bytes, int]:
        return self._vocab.copy()

    @property
    def merges(self) -> Dict[Tuple[bytes, bytes], int]:
        return self._merges.copy()

    @property
    def sow(self) -> str:
        return self._sow.decode(encoding=self._enc)

    @property
    def eow(self) -> str:
        return self._eow.decode(encoding=self._enc)


class BPEB(_BPE_template):
    """
    Byte Pair Encoder class for byte inputs

    Learns to encode any given word, to a series of learned substrings.
    """

    def __call__(self, word: bytes, encode: bool = None) -> bytes:
        # try guessing what we want (a very basic guess based on sow and eow tokens)
        if encode is None:
            # try finding Start or End Of Word token
            if word.find(self._sow) < 0 or word.find(self._eow) < 0:
                return self.encode(word)
            else:
                return self.decode(word)

        if encode:
            return self.encode(word)
        else:
            return self.decode(word)

    def __init__(self,
                 corpus: Iterable[bytes] = None,
                 max_vocab_size: int = 4096,
                 sow: bytes = b'<w/>',
                 eow: bytes = b'</w>'
                 ):
        """
        Constructor of Byte Pair Encoding class, will start learning bpe if corpus is provided.

        :param corpus: a list of tokens or words
        :param max_vocab_size: allowed dictionary size
        :param sow: start of word token
        :param eow: end of word token
        """

        self._max_vocab_size = max_vocab_size
        self._sow = sow
        self._eow = eow
        self._word_freq = None

        self._vocab: Dict[bytes, int] = dict()
        self._vocab_size: int = 0
        self._merges: Dict[Tuple[bytes, bytes], int] = dict()
        self.init()

        if corpus:
            # learn the byte pair encoding
            self.learn_encoding(corpus, max_vocab_size)

    def learn_encoding(self,
                       corpus: Iterable[bytes],
                       max_vocab_size: int = None
                       ):
        """
        Starts the learning of byte pair encodings in a given corpus.

        :param corpus: a list of tokens or words
        :param max_vocab_size: allowed dictionary size
        """

        # get or set the maximum size of the vocabulary and bpe merges
        max_vocab_size = max_vocab_size if max_vocab_size else self._max_vocab_size

        # split the word into characters, string is iterable so it can be further 'joined' with spaces
        # also appends End Of Word token at the end of each token

        if bpelibc:
            iterator_obj = tqdm(corpus, desc='Splitting bytes ...',
                                ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute)
            b_corpus = bpelibc.split_bytes_in_iterable_and_add_boundary(iterator_obj, self._sow, self._eow)
        else:
            b_corpus = [
                self._sow + b' ' +
                b' '.join(np.frombuffer(token, dtype=np.int8)) +
                b' ' + self._eow for token in tqdm(
                    corpus, desc='Splitting bytes ...', ncols=100, ascii=' >>>>>>>>>>>>>=', disable=BPE.mute
                )]

        self._learn_encoding_impl(b_corpus, max_vocab_size)

    def encode(self, word: bytes) -> bytes:
        """
        Helps to encode a word, with the learned Byte Pair Encoding.

        :param word: the word or words to be encoded
        :return: the encoded word
        """

        # support the case of multiple words
        words = word.split(b' ')
        b_words = word.split(b' ')

        # iterate over the list of words
        for i, (w, bw) in enumerate(zip(words, b_words)):
            # if the byte word could be found in the vocabulary
            if self._sow + bw + self._eow in self._vocab:
                words[i] = self._sow + w + self._eow
                continue

            # split byte by byte
            bw = self._sow + b' ' + b' '.join(np.frombuffer(bw, dtype=np.int8)) + b' ' + self._eow
            # dummy dictionary
            word_freq = WordFreq({bw: 1})

            # compute frequency
            pairs = self._make_pairs(word_freq)
            # extract keys
            pairs = pairs.keys()
            # find the pairs available in the learned operations
            match_items = [(i, self._merges[i]) for i in pairs if i in self._merges]

            # continue until there are pairs to merge
            while len(match_items) != 0:
                items, indices = zip(*match_items)

                # choose the most frequent learned operation (the merge list is an ordered list by default)
                # the most frequent merges will be on the front
                best_index = indices.index(min(indices))
                best_merge = items[best_index]
                # merge the best pair
                word_freq.merge_pair(best_merge)

                # compute frequency
                pairs = self._make_pairs(word_freq)
                # extract keys
                pairs = pairs.keys()
                # find the pairs available in the learned operations
                match_items = [(i, self._merges[i]) for i in pairs if i in self._merges]

            # extract the only one word in the dictionary
            words[i] = list(word_freq.keys())[0]

        # return the joined, encoded words
        return b' '.join(words)

    def decode(self, word: bytes) -> bytes:
        """
        Helps to decode an encoded word.

        :param word: a word to decode
        :return: the decoded word
        """

        re_sow = re.escape(self._sow)
        re_eow = re.escape(self._eow)

        # create a regex object with positive lookbehind and lookahead around our regex string
        p = re.compile(rb'(?<=' + re_sow + rb').*?(?=' + re_eow + rb')')
        b_words: List[bytes] = p.findall(word)

        b_words = [b.replace(b' ', b'') for b in b_words]

        return b' '.join(b_words)

    @property
    def vocab(self) -> Dict[bytes, int]:
        return self._vocab.copy()

    @property
    def merges(self) -> Dict[Tuple[bytes, bytes], int]:
        return self._merges.copy()

    @property
    def sow(self) -> bytes:
        return self._sow

    @property
    def eow(self) -> bytes:
        return self._eow


def bigram(corpus: List[str]) -> Dict[Tuple[str, str], int]:
    bgrams = [b for l in corpus for b in zip(list(l)[:-1], list(l)[1:])]
    bgrams = collections.Counter(bgrams)
    return dict(bgrams)
