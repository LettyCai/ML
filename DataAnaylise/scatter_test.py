# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/5/20 15:29'

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

font = {
    'family':'Microsoft Yahei',
    'size':'10'
}
matplotlib.rc("font",**font)

fig = plt.figure(figsize=(20,8),dpi=80)

y1 = [11,17,16,11,12,11,12,6,6,7,8,9,12,15,14,17,18,21,16,17,20,14,15,15,15,19,21,22,22,22,23]
y2 = [26,26,28,19,21,17,16,19,18,20,20,19,22,23,17,20,21,20,22,15,11,15,5,13,17,10,11,13,12,13,6]

print(len(y1),len(y2))

x1 = range(1,32)
x2 = range(51,82)

plt.scatter(x1,y1,label="三月份")
plt.scatter(x2,y2,label="十月份")

#设置x轴刻度
_xtick_labels = ['3月{}日'.format(i) for i in x1]
_xtick_labels += ['10月{}日'.format(i-50) for i in x2]

plt.xticks(list(x1)+list(x2),_xtick_labels,rotation=90)

plt.xlabel("时间")
plt.ylabel("温度")
plt.title("标题")

plt.legend(loc="upper left")


plt.show()