# -*- coding: utf-8 -*-
import jieba
import jieba.posseg as pseg
from relativeness_analysis.vocabulary import Vocabulary
from relativeness_analysis.classifier2 import xgboost
import xlrd, xlwt
import os, sys
import argparse
import numpy as np
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

####################################### 参数区 ########################################################
# 1. model path
file_path = os.getcwd()
model_path = os.path.join(file_path, 'classifier')  # 模型所在的目录，请最好不要在该目录下放其他文件，以免产生错误识别
vocab_path = os.path.join(file_path, 'vocab')  # 词典所在的目录，词典与模型相对应，请最好不要在该目录下放其他文件，以免产生错误识别

####################################### 代码区 ########################################################
def find_vocab(vocab_folder):
    files = os.listdir(vocab_folder)
    candidate_vocab = {}
    for file in files:
        tmp = '.'.join(file.split('.')[:-1]).split('-')
        if len(tmp) == 3:  # vocab-all-1491195238.voc
            v, company, signature = tmp
            if v == 'vocab':
                if candidate_vocab.get(company, None) is None:
                    candidate_vocab[company] = dict()
                candidate_vocab[company][signature] = file
    return candidate_vocab

def find_clf(clf_folder):
    files = os.listdir(clf_folder)
    candidate_clf = {}
    for file in files:
        tmp = '.'.join(file.split('.')[:-1]).split('-')  # # xgboost-all-tf-l1-l2-0.4-1491195238.clf
        if len(tmp) == 7:  # xgboost-all-tf-l1-l2-0.4-1491195238
            c, company, transformer, penalty, norm, thres, signature = tmp
            if c == 'xgboost':
                if candidate_clf.get(company, None) is None:
                    candidate_clf[company] = dict()
                candidate_clf[company][signature] = (file, transformer, penalty, norm, thres)
    return candidate_clf

def match_and_load(candidate_model_file, candidate_vocab_file, model_folder, vocab_folder):
    model = dict()
    for company in candidate_model_file:  # Based on model's key instead of vocab's
        tmp_model = candidate_model_file[company]
        tmp_vocab = candidate_vocab_file.get(company, None)
        if tmp_vocab is not None:
            for signature in set(tmp_model.keys()).intersection(tmp_vocab.keys()):
                tmp = model.get(company, None)
                if tmp is not None:
                    if int(signature) > int(model[company][0]):  # a model created more recently
                        model[company] = (signature, tmp_model[signature][0], tmp_vocab[signature]) + tmp_model[signature][1:]
                else:
                    model[company] = (signature, tmp_model[signature][0], tmp_vocab[signature]) + tmp_model[signature][1:]
    loaded_model = dict()
    for company in model:
        signature, model_file_name, vocab_file_name, transformer, penalty, norm, thres = model[company]
        clf = xgboost.load(os.path.join(model_folder, model_file_name))
        clf.thres = float(thres)
        vocab = Vocabulary.load(os.path.join(vocab_folder, vocab_file_name))
        loaded_model[company] = (signature, clf, vocab, transformer, penalty, norm, thres)
    return loaded_model

# # countvectorizer and tfidftransformer
# def create_transformer(model):
#     transformer = dict()
#     for company in model:
#         cv = CountVectorizer(decode_error='replace', vocabulary=model[company][2].to_dict())
#         use_idf = True if model[company][3].lower() == 'tfidf' else False
#         tfidf = TfidfTransformer(norm=model[company][-2], use_idf=use_idf)
#         transformer[company] = lambda data: tfidf.transform(cv.transform(data))
#     return transformer


# 查找模型和字典文件
candidate_model_file = find_clf(model_path)
candidate_vocab_file = find_vocab(vocab_path)
if len(candidate_vocab_file) == 0 or len(candidate_model_file) == 0:
    raise Exception(u'没有找到训练好的模型和词典文件！')
print(candidate_model_file, candidate_vocab_file)
model = match_and_load(candidate_model_file, candidate_vocab_file, model_path, vocab_path)
# transformer = create_transformer(model)


