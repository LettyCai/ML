import numpy as np
import random

t1 = np.array([1,2,3,])

print(t1)
print(type(t1))

t2 = np.array(range(10))

print(t2)

t3 = np.arange(10)

print(t3.dtype)

t4 = np.array(range(1,4),dtype=float)
print(t4.dtype)

t5 = np.array([1,0,1,0,1],dtype=bool)
print(t5)
t6 = t5.astype("int8")
print(t6)

t7 = np.array([random.random() for i in range(10)])
print(t7)
print(t7.dtype)
print('*'*30)
t8 = np.round(t7,2)
print(t8)

print(t8.shape)
t9 = t8.reshape(2,5)
print(t9.shape)
print(t9)

t10 = t9.flatten()
print(t10)

t11 = t10 + 1
print(t11)