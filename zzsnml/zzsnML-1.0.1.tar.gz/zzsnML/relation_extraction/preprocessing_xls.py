import jieba
import re
import os
import xlwt
# 使用停用词
filepath = os.path.dirname(os.path.realpath(__file__))
stop = open(os.path.join(filepath, './user_data/stop.txt'), 'r+', encoding='utf-8')
stopword = stop.read().split("\n")

# 最长句子长度
word_len = 600

# 判断汉字个数
def han_number(char):
    number = 0
    for item in char:
        if 0x4E00 <= ord(item) <= 0x9FA5:
            number += 1
    return number

# 分句
def cut_j(text_):
    text = re.sub('([。！？\?])([^”’])', r"\1\n\2", text_)
    text = re.sub('([。！？\?][”’])([^，。！？\?])', r'\1\n\2', text)
    text = text.rstrip().split("\n")
    #k = math.floor(han_number(text_)/600)
    j = 0
    t = ['']
    for i in text:
        if han_number(t[j])<word_len:
            t[j] = t[j]+i
        else:
            t.append('')
            j = j+1
    return t
    
# 判断距离
def lenc(x,y,z):
    xl = han_number(x)
    yl = han_number(y)
    xx = [10000]
    yy = [20000]
    min_ = 1000
    for i in range(han_number(z)-max(xl,yl)):
        if z[i:i+xl] == x:
            xx.append(i)
            xx.append(i+xl)
        if z[i:i+yl] == y:
            yy.append(i)
            yy.append(i+yl)
#     print(xx,yy)
    a = 0
    b = 0
    for i in xx:
        for j in yy:
            if min_>abs(i-j):
                a = i
                b = j
                min_ = abs(i-j)
    if a>b:
        return min_,y,x,b,a
    else:
        return min_,x,y,a,b
        
def keyword(entity_1,entity_2,text_,ii=0,jj=0):
    key = {'left':[],'mention_1':[entity_1],'middle':[],'mention_2':[entity_2],'right':[]}
    key['left'] = list(jieba.cut(text_[:ii-len(entity_1)]))
    key['middle'] = list(jieba.cut(text_[ii:jj]))
    key['right'] = list(jieba.cut(text_[jj+len(entity_2):]))    
    print('关键信息提取--------------------------')
    print(key)
    return key
###########################################3

def k(text,x='',y=''):
    min_txt = ['0',1000]
    if x == '':
        p = 0
        k = list(jieba.cut(text))
        d = {}
        for i in k:
            if i in stopword:
                continue
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m1 = ['1',1]
        m2 = ['2',0]
        for i in d:
            if int(d[i])>=m1[1]:
                m2[0] = m1[0]
                m2[1] = m1[1]
                m1[1] = d[i]
                m1[0] = i
            elif d[i]>m2[1]:
                m2[0] = i
                m2[1] = d[i]
    else:
        m1 = [x,0]
        m2 = [y,0]
    jl = cut_j(text)
    keyword_ = []
    for str_ in jl:
        p,xx,yy,ii,jj = lenc(m1[0],m2[0],str_)
        if min_txt[1]>p:
            min_txt[0] = str_
            min_txt[1] = p
            keyword_ = [xx,yy,ii,jj]
    print('关键词---------------------------------------')
    print(keyword_[0],keyword_[1])
    print('这句话两个词相距最近-------------------------')
    print(min_txt)
    keyword(keyword_[0],keyword_[1],min_txt[0],keyword_[2],keyword_[3])
    return min_txt,m1,m2


# =============================================================================
# def position_(text,x='',y=''):
#     min_txt = ['0',1000]
#     if x == '':
#         p = 0
#         k = list(jieba.cut(text))
#         d = {}
#         for i in k:
#             if i in stopword:
#                 continue
#             if i in d:
#                 d[i] += 1
#             else:
#                 d[i] = 1
#         m1 = ['1',1]
#         m2 = ['2',0]
#         for i in d:
#             if int(d[i])>=m1[1]:
#                 m2[0] = m1[0]
#                 m2[1] = m1[1]
#                 m1[1] = d[i]
#                 m1[0] = i
#             elif d[i]>m2[1]:
#                 m2[0] = i
#                 m2[1] = d[i]
#     else:
#         m1 = [x,0]
#         m2 = [y,0]
#     jl = cut_j(text)
#     keyword_ = []
#     for str_ in jl:
#         p,xx,yy,ii,jj = lenc(m1[0],m2[0],str_)
#         if min_txt[1]>p:
#             min_txt[0] = str_
#             min_txt[1] = p
#             keyword_ = [xx,yy,ii,jj]
#     print('关键词:  ',xx,yy,'出现在下面这段话，且距离最近：\n')
#  
#     print(min_txt)
# 
#     return ii,jj
# 
# =============================================================================


