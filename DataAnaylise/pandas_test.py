# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/5/23 10:53'

import pandas as pd
import numpy as np
import string

#创建Series
t = pd.Series(np.arange(10),index=list(string.ascii_uppercase[:10]))
print(t)
print(type(t))

#使用字典创建Series
a = {string.ascii_uppercase[i]:i for i in range(10)}
print(a)
t1 = pd.Series(a,index=list(string.ascii_uppercase[5:15]))
print(t1)

#切片和索引
print(t1[2:10:2])
print(t1[1])
print(t1[[1,2,4]])
print(t1[t1>4])
print(t1[['A','F','g']])

#索引和值
print(t1.index)
print(t1.values)

print('*'*30)

#读取外部文件
t5 = pd.read_csv('./dogNames2.csv')
print(t5)

#创建DataFrame
t2 = pd.DataFrame(np.arange(12).reshape(3,4))
print(t2)

#字典创建
d1 = {"name":['zhangsan','lisi'],"age":[12,26],"tel":[11111,2323423]}

t4 = pd.DataFrame(d1)

t3 = pd.DataFrame(np.arange(12).reshape(3,4),index=list(string.ascii_uppercase[:3]),columns=list(string.ascii_uppercase[-4:]))
print(t3)
print(t3.shape)
print(t3.dtypes)
print(t3.ndim)
print(t3.columns)
print(t3.head(3))
print(t3.describe())

#排序 统计t5中使用次数最多的
print(t5.head(3))
print(t5.info())

#ascending = False 降序排列
df = t5.sort_values(by="Count_AnimalName",ascending=False)

#取行或取列
print(df[:20])
print(df[:20]["Row_Labels"])

#loc和iloc
print(df.loc[1156,'Row_Labels'])
print(df.loc[1156,['Row_Labels','Count_AnimalName']])
print(df.loc[[1156,8620],['Row_Labels','Count_AnimalName']])
print(df.loc[[1156,9140],['Row_Labels','Count_AnimalName']])

print(df.iloc[1:3,[0,1]])

#赋值
df.loc[9140,'Count_AnimalName'] = 1234
print(df.loc[9140,'Count_AnimalName'])

#布尔索引
print(df[df['Count_AnimalName']>800])
print(df[(df['Count_AnimalName']>800) & (df['Count_AnimalName']<1000)])

#判断数据是否为NaN