def read_file_for_eval(path, idx_dict):
    xlrd.book.unpack_SST_table.__globals__["unicode"] = lambda s, e: unicode(s, e, errors="replace")
    book = xlrd.open_workbook(path, encoding_override="utf-8")
    sheet = book.sheet_by_index(0)
    content_begin_with = idx_dict['content_begin_with']
    article_col = idx_dict['article_col']
    title_col = idx_dict['title_col']
    topic_col = idx_dict['topic_col']
    articles = sheet.col_values(article_col, start_rowx=content_begin_with)
    titles = sheet.col_values(title_col, start_rowx=content_begin_with)
    topics = sheet.col_values(topic_col, start_rowx=content_begin_with)
    data = {}
    for i, article in enumerate(articles):
        if sys.version_info.major == 2:
            topic = topics[i].encode('utf-8').strip()
            data[i] = [titles[i].encode('utf-8').strip() + '。' + article.encode('utf-8').strip(), topic]
        else:
            topic = topics[i].strip()
            data[i] = [titles[i].strip() + '。' + article.strip(), topic]
    return data

def test(text, company):
    # global count_vect, tf_transformer
    if company not in model:
        return '不支持的企业'
    if text == '。':
        return '删除'
    # if choose_tag[company]:
    #     processed_text = ' '.join([w for w, flag in pseg.cut(text) if flag in \
    #                     ['n', 'ns', 'nt', 'nz', 'nl', 'ng', 'v', 'vd', 'vn', 'vf', 'vx', \
    #                     'vi', 'vl', 'vg', 'a', 'ad', 'an', 'ag', 'al', 'd']])
    # else:
    processed_text = ' '.join([w for w in jieba.lcut(text)])
    cv = CountVectorizer(decode_error='replace', vocabulary=model[company][2].to_dict())
    tfidf_trans = TfidfTransformer(norm=model[company][-2], use_idf=False)
    counts = cv.transform([processed_text])
    tfidf = tfidf_trans.transform(counts)

    if tfidf.size == 0:
        return '删除'

    thres = float(model[company][-1])
    clf = model[company][1]

    predicted_label = clf.predict(tfidf, return_real_label=True)[0]

    return predicted_label

def main(file_path, _all=False, prefix='./'):
    result_file = '.'.join(os.path.basename(file_path).split('.')[:-1]) + '.xls'
    result_file = os.path.join(prefix, result_file)
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('result')
    sheet.write(0, 0, "标题+内容")
    sheet.write(0, 1, "企业")
    sheet.write(0, 2, "相关性")
    if _all:
        sheet.write(0, 3, "备注：不区分企业")
    else:
        sheet.write(0, 3, "备注：区分企业")

    idx_dict = {}
    idx_dict['content_begin_with'] = 1  # 样本从那一行开始，第0行为标注，第1行开始是样本
    idx_dict['article_col'] = 1  # 内容在excel文件的哪一列(下标从0开始)
    idx_dict['title_col'] = 0  # 标题在excel的哪一列(下标从0开始)
    idx_dict['topic_col'] = 4  # 企业在excel的哪一列(下标从0开始)

    data = read_file_for_eval(file_path, idx_dict)

    for i in data:
        text = data[i][0]
        company = data[i][1]
        if _all:
            relevant = test(text, 'all')
        else:
            relevant = test(text, company)
        sheet.write(i+1, 0, text)
        sheet.write(i+1, 1, company)
        sheet.write(i+1, 2, relevant)
    workbook.save(result_file)
    return result_file


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='判断语料与企业的相关性')
    parser.add_argument('-file', type=str, required=True,
                   help='待判断excel文件路径')
    parser.add_argument('-all', type=int, default=1,
                   help='是否区分企业，默认为不区分企业')
    parser.add_argument('-prefix', type=str, default='./', 
                   help='判断结果输出到哪个目录下，默认为当前目录')

    args = parser.parse_args()
    print(args.file, args.all, args.prefix)
    main(args.file, _all=args.all, prefix=args.prefix)
