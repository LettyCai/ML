import pandas as pd
import numpy as np
import string

# t = pd.read_csv('./IMDB-Movie-Data.csv')
# print(t.info())
# print(t.head(1))
#
# # 获取平均评分
# #print(t['Rating'].mean())
#
# #获取导演的人数
# #print(len(set((t["Director"].tolist()))))
# #print(len(t["Director"].unique()))
#
# #获取演员的人数
# temp_actors_list = t["Actors"].str.split(',').tolist()
# actors_list = [i for j in temp_actors_list for i in j]
# #print(len(set(actors_list)))
#
# #电影时长的最大最小值
# max_runtime = t["Runtime (Minutes)"].max()
# max_runtime_index = t["Runtime (Minutes)"].idxmax()
# runtime_median = t["Runtime (Minutes)"].median()
# #print(max_runtime,max_runtime_index,runtime_median)
#
# #统计每个分类电影的数量
# #将gener数据转化为列表
# temp_genre_list = t["Genre"].str.split(",").tolist()
# #把所有类别数据放进一个列表
# genre_list = []
# for i in temp_genre_list:
#     genre_list.extend(i)
# #去重
# genre_list = list(set(genre_list))
#
# #构造全0数组，列索引是每个分类
# zeros_genre = pd.DataFrame(np.zeros(shape=(t.shape[0],len(genre_list)),dtype=int),columns=genre_list)
#
# for i in range(t.shape[0]):
#     genres = t["Genre"][i]
#     zeros_genre.loc[i,genres.split(",")] = 1  #给出现分类的地方设置为1
#
# for i in genre_list:
#     print(i+":")
#     print(zeros_genre[i].sum())

#数据的合并
t1 = pd.DataFrame(np.zeros(shape=(2,5),dtype=np.float),index=list(string.ascii_uppercase[:2]),columns=list(string.ascii_uppercase[-5:]))
t2 = pd.DataFrame(np.ones(shape=(3,4),dtype=np.float),index=list(string.ascii_uppercase[:3]),columns=range(4))

# print(t1.join(t2))
# print(t2.join(t1))

t1.merge(t2)