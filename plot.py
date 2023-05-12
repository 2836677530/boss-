import matplotlib.pyplot as plt
import matplotlib as mql
import pandas as pd

import jieba
import collections
from wordcloud import WordCloud


jieba.setLogLevel(jieba.logging.INFO)



data=pd.read_csv('C:\\Users\\LUORONG\\Desktop\\数据分析\\newjava.csv')
#从业经验
# exp=[]
# nums=[0,0,0,0,0]
# counts=0
# dataExp=data['experience'].value_counts()
# for i in dataExp.index:
#     if '10年以上'==i:
#         nums[0]=dataExp[i]
#     elif '5-10年'== i:
        
#         nums[1]=dataExp[i]
#     elif '3-5年'==i:
        
#         nums[2]=dataExp[i]
#     elif '1-3年'==i:
     
#         nums[3]=dataExp[i]
#     else:
        
#         counts=counts+dataExp[i]
#         nums[4]=counts
# exp=['10年以上','5-10年','3-5年','1-3年','应届']

# colors=['#FF0000','#0000CD','#00bFFF','#008000','#FF1493','#FFD700','#FF4500']
# mql.rcParams['font.family']='SimHei'
# labels=exp
# plt.style.use('ggplot')
# plt.figure(figsize=(8,6),dpi=100)
# plt.barh(labels,nums,height=0.36,color=colors)
# plt.title('岗位工作经验要求',fontsize=16)
# plt.xlabel('数量',fontsize=12)
# plt.show()
# print(nums,dataExp)

        


# 技术要求词云
word_list=[]
jieba.load_userdict('C:\\Users\\LUORONG\\Desktop\\数据分析\\java.txt')
for i in data['techRequire']:
    str= ','.join(jieba.lcut(i,use_paddle=True))
    for j in str.split(','):
        word_list.append(j)
# print(word_list)
word_counts=collections.Counter(word_list)
# print(word_counts)


my_cloud=WordCloud(
    background_color='white',
    width=900,height=500,
    font_path='simhei.ttf',
    max_font_size=120,
    min_font_size=15,
    random_state=60
).generate_from_frequencies(word_counts)
plt.imshow(my_cloud,interpolation='bilinear')

plt.axis('off')
plt.show()
#岗位薪资水平
# level1=0
# level2=0
# level3=0
# level4=0
# level5=0
# level6=0
# level7=0
# for i in data['salary']:
#     if i <= 5000:
#         level1+=1
#     elif 5000<i<=10000:
#         level2+=1
#     elif 10000<i<=15000:
#         level3+=1
#     elif 15000<i<=20000:
#         level4+=1
#     elif 20000<i<=25000:
#         level5+=1
#     elif 25000<i<=30000:
#         level6+=1
#     else:
#         level7+=1
# nums=[level1,level2,level3,level4,level5,level6,level7]   
# colors=['#FF0000','#0000CD','#00bFFF','#008000','#FF1493','#FFD700','#FF4500']
# mql.rcParams['font.family']='SimHei'
# labels=['5K以下','5K-10K','10K-15K','15K-20K','20K-25K','25K-30K','30K以上']
# plt.style.use('ggplot')
# plt.figure(figsize=(8,6),dpi=100)
# plt.barh(labels,nums,height=0.36,color=colors)
# plt.title('岗位薪资水平',fontsize=16)
# plt.xlabel('数量',fontsize=12)
# plt.show()
#城市岗位图
# grouped=[]
# for i in data['site']:
#     if '地址' in i:
#         continue
#     grouped.append(str(i[0:2]))
# grouped=pa.DataFrame(grouped)
# grouped=grouped.value_counts()
# site=[]
# for i in grouped.index:
#     y = str(i)
#     site.append( y.split('\'')[1])
# nums=grouped.values



# plt.figure(figsize=(9,6),dpi=100)
# mql.rcParams['font.family']='SimHei'
# colors=['#FF0000','#0000CD','#00bFFF','#008000','#FF1493','#FFD700','#FF4500','#00FA9A','#191970','#0032CC']
# plt.bar(site,nums,width=0.5,color=colors)

# plt.title('城市岗位数量')
# plt.xlabel('SITE',fontsize=12)
# plt.ylabel('nums',fontsize=12)

# plt.show()
# #学历饼状图
# plt.rcParams['font.sans-serif']=['SimHei']
# plt.rcParams['axes.unicode_minus']=False
# grouped=data.groupby(['eduBackground']).count()
# datas=grouped['name']

# i=datas[0]
# datas[0]=datas[3]
# datas[3]=i

# labels=['学历不限','博士','大专','中专/中技','本科','硕士','高中']
# plt.pie(datas,labels=labels,autopct='%1.1f%%')
# plt.show()
