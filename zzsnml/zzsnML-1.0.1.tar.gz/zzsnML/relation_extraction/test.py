import pandas as pd
with open('../data/rel_ext_data/corpus.tsv','r',encoding='utf-8') as f:
    data = f.readline()
datas = data.split('\t')
for i in range(len(datas)):
    print(datas[i])