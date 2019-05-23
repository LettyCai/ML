import pandas as pd
import numpy as np
import string

t = pd.read_csv('./IMDB-Movie-Data.csv')
print(t.info())

# 获取平均评分
print(t['Rating'].mean())

#获取导演的人数
print(len(set((t["Director"].tolist()))))
print(len(t["Director"].unique()))

#获取演员的人数
temp_actors_list = t["Actors"].str.split(',').tolist()
actors_list = [i for j in temp_actors_list for i in j]
print(len(set(actors_list)))

#电影时长的最大最小值
max_runtime = t["Runtime (Minutes)"].max()
max_runtime_index = t["Runtime (Minutes)"].argmax()
runtime_median = t["Runtime (Minutes)"].median()
print(max_runtime,max_runtime_index,runtime_median)