def position_mintxt(text,x='',y=''):
    min_txt = ['0',1000]
    if x == '':
        p = 0
        k = list(jieba.cut(text))
        d = {}
        for i in k:
            if i in stopword:
                continue
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        m1 = ['1',1]
        m2 = ['2',0]
        for i in d:
            if int(d[i])>=m1[1]:
                m2[0] = m1[0]
                m2[1] = m1[1]
                m1[1] = d[i]
                m1[0] = i
            elif d[i]>m2[1]:
                m2[0] = i
                m2[1] = d[i]
    else:
        m1 = [x,0]
        m2 = [y,0]
    keyword_ = []
    if han_number(text)<word_len:
        print(m1[0],m2[0])
        p,xx,yy,ii,jj = lenc(m1[0],m2[0],text)
        keyword_ = [xx,yy,ii,jj]
        print(xx,yy)
        min_txt = [text,p]
    else:
        jl = cut_j(text)
        for str_ in jl:
            print(m1[0],m2[0])
            p,xx,yy,ii,jj = lenc(m1[0],m2[0],str_)
            if min_txt[1]>p:
                min_txt[0] = str_
                min_txt[1] = p
                keyword_ = [xx,yy,ii,jj]
    #print(keyword_)
    if min_txt[1]>word_len:
        print('未找到适合的句子')
    else:
        print('关键词:  ',xx,yy,'出现在下面这段话，且距离最近：')
        print(min_txt)
        
    return min_txt[0],ii,jj


import pandas as pd

#Example = namedtuple('Example',    'entity_1, entity_2, left, mention_1, middle, mention_2, right, '    )

def position__last_occering(entity_,text_):  
    #jieba.load_userdict("../user_data/userdict.txt") #加载自定义词典
    jieba.load_userdict(os.path.join(filepath, './user_data/company.txt'))
    jieba.load_userdict(os.path.join(filepath, './user_data/expert.txt'))
    jieba.load_userdict(os.path.join(filepath, './user_data/leader.txt'))
    jieba.load_userdict(os.path.join(filepath, './user_data/region.txt'))
    jieba.load_userdict(os.path.join(filepath, './user_data/researcharea.txt'))

    index = -1
 
    while True:
        end_index = index
 
        index = str(text_).find(entity_,index + 1)
        #if (len(text_) < (index + len(entity_) + 5)) & (end_index != -1):
            #break
        if index == -1:
            break
    print(end_index)
    return end_index
    
def paragraph_sectioning_to7(entity_1,entity_2,text_):   

    p1 = str(text_).find(entity_1)
    
    p2 = position__last_occering(entity_2,text_)
    if (p1 < 0) or (p2 < 0):
        print('出错：句中无实体名！',p1,p2,entity_1,entity_2,text_)
        return "出错：句中无实体名！"
        
    #print('entity_1 position: ',p1,'\n')
    l1 = p1  + len(entity_1)
    l = " ".join(jieba.cut(text_[:p1]))
    #p2 = str(text_).find(entity_2)

    m = " ".join(jieba.cut(text_[l1:p2]))
    l2 = p2  + len(entity_2)
    r = " ".join(jieba.cut(text_[l2:]))
    
    tuple_7 = str(entity_1) + '\t' + str(entity_2) + '\t' + l.replace('\t',' ') + '\t' + str(entity_1) + '\t' + m.replace('\t',' ') + '\t' + str(entity_2) + '\t' + r.replace('\t',' ') + '\n'

    #print('\n',tuple_7,'\n')
    return tuple_7

#Example = namedtuple('Example',    'entity_1, entity_2, text_ '    )
# =============================================================================
# def paragraph_sectioning(text_):   #3to7
# 
#     fields = text_[:].split('\t')
#     print('(fields):   ',len(fields),fields)
#     if len(fields) != 3:
#         return '0','0','0'
#     #print(type(fields))     
#     entity_1 = fields[0]
#     entity_2 = fields[1] 
#     min_text,i,j = position_mintxt(fields[2],x = entity_1, y = entity_2) 
#     #print('===============:',len(min_text), len(fields[2]))
#     return paragraph_sectioning_to7(entity_1,entity_2,min_text),min_text,fields[2]
# 
# =============================================================================
def paragraph_sectioning(text_,e1=None,e2=None):   #3to7

    if e2 is None:
        if e1 is not None:
            return "参数格式错" ,'0','0'
    
    if e1 is None:
        if e2 is not None:
            return "参数格式错",'0','0'
        fields = text_[:].split('\t')
        #print('(fields):   ',len(fields),fields)
        if len(fields) != 3:
            return '0','0','0'
        #print(type(fields))     
        entity_1 = fields[0]
        entity_2 = fields[1] 
        min_text,i,j = position_mintxt(fields[2],x = entity_1, y = entity_2) 
        #print('========1111111=======:',entity_1, entity_2, fields[2])
        return paragraph_sectioning_to7(entity_1,entity_2,min_text),min_text,fields[2]
    
    min_text,i,j = position_mintxt(text_,x = str(e1), y = str(e2)) 
    #print('========2222222=======:',e1,e2,  text_)
    return paragraph_sectioning_to7(e1,e2,min_text),min_text,text_    



