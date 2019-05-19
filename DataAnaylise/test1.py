# coding=utf-8

from matplotlib import pyplot as plt
import random
import matplotlib
from matplotlib import font_manager

font = {
    'family':'Microsoft Yahei',
    'size':'10'
}
matplotlib.rc("font",**font)

y1 = [1,0,1,1,2,4,3,2,3,4,4,5,6,5,4,3,3,1,1,1]
y2 = [1,0,3,1,2,2,3,3,2,1 ,2,1,1,1,1,1,1,1,1,1]

x = range(11,31)

fig = plt.figure(figsize=(20,8),dpi=80)

plt.plot(x,y1,label="自己",color="c")
plt.plot(x,y2,label="同桌")

#设置x轴刻度
_xtick_labels = ['{}岁'.format(i) for i in x]

plt.xticks(x,_xtick_labels)
plt.yticks(range(0,9))
#绘制网格
plt.grid(alpha=0.1)

#添加图例
plt.legend()

plt.show()