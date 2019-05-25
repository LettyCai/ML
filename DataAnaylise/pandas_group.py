import pandas as pd
import numpy as np
import string
import matplotlib.pyplot as plt
import matplotlib

font = {
    'family':'Microsoft Yahei',
    'size':'10'
}
matplotlib.rc("font",**font)

file_url = "./starbucks_store_worldwide.csv"
df = pd.read_csv(file_url)

print(df.info())
print(df.head(1))

#按国家分组
grouped = df.groupby(by="Country")
#统计数量
country_count = grouped["Brand"].count()
# print(country_count["US"])
# print(country_count["CN"])

#统计中国每个省份店铺的数量
# china_data = df[df["Country"]=="CN"]
# grouped = china_data.groupby(by="State/Province").count()["Brand"]

#按照多个条件进行分组
#grouped = df.groupby(by=[df["Country"],df["State/Province"]]).count()

# #获取分组之后某一部分数据
# print(df.groupby(by=["Country","State/Province"])["Country"].count())
# #对某几列数据进行分组
# print(df["Country"].groupby(by=[df["Country"],df["State/Province"]]).count())
#
# #索引和复合索引
# t1 = df[["Country"]].groupby(by=[df["Country"],df["State/Province"]]).count()

#a = pd.DataFrame({'a': range(7),'b': range(7, 0, -1),'c': ['one','one','one','two','two','two', 'two'],'d': list("hjklmno")})

#使用matplotlib显示数量排名前10的国家
data = df.groupby(by="Country").count()["Brand"].sort_values(ascending=False).head(10)


plt.figure(figsize=(40,10),dpi=80)

# _x = data.index
# _y = data.values
#
# plt.bar(_x,_y)
# plt.xlabel("国家")
# plt.ylabel("门店数量")
# plt.title("门店数量前十的国家对比")
#
# plt.show()

#显示中国每个城市门店的数量
china_data = df[df["Country"]=="CN"]
data2 = china_data.groupby(by="City").count()["Brand"].head(25)
print(data2)

_x = data2.index
_y = data2.values

plt.bar(_x,_y)
plt.show()