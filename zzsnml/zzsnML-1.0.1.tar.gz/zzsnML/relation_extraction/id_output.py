import pickle
import pandas as pd
import os
with open('../data/id/id_file.pkl','rb') as f:
    line = pickle.load(f)
# print(line)
if os.path.isdir('../data/result') == False:
    os.makedirs('../data/result')
df = pd.read_excel('../data/result.xlsx')
def get_key (dict, value):
    return [k for k,v in dict.items() if v == value]
id_entity1, id_entity2 = [], []
for value in df['实体1']:
    values = get_key(line, value)
    if len(values) == 0:
        id_entity1.append('')
    else:
        id_entity1.append(values[0])
for value in df['实体2']:
    values = get_key(line, value)
    if len(values) == 0:
        id_entity2.append('')
    else:
        id_entity2.append(values[0])
df['id_entity1'] = id_entity1
df['id_entity2'] = id_entity2
df.to_excel('../data/result/id_result.xlsx',index=False)
