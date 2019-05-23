import numpy as np

t1 = np.loadtxt('./data.csv',dtype=np.int,delimiter=',',skiprows=0,usecols=3,unpack=False)
print(t1)