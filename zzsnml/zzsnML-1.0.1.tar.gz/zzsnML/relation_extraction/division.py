with open('../data/process_data/data.tsv','r',encoding='utf-8') as f:
    data = f.readlines()
with open('../data/test.tsv','w',encoding='utf-8') as f:
    k = 0
    for i in data:
        if k <300:
            k += 1
            print(k)
        elif (k >= 200) & (k < 300):
            f.write(i)
            k += 1
        else:
            break
# with open('../data/test.tsv','w',encoding='utf-8') as f:
#     for i in data:
#         if k < 300:
#             f.write(i)
#             k += 1

with open('../data/process_data/kb.tsv','r',encoding='utf-8') as f:
    data = f.readlines()
with open('../data/kb.tsv','w',encoding='utf-8') as f:
    k = 0
    for i in data:
        if k < 300:
            f.write(i)
            k += 1
        else:
            break