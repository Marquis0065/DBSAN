






from sklearn import datasets
from sklearn.cluster import KMeans
iris = datasets.load_iris()
X = iris.data
y = iris.target
kmeans = KMeans(n_clusters=3).fit(X)
print(kmeans)








#%%
# import seaborn
# import matplotlib.pyplot as plt
# plt.style.use('seaborn')
# #设置字体为黑色
# plt.rcParams['font.family']='SimHei'
# #显示符号
# plt.rcParams['axes.unicode_minus']=False#显示负号\n",
# import pandas as pd
# import os
#
# os.chdir(r'C:\Users\fzh00\Desktop\文件\excel')
#
# a_share = pd.read_excel('全部A股.xlsx')
#
# a_share.dropna(inplace=True)
# data= a_share.iloc[:,2:-1]
# for i in data.columns:
#     data[i]=pd.to_numeric(data[i],errors='coerce')
# data.dropna(inplace=True)
# # 3.做主成分之前，进行中心标准化
# from sklearn import preprocessing
# std_data =preprocessing.scale(data)
# # 4.使用sklearn的主成分分析，用于判断保留主成分的数量
# from sklearn.decomposition import PCA
# pca = PCA(n_components=5)
# pca.fit(std_data)
# # 单个主成分解释的方差(特征值)
# # print(pca.explained_variance_)
# # 单个主成分解释的方差比率
# # print(pca.explained_variance_ratio_)
# #主成分得分
# score= pd.DataFrame(pca.fit_transform(std_data))
# # print(score.head())
# print(pd.concat([data,score],axis=1).corr())














import requests
# from lxml import etree
#
# url = 'https://sz.lianjia.com/zufang/'
# print(url)
# response = requests.get(url)
# #print(response.text)
# result = etree.HTML(response.text).xpath('//em/text()')
# print(result)
# import scrapy
# import missingno
# import numpy
# import os
# os.__file__
# import seaborn
# import matplotlib.pyplot as plt
# plt.style.use('seaborn')
# #设置字体为黑色
# plt.rcParams['font.family']='SimHei'
# #显示符号
# plt.rcParams['axes.unicode_minus']= False
# base_url = 'https://sz.lianjia.com/zufang/longhuaqu/pg'
# import requests
# from lxml import etree
# result = []
# for i in range(1,11):
#   url = base_url+str(i)+'rt200600000001l1/#contentList'
#   res = requests.get(url)
#
#   result = result + etree.HTML(res.text).xpath('//em/text()')[:-1]
# print(result)
# import pandas as pd
# df = pd.DataFrame(result)
#
# df2 = pd.to_numeric(df[0],errors = 'coerce')
# se = pd.Series(df2)
# print(se)
# print(se.tolist())
# plt.hist(se.tolist())
# plt.show()



