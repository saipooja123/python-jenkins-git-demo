# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 15:37:57 2021

@author: RajagiriSaiPooja
"""

# def num1(x):
#     def num2(y):
#         return x+y
#     return num2

# print(num1(2)(3))
import re
data=[5,10,15,25]

y=list(map(lambda x:x*4,data))
print(y)


name="helloworld"

pattern=r"o"
print(re.split(pattern,name))
