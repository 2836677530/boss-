import pandas as pd
data=pd.read_csv('../newjava.csv')
site_counts=data['site'].value_counts()
print(site_counts)

# data.drop_duplicates(subset=['site'],keep='first',inplace=True)
# data.reset_index(drop=True,inplace=True)
# list2=[]
# sites=[]
# for i in site_counts.index:
#     # print(i)
#     for j in range(0,len(data)):
#         # print(data['site'][j])
#         if i==data['site'][j]:
#             list2.append([float(data['经度'][j]),float(data['维度'][j])])
#             sites.append(i)
#             print(type(float(data['经度'][j])),type(data['维度'][j]))
#             continue
# print('----------------------------------------------------')
# result=dict(zip(sites,list2))
# print(type(result))
