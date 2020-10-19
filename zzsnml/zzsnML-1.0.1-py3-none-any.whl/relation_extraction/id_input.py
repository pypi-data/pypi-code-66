import pickle
import os
with open('../data/process_data/dev.tsv','r',encoding='utf-8') as f:
    data = f.readlines()
line1, line2, line3 = {}, {},{}
for i in data:
    key1 = i.split('\t')[0]
    value1 = i.split('\t')[1]
    line1[key1] = value1
    key2 = i.split('\t')[2]
    value2 = i.split('\t')[3]
    line2[key2] = value2
    line3 = {**line1, **line2}
    # set(line3.keys())
print(line3)

if os.path.isdir('../data/id') == False:
    os.makedirs('../data/id')
with open('../data/id/id_file.pkl','wb') as f:
    pickle.dump(line3,f)

import pandas as pd
df = pd.read_csv('../data/process_data/dev.tsv',sep='\t',header=None)
df.drop([0,2],axis=1, inplace=True)
df.to_csv('../data/process_data/data.tsv', sep='\t', header=False,index=False)
# print(df)