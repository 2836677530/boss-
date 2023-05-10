import numpy as np
import pandas as pd
#从csv读取数据
data=pd.read_csv('java.csv')
#检查空值
print('data中元素是否为空值的布尔型DataFrame为:\n', data.isnull())
print('data中元素是否为非空值的布尔型DataFrame为:\n', data.notnull())

print('data中每个特征对应的非空值数为:\n', data.count())
print('data中每个特征对应的缺失率为:\n', 1-data.count() / len(data))

# 薪水
def saveSalary(sal):
    count=[]
    for salary in sal:
        if '元/天' in salary:
            str = salary.split('元')[0]
            num1 = int(str.split('-')[0])
            num2 = int(str.split('-')[1])
            num = int(((num1+num2)/2)*30)
        elif '薪' in salary:
            try:
                str=salary.split('薪')[0]
                str1=str.split('K')[0]
            
                num1=int(str1.split('-')[0])
                num2=int(str1.split('-')[1])
                num3=int(str.split('K')[1].split('·')[1])
                num=int((((num1+num2)/2)*12)/14*1000)
                
            except:
                num=7500
        elif '元/时' in salary:
            str = salary.split('元')[0]
            num1 = int(str.split('-')[0])
            num2 = int(str.split('-')[1])
            num=(((num1+num2)/2)*10*30)
        else:
            str1=salary.split('K')[0]
            
            num1=int(str1.split('-')[0])
            num2=int(str1.split('-')[1])
            num = int(((num1+num2)/2)*1000)
        count.append(num)
    return count
salarys=saveSalary(data['salary'])
#学历和经验
list1=[]#经验
list2=[]#学历
for edu in data['eduBackground']:
    try:
       str1=edu.split('\n')[len(edu.split('\n'))-2]
       str2=edu.split('\n')[len(edu.split('\n'))-1]
       list1.append(str1)
       list2.append(str2)
    except:
        str2=edu.split('\n')[0]
        list2.append(str2)
        list1.append('经验不限')
#调整经验
def saveExp(list1):
    list1_t=[]
    for i in list1: 
        if '天' in i:
           str='经验不限'
           list1_t.append(str)
        elif '月' in i or i == '一年以内' :
            str='0-1年'
            list1_t.append(str)
        else:
            list1_t.append(i)
    return list1_t
list1=saveExp(list1)
#调整学历
def saveEdu(list2):
    list2_t=[]
    for i in list2:
        if '学历要求'in i:

            str='学历不限'
            list2_t.append(str)
        elif '月'in i:

            str='学历不限'
            list2_t.append(str)
        elif '初中' in i:
        
            str='学历不限'
            list2_t.append(str)
        else:
            list2_t.append(i)
    return list2_t
list2=saveEdu(list2)
print(len(data['name']),len(data['site']),len(data['company']),len(salarys),len(list1),len(list2),len(data['techRequire']))
data2=pd.DataFrame({
    'name':data['name'],
    'site':data['site'],
    'company':data['company'],
    'salary':salarys,
    'eduBackground':list2,
    'experience':list1,
    'techRequire':data['techRequire'],
})
data2.to_csv('newjava.csv',',')


