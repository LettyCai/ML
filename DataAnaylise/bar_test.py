# -*- coding: utf-8 -*-
__author__ = 'clj'
__date__ = '2019/5/20 16:14'

from matplotlib import pyplot as plt
import matplotlib
from matplotlib import font_manager

font = {
    'family':'Microsoft Yahei',
    'size':'10'
}
matplotlib.rc("font",**font)



a = ["战狼2","速度与激情8","功夫瑜伽","西游伏妖篇","变形金刚5：最后的骑士","摔跤吧！爸爸","加勒比海盗5：死无对证","金刚：骷髅岛","极限特工：终极回归","生化危机6：终章","乘风破浪","神偷奶爸3","智取威虎山","大闹天竺","金刚狼3：殊死一战","蜘蛛侠：英雄归来","悟空传","银河护卫队2","情圣","新木乃伊",]

b=[56.01,26.94,17.53,16.49,15.45,12.96,11.8,11.61,11.28,11.12,10.49,10.3,8.75,7.55,7.32,6.99,6.88,6.86,6.58,6.23]

_x = range(len(a))

_y = b

plt.barh(_x,b,height=0.2,color="orange")

plt.yticks(_x,a)

plt.show()