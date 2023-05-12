import os
import pandas as pd
from flask import Flask
# from flask_cors import *
from flask_cors import CORS
# from main_hw import app_hw
import collections
import jieba

app=Flask(__name__)
CORS(app, supports_credentials=True)  # 解决ajax的跨域访问问题
CORS(app,resources=r'/*')



@app.route('/')
def sinde():
    return 'helloworld'

@app.route('/expCounts',methods=['GET', 'POST'])
def expCounts():
    data=pd.read_csv('../newjava.csv')
    nums=[0,0,0,0,0]
    counts=0
    dataExp=data['experience'].value_counts()
    for i in dataExp.index:
        if '10年以上'==i:
            nums[0]=dataExp[i]
        elif '5-10年'== i:

            nums[1]=dataExp[i]
        elif '3-5年'==i:

            nums[2]=dataExp[i]
        elif '1-3年'==i:
        
            nums[3]=dataExp[i]
        else:
            counts=counts+dataExp[i]
            nums[4]=counts
    result=[]
    for i in nums:
        result.append(int(i))

    exp=['10年以上','5-10年','3-5年','1-3年','应届']
    return {'exp':exp,'data':result}

# @app.route('/sitedata',methods=['GET','POST'])
@app.route('/data',methods=['GET','POST'])
def sitedata():
    data=pd.read_csv('../newjava.csv')
    grouped=[]
    for i in data['site']:
        if '地址' in i:
            continue
        grouped.append(str(i[0:2]))
    grouped=pd.DataFrame(grouped)
    grouped=grouped.value_counts()
    nums = grouped.values.tolist()
    site=[]
    for i in grouped.index:
        y = str(i)
        site.append( y.split('\'')[1])
    
    return {'site':site,'nums':nums}

@app.route('/circle',methods=['GET','POST'])
def eduCircle():
    data=pd.read_csv('../newjava.csv')
    edu=data['eduBackground'].value_counts()
    nums=[0,0,0,0]
    for i in edu.index:
        if'博士'in i or '硕士' in i:
            nums[0]+=edu[i]
        elif '本科' in i:
            nums[1]+=edu[i]
        elif '大专' in i or '中专' in i :
            nums[2]+=edu[i]
        else:
            nums[3]+=edu[i]
    result=[]
    for i in nums:
        result.append(int(i))
    edu=['博士/硕士','本科','专科','学历不限']
    key=['value','name']
    key_values=[]
    for i in range(0,len(result)):
        lists=[result[i],edu[i]]
        key_values.append(dict(zip(key,lists)))
    return {'key_values':key_values,'edu':edu}

@app.route('/wordclound',methods=['GET','POST'])
def worldclound():
    data=pd.read_csv('../newjava.csv')
    word_list=[]
    jieba.load_userdict('C:\\Users\\LUORONG\\Desktop\\数据分析\\java.txt')
    for i in data['techRequire']:
        str= ','.join(jieba.lcut(i,use_paddle=True))
        for j in str.split(','):
            word_list.append(j)
    word_counts=collections.Counter(word_list)
    words_list = word_counts.most_common(30)
    # print(words_list)
    lists = []
    key = ['name', 'value']
    key_words = []
    for words in words_list:
        # print(words)
        word = '{}'.format(words)
        # print(word)
        name = word.split(',')[0].split('\'')[1]
        num = int(word.split(',')[1].split(')')[0])
        lists = [name, num]
        key_words.append(dict(zip(key, lists)))
    return {'key_words': key_words}
@app.route('/count',methods=['GET','POST'])
def salary():
    data=pd.read_csv('../newjava.csv')
    level1=0
    level2=0
    level3=0
    level4=0
    level5=0
    level6=0
    level7=0
    for i in data['salary']:
        if i <= 5000:
            level1+=1
        elif 5000<i<=10000:
            level2+=1
        elif 10000<i<=15000:
            level3+=1
        elif 15000<i<=20000:
            level4+=1
        elif 20000<i<=25000:
            level5+=1
        elif 25000<i<=30000:
            level6+=1
        else:
            level7+=1
    nums=[level1,level2,level3,level4,level5,level6,level7]   
    labels=['5K以下','5K-10K','10K-15K','15K-20K','20K-25K','25K-30K','30K以上']
    return {'salary':labels,'values':nums}
@app.route('/cityinfo',methods=['GET','POST'])
def map():
    data=pd.read_csv('../siteinfo.csv',encoding='gbk')

    site_counts=data['site'].value_counts()
    key=['value','name']
    key_values=[]
    for i in site_counts.index:
        lists=[int(site_counts[i]),i]
        key_values.append(dict(zip(key,lists)))

    data.drop_duplicates(subset=['site'],keep='first',inplace=True)
    data.reset_index(drop=True,inplace=True)

    list2=[]
    sites=[]
    for i in site_counts.index:
        # print(i)
        for j in range(0,len(data)):
            # print(data['site'][j])
            if i==data['site'][j]:
                list2.append([float(data['经度'][j]),float(data['维度'][j])])
                sites.append(i)
                continue
    result=dict(zip(sites,list2))
    return {'key_values':key_values,'list':result}
if __name__=='__main__':
    
    app.run(debug=True)
