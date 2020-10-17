import ngsl
from ngsl.dictionary import DICTIONARY


def test_include():
    assert ngsl.include('smile')
    assert ngsl.include('smiles')


def test_get_infinitiv():
    assert ngsl.get_infinitiv('smiles') == 'smile'


def test_get_infinitiv_list():
    assert ngsl.get_infinitiv_list(['smiles', 'quarterback']) == ['smile']


def test_all_infinitiv():
    assert ngsl.all_infinitiv() == DICTIONARY.keys()


def test_get_rank():
    assert ngsl.get_rank("and") == 3


def test_classify():
    words = ["snapback", "smiles", "and", "the", "snapback", "1st", "smiles"]
    result = ngsl.classify(words=words)
    assert result.ngsl_words == ["the", "and", "smile"]
    assert result.not_ngsl_words == ["snapback"]


def test_has_number():
    assert ngsl._has_number('1st')
    assert not ngsl._has_number('first')
    assert ngsl._has_number('catch22')
