with open('../data/notCoutent.txt','r',encoding='utf-8') as f:
    data = f.readlines()
df = []
for i in data:
    df.append(i)
df = set(df)
with open('../data/notCoutent_chong.txt','w',encoding='utf-8') as f:
    for i in df:
        f.write(i)