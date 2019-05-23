from typing import Any, Union

import numpy as np
import random

#生成数组
t1 = np.array([1,2,3,])

print(t1)
print(type(t1))

t2 = np.array(range(10))
print(t2)

t3 = np.arange(10)

#数组的类型
print(t3.dtype)
#指定数组的类型
t4 = np.array(range(1,4),dtype=float)
print(t4.dtype)

t5 = np.array([1,0,1,0,1],dtype=bool)
print(t5)
#转换类型
t6 = t5.astype("int8")
print(t6)

t7 = np.array([random.random() for i in range(10)])
print(t7)

print(t7.dtype)
print('*'*30)
#指定小数位数
t8 = np.round(t7,2)
print(t8)
#改变数据的形状
print(t8.shape)
t9 = t8.reshape(2,5)
print(t9.shape)
print(t9)

#一维化
t10 = t9.flatten()
print(t10)
#数组和数字的计算
t11: Union[int, Any] = t10 + 1
print(t11)
#数组和数组的计算
t5 = np.arange(0,24).reshape(4,6)
t6 = np.arange(100,124).reshape(4,6)
print(t5,t6)
print('*'*20)
print(t5+t6)
print('*'*30)
#转置
t1 = np.array(range(0,18)).reshape(3,6)
print(t1)
t2 = t1.transpose()
print(t2)
t3 = t1.swapaxes(1,0)
print(t3)
t4 = t1.T
print(t4)
print('*'*30)

t1 = np.array(range(1,33)).reshape(8,4)
print(t1)
#取一行
print(t1[2])
#取连续的多行
print(t1[1:])
#取不连续的多行
print(t1[[1,4]])
#取列
print(t1[:,2])
#取连续的多列
print(t1[:,2:])
#取不连续的多列
print(t1[:,[0,2,3]])
#取多行和多列
print(t1[2,3])
#取多行和多列，第2行到第5行，第2列到第3列
print(t1[2:5,1:3])
#取多个不相邻的点(0,0)(2,1)(2,3) 三个点)
print(t1[[0,2,2],[0,1,3]])

#布尔索引  选择小于10的元素，赋值为3
t1[t1<10] = 3
print(t1)

#三元操作符
t2 = np.where(t1<10,0,10)
print(t2)
