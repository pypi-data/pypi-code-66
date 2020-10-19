#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2020/7/22 15:03
# @Author  : 程婷婷
# @FileName: extract.py
# @Software: PyCharm
import pandas as pd
import re
import jieba.posseg as pseg
import emoji
import time as time_time
import os
import difflib
from pyhanlp import *
class Extract:
    def __init__(self, country):
        self.country = country

    def read_txt(self, filenames):
        # r'./feature_dict.txt'
        lines = []
        f = open(filenames,'r', encoding='utf-8')
        for line in f.readlines():
            lines.append(line.strip('\n'))
        return lines
    def segment_para(self, para):
        split_pattern = re.compile(r'\n|。|？|！|\?|\!')
        global_sentences = split_pattern.split(emoji.demojize(str(para)))
        global_sentences = [str(i)+'。' for i in global_sentences]
        return global_sentences
    def filter_para(self, filter_list, sentence):
        phrase = ''
        for i in filter_list:
            if sentence.count(i) != 0:
                phrase = sentence
                break
        return phrase
    def money_pattern(self, global_sentences, filter_list, money_pattern, money_feature):
        # split_pattern = re.compile(r'\，\；')
        sentences, money = [], []
        sentences = [self.filter_para(filter_list=filter_list, sentence=index) for index in global_sentences]
        sentences = [i for i in sentences if len(i) != 0]
        for i in sentences:
            index = 0
            psg = ''
            words = []
            for term in HanLP.segment(i):
                if term.word in money_feature:
                    psg += 'E'
                else:
                    psg += str(term.nature)
                words.append(term.word)
                psg += str(index)
                index += 1
            for pattern_str in money_pattern:
                pattern = re.compile(r'' + pattern_str)
                rules = re.finditer(pattern, psg)
                for j in rules:
                    num = re.sub(r'\D', ' ', (j.group()))
                    num = num.strip()
                    start = int(num.split(' ')[0]) + 1
                    end = int(num.split(' ')[-1]) + 1
                    money.append(''.join(words[start:end]))
        money = [index for index in money if len(index) != 0]
        money = list(set(money))
        print(money)
        return ','.join(money)
    def write_excel(self, filename, df):
        if os.path.exists(os.path.dirname(filename)) ==False:
            os.mkdir(os.path.dirname(filename))
        # df[column] = data
        xlsx_content = pd.ExcelWriter(filename, engine='xlsxwriter')
        df.to_excel(xlsx_content, sheet_name='Sheet1')
        xlsx_content.close()

    def project_pattern(self):
        pattern = re.compile(r'([\。\!\！\:\：\ \丨]|)[a-zA-Z0-9\u4e00-\u9fa5]+((\u9879\u76ee)|(\u5de5\u7a0b)|(\u96a7\u9053))')
        charter = ['。','!','！',':','：',',',' ','【','】','，']
        # for i in range(len(data)):
        #     sent = data[i]
        sent = self.title
        try:
            f1 = re.finditer(pattern, sent)
            f1.__next__()
        except StopIteration:
            pattern = re.compile(r'([\。\!\！\:\：\ \丨]|)[a-zA-Z0-9\u4e00-\u9fa5]+((\u9879\u76ee)|(\u5de5\u7a0b))')
            sent = self.para
        f1 = re.finditer(pattern, sent[:800])
        project = []
        for index in f1:
            start = index.span()[0]
            end = index.span()[1]
            before = sent[start:end].strip(' ')
            after = re.sub('一带一路项目', '', before)
            if len(after) != 0:
                if after[0] in charter:
                    after = after.replace(after[0], '')
            if len(after) > 2:
                if (len(before) < 4) or ('个项目' in before):
                    pass
                else:
                    project.append(after)
        projects = list(set(project))
        projects.sort(key=project.index)
        return ','.join(projects[:2])

    def address_pattern(self, global_sentences, filter_list, address_pattern):
        # pattern = re.compile(r'')
        # pattern1 = re.compile(r'')
        address = []
        sentences = [self.filter_para(filter_list=filter_list, sentence=index) for index in global_sentences]
        sentences = [index for index in sentences if len(index) != 0]
        for i in sentences:
            for pattern_str in address_pattern:
                pattern = re.compile(r'' + pattern_str)
                f= re.finditer(pattern, i)
                for index in f:
                    start = index.span()[0]
                    end = index.span()[1]
                    before = i[start:end - 1].strip()
                    after = re.sub('\d','',before)
                    if len(before)-len(after) < 6:
                        address.append(''.join(before))
        address = list(set(address))
        print(address)
        # address.sort(key=addr.index)
        return ','.join(address)

    def capacity_pattern(self, global_sentences, filter_list, capacity_pattern):
        # pattern = re.compile(r'')
        # pattern1 = re.compile(r'')
        # pa = [pattern, pattern1]
        capacity = []
        for index in global_sentences:
            index = self.filter_para(filter_list=filter_list, sentence=index)
            if len(index) != 0:
                for pattern_str in capacity_pattern:
                    pattern = re.compile(r'' + pattern_str)
                    f1 = re.finditer(pattern, index)
                    for i in f1:
                        start = i.span()[0]
                        end = i.span()[1]
                        if bool(re.search('\d+', i.group())):
                            capacity.append(''.join(index[start + 1:end - 1]))
        capacity = list(set(capacity))
        print(capacity)
        return ','.join(capacity)

    def country_pattern(self, title, para):
        country_dict = {}
        country_result = ''
        paragraph = title + para
        for i in self.country:
            num = paragraph[:5000].count(i)
            country_dict[i] = num
        cou = max(country_dict.values())
        if cou != 0:
            country_result = ','.join([k for k, v in country_dict.items() if v == cou])
        else:
            for i in self.country:
                num = paragraph[5000:].count(i)
                country_dict[i] = num
            cou = max(country_dict.values())
            if cou != 0:
                country_result = ','.join([k for k, v in country_dict.items() if v == cou])
        return country_result

    def org_pattern(self, global_sentences):
        # split_pattern = re.compile(r'\n|。|？|！|\?|\!')
        # sentences = split_pattern.split(self.para)
        province = self.read_txt(self.filename_province)
        all_list = []
        first_list, second_list = [], []
        j = 0
        def extactCompany(tree):
            words, word1, word2= '', '', ''
            list1, list2 = [], []
            id = 0
            for word in tree.iterator():
                if word.HEAD.POSTAG == 'nt' and word.DEPREL == '定中关系' and ((word.HEAD.DEPREL == '定中关系') or (word.HEAD.DEPREL == '主谓关系')):
                    id = word.ID
                    word3 = word.LEMMA + word.HEAD.LEMMA
                    list1.append(word3)
                if word.POSTAG == 'nt'and ((word.DEPREL == '定中关系') or (word.DEPREL == '主谓关系')):
                    if word.ID - id != 1:
                        words = word.LEMMA
                        word1 = word.HEAD.LEMMA
                        list1.append(words)
                if word.HEAD.LEMMA == words and word.DEPREL == '并列关系' and word.POSTAG == 'nt':
                    list2.append(word.LEMMA)
                else:
                    if word.HEAD.LEMMA == word1 and word.DEPREL == '状中结构':
                        word2 = word.LEMMA
                    if word.HEAD.LEMMA == word2 and word.DEPREL == '介宾关系' and word.POSTAG == 'nt':
                        list2.append(word.LEMMA)
            return list1, list2

        for index in global_sentences:
            if ('签' in index) or ('中标' in index) or ('项目' in index):
                index += '。'
                model = HanLP.newSegment('crf').enableOrganizationRecognize(True)
                org_list = model.seg(str(index))
                for item in org_list:
                    if (str(item.nature) == 'nt'):
                        tree = HanLP.parseDependency(index)
                        list1, list2 = extactCompany(tree)
                        all_list.extend(list1)
                        all_list.extend(list2)
        for i in all_list:
            if (i[:2] in province) or (i[:3] in province):
                second_list.append(i)
            else:
                first_list.append(i)
        return ','.join(list(set(first_list))), ','.join(list(set(second_list)))

    def org_patterns(self, global_sentences, filter_list, province, model):
        sentences = [self.filter_para(filter_list=filter_list, sentence=index) for index in global_sentences]
        sentence = ''
        for index in sentences:
            if len(index) != 0:
                sentence += index
        org, first_list, second_list = [], [], []
        org_list = model.seg(str(sentence))
        org_list = list(org_list)
        for item in org_list:
            if ((str(item.nature) == 'nt')  or (str(item.nature) == 'ntc')) and ('银行' not in str(item.word)):
                num = org_list.index(item)
                word = item.word
                if str(org_list[num-1].nature) == 'ns':
                    word = org_list[num-1].word + item.word
                org.append(word)
        org = list(set(org))
        for i in org:
            i = i.strip()
            if (i[:1] in province) or (i[:2] in province) or (i[:3] in province):
                second_list.append(i)
            else:
                first_list.append(i)
        print(first_list)
        print(second_list)
        return ','.join(list(set(first_list))), ','.join(list(set(second_list)))

    def pro(self, global_sentences, title, objects, filter_list):
        # split_pattern = re.compile(r'\n|。|？|！|\?|\!|\s|；')
        # sentences = split_pattern.split(self.para)
        list_re = []
        title_two = ''
        def string_similar(str1, str2):
            return difflib.SequenceMatcher(None, str1, str2).quick_ratio()
        # sentences = hanlp.utils.rules.split_sentence(para)
        def value(id, id1, filter, tree):
            words = ''
            if (id != 0) and (id1 != id):
                for word in tree.iterator():
                    if word.ID >= id and word.ID <= id1:
                        if word.CPOSTAG in filter:
                            words = ''
                            break
                        else:
                            words += word.LEMMA
            if len(words) != 0:
                return words.split()[-1]
            else:
                return words
        #规则1：根据动词和所抽取实体首词以及首词的粗粒度词性总结
        def one_pattern(tree, objects):
            verb = ['签署','签订', '完成', '支援', '援助', '中标', '建设']
            word_cpostag = ['ns', 'vg', 'nz', 'nh', 'ni']
            list1= []
            id, id0, id1, id_end = 0, 0, 0, 0
            for word in tree.iterator():
                # print(tree)
                if id == 0:
                    if word.LEMMA in verb:
                        id = word.ID + 1
                        id0 = word.ID + 2
                if id != 0:
                    if word.ID == id:
                        if word.CPOSTAG in word_cpostag:
                            id_end = id
                    elif word.ID == id0:
                        if word.CPOSTAG in word_cpostag:
                            id_end = id0
                if (id_end != 0) and (word.LEMMA in objects):
                    id1 = word.ID
                    break
            words = value(id=id_end, id1=id1, filter = ['v', 'u'], tree=tree)
            if len(words) != 0:
                list1.append(words)
            return list1
        #规则2：
        def two_pattern(tree, objects):
            id, id1 = 0, 0
            list2 = []
            word_cpostag = ['ns', 'Vg', 'nz', 'nh', 'ni']
            for word in tree.iterator():
                if word.DEPREL == '定中关系' and word.CPOSTAG in word_cpostag :
                    id = word.ID
                    # print(id)
                if (word.LEMMA in objects) and (id != 0):
                    id1 = word.ID
                    # print(id1)
                    break
            words = value(id=id, id1=id1, filter = [ 'wp', 'u'], tree=tree)
            if len(words) != 0:
                list2.append(words)
            return list2
        #规则三
        def three_pattern(tree, objects):
            id, id1 = 0, 0
            list3 = []
            word_cpostag = ['ns', 'Vg', 'nh', 'ni']
            for word in tree.iterator():
                if word.CPOSTAG in word_cpostag  :
                    id = word.ID
                    # print(id)
                if (word.LEMMA in objects) and (id != 0) and (word.HEAD.CPOSTAG == 'v'):
                    id1 = word.ID
                    # print(id1)
                    break
            words = value(id=id, id1=id1, filter = ['v', 'wp', 'u'], tree=tree)
            if len(words) != 0:
                list3.append(words)
            return list3

        tree = HanLP.parseDependency(title)
        title_two = two_pattern(tree, objects)
        list_re.extend(title_two)
        sentences = [self.filter_para(filter_list=filter_list, sentence=i)for i in global_sentences]
        sentences = [i for i in sentences if len(i) != 0 ]
        # print(sentences)
        for index in sentences:
            # if len(index) != 0:
                # index += '。'
            # print(index)
            tree = HanLP.parseDependency(index)
            para_three = three_pattern(tree ,objects)
            list_re.extend(para_three)
            # if len(title_two) == 0:
            para_one = one_pattern(tree, objects)
            list_re.extend(para_one)
        list_re = list(set(list_re))
        for i in range(len(list_re)-1, 0, -1):
            sum = string_similar(list_re[0], list_re[i])
            if sum >= 0.8:
                list_re.pop(i)
        return ','.join(list_re)

    def time1(self, global_sentences, filter_list, time_pattern):
        # split_pattern = re.compile(r'\n|。|？|！|\?|\!')
        num  = []
        sentences = [self.filter_para(filter_list=filter_list, sentence=para) for para in global_sentences]
        for phrase in sentences:
            if len(phrase) != 0:
                run = False
                for pattern_str in time_pattern:
                    pattern = re.compile(r'' + pattern_str)
                    num1 = re.finditer(pattern, phrase)
                    for index in num1:
                        start = re.finditer('\d+', index.group())
                        for i in start:
                            start = i.span()[0]
                            num.append(index.group()[start:])
                            run = True
                            break
                    if run:
                        break
        time = list(set(num))
        print(time)
        return ','.join(time)
    def state(self, global_sentences, title, filter_list, state_pattern, state_no_words):
        state = []
        states = False
        year = time_time.asctime(time_time.localtime(time_time.time()))[-4:]
        def isyears(string):
            years = re.finditer('(\d){4}', string)
            return [index.group() for index in years]
        start1 = state_pattern.index('建设阶段')
        start2 = state_pattern.index('运营阶段')
        start3 = state_pattern.index('完成阶段')
        sentences = [self.filter_para(filter_list=filter_list, sentence=i) for i in global_sentences]
        if len(state) == 0:
            for para in sentences:
                if len(para) != 0:
                    for term in HanLP.segment(para):
                        if str(term.nature) == 'ns' or str(term.nature) == 'nt' or str(term.nature) == 'ntc' or str(term.nature) == 'nsf' or str(term.nature) == 'm':
                            states = True
                    if states:
                        for pattern_str in state_pattern[start1+1:start2]:
                            pattern = re.compile(r'' + pattern_str)
                            result = re.finditer(pattern, para)
                            for item in result:
                                word = item.group()
                                if len(word) != 0:
                                    if len(self.filter_para(filter_list=state_no_words, sentence=word)) == 0:
                                        years = isyears(word)
                                        if len(years) == 0:
                                            state.append('建设阶段')
                                            # print(word)
                                            # print(para)
                                            states = False
                                        else:
                                            if years[-1] == year:
                                                state.append('建设阶段')
                                                states = False
                                break
                    if states:
                        for pattern_str2 in state_pattern[start2+1:start3]:
                            pattern_two = re.compile(pattern_str2)
                            two_result = re.finditer(pattern_two, para)
                            for item in two_result:
                                word = item.group()
                                if len(word) != 0:
                                    if len(self.filter_para(filter_list=state_no_words, sentence=word)) == 0:
                                        years = isyears(word)
                                        if len(years) == 0:
                                            state.append('运营阶段')
                                            states = False
                                        else:
                                            if years[-1] > year:
                                                state.append('建设阶段')
                                                states = False
                                            if years[-1] == year:
                                                state.append('运营阶段')
                                                states = False
                                break
                    if states:
                        for pattern_str3 in state_pattern[start3+1:]:
                            pattern_three = re.compile(pattern_str3)
                            three_result = re.finditer(pattern_three, para)
                            for item in three_result:
                                word = item.group()
                                if len(word) != 0:
                                    if len(self.filter_para(filter_list=state_no_words, sentence=word)) == 0:
                                        years = isyears(word)
                                        if len(years) == 0:
                                            state.append('完成阶段')
                                        else:
                                            if years[-1] <= year:
                                                state.append('完成阶段')
                                break
        state = list(set(state))
        if len(state) == 0:
            state.append('建设阶段')
        print(state)
        return ','.join(state)

