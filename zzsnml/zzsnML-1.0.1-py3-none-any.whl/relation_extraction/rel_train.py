from collections import Counter
import os
from relation_extraction import rel_ext
import pandas as pd

def simple_bag_of_words_featurizer(kbt, corpus, feature_counter):
    for ex in corpus.get_examples_for_entities(kbt.sbj, kbt.obj):
        #print(ex.middle)
        for word in ex.middle.split(' '):
            feature_counter[word] += 5
    for ex in corpus.get_examples_for_entities(kbt.obj, kbt.sbj):
        for word in ex.middle.split(' '):
            feature_counter[word] += 1
    return feature_counter

def left_bag_of_words_featurizer(kbt, corpus, feature_counter):
    for ex in corpus.get_examples_for_entities(kbt.sbj, kbt.obj):
        #print(ex.left)
        for word in ex.left.split(' '):
            feature_counter[word] += 1
    for ex in corpus.get_examples_for_entities(kbt.obj, kbt.sbj):
        for word in ex.left.split(' '):
            feature_counter[word] += 1
    return feature_counter
def right_bag_of_words_featurizer(kbt, corpus, feature_counter):
    for ex in corpus.get_examples_for_entities(kbt.sbj, kbt.obj):
        #print(ex.left)
        for word in ex.right.split(' '):
            feature_counter[word] += 1
    for ex in corpus.get_examples_for_entities(kbt.obj, kbt.sbj):
        for word in ex.right.split(' '):
            feature_counter[word] += 1
    return feature_counter


def train_(rex_ext_data_home='./data'): 
    #rex_ext_data_home = os.path.join('..','data')
    # rex_ext_data_home_corpus = r'../data/rel_ext_data/corpus.tsv.gz'
    # rex_ext_data_home_kb = r'../data/rel_ext_data/kb.tsv.gz'
    # corpus = rel_ext.Corpus(rex_ext_data_home_corpus)
    # kb = rel_ext.KB(rex_ext_data_home_kb)

    corpus = rel_ext.Corpus(os.path.join(rex_ext_data_home,'corpus.tsv'))
    kb = rel_ext.KB(os.path.join(rex_ext_data_home, 'kb.tsv'))
    dataset = rel_ext.Dataset(corpus, kb)
    dataset.count_examples()
    dataset.count_relation_combinations()
    #print(dataset)
    
    # splits = dataset.build_splits()
#    kbts_by_rel, labels_by_rel = dataset.build_dataset()
#    all_relations = set(kbts_by_rel.keys())
    train_result = rel_ext.train_models(
        #all_relations,
        featurizers=[left_bag_of_words_featurizer,simple_bag_of_words_featurizer,right_bag_of_words_featurizer],
        data=dataset
        )
    print(train_result)
# rel_ext.examine_model_weights(train_result)
if __name__ == '__main__':
    train_()