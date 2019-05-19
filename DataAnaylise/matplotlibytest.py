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

# x = range(2,26,2)
#
# y = range(15,39,2)
#
# fig = plt.figure(figsize=(20,8),dpi=80)
#
# plt.plot(x,y)
#
# #plt.savefig("./a.png")
# plt.xticks(range(25,50))
# plt.yticks(range(min(y),max(y)-1))
# plt.show()

#
a = [random.randint(20,35) for i in range(120)]
t = range(1,121)

fig = plt.figure(figsize=(20,8),dpi=80)

_x = list(t)
_xtick_labels = ["10点{}分".format(i) for i in range(60)]
_xtick_labels += ["11点{}分".format(i) for i in range(60)]
plt.xticks(_x[::3],_xtick_labels[::3],rotation=90)
plt.xlabel("时间")

plt.plot(t,a)
plt.show()