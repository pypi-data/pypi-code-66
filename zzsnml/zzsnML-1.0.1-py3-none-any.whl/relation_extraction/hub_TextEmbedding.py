# -*- coding: utf-8 -*-
"""
Created on Sun Jun  7 21:31:42 2020

@author: zhangzib
"""

#please refer to https://hub.tensorflow.google.cn/google/bert_chinese_L-12_H-768_A-12/1


import sys
sys.path.insert(0, 'D:/peking_code/code_python/Bert201912/bert-master')

import numpy as np

import tensorflow as tf
import tensorflow_hub as hub

import bert
from bert import run_classifier
from bert import optimization
from bert import tokenization

# 问题： 怎样降维

#############################################################################################
#how the input preprocessing should be done to retrieve the input ids, masks, and segment ids:

def create_tokenizer_from_hub_module(bert_model_hub):
    #with tf.Graph().as_default():
    bert_module = hub.Module(bert_model_hub)
    tokenization_info = bert_module(signature="tokenization_info", as_dict=True)
    with tf.compat.v1.Session() as sess:
        vocab_file, do_lower_case = sess.run([tokenization_info["vocab_file"],
                                              tokenization_info["do_lower_case"]])
    return tokenization.FullTokenizer(
        vocab_file=vocab_file, do_lower_case=do_lower_case)


def convert_text_to_features(model,text_):  #created by zzb 20200615
    tokenizer = create_tokenizer_from_hub_module(model)
    example_ = run_classifier.InputExample(guid='',text_a=text_, label='A')
    MAX_SEQ_LENGTH=128
    input_feature = run_classifier.convert_single_example(0, example_, ['A','B'], MAX_SEQ_LENGTH, tokenizer)
    features1 = []
    features2 = []
    features3 = []
    features1.append(input_feature.input_ids)
    features2.append(input_feature.input_mask)
    features3.append(input_feature.segment_ids)
    bert_inputs = dict(
        input_ids=tf.convert_to_tensor(np.array(features1)),
        input_mask=tf.convert_to_tensor(np.array(features2)),
        segment_ids=tf.convert_to_tensor(np.array(features3)))
    
    return bert_inputs

#############################################################################################
def text2vec(text_): 
    
    model_ = "../embeding"
    
    #model_ = "https://hub.tensorflow.google.cn/google/bert_chinese_L-12_H-768_A-12/1"
        
    bert_inputs = convert_text_to_features(model_,text_)
    
    hub_layer = hub.Module(model_, trainable=True)
    
    _output = hub_layer(bert_inputs, signature="tokens", as_dict=True)
    with tf.compat.v1.Session() as sess:
        tf.compat.v1.global_variables_initializer().run()
        pooled_output = sess.run(_output["pooled_output"])  #The pooled_output is a [batch_size, hidden_size] Tensor
    #print(type(pooled_output[0]))
    return pooled_output[0].tolist() #size: hidden_size


if __name__ == '__main__':

    print("Version: ", tf.__version__)
    print("Eager mode: ", tf.executing_eagerly())
    print("Hub version: ", hub.__version__)

    
    t = "要坚持以习近平新时代中国特色社会主义思想为指导，深入学习贯彻党的十九届四中全会精神"
    print(text2vec(t))

# =============================================================================
#model = "https://storage.googleapis.com/tfhub-modules/google/bert_chinese_L-12_H-768_A-12/1.tar.gz"
#model = "https://tfhub.dev/tensorflow/bert_zh_L-12_H-768_A-12/1"
#=============================================================================