# if __name__ == '__main__':
#     txt_path = r'./data/feature_dict.txt'
#     province_path = r'./province.txt'
#     country_path = r'./data/国家名称.xls'
#     excel_path = r'C:\Users\lenovo\Desktop\一带一路_0706.xls'
#     country_df = pd.read_excel(country_path, header= None)[0].tolist()
#     country_df.remove('中国')
#     # nlp = StanfordCoreNLP(r'E:\迅雷下载\stanford-corenlp-latest\stanford-corenlp-4.1.0', lang='zh')
#     df = pd.read_excel(excel_path)[:200]
#     money_results = []
#     project_results = []
#     project_results1 = []
#     address_results =[]
#     capacity_results =[]
#     country_results = []
#     org_results = []
#     org_results1 = []
#     time_results = []
#     state_results = []
#     for i in range(len(df['内容'])):
#         print('============================================================'+ str(i))
#         extract = Extract(country=country_df)
#         province = extract.read_txt(province_path)
#         money_feature = extract.read_txt(txt_path)
#         address_filter = extract.read_txt(r'./data/filter/address_filter.txt')
#         capacity_filter = extract.read_txt(r'./data/filter/capacity_filter.txt')
#         entity_filter = extract.read_txt(r'./data/filter/entity_filter.txt')
#         money_filter = extract.read_txt(r'./data/filter/money_filter.txt')
#         project_filter = extract.read_txt(r'./data/filter/project_filter.txt')
#         state_filter = extract.read_txt(r'./data/filter/state_filter.txt')
#         state_no_words = extract.read_txt(r'./data/filter/state_no_words.txt')
#         time_filter = extract.read_txt(r'./data/filter/time_filter.txt')
#         address_pattern = extract.read_txt('./data/pattern/address_pattern.txt')
#         capacity_pattern = extract.read_txt('./data/pattern/capacity_pattern.txt')
#         money_pattern = extract.read_txt(r'./data/pattern/money_pattern.txt')
#         state_pattern = extract.read_txt(r'./data/pattern/state_pattern.txt')
#         time_pattern = extract.read_txt(r'./data/pattern/time_pattern.txt')
#         global_sentences = extract.segment_para(para=df['内容'][i])
#         money_results.append(extract.money_pattern(global_sentences=global_sentences, filter_list = money_filter, money_pattern = money_pattern, money_feature=money_feature))
#         # project_results.append(extract.project_pattern())
#         address_results.append(extract.address_pattern(global_sentences=global_sentences, filter_list = address_filter, address_pattern = address_pattern))
#         capacity_results.append(extract.capacity_pattern(global_sentences=global_sentences, filter_list = capacity_filter, capacity_pattern = capacity_pattern))
#         # print(df['内容'][475])
#         jia, yi = extract.org_patterns(global_sentences = global_sentences, filter_list = entity_filter, province=province)
#         org_results.append(jia)
#         org_results1.append(yi)
#         project_results1.append(extract.pro(global_sentences=global_sentences, title=df['标题'][i], objects = project_filter, filter_list=project_filter))
#         country_results.append(extract.country_pattern(title=df['标题'][i], para=df['内容'][i]))
#         state_results.append(extract.state(global_sentences=global_sentences, title=df['标题'][i], filter_list = state_filter, state_pattern = state_pattern, state_no_words= state_no_words))
#         time_results.append(extract.time1(global_sentences=global_sentences, filter_list = time_filter, time_pattern = time_pattern))
#     df['合同金额'] = money_results
#     # df['项目名称1'] = project_results
#     df['项目名称'] = project_results1
#     df['项目位置'] = address_results
#     df['项目产能'] = capacity_results
#     df['国家'] = country_results
#     df['企业识别甲方'] = org_results
#     df['企业识别乙方'] = org_results1
#     df['项目周期'] = time_results
#     df['项目状态'] = state_results
#     # extract.write_excel('./result/合同信息抽取.xlsx', df)
#     df.to_excel('./result/合同信息抽取.xlsx', columns=['标题', '内容', '原文链接', '合同金额', '项目名称', '项目位置', '项目产能','国家', '企业识别甲方', '企业识别乙方', '项目周期', '项目状态'])
#     # jpype._jclass.ArrayIndexOutOfBoundsException: java.lang.ArrayIndexOutOfBoundsException: 5777
#     # nlp.close()
