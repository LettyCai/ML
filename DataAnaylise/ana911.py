
from matplotlib import pyplot as plt
import random
import matplotlib
import pandas as pd
import numpy as np
import string

#显示所有列
pd.set_option('display.max_columns', None)
#显示所有行
pd.set_option('display.max_rows', None)
#设置value的显示长度为100，默认为50
pd.set_option('max_colwidth',500)

font = {
    'family':'Microsoft Yahei',
    'size':'10'
}
matplotlib.rc("font",**font)

file_path = "./911.csv"

df = pd.read_csv(file_path)

# print(df.info())
print(df.head(1))

#1、统计不同类型的紧急情况的次数

# #获取分类
# data = df["title"].str.split(":").head(20).values
# data_list = list(set([i[0] for i in data]))
#
# # temp_list = df["title"].str.split(":").tolist()
# # cate_list = [i[0] for i in temp_list]
#
# #构造全为0的数组
# zeros_df = pd.DataFrame(np.zeros(shape=(df.shape[0],len(data_list))),columns = data_list)
#
# #赋值
# # for cate in data_list:
# #     zeros_df[cate][df["title"].str.contains(cate)] = 1
#
# sum_ret = zeros_df.sum(axis=0)
# print(sum_ret)

#2、通过添加分类信息获取不同类型紧急电话的次数

# #获取分类
# temp_list = df["title"].str.split(":").tolist()
# cate_list = [i[0] for i in temp_list]
#
# #给数据中添加一列分类信息
# cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)),columns=["cate"])
# df["cate"] = cate_df
#
# print(df.groupby(by="cate").count()["title"])

#3、按照时间进行统计
# #转化时间戳
# df["timeStamp"] = pd.to_datetime(df["timeStamp"])
# df.set_index("timeStamp",inplace=True)
#
# print(df.head(5))
#
# #统计出数据中不同月份电话次数
# count_by_month = df.resample("M").count()["title"]
# print(count_by_month.head(5))
#
# #画折线图
# _x = count_by_month.index
# _y = count_by_month.values
#
# _x = [i.strftime("%Y%m%d") for i in _x]
#
# plt.figure(figsize=(20,8),dpi=80)
# plt.plot(range(len(_x)),_y)
# plt.xticks(range(len(_x)),_x,rotation=45)
#
# plt.show()

#4、统计不同月份不同类型电话次数
#把时间字符串转化为时间类型，并设为索引

df["timeStamp"] = pd.to_datetime(df["timeStamp"])


#添加列，表示分类
temp_list = df["title"].str.split(":").tolist()
cate_list = [i[0] for i in temp_list]

#给数据中添加一列分类信息
cate_df = pd.DataFrame(np.array(cate_list).reshape((df.shape[0],1)),columns=["cate"])
df["cate"] = cate_df

df.set_index("timeStamp",inplace=True)
plt.figure(figsize=(20, 8), dpi=80)
#分组
for group_name,group_data in df.groupby(by="cate"):
    #对不同的分类都进行绘图
    count_by_month = group_data.resample("M").count()["title"]

    _x = count_by_month.index
    _y = count_by_month.values

    _x = [i.strftime("%Y%m%d") for i in _x]

    plt.plot(range(len(_x)),_y,label=group_name)

    print('*'*20)

plt.xticks(range(len(_x)), _x, rotation=45)
plt.legend(loc="best")
plt.show()





