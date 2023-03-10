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
import missingno
import numpy
import os
os.__file__
import seaborn
import matplotlib.pyplot as plt
plt.style.use('seaborn')
#设置字体为黑色
plt.rcParams['font.family']='SimHei'
#显示符号
plt.rcParams['axes.unicode_minus']= False
base_url = 'https://sz.lianjia.com/zufang/longhuaqu/pg'
import requests
from lxml import etree
result = []
for i in range(1,11):
  url = base_url+str(i)+'rt200600000001l1/#contentList'
  res = requests.get(url)

  result = result + etree.HTML(res.text).xpath('//em/text()')[:-1]
print(result)
import pandas as pd
df = pd.DataFrame(result)

df2 = pd.to_numeric(df[0],errors = 'coerce')
se = pd.Series(df2)
print(se)
print(se.tolist())
plt.hist(se.tolist())
plt.show()



