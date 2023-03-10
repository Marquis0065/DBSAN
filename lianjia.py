import urllib;
import pandas as pd
from requests_html import HTMLSession

url  = 'https://gdca.miit.gov.cn/zwgk/txfz/art/2022/art_983086ff767d487ebe11973b975e9a49.html'
session = HTMLSession()
response = session.get(url)
df2 = pd.read_html(response.text)[2][1:]
print(df2)



# s = 'abcdef'
# print(s)
# print(list(s))
# print(list(s).reverse())



# dict = {}
# dict.setdefault(('a'))
# print(dict)
# dict2= dict.copy()
# print(dict2)
# dict['a'] = '修改后的dict'
# print('dict',dict)
# print(dict2)
# del dict
# dict2['a']='dict2赋值了'
# print('删除dict后：',dict2)



# class Student:
#     __name = ''
#     def __init__(self,name):
#         self.__name = name
#     def getName(self):
#         return self.__name
#
# if __name__ =='__main__':
#     student = Student('borphi')
# print(student.getName())








