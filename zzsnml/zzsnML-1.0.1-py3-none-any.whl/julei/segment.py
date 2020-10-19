# -*- coding: utf-8 -*-
"""
Created on Wed April 17 22:06:20 2019

@author: Wu-Daqing
"""
import time
import os
import re
import pickle
import xlrd
import collections
from pyhanlp import JClass
class Segment:
    def __init__(self):
        pass
    def make_dir(self):
        if os.path.isdir('result/segment/') == False:
            os.makedirs(r'result/segment/') # 为分词结果创建文件夹

    # 定义从excel中读取内容的函数 （excel格式：日期 时间 内容）
    def load_data(self,excel_path):
        excel = xlrd.open_workbook(excel_path)
        table = excel.sheet_by_index(0)
        num_rows = table.nrows-1
        content = []
        for idx in range(1,num_rows+1):
            row = table.row_values(idx)
            content.append(row[2])
        return content

    def data_segment(self):
        file_names = sorted(os.listdir('data/')) # 把data文件夹下的所有原始excel数据的名称作为字符串组成list
        original_data = collections.defaultdict(list)
        for file_name in file_names:
            if file_name[-5:] == '.xlsx':
                excel_paths = 'data/' + file_name
                content = self.load_data(excel_paths)
                print(time.strftime('%Y-%m-%d %H:%M:%S'),file_name.split('_')[0],'文本读取完毕')
                original_data[file_name.split('_')[0]] = content # 以日期字符串作为key的原始数据
        self.make_dir()
        data_segment_txt = open('result/segment/data_segment.txt','wb') # 把分词结果写进txt文件里，以方便训练word2vec
        vocabulary_segment = collections.defaultdict(int)
        find_chinese = re.compile(u"[\u4e00-\u9fa5]+")
        symbols = "[A-Za-z0-9\[\`\~\!\@\#\$\^\&\*\(\)\=\|\{\}\'\:\;\'\,\[\]\.\<\>\/\?\~\！\@\#\\\&\*\%\t\n\r\f\b\000\v]"
        PerceptronLexicalAnalyzer = JClass('com.hankcs.hanlp.model.perceptron.PerceptronLexicalAnalyzer')
        segment = PerceptronLexicalAnalyzer()
        for key in original_data.keys():
            content = original_data[key]
            for i in range(len(content)):
                words = list(segment.analyze(content[i]).toWordArray())
                for word in words:
                    if re.findall(find_chinese,word) == []:
                        continue
                    elif re.sub(symbols, "",re.findall(find_chinese,word)[0]) == '':
                        continue
                    elif len(re.sub(symbols, "",re.findall(find_chinese,word)[0])) == 1:
                        continue
                    else:
                        word_filtrated = re.sub(symbols, "",re.findall(find_chinese,word)[0])
                        vocabulary_segment[word_filtrated] += 1
                        data_segment_txt.write(word_filtrated.encode('utf-8'))
                        data_segment_txt.write(' '.encode('utf-8'))
                data_segment_txt.write('\n'.encode('utf-8'))
                if (i+1)%100 == 0 or i+1 == len(content):
                    print(time.strftime('%Y-%m-%d %H:%M:%S'),key,'第',i+1,'条文本分词完毕并写入')
        data_segment_txt.close()
        return vocabulary_segment
    def dump_pkl(self):
        vocabulary_segment = self.data_segment()
        with open('result/segment/vocabulary_segment.pkl','wb') as save1:
            pickle.dump(vocabulary_segment,save1)
        print(time.strftime('%Y-%m-%d %H:%M:%S'),'词表长度:',len(vocabulary_segment))
        return vocabulary_segment
    def write(self):
        vocabulary_segment = self.data_segment()
        vocabulary_segment_sorted = sorted(vocabulary_segment.items(),key=lambda item:item[1],reverse=True) # 对字典中词的频率从大到小排序
        vocabulary_segment_txt = open('result/segment/vocabulary_segment.txt','wb')
        for value in vocabulary_segment_sorted:
            vocabulary_segment_txt.write(value[0].encode('utf-8'))
            vocabulary_segment_txt.write(' '.encode('utf-8'))
            vocabulary_segment_txt.write(str(value[1]).encode('utf-8'))
            vocabulary_segment_txt.write('\n'.encode('utf-8'))
        vocabulary_segment_txt.close()
# se  = Segment()
# se.write()