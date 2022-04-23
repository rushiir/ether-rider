# -*- coding: utf-8 -*-
"""
Created on Wed Mar 30 13:28:07 2022

@author: ningesh
"""

lst = [None, None, '1', '1', '1']
#print(type(lst))
lst = list(filter((None).__ne__, lst))
print(lst)
count = len(lst)
print("Count",count)