Text_Minlen = 30
def preprocessing_xls_4train(src_filename):
    data1 = pd.read_excel(src_filename,keep_default_na=False)
    kb_ = {}
    with open('./data/corpus.tsv','w', encoding='UTF-8') as f_corpus:
        for indexs in data1.index:
            line_ = list(data1.loc[indexs].values[:])

            if len(line_[0])<2:
                continue                
            if len(line_[2])<2:
                continue  
            if len(line_[3]) < Text_Minlen :
                continue                        
            #min_txt,position_1,position_2 = position_mintxt(line_[3],x=line_[0],y=line_[2])
            tuple_7 = paragraph_sectioning_to7(line_[0],line_[2],line_[3])
            if len(tuple_7)<30:
                continue                
            f_corpus.writelines(tuple_7)
    
            if len(line_[1]) < 2:#   为空时 是负样本
                continue
            if str(line_[1]) not in kb_.keys():
                kb_[str(line_[1])] = []     
            kb_triple_str =  str(line_[1]) + '\t' + str(line_[0]) + '\t' + str(line_[2])     
            #kb_[str(line_[1])].append(str(line_[1]) + '\t' + str(line_[0]) + '\t' + str(line_[2]))
            #print('--len(unrelated_pairs)-----------------------------',str(line_[1]),len(kb_[str(line_[1])])) 
            #f_kb.writelines(str(line_[1]) + '\t' + str(line_[0]) + '\t' + str(line_[2]) + '\n')
            if  kb_triple_str not in kb_[str(line_[1])] :
                kb_[str(line_[1])].append(kb_triple_str)
 
    with open('./data/kb.tsv','w', encoding='UTF-8') as f_kb: 
        for rel_ in kb_.keys():
            if len( kb_[rel_]) < 2:  #某一个关系rel存在的KBTriple(rel, sbj, obj)少于2个，单个三元组存在的examples不会太多，比如实际中超不过20个
                continue
            for truple_ in kb_[rel_]:
                f_kb.writelines(str(truple_) + '\n')
    return '1'
    
def clean_xls_4train(src_filename):
   
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('关系样本')
    sheet.write(0, 0, "左实体1")
    sheet.write(0, 1, "关系类型")
    sheet.write(0, 2, "右实体")
    sheet.write(0, 3, "语料")

    i = 0    
    
    
    
    data1 = pd.read_excel(src_filename)
   

    for indexs in data1.index:

        line_ = list(data1.loc[indexs].values[:])
#            if len(line_[1])<2:  #为空时 是负样本
#                continue  
        if len(line_[0])<2:
            continue                
        if len(line_[2])<2:
            continue  
        if len(line_[3]) < Text_Minlen :
            continue                        
        #min_txt,position_1,position_2 = position_mintxt(line_[3],x=line_[0],y=line_[2])
        tuple_7 = paragraph_sectioning_to7(line_[0],line_[2],line_[3])
        if len(tuple_7)<30:
            continue                

        i = i+1
        sheet.write(i, 0, line_[0])
        sheet.write(i, 1, line_[1])
        sheet.write(i, 2, line_[2])
        sheet.write(i, 3, line_[3])


    workbook.save(os.path.join(os.path.dirname(os.path.abspath(src_filename)),'cleaned_teain_corpus.xlsx'))




def preprocessing_xls_4pred(src_filename):    
    if not os.path.isfile(src_filename):
        src_filename = os.path.join('../data',src_filename)
        if not os.path.isfile(src_filename):
            return 'xls文件不存在！' 
        
    data1 = pd.read_excel(src_filename)
    dir_ = os.path.dirname(os.path.abspath(src_filename))
    tsv_file = os.path.join(dir_,'test.tsv')
    tsv_4section = os.path.join(dir_,'test_4section.tsv')

    with open(tsv_file,'w', encoding='UTF-8') as f_corpus,open(tsv_4section,'w', encoding='UTF-8') as f2_corpus:
        for indexs in data1.index:
            line_ = list(data1.loc[indexs].values[:])
            print('----------', len(line_))
            if len(line_[0])<2:
                continue                
            if len(line_[2])<2:
                continue  
            if len(line_[3]) < Text_Minlen :
                continue  
            #print('------&&&&--line_[3]--', line_[3])
            min_text,i,j = position_mintxt(line_[3],x = line_[0], y = line_[2])
            tuple_7 = paragraph_sectioning_to7(line_[0],line_[2],min_text)
            if len(tuple_7)<30:
                continue                
            tuple_4 = str(line_[0]) + '\t' + str(line_[2]) + '\t' + str(min_text).replace('\t',' ') + '\t' + str(line_[3]).replace('\t',' ')  + '\n'
            f2_corpus.writelines(tuple_4)
            f_corpus.writelines(tuple_7)

    return tsv_file #返回全路径
    #print(dirpath)

if __name__=="__main__":
    #preprocessing_xls_4pred('../user_data/pre.xls')
    #clean_xls_4train('../user_data/所有关系0603.xls')
    preprocessing_xls_4train('./user_data/t.xls')
    




